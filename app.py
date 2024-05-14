from flask import Flask, request, send_file
import os
from watermark import add_invisible_watermark

app = Flask(__name__)

@app.route('/purchase', methods=['POST'])
def purchase():
    email = request.form['email']
    input_pdf = "input_book.pdf"
    output_pdf = f"watermarked_books/{email}.pdf"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    
    # Add watermark
    add_invisible_watermark(input_pdf, email, output_pdf)
    
    # Generate download link (example link, you might use a more secure method)
    download_link = f"http://yourdomain.com/download/{email}.pdf"
    
    # Send the download link to the user (via email or directly in response)
    return {"download_link": download_link}

@app.route('/download/<email>.pdf', methods=['GET'])
def download(email):
    output_pdf = f"watermarked_books/{email}.pdf"
    return send_file(output_pdf, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
