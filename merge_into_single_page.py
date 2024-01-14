# 単一ページにマージ (ファイルをドラッグアンドドロップ)
import os, sys
from pypdf import PdfWriter, PdfReader, Transformation, PaperSize

tatepages = 9
yokopages = 4

for inputFile in sys.argv[1:]:
  reader = PdfReader(inputFile)
  writer = PdfWriter()

  # Create a new blank page to merge
  # 横向き
  #new_page = writer.add_blank_page(PaperSize.A4.height, PaperSize.A4.width)
  # 縦向き
  new_page = writer.add_blank_page(PaperSize.A4.width, PaperSize.A4.height)

  # Calculate the size of each grid cell
  page_width = new_page.mediabox.width / yokopages
  page_height = new_page.mediabox.height / tatepages

  # Loop through each cell of the 3x4 grid
  for i in range(0, tatepages):
    for j in range(0, yokopages):
      page_index = i * yokopages + j

      # Check if there are more pages to add
      if page_index < len(reader.pages):
        page = reader.pages[page_index]
        page.scale_to(page_width, page_height)
        page.mediabox = new_page.mediabox
        page.cropbox = new_page.cropbox

        # Calculate the coordinates of the cell
        x = j * page_width
        y = (tatepages - i - 1) * page_height  # Reverse the order for correct placement

        # Add the page to the cell
        page.add_transformation(Transformation().translate(x, y))
        new_page.merge_page(page)

  # Save the modified PDF
  outputFileName = os.path.splitext(inputFile)[0] + "_merged.pdf"
  writer.write(outputFileName)
  writer.close()