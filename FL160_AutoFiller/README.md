
# FL160 AutoFiller

This is a lightweight automation tool that uses the Jinja2 template engine to generate pre-filled FL160 form content based on structured input data.

## Background

During my internship at a family law firm, I encountered a repetitive pain point: manually filling out large volumes of legal forms (e.g., FL-150, FL-160) using Adobe Acrobat. The process was time-consuming, error-prone, and difficult to scale—especially for templates with little structural variation.

This repository is a lightweight prototype born out of that experience. It uses Jinja2 to generate form content from structured JSON data, providing a basic foundation for document automation in legal workflows.

Given the constraints of working in law offices—limited technical infrastructure and the highly sensitive nature of client data—this early version avoids cloud-based AI/LLMs and instead focuses on safe, deterministic generation.

The current implementation is intentionally simple. In future iterations, this tool could evolve into a more robust solution for local, secure, and scalable legal form generation.

## Features

- Template-driven form generation using Jinja2
- Simple input/output interface
- Ideal for law office automation or document preparation demos

## Project Structure
 FL160_AutoFiller/
  - Main script: renders template and writes output:
    - main.py
  - Input data for the form               
    - form_data.json     
  - Jinja2 template defining the form format
    - template.txt
  - Project introduction and instructions       
    - README.md           

## How to Use

1. **Install dependencies:**
```bash
pip3 install Jinja2
```
2.	**Edit the form data:**
    - Modify form_data.json to fit your case.
4.	**Run the script:**
```bash
  python main.py
```
4.	**Result:**
    - A file named FL160_filled_output.txt will be generated containing your filled form content.
  
## Example Use Case
**Useful for:**

	- Law offices filling out repetitive form templates
	- Demonstrating text generation using Jinja2
	- Document automation for internal workflows  


**Author: Zheyue** 

**License: MIT**
