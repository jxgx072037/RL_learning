import easyocr
from translate import Translator
import os
import sys
from PIL import Image

class ImageToNotes:
    def __init__(self):
        # 初始化OCR读取器，支持中英文
        self.reader = easyocr.Reader(['ch_sim', 'en'])
        # 初始化翻译器
        self.translator = Translator(to_lang='zh')
        
    def process_image(self, image_path):
        """处理图片，返回识别的文字"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"找不到图片文件：{image_path}")
            
        # 读取图片
        result = self.reader.readtext(image_path)
        
        # 提取文字
        text = '\n'.join([item[1] for item in result])
        return text
    
    def translate_text(self, text):
        """翻译文字"""
        try:
            return self.translator.translate(text)
        except Exception as e:
            print(f"翻译时出错：{str(e)}")
            return text
    
    def process_and_translate(self, image_path):
        """处理图片并翻译"""
        text = self.process_image(image_path)
        translated = self.translate_text(text)
        return text, translated

def main():
    if len(sys.argv) < 2:
        print("使用方法：python image_to_notes.py <图片路径>")
        return
        
    image_path = sys.argv[1]
    processor = ImageToNotes()
    
    try:
        original, translated = processor.process_and_translate(image_path)
        print("\n原文：")
        print(original)
        print("\n翻译：")
        print(translated)
    except Exception as e:
        print(f"处理过程中出错：{str(e)}")

if __name__ == "__main__":
    main() 