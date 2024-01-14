# 画像を抽出 (ファイルをドラッグアンドドロップ)
import os, sys
from pypdf import PdfReader

def extract(inputFile):
  reader = PdfReader(inputFile)
  count = 1
  for page in reader.pages:
    folderPath = os.path.splitext(inputFile)[0] + "_images"
    for image_file_object in page.images:
      os.makedirs(folderPath, exist_ok=True)
      outputFilePath = folderPath + "/" + str(count) + "_" + image_file_object.name
      if (os.path.isfile(outputFilePath)):
        print("file already exists in " + outputFilePath)
      else:
        with open(folderPath + "/" + str(count) + "_" + image_file_object.name, "wb") as fp:
          fp.write(image_file_object.data)
      count += 1

if __name__ == "__main__":
  for inputFile in sys.argv[1:]:
    print(inputFile + ": extracting...")
    extract(inputFile)