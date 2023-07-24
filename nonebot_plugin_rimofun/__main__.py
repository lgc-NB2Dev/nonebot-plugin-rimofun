import random
import re
from typing import List, Literal, Type

from nonebot import on_command, on_message
from nonebot.internal.adapter import Event, Message
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.typing import T_State
from nonebot_plugin_saa import MessageFactory

from .config import config
from .data_source import (
    bnhhsh_trans,
    not_translate,
    parse_yinglish_param,
    unvcode_convert,
    yinglish_trans,
)

nickname = list(config.nickname)[0] if config.nickname else "咱"


def get_command_matcher(commands: List[str], *args, **kwargs) -> Type[Matcher]:
    return on_command(commands[0], *args, aliases=set(commands[1:]), **kwargs)


matcher_unvcode = get_command_matcher(config.rimofun_unvcode_commands)
matcher_bnhhsh = get_command_matcher(config.rimofun_bnhhsh_commands)
matcher_yinglish = get_command_matcher(config.rimofun_yinglish_commands)
matcher_translate = get_command_matcher(config.rimofun_translator_commands)


@matcher_unvcode.handle()
@matcher_bnhhsh.handle()
@matcher_yinglish.handle()
@matcher_translate.handle()
async def _(matcher: Matcher, arg: Message = CommandArg()):
    if arg.extract_plain_text().strip():
        matcher.set_arg("arg", arg)


@matcher_unvcode.got("arg", f"请问您要让{nickname}帮忙反屏蔽什么文本呢？")
@matcher_bnhhsh.got("arg", f"请问您要让{nickname}帮你解释一下什么看不懂的缩写呢？")
@matcher_yinglish.got(
    "arg",
    (
        f"{nickname}要让您接下来发出来的话变得涩涩哦♡~快请您发送消息吧！\n"
        "您还可以在消息后面跟上空格，再加上一个百分比，就可以控制生成文本的涩涩程度！"
    ),
)
@matcher_translate.got("arg", f"要让{nickname}帮您翻译一下什么语句呢？")
async def _(matcher: Matcher, arg: str = ArgPlainText("arg")):
    if not arg.strip():
        await matcher.reject(f"hmm……{nickname}没有在您刚刚发的消息里看到文本呢……请您重新发一下吧qwq")
    matcher.skip()


@matcher_unvcode.handle()
async def _(matcher: Matcher, arg: str = ArgPlainText("arg")):
    result = unvcode_convert(arg.strip())
    await matcher.finish(f"{nickname}已经帮您处理好啦！请看看下面的结果~\n{result}")


@matcher_bnhhsh.handle()
async def _(matcher: Matcher, arg: str = ArgPlainText("arg")):
    result = bnhhsh_trans(arg)
    if not result:
        await matcher.finish(f"{nickname}没有在刚刚的文本中找到英文呢……如果您还需要帮助，请重新询问我吧~")

    message = "\n".join([f"{k}：{v}" for k, v in result.items()])
    await matcher.finish(f"就让学识渊博的{nickname}来帮您解释清楚吧(/≧▽≦)/\n{message}")


@matcher_yinglish.handle()
async def _(matcher: Matcher, arg: str = ArgPlainText("arg")):
    try:
        txt, percent = parse_yinglish_param(arg.strip())
    except ValueError:
        await matcher.finish(
            f"{nickname}发现您输入的涩涩程度百分比有问题哦quq\n这个百分比需要大于 0%，同时小于等于 100% 呢……",
        )

    result = yinglish_trans(txt, percent)
    await matcher.finish(f"收到命令，{nickname}马上就让您的话语变得涩涩起来！！\n{result}")


@matcher_translate.handle()
async def _(matcher: Matcher, arg: str = ArgPlainText("arg")):
    result = not_translate(arg)
    await matcher.finish(f"请您看看{nickname}的翻译厉不厉害！嘿嘿~\n{result}")


async def trigger_rule(event: Event, state: T_State):
    msg_txt = event.get_plaintext().strip()
    if not msg_txt:
        return False

    is_english = re.fullmatch(r"^[a-zA-Z0-9@$!%*?&#^-_.+\s]+$", msg_txt)
    random_val = random.random()

    types: List[Literal["bnhhsh", "yinglish", "translator"]] = []

    if (
        is_english
        and config.rimofun_bnhhsh_reply_chance
        and random_val < config.rimofun_bnhhsh_reply_chance
    ):
        types.append("bnhhsh")

    if (
        config.rimofun_yinglish_reply_chance
        and random_val < config.rimofun_yinglish_reply_chance
    ):
        types.append("yinglish")

    if (
        is_english
        and config.rimofun_translator_reply_chance
        and random_val < config.rimofun_translator_reply_chance
    ):
        types.append("translator")

    if types:
        state["type"] = random.choice(types)
        return True

    return False


matcher_initiative = on_message(
    rule=trigger_rule,
    block=False,
    priority=config.rimofun_initiative_priority,
)


@matcher_initiative.handle()
async def _(event: Event, state: T_State):
    msg_txt = event.get_plaintext().strip()
    trigger_type: Literal["bnhhsh", "yinglish", "translator"] = state["type"]

    if trigger_type == "bnhhsh":
        result = bnhhsh_trans(msg_txt)
        reply = "\n".join([f"{k}：{v}" for k, v in result.items()])
        await MessageFactory(f"让{nickname}解释一下消息里出现的神秘字母吧~\n{reply}").finish(reply=True)

    if trigger_type == "yinglish":
        reply = yinglish_trans(msg_txt)
        await MessageFactory(f"让{nickname}来把你说的话变得更涩一点~\n{reply}").finish(reply=True)

    if trigger_type == "translator":
        reply = not_translate(msg_txt)
        await MessageFactory(f"让{nickname}把这条消息翻译一下吧！\n{reply}").finish(reply=True)
