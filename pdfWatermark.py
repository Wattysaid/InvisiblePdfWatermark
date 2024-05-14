import fitz  # PyMuPDF
import hashlib

def generate_hash(email):
    hash_object = hashlib.sha256(email.encode())
    return hash_object.hexdigest()

def add_invisible_watermark(pdf_path, email, output_path):
    unique_hash = generate_hash(email)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page and add the watermark
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Add watermark text
        watermark_text = f"Unique ID: {unique_hash}"
        
        # Set the text as invisible (very small font and white color)
        text = fitz.TextWriter(page.rect)
        text.append(0, 0, watermark_text, fontsize=0.1, color=(1, 1, 1))
        page.insert_textbox(page.rect, watermark_text, fontsize=0.1, color=(1, 1, 1), rotate=0)
        
    # Save the watermarked PDF
    pdf_document.save(output_path)
    pdf_document.close()

# Example usage
email = "buyer@example.com"
input_pdf = "input_book.pdf"
output_pdf = "watermarked_book.pdf"
add_invisible_watermark(input_pdf, email, output_pdf)
