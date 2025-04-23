---
title: Exportar ecuaciones de Excel a otros formatos con Python.NET
linktitle: Exportar ecuación
type: docs
weight: 100
url: /es/python-net/export-equation/
description: Aprende cómo exportar ecuaciones de Excel a los formatos LaTeX y MathML usando Aspose.Cells para Python via .NET.
---

A veces, es necesario exportar las fórmulas de Excel a otros formatos en tu código para cumplir con los requisitos de tu trabajo. La biblioteca Aspose.Cells puede satisfacer tus necesidades. El siguiente contenido explica métodos para exportar fórmulas de Excel a otros formatos.

Aquí hemos preparado un código de ejemplo para ayudarte a lograr tus objetivos usando Aspose.Cells. También se proporcionan los archivos de muestra necesarios.

Archivo de ejemplo: [Sample.xlsx](Sample.xlsx)

## **Exportar ecuaciones como expresiones LaTeX**

Para exportar ecuaciones en Excel como expresiones LaTeX, usa el método [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/).

El siguiente código de ejemplo demuestra cómo usar el método [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) e insertar los resultados generados en HTML:

### Código en Python

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

## **Exportar ecuaciones como expresiones MathML**

Para exportar ecuaciones en Excel como expresiones MathML, usa el método [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/).

El siguiente código de ejemplo demuestra cómo usar el método [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) e insertar los resultados generados en HTML:

### Código en Python

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
