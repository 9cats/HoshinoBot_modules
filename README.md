# HoshinoBot插件库
个人整理的HoshinoBot插件库，方便管理
## 主要参考
### 参考文章
 [Linux 下部署一个公主连结 qq 群聊机器人](https://cn.pcrbot.com/deploy-a-priconne-bot-on-linux/)
### 常用站点
[pcrbot](https://cn.pcrbot.com/)

[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)

[go-cqhttp](https://docs.go-cqhttp.org/guide/#go-cqhttp)

[HoshinoBot插件索引](https://github.com/pcrbot/HoshinoBot-plugins-index)

## HoshinoBot插件
| 插件 | 名称 | 作用 |
| ---- | --- | ---- |
| botmanage | 机器人管理 | 提醒/广播/清理图片/反馈/取码/邀请入群/退群/帮助/功能列表/服务端信息 |
| dice | 掷骰子 | 产生随机结果 |
| groupmaster | 群管理 | 自定义回复/入群通知/随机复读 |
| mikan | 追番 | mikan番剧订阅 |
| pcrclanbattle | 会战工具 | 机器人提供会战工具使用 |
| priconne | 一个整合modules | 抽卡/猜头像/信息查询/切噜/jjc查询 |
| Rua | 搓你 | 发送一张搓群友头像的gif图片 |
| feedback | 反馈 | 向HoshinoBot发送反馈信息 |
| aircon | 群空调 | 通过比较科学的算法来得到群活跃度 |
| antiqks | 骑空士的阴谋 | 揭发群友的阴谋 |
| gacha | 模拟抽卡 | 别看了，井田人竟是我自己 |
| pcr-avatar-guess | 猜头像 | 优衣你不识得？ |
| pcr-cherugo | 切噜 | 切啰巴切拉切蹦切蹦 |
| pcr-desc-guess | 猜角色 | 根据描述猜出角色 |
| pcr-login-bouns | 群签到 | 妈亲自来给你签到 |
| pcr-query | pcr查询 | 查找pcr的相关信息信息 |
| random-repeater | 复读机 | 概率跟着群友+1 |
| setu_mix | 涩图 | DDDD |
| sleeping-set | 精致睡眠 | 群禁言 |
| chat | 聊天 | 自定义回复群友内容 |
| rss | 推送 | 推送up主或官方 |
| PcrRun | 赛跑（下注） | pcr角色的赛跑小游戏 |
| PcrDuel | 比拼（下注） | 创建贵族进行俄罗斯转盘决斗，提升贵族等级，争夺pcr女友的小游戏 |

![关于我的项目只有setu插件更新这回事](https://img-blog.csdnimg.cn/img_convert/93e4a4317f5ffdfb7bfd4e3a732f5181.png)

关于只有我的涩图插件在更新这档事

## 各插件可用指令相关详情

### botmanage
| 服务 | 命令 | 参数 | 作用 |
| ---- | --- | ---- | ---- |
| feedback | 来杯咖啡 | 反馈内容 | 向hoshino开发组发送反馈信息 |
| data_cleaner | 清理数据 | 无 | 清理图片数据 |
| help | help/帮助 | 无 | 显示帮助菜单 |
| service_manage | enable(disable) | 服务名 | 启用(禁用)服务 |
### dice
| 服务 | 命令 | 参数 | 作用 |
| ---- | --- | ---- | ---- |
| dice | .r | [n d m] | 产生(random(1,6))[n*(1,m+1)]的随机数 |
### groupmaster
无可用命令
### mikan
| 服务 | 命令 | 参数 | 作用 |
| ---- | --- | ---- | ---- |
| mikan | 来点新番 | 无 | 订阅新番 |
### pcrclanbattle
请参考[会战机器人功能](https://github.com/9cats/HoshinoBot_modules/blob/master/pcrclanbattle/clanbattle/README.md)
### priconne

| 服务 | 命令 | 参数 | 作用 |
| ---- | --- | ---- | ---- |
| gacha | 来一井 | 无 | 抽卡 |
| avatar_guess | 猜头像 | 无 | 猜头像 |
| desc_guess | 猜角色 | 无 | 猜角色 |
(信息查询/JJC查询/切噜/没有加上)