from nonebot import require
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_saa")

from . import __main__ as __main__  # noqa: E402
from .config import ConfigModel, config  # noqa: E402

__version__ = "0.2.0"
__plugin_meta__ = PluginMetadata(
    name="RimoFun",
    description="用 RimoChan 开发的工具做的一个有趣的插件",
    usage=(
        "指令列表：\n"
        "注：以下指令后面带不带参数都可以，如果没带参数，Bot 将会询问你\n"
        " \n"
        "▶ unvcode\n"
        "  ▷ 介绍：反和谐超级武器，幼女 Code！\n"
        f"  ▷ 指令：{'；'.join(config.rimofun_unvcode_commands)}\n"
        " \n"
        "▶ bnhhsh\n"
        "  ▷ 介绍：不对劲的拼音首字母缩写翻译工具！\n"
        f"  ▷ 指令：{'；'.join(config.rimofun_bnhhsh_commands)}\n"
        " \n"
        "▶ yinglish\n"
        "  ▷ 介绍：淫语翻译机！\n"
        f"  ▷ 指令：{'；'.join(config.rimofun_yinglish_commands)}\n"
        " \n"
        "▶ not translator\n"
        "  ▷ 介绍：不会翻译机！\n"
        f"  ▷ 指令：{'；'.join(config.rimofun_translator_commands)}"
    ),
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-rimofun",
    type="application",
    config=ConfigModel,
    supported_adapters={
        "~onebot.v11",
        "~onebot.v12",
        "~telegram",
        "~kaiheila",
        "~qqguild",
    },
    extra={"License": "MIT", "Author": "student_2333"},
)
