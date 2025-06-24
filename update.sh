#!/usr/bin/env bash
# 从 git 远程更新词库

set -exof pipefail

# 获取当前用户的用户名
user_name=$(whoami)

# 确定 Rime 配置文件夹
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    rime_path="$HOME/.local/share/fcitx5/rime/"
    elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
    # Windows
    rime_path="C:\\Users\\$user_name\\AppData\\Roaming\\Rime"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
    # MacOS (未经测试)
    rime_path="$HOME/Library/Rime/"
    elif [[ -n "$ANDROID_DATA" ]]; then
    # Android (fcitx5 for Android)
    rime_path="/storage/emulated/0/Android/data/org.fcitx.fcitx5.android/files/data/rime"
    
    # Termux 环境检测
    if [ -n "$PREFIX" ]; then
        # 检查是否已 root
        if [ -x "$(command -v su)" ]; then
            # Termux 且已 root
            export PATH=/data/data/com.termux/files/usr/bin:$PATH
        else
            echo "Termux 环境，但未 root。请手动更新词库。"
            exit 1
        fi
    fi
else
    echo "无法确定当前平台。"
    exit 1
fi

# 检查 Rime 配置文件夹是否存在
if [ ! -d "$rime_path" ]; then
    echo "Rime 配置文件夹不存在，正在克隆..."
    git clone https://github.com/lxl66566/rime.git "$rime_path"
else
    # 检查是否是 Git 仓库
    if [ ! -d "$rime_path/.git" ]; then
        echo "错误：Rime 配置文件夹已存在，但不是 Git 仓库。"
        exit 1
    fi
    
    # 绕过 safe directory 限制 (尝试使用 Git 自身的参数)
    git -C "$rime_path" config --local safe.directory "$rime_path"
    
    # Fetch 并 reset 到最新远程分支
    echo "Rime 配置文件夹已存在，正在更新..."
    git -C "$rime_path" fetch origin
    git -C "$rime_path" reset --hard origin/main
    
    # 删除私人词库
    rm -f "$rime_path/dicts/absx-personal.dict.yaml.zst.enc"
    sed -i '/absx-personal.dict.yaml.zst.enc/d' "$rime_path/chinese.dict.yaml"
fi
