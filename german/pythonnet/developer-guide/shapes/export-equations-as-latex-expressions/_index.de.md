---
title: Excel Ausdrücke in andere Formate mit Python.NET exportieren
linktitle: Ausdruck exportieren
type: docs
weight: 100
url: /de/python-net/export-equation/
description: Lernen Sie, wie Sie Excel Ausdrücke mit Aspose.Cells für Python via .NET in LaTeX und MathML Formate exportieren.
---

Manchmal müssen Sie Excel-Formeln in Ihrem Code in andere Formate exportieren, um Ihren Arbeitsanforderungen gerecht zu werden. Die Aspose.Cells-Bibliothek kann Ihre Anforderungen erfüllen. Der folgende Inhalt erklärt Methoden zum Exportieren von Excel-Formeln in andere Formate.

Wir haben Beispielcode vorbereitet, um Ihnen bei der Erreichung Ihrer Ziele mit Aspose.Cells zu helfen. Notwendige Beispieldateien sind ebenfalls bereitgestellt.

Beispiel-Datei: [Sample.xlsx](Sample.xlsx)

## **Ausdrücke als LaTeX-Ausdrücke exportieren**

Um Gleichungen in Excel als LaTeX-Ausdrücke zu exportieren, verwenden Sie die [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) Methode.

Der folgende Beispielcode zeigt, wie man die [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) Methode verwendet und die generierten Ergebnisse in HTML einfügt:

### Python-Code

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

## **Ausdrücke als MathML-Ausdrücke exportieren**

Um Gleichungen in Excel als MathML-Ausdrücke zu exportieren, verwenden Sie die [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) Methode.

Der folgende Beispielcode zeigt, wie man die [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) Methode verwendet und die generierten Ergebnisse in HTML einfügt:

### Python-Code

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
