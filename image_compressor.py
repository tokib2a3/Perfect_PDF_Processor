# 画像を圧縮 (ファイルをドラッグアンドドロップ)
import os, sys
from pypdf import PdfReader, PdfWriter

def compress_images(inputFile, quality=80):
  reader = PdfReader(inputFile)
  writer = PdfWriter()
  count = 1
  for page in reader.pages:
    writer.add_page(page)
  for page in writer.pages:
    for image in page.images:
      image.replace(image.image, quality=quality)
  outputFileName = os.path.splitext(inputFile)[0] + "_compressed.pdf"
  writer.write(outputFileName)

if __name__ == "__main__":
  for inputFile in sys.argv[1:]:
    print(inputFile + ": compressing images...")
    compress_images(inputFile, input("quality (default: 80): "))