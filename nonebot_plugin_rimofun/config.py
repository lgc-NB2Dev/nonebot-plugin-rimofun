from typing import List, Set

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    nickname: Set[str]

    # unvcode
    rimofun_unvcode_mse: float = 0.2
    """unvcode 的全局字符串不同阈值，比如 0.2 代表匹配 80% 相同的字符"""

    rimofun_unvcode_commands: List[str] = ["unvcode", "幼女码"]
    """手动触发 bnhhsh 的命令"""

    # bnhhsh
    rimofun_bnhhsh_unvcode: bool = True
    """bnhhsh 是否使用 unvcode 反和谐"""

    rimofun_bnhhsh_commands: List[str] = ["bnhhsh", "不能好好说话"]
    """手动触发 bnhhsh 的命令"""

    rimofun_bnhhsh_reply_chance: float = 0.0
    """bnhhsh 自动回复纯英文消息的触发概率，值应在 0~1 之间"""

    # yinglish
    rimofun_yinglish_unvcode: bool = False
    """yinglish 是否使用 unvcode 反和谐"""

    rimofun_yinglish_commands: List[str] = ["yinglish", "淫语"]
    """手动触发 yinglish 的命令"""

    rimofun_yinglish_reply_chance: float = 0.0
    """yinglish 自动回复任意文本消息的触发概率，值应在 0~1 之间"""

    rimofun_yinglish_yingness: float = 0.7
    """yinglish 默认淫乱度，值应在 0~1 之间"""

    # not translator
    rimofun_translator_commands: List[str] = ["not translator", "不会翻译"]
    """手动触发 not-translator 的命令"""

    rimofun_translator_reply_chance: float = 0.0
    """translator 自动回复纯英文消息的触发概率，值应在 0~1 之间"""

    # other
    rimofun_initiative_priority: int = 99
    """自动回复 matcher 的优先级"""


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
