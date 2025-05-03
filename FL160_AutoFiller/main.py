from jinja2 import Template
import json

#read template
with open("template.txt",'r',encoding='utf-8') as f:
    template_text = f.read()

# read data from form
with open("form_data.json","r",encoding = "utf-8") as f:
  form_data = json.load(f)

# Rendering template
template = Template(template_text)
output = template.render(form_data)

#output file
with open("FL160_filled_output.txt","w",encoding="utf-8") as f:
    f.write(output)
print("FL160_filled_output.txt created successfully!")