# ページを回転 (ファイルをドラッグアンドドロップ、角度を指定)
import os, sys, math
from pypdf import PdfWriter, PdfReader, Transformation
for inputFile in sys.argv[1:]:
  angle = int(input("enter the angle to rotate (clockwise) for " + inputFile))
  reader = PdfReader(inputFile)
  writer = PdfWriter()
  for i in range(len(reader.pages)):
    writer.add_page(reader.pages[i])
    writer.pages[i].add_transformation(Transformation().rotate(angle).translate(float(reader.pages[i].mediabox.height) * math.sin(math.radians(angle)) / 2, -float(reader.pages[i].mediabox.width) * math.sin(math.radians(angle)) / 2))
  outputFileName = os.path.splitext(inputFile)[0] + "_rotated.pdf"
  writer.write(outputFileName)