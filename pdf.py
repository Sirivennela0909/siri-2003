import fitz  # PyMuPDF
import os

class PDFConverter:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def convert_to_text(self, output_path):
        try:
            doc = fitz.open(self.pdf_path)
            text = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text += page.get_text()
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Text extracted to {output_path}")
        except Exception as e:
            print(f"An error occurred while converting PDF to text: {e}")

    def convert_to_images(self, output_folder, image_format='png'):
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            doc = fitz.open(self.pdf_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                image_path = os.path.join(output_folder, f"page_{page_num + 1}.{image_format}")
                pix.save(image_path)
            print(f"Images saved to {output_folder}")
        except Exception as e:
            print(f"An error occurred while converting PDF to images: {e}")

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    if not os.path.isfile(pdf_path):
        print("The specified PDF file does not exist.")
        return

    converter = PDFConverter(pdf_path)

    while True:
        print("\nPDF Converter")
        print("1. Convert to Text")
        print("2. Convert to Images")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            output_path = input("Enter the output text file path: ")
            converter.convert_to_text(output_path)
        elif choice == '2':
            output_folder = input("Enter the output folder for images: ")
            image_format = input("Enter the image format (png/jpg): ").lower()
            if image_format not in ['png', 'jpg']:
                print("Invalid image format. Please enter 'png' or 'jpg'.")
                continue
            converter.convert_to_images(output_folder, image_format)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
