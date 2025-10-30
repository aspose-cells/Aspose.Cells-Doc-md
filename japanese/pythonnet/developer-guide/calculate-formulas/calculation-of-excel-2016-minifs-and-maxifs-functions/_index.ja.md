---
title: Excel 2016のMINIFSとMAXIFS関数をPython.NETで計算する例
linktitle: Excel 2016のMINIFSおよびMAXIFS関数の計算
type: docs
weight: 300
url: /ja/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Aspose.Cells for Python via .NET APIを使用してExcel 2016のMINIFSとMAXIFS関数を計算する方法とサンプルコードを学びます。
keywords: python excel、minifs maxifs、数式計算、aspose.cells
---

## **可能な使用シナリオ**
Microsoft Excel 2016はMINIFSとMAXIFS関数をサポートしています。これらの関数はExcel 2013以前ではサポートされていません。Aspose.Cellsもこれらの関数の計算をサポートしています。以下のスクリーンショットはこれらの関数の使用例です。スクリーンショット内の赤いコメントを読んで、これらの関数の動作を理解してください。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016のMINIFSおよびMAXIFS関数の計算**
以下のサンプルコードは、[サンプルExcelファイル](5115149.xlsx)を読み込み、[workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)メソッドを呼び出して数式計算を実行し、その結果を[出力PDF](5115154.pdf)として保存します。


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
{{< app/cells/assistant language="python-net" >}}
