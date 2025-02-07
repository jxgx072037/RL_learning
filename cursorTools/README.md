# 图片文字识别工具

这个工具用于将图片中的文字识别出来并翻译成中文，然后可以将结果添加到Markdown笔记中。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 将图片文件放在合适的位置
2. 运行以下命令：
```bash
python image_to_notes.py <图片路径>
```

例如：
```bash
python image_to_notes.py ../images/screenshot.png
```

## 功能特点

- 支持中英文OCR识别
- 自动翻译成中文
- 保持原始格式
- 输出便于复制到Markdown文件

## 注意事项

1. 确保图片清晰可读
2. 支持的图片格式：jpg, png, bmp
3. 第一次运行时会下载必要的模型文件，可能需要一些时间 