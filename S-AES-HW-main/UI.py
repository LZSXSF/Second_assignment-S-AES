import tkinter as tk
from extend_function import *
from main_function import *

# 创建主窗口
window = tk.Tk()
window.title('S-AES')
window.geometry('600x400')
window.config(bg='#e0f7fa')  # 更改背景颜色

# 尺寸设计
title_label = tk.Label(window, text='S-AES 加密解密工具', font=('Arial', 18, 'bold'), bg='#e0f7fa')
title_label.pack(pady=20)

# 选择模式部分
mode_frame = tk.Frame(window, bg='#e0f7fa')
mode_frame.pack(pady=10)

# 创建一个变量来存储选择的模式，默认为'二进制'
mode_var = tk.StringVar()
mode_var.set('二进制')

# 创建两个Radiobutton来选择模式
binary_mode_button = tk.Radiobutton(mode_frame, text='二进制', variable=mode_var, value='二进制', bg='#e0f7fa', font=('Arial', 12))
binary_mode_button.pack(side=tk.LEFT, padx=20)
text_mode_button = tk.Radiobutton(mode_frame, text='字符', variable=mode_var, value='字符', bg='#e0f7fa', font=('Arial', 12))
text_mode_button.pack(side=tk.LEFT, padx=20)

# 输入部分
input_frame = tk.Frame(window, bg='#e0f7fa')
input_frame.pack(pady=10)

# 明文(密文)输入
input_label = tk.Label(input_frame, text='明文(密文):', bg='#e0f7fa', font=('Arial', 12))
input_label.pack(side=tk.LEFT)
input_entry = tk.Entry(input_frame, width=30, font=('Arial', 12))
input_entry.pack(side=tk.LEFT, padx=5)

# 密钥输入
key_label = tk.Label(input_frame, text='密钥:', bg='#e0f7fa', font=('Arial', 12))
key_label.pack(side=tk.LEFT)
key_entry = tk.Entry(input_frame, width=30, font=('Arial', 12))
key_entry.pack(side=tk.LEFT, padx=5)

# 密钥提示
key_hint = tk.Label(input_frame, text='(请输入16bit的密钥)', bg='#e0f7fa', font=('Arial', 10), fg='gray')
key_hint.pack(side=tk.LEFT)

# 输出部分
output_frame = tk.Frame(window, bg='#e0f7fa')
output_frame.pack(pady=10)

# 输出标签
output_label = tk.Label(output_frame, text='输出:', bg='#e0f7fa', font=('Arial', 12))
output_label.pack(side=tk.LEFT)
output_entry = tk.Entry(output_frame, width=40, font=('Arial', 12))
output_entry.pack(side=tk.LEFT, padx=5)

# 加密解密按钮
button_frame = tk.Frame(window, bg='#e0f7fa')
button_frame.pack(pady=20)

# 定义加密和解密函数
def encrypt():
    output_entry.delete(0, tk.END)  # 清空输出框
    mode = mode_var.get()  # 获取选择的模式
    if mode == '二进制':
        output_entry.insert(0, Encrypt(input_entry.get(), key_entry.get()))
    else:
        output_entry.insert(0, ascii_encrypt(input_entry.get(), key_entry.get()))

def decrypt():
    output_entry.delete(0, tk.END)  # 清空输出框
    mode = mode_var.get()  # 获取选择的模式
    if mode == '二进制':
        output_entry.insert(0, Decrypt(input_entry.get(), key_entry.get()))
    else:
        output_entry.insert(0, ascii_decrypt(input_entry.get(), key_entry.get()))

# 加密和解密按钮
encrypt_button = tk.Button(button_frame, text='加密', command=encrypt, bg='#4caf50', font=('Arial', 12), fg='white')
encrypt_button.pack(side=tk.LEFT, padx=20)

decrypt_button = tk.Button(button_frame, text='解密', command=decrypt, bg='#f44336', font=('Arial', 12), fg='white')
decrypt_button.pack(side=tk.LEFT, padx=20)

# 清空和退出按钮
clear_button = tk.Button(button_frame, text='清空', command=lambda: [input_entry.delete(0, tk.END), key_entry.delete(0, tk.END), output_entry.delete(0, tk.END)], font=('Arial', 12))
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text='退出', command=window.quit, font=('Arial', 12))
exit_button.pack(side=tk.LEFT, padx=10)

# 运行界面
window.mainloop()
