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
| rua | 搓你 | 发送一张搓群友头像的gif图片 |
| setu_renew | 涩图 | 发送涩图，DDDD |
| rss | 推送 | 推送up主或官方 |
| xcw | 小仓唯 | 别骂了别骂了，我就是hentai |

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
### rua
@某人并加上"rua"，就能让机器人发送一个挫头像的gif图
### setu_renew
来 [num] 张 [keyword] 涩/色/瑟图 : 来num张keyword的涩图 (不指定数量与关键字发送一张随机涩图)
涩/色/瑟图 : 发送一张随机涩图
本日涩图排行榜 [page] : 获取[第page页]p站排行榜(需开启acggov模块)
看涩图 [n] 或 [start end] : 获取p站排行榜[第n名/从start名到end名]色图(需开启acggov模块)
提取图片 pid : 获取指定pid的图片,若本地有则会直接发送,否则将给出原图链接.
### rss
rss help : 查看帮助
rss add rss地址 : 添加rss订阅,需使用完整rss订阅网址.
rss addb up主id 或 rss add-bilibili up主id : 添加b站up主订阅
rss addr route 或 rss add-route route : 添加rsshub route订阅, route请查询rsshub文档.
rss list : 查看订阅列表
rss rm 序号 或 rss remove 序号 : 删除订阅列表指定项
rss mode 模式id : 设置推送消息模式 0=标准模式(默认),推送消息包含详情及图片 1=简略模式,推送消息仅包含标题
### xcw
@xcw并加上"骂我"，然后你就是hentai了