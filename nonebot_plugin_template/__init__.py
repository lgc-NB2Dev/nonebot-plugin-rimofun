from nonebot.plugin import PluginMetadata

from nonebot_plugin_template.config import ConfigModel

from .__main__ import *  # noqa: F401, F403

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    "Template",
    "插件模板",
    "这是一个一个一个插件模板",
    ConfigModel,
    {"License": "MIT", "Author": "student_2333"},
)
