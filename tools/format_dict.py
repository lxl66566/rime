#!/usr/bin/env python3
# 格式化 dict 文件，排序
# 使用方法：`python3 tools/format_dict.py` 格式化 dicts/absx.dict.yaml
#         `python3 tools/format_dict.py -` 格式化 stdin 并输出到 stdout
#         `python3 tools/format_dict.py <file_path>` 格式化指定文件

import sys
import unittest
from pathlib import Path
from typing import override


class Word:
    def __init__(self, main: str, spell: str, rank: str | None = None):
        self.main: str = main
        self.spell: str = spell
        self.rank: int | None = int(rank) if rank is not None else None

    def __lt__(self, other: "Word") -> bool:
        """
        Word 直接比读音
        """
        if self.spell < other.spell:
            return True
        elif self.spell > other.spell:
            return False

        if self.rank is None:
            return False
        if other.rank is None:
            return True
        return self.rank > other.rank

    @override
    def __eq__(self, other) -> bool:  # type: ignore
        assert isinstance(other, Word)
        return self.spell == other.spell and self.rank == other.rank

    @override
    def __repr__(self):
        if self.rank is None:
            return f"{self.main}\t{self.spell}"
        else:
            return f"{self.main}\t{self.spell}\t{self.rank}"

    @override
    def __str__(self):
        return self.__repr__()

    @override
    def __hash__(self) -> int:
        return hash(self.spell) + (self.rank or 0)

    @staticmethod
    def from_str(s: str) -> "Word":
        spl = s.strip().split("\t")
        if len(spl) == 2:
            # 无 rank
            return Word(spl[0], spl[1])
        elif len(spl) == 3:
            # 有 rank
            return Word(spl[0], spl[1], spl[2])
        if len(spl) == 1:
            # 用户输入的字符串，没有 "\t" 分隔
            part1, rest = spl[0].split(maxsplit=1)
            rest_spl = rest.split()
            if rest_spl[-1].isdigit():
                rank = rest_spl.pop()
                return Word(part1, " ".join(rest_spl), rank)
            else:
                return Word(part1, " ".join(rest_spl))
        raise ValueError(f"Invalid word line: `{s}`")


if __name__ == "__main__":
    file = None
    # 读取文件
    filepath = sys.argv[1] if len(sys.argv) > 1 else "dicts/absx.dict.yaml"
    if filepath.strip() != "-":
        assert filepath.endswith(".yaml") or filepath.endswith(".yml")
        file = Path(filepath)

    if file is not None:
        text = file.read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    comment: list[str] = []
    first_comment_flag = True
    header: list[str] = []
    header_flag = False
    words: list[Word] = []

    for line in text.splitlines():
        if line.strip() == "":
            continue
        if header_flag:
            if not (line.startswith("---") or line.startswith("...")):
                header.append(line)
                continue
            else:
                header_flag = False
                continue

        if line.startswith("#") and first_comment_flag:
            comment.append(line)
            continue
        else:
            first_comment_flag = False

        if line.startswith("---"):
            header_flag = True
            continue

        word = Word.from_str(line)
        words.append(word)

    new_texts: list[str] = []
    new_texts.extend(comment)
    new_texts.extend(["\n", "---"])
    new_texts.extend(header)
    new_texts.extend(["...", "\n"])
    new_texts.extend(map(str, sorted(words)))
    new_texts.extend(["\n"])

    new_text = "\n".join(new_texts)

    if file is not None:
        # 写入文件
        _ = file.write_text(new_text, encoding="utf-8")
    else:
        _ = sys.stdout.write(new_text)


class TestWord(unittest.TestCase):
    def test_from_str(self):
        self.assertEqual(Word.from_str("a\tb\t100"), Word("a", "b", "100"))
        self.assertEqual(Word.from_str("a\tb c d\t100"), Word("a", "b c d", "100"))
        self.assertEqual(Word.from_str("a\tb"), Word("a", "b"))
        self.assertEqual(Word.from_str("a b"), Word("a", "b"))
        self.assertEqual(Word.from_str("a b c"), Word("a", "b c"))
        self.assertEqual(Word.from_str("a b 100"), Word("a", "b", "100"))
