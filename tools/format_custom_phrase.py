# 格式化 custom_phrase.txt 文件，排序 + 分组

import re
from pathlib import Path
from typing import override


def is_chinese_string(s: str):
    # 使用正则表达式匹配任意数量的汉字
    return bool(re.fullmatch(r"[\u4e00-\u9fa5]+", s))


def is_alphanumeric(s: str):
    # 使用正则表达式匹配任意数量的数字和字母，还有 - 和 _
    return bool(re.fullmatch(r"[a-zA-Z0-9-_]+", s))


def is_chinese_alphanumeric(s: str):
    # 使用正则表达式匹配任意数量的汉字、数字和字母，还有 - 和 _
    return bool(re.fullmatch(r"[\u4e00-\u9fa5a-zA-Z0-9-_]+", s))


class Word:
    def __init__(self, hanzi: str, duyin: str, quanzhong: str | None = None):
        self.main: str = hanzi
        self.spell: str = duyin
        self.rank: str | None = quanzhong

    def __lt__(self, other: "Word") -> bool:
        """
        汉字的话先比汉字长度，再比字母顺序
        英文直接比字母顺序
        混合比拼写顺序
        """
        if is_chinese_string(self.main):
            if len(self.main) < len(other.main):
                return True
            if len(self.main) > len(other.main):
                return False
        elif is_alphanumeric(self.main):
            if self.main < other.main:
                return True
            elif self.main > other.main:
                return False

        if self.spell < other.spell:
            return True
        elif self.spell > other.spell:
            return False

        if self.rank is None:
            return False
        if other.rank is None:
            return True
        return self.rank < other.rank

    @override
    def __eq__(self, other) -> bool:
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


# 分组
comment: list[str] = []  # 最前面的注释
english: list[Word] = []
chinese: list[Word] = []
mixed: list[Word] = []  # 混合排序
farra: list[Word] = []  # 无法推断的
comment_flag = True


def classify_push(word: Word):
    if is_chinese_string(word.main):
        chinese.append(word)
    elif is_alphanumeric(word.main):
        english.append(word)
    elif is_chinese_alphanumeric(word.main):
        mixed.append(word)
    else:
        farra.append(word)


# 读取 custom_phrase.txt 文件
file = Path("custom_phrase.txt")
text = file.read_text(encoding="utf-8")


for line in text.splitlines():
    if line.startswith("#"):
        if comment_flag:
            comment.append(line)
        continue
    line = line.strip()
    if not line:
        comment_flag = False
        continue
    spl = line.split()
    hanzi = spl[0]
    duyin = spl[1]
    quanzhong = None
    if len(spl) > 2:
        quanzhong = spl[2]
    word = Word(hanzi, duyin, quanzhong)
    classify_push(word)

new_texts: list[str] = []
new_texts.extend(comment)
new_texts.extend(["\n"])
new_texts.extend(map(str, sorted(chinese)))
new_texts.extend(["\n"])
new_texts.extend(map(str, sorted(english)))
new_texts.extend(["\n"])
new_texts.extend(map(str, sorted(mixed)))
new_texts.extend(["\n"])
new_texts.extend(map(str, farra))

new_text = "\n".join(new_texts)

# 写入文件
file = Path("custom_phrase.txt")
_ = file.write_text(new_text, encoding="utf-8")
