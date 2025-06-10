import json
from jinja2 import Environment, FileSystemLoader
import os

# Load JSON data
with open('data.json') as f:
    data = json.load(f)

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('portfolio_template.html')

# Render the template with data
output = template.render(data)

# Ensure the output directory exists
os.makedirs('output', exist_ok=True)

# Write the output to an HTML file
with open('output/portfolio.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("\n✅ Portfolio generated successfully! Check the 'output/portfolio.html' file.")
