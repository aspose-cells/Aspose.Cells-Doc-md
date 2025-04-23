---
title: Esporta equazioni di Excel in altri formati con Python.NET
linktitle: Esporta Equazione
type: docs
weight: 100
url: /it/python-net/export-equation/
description: Scopri come esportare equazioni di Excel in formati LaTeX e MathML usando Aspose.Cells per Python via .NET.
---

A volte, potrebbe essere necessario esportare formule di Excel in altri formati nel tuo codice per soddisfare le esigenze lavorative. La libreria Aspose.Cells può soddisfare le tue esigenze. Il contenuto seguente spiega i metodi per esportare formule di Excel in altri formati.

Abbiamo preparato un esempio di codice qui per aiutarti a raggiungere i tuoi obiettivi usando Aspose.Cells. Sono anche forniti i file di esempio necessari.

File di esempio: [Sample.xlsx](Sample.xlsx)

## **Esporta Equazioni come Espressioni LaTeX**

Per esportare le equazioni in Excel come espressioni LaTeX, usa il metodo [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/)

Il seguente esempio di codice dimostra come usare il metodo [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) e inserire i risultati generati in HTML:

### Codice Python

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

## **Esporta Equazioni come Espressioni MathML**

Per esportare le equazioni di Excel come espressioni MathML, usa il metodo [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/)

Il seguente esempio di codice mostra come utilizzare il metodo [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) e inserire i risultati generati in HTML:

### Codice Python

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
