# [Rime](https://blog.isteed.cc/post/rime-2022/)

fork 自 <https://github.com/LufsX/rime> ，并添加自己的设置，方案，词库。

# 使用

Rime 的使用教程网上到处都是，我这里就不说得太详细了。

## 安装

第一步是安装 Rime 在对应平台上的替代品。

- Linux：不多说，fcitx5 + fcitx5-rime。想必用 linux 的装 rime 完全没有难度。
- Windows：安装[小狼毫](https://github.com/rime/weasel/releases)
- Android：小企鹅输入法（fcitx5 for Andriod）和同文输入法都支持 rime。我选用前者。
  - 下载[小企鹅输入法](https://github.com/fcitx5-android/fcitx5-android/releases) 和下面的 `plugin.rime`。注意：不要安装 Google Play 上的小企鹅输入法版本。和插件不兼容。

## 配置

进入到配置文件夹（的父级文件夹），直接 clone 该仓库内容即可：

```sh
git clone https://github.com/lxl66566/rime.git --recursive
```

这一份配置可以跨多平台，不需要任何修改。我本人在以下三个平台使用此配置。

配置文件夹：

- Linux：`~/.local/share/fcitx5/rime/`
- Windows：`C:\Users\<user_name>\AppData\Roaming\Rime`
- Andriod（fcitx5 for Andriod）：`/Android/data/org.fcitx.fcitx5.android/files/data/rime`

## 使用技巧

- 需要 _重新部署_，更改的配置才会生效。
- 自己制做词库，我用的 vscode + [Rime formatter](https://github.com/lxl66566/rime-formatter)，我自己写的，非常好用。
