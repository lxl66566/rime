# [Rime](https://blog.isteed.cc/post/rime-2022/)

![GitHub repo size](https://img.shields.io/github/repo-size/lxl66566/rime)

自用 rime 配置：fork 自 <https://github.com/LufsX/rime> ，并爆改设置，方案，词库，包含了[我个人的大量习惯](#我的习惯)，仅供参考，不建议直接使用。

Rime 的部署教程网上到处都是，我这里就不说得太详细了。

本配置支持的方案（切换方案请按 F1 键）：

- 全拼（朙月拼音）
- 小鹤双拼
- 日本語

<details>
  <summary>如何卸载日语方案</summary>
  删除所有 `japanese` 开头的 yaml 文件与 `dicts-jap` 即可。
</details>

## 使用本方案

第一步是安装 Rime 在对应平台上的替代品。

- Linux：不多说，fcitx5 + fcitx5-rime。想必用 linux 的装 rime 完全没有难度。
- Windows：安装[小狼毫](https://github.com/rime/weasel/releases)
- Android：[小企鹅输入法（fcitx5 for Andriod）](https://github.com/fcitx5-android/fcitx5-android)和[同文输入法（trime）](https://github.com/osfans/trime)都支持 rime。小企鹅输入法的默认键位等都更顺手合理，而同文输入法界面较差，需要自己画，不过支持自由选择配置位置。
  - 对于小企鹅输入法（fcitx5 for Andriod）：下载[小企鹅输入法](https://github.com/fcitx5-android/fcitx5-android/releases) 和链接下面的 `plugin.rime`。不要安装 Google Play 上的小企鹅输入法版本，和插件不兼容。
  - 对于同文输入法（trime）：在 [releases](https://github.com/osfans/trime/releases) 中下载安装即可。装完后，在 _配置 - 用户文件夹_ 里修改路径为你的配置路径。
- MacOS：本人没有 mac 设备，此配置未在 mac 上测试，不保证可用性，欢迎 PR 适配。

第二步，进入到配置文件夹的**父级文件夹**，直接 clone 该仓库 / 下载 zip 解压即可。这一份配置可以跨平台，不需要做适配性的修改：

```sh
git clone https://github.com/lxl66566/rime.git --recursive
```

配置文件夹：

- Linux：`~/.local/share/fcitx5/rime/`
- Windows：`C:\Users\<user_name>\AppData\Roaming\Rime`
- Andriod（fcitx5 for Andriod）：`/storage/emulated/0/Android/data/org.fcitx.fcitx5.android/files/data/rime`
- Andriod（同文输入法）：自定义

当然，在 Android 上用 git **非常麻烦**（需要 root，并且 termux 要玩 git 简直是地狱级难度），建议直接把整个配置文件夹从电脑上拷过去。

第三步，删除本人的私人词库：删除 `dicts/absx-personal.dict.yaml.zst.enc`，并在 `chinese.dict.yaml` 里删除该词库对应条目。我的私人词库使用 [git-simple-encrypt](https://github.com/lxl66566/git-simple-encrypt) 加密，密码为复杂型。

```sh
# 你也可以用下面的 bash 命令快速删除
rm -f "dicts/absx-personal.dict.yaml.zst.enc"
sed -i '/- dicts\/absx-personal/d' "chinese.dict.yaml"
```

## 其他

- 每次更改配置后需要 _重新部署_ 才会生效。
- 更改词库可以用 vscode + [Rime formatter](https://github.com/lxl66566/rime-formatter)，我自己写的，非常好用。
- 本配置已经包含了我做的几个其他特定领域词库：[rime-dict2](https://github.com/lxl66566/rime-dict2)。

## 我的习惯与更改

- 禁止自动建议 emoji。如果我要打 emoji，我会在拼音下输入 `emoji` 后手动选择。（配置：`dicts/emoji.dict.yaml`）
- 在数字后输入全角符号，不要自动转换为半角。（配置：`lufs_symbols.yaml punctuator/digit_separators`，[相关 issue](https://github.com/rime/librime/issues/972)）
- 禁止上下文自动建议：质量太差了。（配置：`enable_sentence: false`，[相关 issue](https://github.com/rime/home/issues/1133)）
- 禁用 userdb 个人词库：我选择将我的词语权重手动记录到 [dicts/absx.dict.yaml](dicts/absx.dict.yaml)、dicts/absx-personal.dict.yaml 和 [custom_phrase.txt](custom_phrase.txt)，通过 git 同步。（配置：`translator/enable_user_dict: false`，[相关 issue](https://github.com/rime/weasel/issues/1290)）
  - 我不太信任第三方的同步服务，然后 syncthing 又[很难用](https://t.me/withabsolutex/2090)。
  - 我个人不喜欢历史词频决定权重的方式。
  - userdb 有[一些问题](https://github.com/rime/librime/issues/1097)。
