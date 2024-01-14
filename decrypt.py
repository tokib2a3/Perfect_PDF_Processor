# PDFを復号化 (復号化するファイルをドラッグアンドドロップ)
import os, sys
from pypdf import PdfReader, PdfWriter
for input_fname in sys.argv[1:]:
  reader = PdfReader(input_fname)
  writer = PdfWriter()
  if reader.is_encrypted:
    while True:
      try:
        for page in reader.pages:
          writer.add_page(page)
        output_fname = os.path.splitext(input_fname)[0] + "_decrypted.pdf"
        with open(output_fname, "wb") as f:
          writer.write(f)
        print("decrypted " + input_fname)
        break
      except:
        reader.decrypt(input("enter password for " + input_fname))
  else:
    print("the file " + input_fname + " is not encrypted")