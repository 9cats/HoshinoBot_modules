# TODO: rewrite this


import random
from datetime import timedelta

import nonebot
from nonebot import Message, MessageSegment, message_preprocessor, on_command
from nonebot.message import _check_calling_me_nickname

import hoshino
from hoshino import R, Service, util

# ============================================ #

BANNED_WORD = (
    'rbq', 'RBQ', '憨批', '废物', '死妈', '崽种', '傻逼', '傻逼玩意',
    '没用东西', '傻B', '傻b', 'SB', 'sb', '煞笔', 'cnm', '爬', 'kkp',
    'nmsl', 'D区', '口区', '我是你爹', 'nmbiss', '弱智', '给爷爬', '杂种爬','爪巴'
)
@on_command('ban_word', aliases=BANNED_WORD, only_to_me=True)
async def ban_word(session):
    ctx = session.ctx
    user_id = ctx['user_id']
    msg_from = str(user_id)
    if ctx['message_type'] == 'group':
        msg_from += f'@[群:{ctx["group_id"]}]'
    elif ctx['message_type'] == 'discuss':
        msg_from += f'@[讨论组:{ctx["discuss_id"]}]'
    hoshino.logger.critical(f'Self: {ctx["self_id"]}, Message {ctx["message_id"]} from {msg_from}: {ctx["message"]}')
    hoshino.priv.set_block_user(user_id, timedelta(hours=8))
    pic = R.img(f"chieri{random.randint(1, 4)}.jpg").cqcode
    await session.send(f"不理你啦！バーカー\n{pic}", at_sender=True)
    await util.silence(session.ctx, 8*60*60)
