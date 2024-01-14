# 複数PDFをマージ (マージするファイルすべてをドラッグアンドドロップ)
import os, sys
from pypdf import PdfMerger
print("start")
merger = PdfMerger()
for x in sys.argv[1:]:
  print("appending " + x)
  merger.append(x)
print("merging...")
outputFileName = os.path.splitext(sys.argv[1])[0] + "_merged.pdf"
merger.add_metadata(
  {
    "/Producer": "Perfect PDF Processor",
  }
)
merger.write(outputFileName)
merger.close()
print("done")