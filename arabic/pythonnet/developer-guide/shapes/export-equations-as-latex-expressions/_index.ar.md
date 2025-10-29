---
title: تصدير معادلات إكسل إلى صيغ أخرى باستخدام Python.NET
linktitle: تصدير المعادلة
type: docs
weight: 100
url: /ar/python-net/export-equation/
description: تعرف على كيفية تصدير معادلات إكسل إلى صيغ LaTeX و MathML باستخدام Aspose.Cells لـ بايثون via .NET.
---

أحيانًا، قد تحتاج إلى تصدير صيغ إكسل إلى صيغ أخرى في كودك لتلبية متطلبات عملك. يمكن لمكتبة Aspose.Cells تلبية احتياجاتك. يشرح المحتوى التالي طرق تصدير معادلات إكسل إلى صيغ أخرى.

لقد أعددنا رمزًا نموذجيًا هنا لمساعدتك على تحقيق أهدافك باستخدام Aspose.Cells. كما يتم توفير ملفات العينة اللازمة.

ملف عينة: [Sample.xlsx](Sample.xlsx)

## **تصدير المعادلات كتعابير LaTeX**

لتصدير المعادلات في إكسل كتعبيرات LaTeX، استخدم الدالة [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/).

يوضح الرمز النموذجي التالي كيفية استخدام الدالة [to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/) وإدراج النتائج المُولدة في HTML:

### كود بايثون

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

## **تصدير معادلات كتعبيرات MathML**

لتصدير المعادلات في إكسل كتعبيرات MathML، استخدم الدالة [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/).

يوضح الرمز النموذجي التالي كيفية استخدام الدالة [to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/) وإدراج النتائج المُولدة في HTML:

### كود بايثون

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
