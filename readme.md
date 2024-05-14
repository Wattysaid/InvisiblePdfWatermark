# Automated PDF Watermarking System

This repository contains a Python-based solution to automatically add an invisible watermark to PDF files upon user purchase. The watermark is a unique hash generated from the purchaser's email address. This helps trace the origin of any unauthorized distribution of the document.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Flask Server](#running-the-flask-server)
- [Deployment](#deployment)
- [Security Considerations](#security-considerations)
- [Acknowledgements](#acknowledgements)

## Overview

This project provides an automated system for:

1. Handling user purchases.
2. Generating a unique hash based on the purchaser's email.
3. Embedding an invisible watermark in the purchased PDF.
4. Providing a secure download link for the watermarked PDF.

## Features

- **Invisible Watermarking:** Embeds a unique, nearly invisible watermark in each PDF.
- **Automated Process:** Fully automated from purchase to delivery.
- **Flask-based Web Server:** Handles user purchases and serves watermarked PDFs.
- **Unique Download Links:** Securely delivers watermarked PDFs to purchasers.

## Prerequisites

- Python 3.7 or higher
- Flask
- PyMuPDF (also known as `fitz`)
- hashlib
- A web server for deployment (e.g., Heroku, AWS)

## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/pdf-watermarking-system.git
cd pdf-watermarking-system
```

2. **Clone the Repository:**

### Install Dependencies:

```bash
pip install -r requirements.txt
```
3. **Usage**
   Generate Hash and Add Invisible Watermark
The script watermark.py contains the function to generate a unique hash and add an invisible watermark to a PDF.

```python
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

```
