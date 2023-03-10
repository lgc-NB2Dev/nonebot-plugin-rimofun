import re
from typing import Dict, List, Tuple

from nonebot import logger
from unvcode import unvcode
from yinglish import chs2yin

from .bnhhsh.bnhhsh import dp
from .config import config
from .not_translator.not_translator import translate


def char_to_hex(s):
    return f"0x{s.encode('utf-8').hex()}"


def unvcode_convert(txt: str) -> str:
    result, mse = unvcode(txt, mse=config.rimofun_unvcode_mse)
    change_dict: Dict[str, Tuple[str, float]] = {
        txt[i]: (result[i], x) for i, x in enumerate(mse) if (x is not None)
    }

    for ori, (res, n) in change_dict.items():
        logger.debug(
            "unvcode: "
            f"替换 {ori}({char_to_hex(ori)}) -> {res}({char_to_hex(res)}) "
            f"({(1-n) * 100:.2f}% 相似)",
        )

    return result


def bnhhsh_trans(txt: str) -> Dict[str, str]:
    words: List[str] = [x.lower() for x in re.findall(r"[a-zA-Z-_]+", txt)]
    will_trans = []
    for it in words:
        if it not in will_trans:
            will_trans.append(it)

    translated = [dp(x) for x in will_trans]

    if config.rimofun_bnhhsh_unvcode:
        translated = [unvcode_convert(x) for x in translated]

    return {will_trans[i]: x for i, x in enumerate(translated)}


def parse_yinglish_param(params: str) -> Tuple[str, float]:
    if params.endswith("%"):
        param_li = params.split(" ")

        txt = " ".join(param_li[:-1])
        percent = param_li[-1][:-1]

        if re.fullmatch(r"^([0-9]+)(.([0-9]+))?$", percent):
            percent_num = float(percent) / 100
            if not 0 < percent_num <= 1:
                raise ValueError

            return txt, percent_num

    return params, config.rimofun_yinglish_yingness


def yinglish_trans(txt: str, yingness: float = config.rimofun_yinglish_yingness) -> str:
    result = chs2yin(txt, yingness)

    if config.rimofun_yinglish_unvcode:
        return unvcode_convert(result)

    return result


def not_translate(txt: str) -> str:
    return translate(txt)
