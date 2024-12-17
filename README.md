# [Rime](https://blog.isteed.cc/post/rime-2022/)

自用 rime 配置：fork 自 <https://github.com/LufsX/rime> ，并添加自己的设置，方案，词库。Rime 的部署教程网上到处都是，我这里就不说得太详细了。

本配置支持的方案（切换方案请按 F1 键）：

- 全拼（朙月拼音）
- 小鹤双拼
- 日本語

<details>
  <summary>如何卸载日语方案</summary>
  删除所有 `japanese` 开头的 yaml 文件与 `dicts-jap` 即可。
</details>

## 安装

第一步是安装 Rime 在对应平台上的替代品。

- Linux：不多说，fcitx5 + fcitx5-rime。想必用 linux 的装 rime 完全没有难度。
- Windows：安装[小狼毫](https://github.com/rime/weasel/releases)
- Android：小企鹅输入法（fcitx5 for Andriod）和同文输入法都支持 rime。我选用前者。
  - 下载[小企鹅输入法](https://github.com/fcitx5-android/fcitx5-android/releases) 和链接下面的 `plugin.rime`。注意：不要安装 Google Play 上的小企鹅输入法版本。和插件不兼容。
- MacOS：本人没有 mac 设备，此配置未在 mac 上测试，不保证可用性。

第二步，进入到配置文件夹（的父级文件夹），直接 clone 该仓库内容即可。这一份配置可以跨多平台，不需要任何修改：

```sh
git clone https://github.com/lxl66566/rime.git --recursive
```

配置文件夹：

- Linux：`~/.local/share/fcitx5/rime/`
- Windows：`C:\Users\<user_name>\AppData\Roaming\Rime`
- Andriod（fcitx5 for Andriod）：`/Android/data/org.fcitx.fcitx5.android/files/data/rime`

## 其他

- 每次更改配置后需要 _重新部署_ 才会生效。
- 更改词库可以用 vscode + [Rime formatter](https://github.com/lxl66566/rime-formatter)，我自己写的，非常好用。
- 本配置已经包含了我的 [rime-dict2](https://github.com/lxl66566/rime-dict2)。
- 我使用 git 在多设备之间同步词库；这种方法忽略了 userdb，因此我尽可能将我的习惯手动记录到 [absx.dict.yaml](dicts/absx.dict.yaml) 以保持同步。
  - 不使用官方同步功能的原因是我不太信任第三方的同步服务，然后 syncthing 又[很难用](https://t.me/withabsolutex/2090)。
