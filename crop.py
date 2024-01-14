# クロップ (単一ファイルをドラッグアンドドロップ)
import os, sys
from pypdf import PdfReader, PdfWriter
with open(sys.argv[1], "rb") as inputFile:
  reader = PdfReader(inputFile)
  writer = PdfWriter()
  for page in reader.pages:
    width = page.mediabox.right - page.mediabox.left
    height = page.mediabox.top - page.mediabox.bottom

    page.mediabox.top -= height / 17.5
    page.mediabox.bottom += height / 13.0
    page.cropbox.top -= height / 17.5
    page.cropbox.bottom += height / 13.0

    writer.add_page(page)
  writer.add_metadata(reader.metadata)
outputFileName = os.path.splitext(sys.argv[1])[0] + "_cropped.pdf"
writer.write(outputFileName)