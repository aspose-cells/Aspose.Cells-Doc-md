---
title: Python.NETを使った高度な条件付き書式の適用
linktitle: 高度な条件付き書式の適用
type: docs
weight: 70
url: /ja/python-net/apply-advanced-conditional-formatting/
description: Aspose.Cells for Python via .NETを使用して、データバー、カラースケール、アイコンセットなどのExcelの高度な条件付き書式機能を実装する方法を学びます。
keywords: Python Excelの書式設定、条件付き書式Python、データバーPython、カラースケールPython、アイコンセットPython、Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007以降（2010/2013/2016）は、セルの塗りつぶし、罫線、彩色アイコン、矢印、フラグ、フォント設定などの高度な条件付き書式機能を提供しています。

{{% /alert %}} 

## **Excelファイルに高度な条件付き書式を実装**
Aspose.Cells for Python via .NETはすべての高度な条件付き書式機能をサポートしています。

- シェーディングされたデータバーを追加して、単純な棒グラフをセルに埋め込むことで、基になる数値を視覚的に強調できます。
- セルの色が他のセルの値との関係に基づいて自動的に色分けされます。デフォルトの設定では、最小値が赤で、最大値が緑になります。
- カラースケールではなくアイコンセットを使用し、セルに小さな矢印や信号機などのアイコンを追加します。

Aspose.Cellsは、実行時にMicrosoft Excel 2007およびそれ以降のバージョンでXLSX形式で提供されるセルの条件付き書式を完全にサポートしています。この例では、アイコンセット、データバー、カラースケール、時間帯、最上位/最下位などの異なる属性セットでの高度な条件付き書式タイプの演習を示します。

- [**Adding Color Scale Conditional Formattings**](/cells/ja/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/ja/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/ja/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/ja/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/ja/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/ja/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/ja/python-net/how-to-add-top10-conditional-formatting/)



### **Excelのカラー選択を使ったカラースケール書式設定を計算する**
このコードは、Excelのカラースケール条件付き書式ルールに対して選択された色を判定する方法を示しています。

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
