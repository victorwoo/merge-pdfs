import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_paths, output_path):
    """
    合并多个PDF文件为一个文件。
    
    :param pdf_paths: PDF文件路径列表
    :param output_path: 输出PDF文件的完整路径
    """
    pdf_writer = PdfWriter()
    for path in pdf_paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

def sort_pdf_files(pdf_files):
    """
    根据特定规则对PDF文件进行排序。
    
    :param pdf_files: PDF文件名列表
    :return: 排序后的PDF文件名列表
    """
    # 定义特殊文件前缀
    special_prefixes = {'封面': [], '目录': [], '第': [], '封底': []}
    other_files = []

    # 将文件分配到对应的类别
    for file_name in pdf_files:
        base_name = os.path.splitext(file_name)[0]
        if base_name.startswith('封面'):
            special_prefixes['封面'].append(file_name)
        elif base_name.startswith('目录'):
            special_prefixes['目录'].append(file_name)
        elif base_name.startswith('第'):
            special_prefixes['第'].append(file_name)
        elif base_name.startswith('封底'):
            special_prefixes['封底'].append(file_name)
        else:
            other_files.append(file_name)

    # 对'目录'和'其他文件'进行字母顺序排序
    special_prefixes['目录'].sort()
    other_files.sort()

    # 对'第'页的文件按页码数字排序
    special_prefixes['第'].sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # 合并所有排序后的文件列表
    sorted_files = special_prefixes['封面'] + \
                   special_prefixes['目录'] + \
                   special_prefixes['第'] + \
                   special_prefixes['封底'] + \
                   other_files

    return sorted_files

def get_pdf_files_from_directory(directory):
    """
    获取目录下所有PDF文件。
    
    :param directory: 目录路径
    :return: PDF文件名列表
    """
    return [file for file in os.listdir(directory) if file.endswith('.pdf')]

def get_source_directory():
    """
    获取源文件目录的路径。
    
    :return: 源文件目录的路径
    """
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
        
        if os.path.isdir(source_dir):
            return source_dir        
        else:
            print(f"提供的路径 '{source_dir}' 不是一个有效的目录。")
    else:
        pass
    
    source_dir = input("请输入一个有效的源文件目录的路径：")
    if not os.path.isdir(source_dir):
        print(f"提供的路径 '{source_dir}' 不是一个有效的目录。")
        sys.exit(1)
    return source_dir

def main():
    source_dir = get_source_directory()

    # 移除路径末尾的目录分隔符
    source_dir = source_dir.rstrip(os.sep)

    # 列出源文件目录下的所有pdf文件
    pdf_files = get_pdf_files_from_directory(source_dir)

    # 根据规则对pdf的顺序做排序
    sorted_pdf_files = sort_pdf_files(pdf_files)

    # 使用PyPDF2合并源pdf文件
    output_filename = os.path.basename(source_dir) + '.pdf'
    output_path = os.path.join(os.path.dirname(source_dir), output_filename)
    full_pdf_paths = [os.path.join(source_dir, file) for file in sorted_pdf_files]
    merge_pdfs(full_pdf_paths, output_path)

    print(f"PDF文件已合并并保存为：{output_path}")

if __name__ == "__main__":
    main()