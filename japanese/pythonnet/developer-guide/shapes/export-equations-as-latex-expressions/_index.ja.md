---
title: Python.NETを使ったExcel方程式の他フォーマットへのエクスポート
linktitle: 方程式のエクスポート
type: docs
weight: 100
url: /ja/python-net/export-equation/
description: Aspose.Cells for Python via .NETを使用してExcelの方程式をLaTeXやMathMLフォーマットにエクスポートする方法を学びます。
---

時には、作業要件を満たすためにExcelの数式を他のフォーマットにエクスポートする必要があります。Aspose.Cellsライブラリはこれを実現します。以下はExcelの式を他のフォーマットにエクスポートする方法について説明します。

Aspose.Cellsを使用して目標を達成するためのサンプルコードを準備しています。必要なサンプルファイルも提供します。

サンプルファイル：[Sample.xlsx](Sample.xlsx)

## **数式をLaTeX表現としてエクスポート**

Excelの数式をLaTeX式としてエクスポートするには、[to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/)メソッドを使用します。

以下のサンプルコードは、[to_latex()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/accentequationnode/to_la_te_x/)メソッドの使用方法を示し、生成された結果をHTMLに挿入します。

### Pythonコード

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

## **方程式をMathML表現としてエクスポート**

Excelの方程式をMathML表現としてエクスポートするには、[to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/)メソッドを使用します。

以下のサンプルコードは、[to_math_ml()](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.equations/equationnode/to_math_ml/)メソッドの使用例を示し、生成された結果をHTMLに挿入します。

### Pythonコード

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
