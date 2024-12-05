# m324-task-2-git_Justin_Urbanek

## Overview

This project provides a Python script that converts a Markdown file into an HTML file, applying a `main.css` stylesheet to the output HTML. The generated HTML is properly structured with `DOCTYPE`, `<html>`, `<head>`, and `<body>` tags, making it a valid HTML5 document.

## Setup

### Pre-requisites

1. **Python 3.x** installed on your system.
2. **`markdown` Python package** installed.

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/Draud-Egomann/m324-task-2-git_Justin_Urbanek.git
    cd m324-task-2-git_Justin_Urbanek
    ```

2. **Create a virtual environment** (optional but recommended for managing dependencies):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    The script requires the `markdown` library to convert Markdown to HTML. Install it with pip:

    ```bash
    pip install markdown
    ```

4. **Prepare the `main.css` file**:

    The script expects a `main.css` file to be present in the same directory as the generated HTML file. You can customize your own `main.css` file or use a basic one with styles for headers, paragraphs, and other elements.

### Usage

To run the script, use the following command:

```bash
python script.py -i input.md -o output.html
```