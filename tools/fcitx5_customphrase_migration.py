#!/usr/bin/env python3
# 从 fcitx5_pinyin_customphrase.txt 迁移到 rime 的 custom_phrase.txt

from pathlib import Path

# 读取 fcitx5_pinyin_customphrase.txt 文件
fcitx5_file = Path("fcitx5_pinyin_customphrase.txt")
text = fcitx5_file.read_text(encoding="utf-8")

with open("custom_phrase.txt", "a", encoding="utf-8") as f:
    for line in text.splitlines():
        if line.startswith("#"):
            continue
        line = line.strip()
        if not line:
            continue
        duyin, rest = map(str.strip, line.split(","))
        quanzhong, hanzi = map(str.strip, rest.split("="))
        if not hanzi or not duyin or not quanzhong:
            continue
        quanzhong = 10000 // int(quanzhong)  # fcitx5 的是次序，而 rime 是频率，负相关
        _ = f.write(f"{hanzi} {duyin} {quanzhong}\n")
