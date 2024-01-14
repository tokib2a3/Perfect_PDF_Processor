# ページを90度回転 (ファイルをドラッグアンドドロップ)
import os, sys, math
from pypdf import PdfWriter, PdfReader, Transformation
for inputFile in sys.argv[1:]:
  reader = PdfReader(inputFile)
  writer = PdfWriter()
  for i in range(len(reader.pages)):
    writer.add_page(reader.pages[i])
    writer.pages[i].rotate(90)
  outputFileName = os.path.splitext(inputFile)[0] + "_rotated.pdf"
  writer.write(outputFileName)