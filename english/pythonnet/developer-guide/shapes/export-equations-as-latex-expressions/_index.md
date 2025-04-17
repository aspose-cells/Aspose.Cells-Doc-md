---
title: Export Excel Equations to Other Formats with Python.NET
linktitle: Export Equation
type: docs
weight: 100
url: /python-net/export-equation/
description: Learn how to export Excel equations to LaTeX and MathML formats using Aspose.Cells for Python via .NET.
---

Sometimes you may need to export Excel formulas to other formats in your code to meet your work requirements. The Aspose.Cells library can meet your needs. The following content explains methods for exporting Excel formulas to other formats.

We have prepared sample code here to help you achieve your goals using Aspose.Cells. Necessary sample files are also provided.

Sample file: [Sample.xlsx](Sample.xlsx)

## **Export Equations as LaTeX Expressions**

To export equations in Excel as LaTeX expressions, use the [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) method.

The following sample code demonstrates how to use the [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) method and insert the generated results into HTML:

### Python Code

```python
import os
from aspose.cells import Workbook
from aspose.cells.drawing import TextBox
from aspose.cells.drawing.equations import EquationNode

dir_path = "testcase/data"
workbook = Workbook(os.path.join(dir_path, "Sample_equation.xlsx"))

html_content = [
    "<!DOCTYPE html>",
    "<html lang=\"en\">",
    "<head>",
    "    <meta charset=\"UTF-8\">",
    "    <title>Title</title>",
    "    <script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script>",
    "    <script type=\"text/x-mathjax-config\">",
    "        MathJax.Hub.Config({",
    "            tex2jax: {",
    "                inlineMath: [['$','$'], ['\\\\(','\\\\)']],",
    "                processEscapes: true",
    "            }",
    "        });",
    "    </script>",
    "</head>",
    "<body>"
]

textboxes = workbook.worksheets[0].text_boxes
text_box = textboxes[0] # Assuming first shape is TextBox
math_node = text_box.get_equation_paragraph().get_child(0)
latex_expression = math_node.to_la_te_x()
html_content.append(f"<p>${latex_expression}$</p>")
html_content.append("</body>")
html_content.append("</html>")

with open("result.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_content))
```

## **Export Equations as MathML Expressions**

To export equations in Excel as MathML expressions, use the [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) method.

The following sample code demonstrates how to use the [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) method and insert the generated results into HTML:

### Python Code

```python
import os
from aspose.cells import Workbook
from typing import List

dir_path = "testcase/data/"
        
workbook = Workbook(os.path.join(dir_path, "Sample_equation.xlsx"))

html_builder = [
    "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>Title</title>\n",
    "    <script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script>\n</head>\n<body>"
]

textboxes = workbook.worksheets[0].text_boxes
text_box = textboxes[0]  # Type inferred as TextBox from ShapeCollection
math_node = text_box.get_equation_paragraph().get_child(0)
html_builder.append(math_node.to_math_ml())
html_builder.append("</body>\n</html>")

html_content = "\n".join(html_builder)

output_path = os.path.join(dir_path, "result.html")
with open(output_path, "w", encoding="utf-8") as file:
    file.write(html_content)
```