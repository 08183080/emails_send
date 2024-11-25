import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yagmail

def get_contents(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def get_emails(path):
    with open(path, 'r') as f:
        return f.read().splitlines()

def send_email(src, dst, subject, contents, attachments):
    pwd = os.environ.get('wangyi_emai_auth')

    yag = yagmail.SMTP(user=src, password=pwd, host='smtp.163.com', port='465')
    yag.send(to=dst, subject=subject, contents=contents, attachments=attachments)
    yag.close()

def send_emails(src, tos, subject, contents, attachments):
    for to in tos:
        send_email(src, to, subject, contents, attachments)

def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        entry_attachment.delete(0, tk.END)
        entry_attachment.insert(0, filepath)

def browse_emails_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        entry_emails.delete(0, tk.END)
        entry_emails.insert(0, filepath)

def start_sending():
    src = entry_email.get()
    tos = get_emails(entry_emails.get())
    subject = entry_subject.get()
    contents = text_contents.get("1.0", tk.END)
    attachments = entry_attachment.get()

    if not src or not tos or not subject or not contents:
        messagebox.showerror("错误", "请填写所有必填信息")
        return

    try:
        send_emails(src, tos, subject, contents, attachments)
        messagebox.showinfo("成功", "邮件已成功发送")
    except Exception as e:
        messagebox.showerror("错误", f"发送邮件时发生错误: {e}")

# 创建主窗口
root = tk.Tk()
root.title("邮箱群发器")

# 创建标签和输入框
tk.Label(root, text="发件人邮箱:").grid(row=0, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1)

tk.Label(root, text="收件人邮箱列表文件:").grid(row=1, column=0)
entry_emails = tk.Entry(root)
entry_emails.grid(row=1, column=1)
tk.Button(root, text="浏览", command=browse_emails_file).grid(row=1, column=2)

tk.Label(root, text="邮件主题:").grid(row=2, column=0)
entry_subject = tk.Entry(root)
entry_subject.grid(row=2, column=1)

tk.Label(root, text="邮件内容:").grid(row=3, column=0)
text_contents = tk.Text(root, height=10, width=50)
text_contents.grid(row=3, column=1)

tk.Label(root, text="附件:").grid(row=4, column=0)
entry_attachment = tk.Entry(root)
entry_attachment.grid(row=4, column=1)
tk.Button(root, text="浏览", command=browse_file).grid(row=4, column=2)

# 创建发送按钮
send_button = tk.Button(root, text="发送邮件", command=start_sending)
send_button.grid(row=5, column=1)

# 启动主循环
root.mainloop()