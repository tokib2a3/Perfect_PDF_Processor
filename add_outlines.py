from pypdf import PdfReader, PdfWriter
import sys

def add_outline(output, title, page_num, parent=None):
  output.add_outline_item(title, page_num, parent)

def display_outlines(outlines, indent=0):
  flag = False
  for outline in outlines:
    if flag:
      display_outlines(outline, indent + 2)
      flag = False
    else:
      print(" " * indent + outline['/Title'])
      if '/Count' in outline:
        flag = True

def main():
  if len(sys.argv) < 2:
    print("Usage: python add_outlines.py <input_pdf_file>")
    return

  input_file = sys.argv[1]
  output = PdfWriter()

  with open(input_file, "rb") as file:
    input_pdf = PdfReader(file)

    for page in input_pdf.pages:
      output.add_page(page)

    outline_root = output.add_outline_item("Root", 0)
    while True:
      try:
        print("Enter bookmark title (or 'exit' to finish):")
        title = input()
        if title.lower() == 'exit':
          break

        print("Enter page number:")
        page_num = int(input())

        print("Enter parent bookmark title (or leave blank if none):")
        parent_title = input()
        parent = None
        if parent_title:
          parent = outline_root
          for outline in output.outline:
            if outline['/Title'] == parent_title:
              parent = outline
              break

        add_outline(output, title, page_num, parent)
        print("Bookmark added.")
      except ValueError:
        print("Invalid input. Page number must be an integer.")

    print("Outputting to result.pdf")
    with open("result.pdf", "wb") as result_file:
      output.write(result_file)

    print("\nBookmarks in the output PDF:")
    display_outlines(output.outline)

if __name__ == "__main__":
  main()
