# フォントの対応を表示 (ファイルをドラッグアンドドロップ、ページ番号を入力)
import re, sys
from pypdf import PdfReader
def replaceStr(m):
  return "<" + chr(int(m.group(1), 16)) + ">"
with open(sys.argv[1], "rb") as inputFile:
  reader = PdfReader(inputFile)
  while True:
    pagenum = int(input("page number? (1 - " + str(len(reader.pages)) + ")")) - 1
    page = reader.pages[pagenum]
    try:
      fonts = page["/Resources"]["/Font"]
      for font in fonts.keys():
        print(font)
        try:
          toUnicode = fonts[font]["/ToUnicode"]
          print(re.sub("<([0-9A-F]{4})>", replaceStr, toUnicode.get_data().decode()))
        except:
          print("UnicodeTable not found")
    except:
      print("It seems that this page does not contain any font.")