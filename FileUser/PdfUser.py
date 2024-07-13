import PyPDF2
import re
from collections import Counter
import string
import tkinter as tk
from tkinter import filedialog
import fitz
from docx import Document

def extract_text_from_pdf(pdf_path,start_page=1,end_page=999):
    # 打开PDF文件
    with open(pdf_path, 'rb') as file:
        # 创建PyPDF2的PdfFileReader对象
        pdf_reader = PyPDF2.PdfReader(file)
        # 获取PDF文档的总页数
        num_pages = len(pdf_reader.pages)
        # 确保开始页和结束页在有效范围内
        # 选择打印页数范围，未启用
        start_page = max(1, start_page)
        end_page = min(num_pages, end_page)
        # 初始化文本变量
        text = ""
        # 循环遍历每一页
        for page_num in range(num_pages):
            # 获取当前页
            page = pdf_reader.pages[page_num]

            # 提取当前页的文本--关键词
            # text = page.extract_text()
            # if re.search(key_word, text, re.IGNORECASE):
            #     print(f"Found '{key_word}' on page {page_num + 1}")

            # 提取当前页的文本
            text += page.extract_text()

    return text



def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# 前N词汇统计排名
def analyze_text(text):
    # 去除标点符号和换行符
    text = text.translate(str.maketrans('', '', string.punctuation + '\n'))
    # 转换为小写
    text = text.lower()
    # 将文本拆分为单词
    words = text.split()
    # 使用Counter进行词频统计
    word_count = Counter(words)
    # 打印词频统计结果
    print("Top 10 Words and Their Frequencies:")
    for word, frequency in word_count.most_common(10):
        print(f"{word}: {frequency}")

# 指定PDF文件路径
pdf_path = 'C:\\Users\Acer\Desktop\MOOC\计算机网络\BGP协议简介（1）.pdf'
key_word='主题'
out_file='outfile.txt'

# 调用函数提取文本
# extracted_text = extract_text_from_pdf(pdf_path)

# 打印提取的文本
# print(extracted_text)

# 调用函数保存文本到文件
# save_text_to_file(extracted_text, out_file)
# print(f"Text extracted from PDF has been saved to: {out_file}")

# 读取文本文件内容
# with open(out_file, 'r', encoding='utf-8') as file:
#     text_content = file.read()

# 调用函数进行文本处理与分析
# analyze_text(text_content)


def extract_text_from_selected_pdf():
    # 弹出文件选择对话框
    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    # 如果用户取消选择文件，则直接返回
    if not file_path:
        return
    # 调用PDF文本提取函数
    extracted_text = extract_text_from_pdf(file_path)
    # 在文本框中显示提取的文本
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, extracted_text)

# 选择PDF解析
# 创建Tkinter窗口
# root = tk.Tk()
# root.title("PDF Text Extractor")
# # 添加按钮和文本框
# browse_button = tk.Button(root, text="Choose PDF", command=extract_text_from_selected_pdf)
# browse_button.pack(pady=10)
# text_box = tk.Text(root, height=10, width=50)
# text_box.pack(pady=10)
# # 运行Tkinter事件循环
# root.mainloop()

# PDF导出为doc文件
def convert_pdf_to_docx(pdf_path, output_docx):
    doc = fitz.open(pdf_path)
    document = Document()
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()
        document.add_paragraph(text)
    document.save(output_docx)

# 指定输出的Word文档路径
# output_docx = 'converted_document.docx'
# # 调用函数进行PDF到Word的转换
# convert_pdf_to_docx(pdf_path, output_docx)
# print(f"PDF has been converted to Word document: {output_docx}")





#读取PDF文本
def extract_text_with_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text
#调用函数进行PDF文本提取
# text_with_pymupdf = extract_text_with_pymupdf(pdf_path)
# # 打印提取的文本
# print(text_with_pymupdf)


import os

# 使用函数创建文件夹
def create_directory(directory_path):
    try:
        # 如果文件夹不存在，则创建文件夹
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created successfully")
        else:
            print(f"Directory '{directory_path}' already exists")
    except OSError as error:
        print(f"Error: {error}")


#导出PDF中的图片，待实现
import fitz

def extract_images(pdf_file_path):
    doc = fitz.open(pdf_file_path)
    create_directory(pdf_filePNG_path)
    for i in range(doc.page_count):
        page = doc.load_page(i)
        image_list = page.get_images()

        for image_index, img in enumerate(page.get_images(), start=1):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            pix.save(pdf_filePNG_path +"\\"+"page-%i.png" % page.number)
            # if pix.n >= 5:       # CMYK: convert to RGB first
            #     pix = fitz.Pixmap(fitz.csRGB, pix)
            # pix.save("page-%i.png" % page.number)
            # image_path = f"{pdf_filePNG_path}_page{i+1}_image{image_index}.png"
            # print(image_path)
            # pix._writeIMG(image_path,1,85)
            # pix = None

    doc.close()
    print('导出PDF中图片成功！')


pdf_filePNG_path='C:\\Users\Acer\Desktop\MOOC\计算机网络\png2'
image_folder_path = 'images'
extract_images(pdf_path)