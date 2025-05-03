# FL160 AutoFiller

This is a lightweight automation tool that uses the Jinja2 template engine to generate pre-filled FL160 form content based on structured input data.

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
