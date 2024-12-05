import argparse
import markdown
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
    parser.add_argument('-i', '--input_file', required=True, help="Path to the input Markdown file.")
    parser.add_argument('-o', '--output_file', help="Name of the output HTML file. Default is the same as input file.")
    return parser.parse_args()

def markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    # If no output file name is provided, use the same name as input with .html extension
    if not output_file:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{base_name}.html"

    full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.splitext(os.path.basename(input_file))[0]}</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    {html_content}
</body>
</html>
"""

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)

    print(f"Conversion successful! HTML output saved to: {output_file}")

def main():
    args = parse_arguments()
    markdown_to_html(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
