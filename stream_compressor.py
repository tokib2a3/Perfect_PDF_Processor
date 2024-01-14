# ストリームを圧縮 (ファイルをドラッグアンドドロップ)
import os, sys
from pypdf import PdfReader, PdfWriter

def compress_stream(inputFile):
  reader = PdfReader(inputFile)
  writer = PdfWriter()
  for page in reader.pages:
    writer.add_page(page)
  for page in writer.pages:
    page.compress_content_streams()
  # writer.add_metadata(reader.metadata)
  outputFileName = os.path.splitext(inputFile)[0] + "_compressed.pdf"
  writer.write(outputFileName)

if __name__ == "__main__":
  for inputFile in sys.argv[1:]:
    print(inputFile + ": compressing stream...")
    compress_stream(inputFile)