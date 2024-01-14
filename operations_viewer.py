# オペレーションの表示 (ファイルをドラッグアンドドロップ、ページ番号を入力)
import os, sys
from pypdf import PdfReader
from pypdf.generic import ContentStream
with open(sys.argv[1], "rb") as inputFile:
  reader = PdfReader(inputFile)
  while True:
    pagenum = int(input("page number? (1 - " + str(len(reader.pages)) + ")")) - 1
    page = reader.pages[pagenum]
    content = page["/Contents"]
    if not isinstance(content, ContentStream):
      stream = ContentStream(content, reader)
    i = 0
    for ope in stream.operations:
      print(i, ope)
      i += 1