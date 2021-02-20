import os
import random


from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment


from hoshino import R, Service, priv


sv = Service('mawo', enable_on_default=True, visible=False)
xcw_folder = R.get('record/mawo/').path


def get_xcw():
    files = os.listdir(xcw_folder)
    filename = random.choice(files)
    rec = R.get('record/mawo/', filename)
    return rec


@sv.on_fullmatch('骂我', only_to_me=True)
async def xcw(bot, ev) -> MessageSegment:
    # conditions all ok, send a xcw.
    file = get_xcw()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
        sv.logger.error(xcw_folder)
        sv.logger.error(f'file:///{os.path.abspath(file.path)}')
