# merge-pdfs

![banner](img/banner.png)

## 简介

`merge-pdfs` 是一个 Python 脚本，用于合并多个 PDF 文件。它支持自定义排序规则，确保合并后的 PDF 文件按照特定的顺序排列。

## 功能

- **自定义排序**：根据文件名前缀（封面、目录、第X页、封底）自动排序。
- **命令行操作**：支持从命令行接收源目录路径，无需手动输入。
- **一键合并**：将指定目录下的所有 PDF 文件合并为一个文件。

## 使用方法

### 运行可执行程序

对于 Windows 和 macOS 用户，可以直接运行以下可执行程序：

- **Windows**：`merge-pdfs.exe`
- **macOS**：`merge-pdfs`

#### 命令行参数

1. **命令行参数**：如果提供了命令行参数，程序将使用该参数作为源目录路径。

```bash
merge-pdfs "路径/到/你的/PDF文件目录"
```

2. **交互式输入**：如果没有提供命令行参数，程序将提示用户输入源目录路径。

#### 排序规则

- **封面.pdf**：如果有名为“封面.pdf”的文件，它将被放在第一页。
- **目录*.pdf**：所有以“目录”开头的文件将跟在封面之后，按字母顺序升序排序。
- **第*页.pdf**：所有以“第”开头的文件将跟在目录之后，按页码数字顺序排序。
- **封底.pdf**：如果有名为“封底.pdf”的文件，它将被放在最后一页。
- **其他文件**：不在上述规则中的文件将按字母顺序升序排序。

## 开发指南

### 安装依赖

确保 Python 环境已安装，并安装以下依赖库：

```bash
pip install PyPDF2
```

### 运行脚本

```bash
python merge-pdfs.py "路径/到/你的/PDF文件目录"
```

如果没有提供命令行参数，脚本将提示用户输入源目录路径。

### 代码说明

- `merge_pdfs` 函数：合并 PDF 文件的核心函数。
- `sort_pdf_files` 函数：根据自定义规则对 PDF 文件进行排序的函数。
- `get_pdf_files_from_directory` 函数：从指定目录获取所有 PDF 文件的函数。
- `get_source_directory` 函数：获取源文件目录路径的函数，支持命令行参数和交互式输入。
- `main` 函数：主函数，负责调用其他函数并执行合并操作。

### 注意事项

- 确保源目录路径正确无误。
- 脚本运行时需要有足够的权限访问和写入文件。
- 合并后的 PDF 文件将保存在源目录的上一级目录中，文件名为源目录名加“.pdf”。

## 编译指南

### 使用 PyInstaller 打包脚本

要将 `merge-pdfs` 脚本打包成可执行文件，可以使用 PyInstaller。以下是简要步骤：

1. **安装 PyInstaller**：
   
```bash
pip install pyinstaller
```

2. **打包脚本**：

```bash
pyinstaller --onefile merge-pdfs.py
```

3. **查看输出文件**：
   
可执行文件将位于 `dist` 目录下。

### 注意事项

- 确保没有其他 Python 进程正在运行 `merge-pdfs.py` 脚本。
- 打包后的可执行文件可能需要以管理员权限运行。

## 贡献

欢迎对本项目进行贡献，包括但不限于代码优化、功能扩展和 bug 修复。请在提交 pull request 前确保代码风格一致，并提供相应的测试用例。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。
