<!-- markdownlint-disable MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/rimofun/rimofun.png" width="180" height="180"  alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-RimoFun

_✨ 基于 [RimoChan](https://github.com/RimoChan) 开发的工具的有趣插件~ ✨_

[幼女 Code](https://github.com/RimoChan/unvcode) | [不能好好说话](https://github.com/RimoChan/bnhhsh) | [淫语翻译机](https://github.com/RimoChan/yinglish) | [不会翻译机](https://github.com/RimoChan/not_translator)

<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/uv">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/4a5fe67b-9572-412a-84b8-064ca20f9157">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/4a5fe67b-9572-412a-84b8-064ca20f9157.svg" alt="wakatime">
</a>

<br />

<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-rimofun.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-rimofun">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-rimofun.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-rimofun">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-rimofun" alt="pypi download">
</a>

<br />

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-rimofun:nonebot_plugin_rimofun">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-rimofun" alt="NoneBot Registry">
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-rimofun:nonebot_plugin_rimofun">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-rimofun" alt="Supported Adapters">
</a>

</div>

## 📖 介绍

把一些 [RimoChan](https://github.com/RimoChan) 的有趣的项目揉在了一起，做出了这个插件！

## 💿 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-rimofun
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-rimofun
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-rimofun
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-rimofun
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-rimofun
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_rimofun"
]
```

</details>

## ⚙️ 配置

我真的懒得写文档了，请自行查看 [config.py](nonebot_plugin_rimofun/config.py)，感谢您的配合……

## 🎉 使用

![help](https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/rimofun/-6cb8f68366e0b5f5.png)

<!--
### 指令表

不想写文档了……累了……
看看 [\_\_init\_\_.py](nonebot_plugin_rimofun/__init__.py) 吧，谢谢您了……
-->

## 📞 联系

QQ：3076823485  
Telegram：[@lgc2333](https://t.me/lgc2333)  
吹水群：[168603371](https://qm.qq.com/q/EikuZ5sP4G)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [RimoChan](https://github.com/RimoChan)

- 感谢这位大佬写出了这些有趣的项目！！！没有这位大佬的这些精彩作品就不会有这个插件！本 fw 在这里衷心感谢……！

## 💰 赞助

**[赞助我](https://blog.lgc2333.top/donate)**

感谢大家的赞助！你们的赞助将是我继续创作的动力！

## 📝 更新日志

### 0.3.0

- 适配 Pydantic V1 & V2
- 换用 alconna

### 0.2.0

- 使用 [SAA](https://github.com/felinae98/nonebot-plugin-send-anything-anywhere) 兼容多平台消息发送

### 0.1.1

- 🎉 NoneBot 2.0 🚀
