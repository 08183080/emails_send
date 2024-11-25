# emails_send
邮箱群发器，目前只支持网易邮箱。

# log
- [x] 11/25，我的【AI信息流】项目遇到问题，启发我想剥离出邮件群发器，花了10min做好了


# how-to-use
1.电脑环境变量设置网易邮箱开发者授权码：'wangyi_emai_auth'

2.发送的邮件列表用 emails.txt 存储


# cmds:
执行以下命令导出生成exe可执行文件：

```pyinstaller -F .\app.py --windowed --icon D:\emails_send\logo.png```