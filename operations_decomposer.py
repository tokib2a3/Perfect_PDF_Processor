# オペレーションの分解と表示 (ファイルをドラッグアンドドロップ、ページ番号を入力)
import os, sys
from pypdf import PdfReader, PdfWriter, PageObject
from pypdf.generic import ContentStream, NameObject
with open(sys.argv[1], "rb") as inputFile:
  reader = PdfReader(inputFile)
  while True:
    writer = PdfWriter()
    pagenum = int(input("page number? (1 - " + str(len(reader.pages)) + ")")) - 1
    page = reader.pages[pagenum]
    content = page["/Contents"]
    if not isinstance(content, ContentStream):
      stream = ContentStream(content, reader)
    i = 0
    for ope in stream.operations:
      newpage = PageObject.create_blank_page(reader)
      print(i, ope)
      temp = ContentStream(content, reader)
      del temp.operations[i+1:len(temp.operations)]
      newpage[NameObject("/Contents")] = temp
      newpage[NameObject("/Resources")] = page["/Resources"]
      writer.add_page(newpage)     
      i += 1
    outputFileName = os.path.splitext(sys.argv[1])[0] + "_operations_page" + str(pagenum + 1) + ".pdf"
    writer.write(outputFileName)