---
title: Python.NET ile Excel Denklemlerini Diğer Formatlara Dışa Aktarın
linktitle: Dışa Aktar Denklemi
type: docs
weight: 100
url: /tr/python-net/export-equation/
description: Aspose.Cells for Python via .NET kullanarak Excel denklemelerini LaTeX ve MathML formatlarına nasıl aktaracağınızı öğrenin.
---

Bazen, çalışma kodunuzda Excel formüllerini diğer formatlara aktarmanız gerekebilir. Aspose.Cells kütüphanesi ihtiyaçlarınızı karşılayabilir. Aşağıdaki içerik, Excel formüllerini diğer formatlara dışa aktarma yöntemlerini açıklar.

Burada Aspose.Cells kullanarak hedeflerinize ulaşmanıza yardımcı olacak örnek kodlar hazırlanmıştır. Gerekli örnek dosyalar da sağlanmıştır.

Örnek dosya: [Sample.xlsx](Sample.xlsx)

## **Denklemleri LaTeX İfadeleri Olarak Dışa Aktarın**

Excel'deki denklemleri LaTeX ifadeleri olarak dışa aktarmak için [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) metodunu kullanın.

Aşağıdaki örnek kod, [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) metodunu nasıl kullanacağınızı ve oluşturulan sonuçları HTML'ye nasıl ekleyeceğinizi gösterir:

### Python Kodu

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

## **Denklemleri MathML İfadeleri Olarak Dışa Aktarın**

Excel'de denklemleri MathML ifadeleri olarak dışa aktarmak için [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) metodunu kullanın.

Aşağıdaki örnek kod, [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) metodunu nasıl kullanacağınızı ve oluşturulan sonuçları HTML'ye nasıl ekleyeceğinizi gösterir:

### Python Kodu

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
{{< app/cells/assistant language="python-net" >}}
