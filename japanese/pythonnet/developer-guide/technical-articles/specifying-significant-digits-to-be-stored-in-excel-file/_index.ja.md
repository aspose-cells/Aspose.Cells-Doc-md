---
title: Python.NETを使用してExcelファイルに保存される有効桁数を指定する方法
linktitle: 有意義な桁数の指定
type: docs
weight: 30
url: /ja/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aspose.Cells for Python via .NET APIを使用して、Excelファイルに格納されている有効数字の制御方法を学びます。
---

## **可能な使用シナリオ**

デフォルトでは、Aspose.CellsはExcelファイル内に64ビット浮動小数点数の17桁の有効数字を格納します。これはMS Excelの15桁のみ格納するのとは異なります。この動作は、[**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/)属性を使用して17桁から15桁に変更できます。

## **Excelファイルに保存する有効桁数を指定**

以下のサンプルコードは、Aspose.Cellsに64ビット浮動小数点数を格納する際に15桁の有効数字を使用させる方法を示しています。[出力Excelファイル](22774105.xlsx)（拡張子を.zipに変えて格納された値を確認してください）のスクリーンショットは、この設定が格納された値にどのように影響するかを示しています：

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

```python
from aspose.cells import Workbook, CellsHelper
import aspose.cells
import os
import pytest

# Set significant digits to 15
CellsHelper.set_significant_digits(15)

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set value with extended precision
cell = worksheet.cells.get("A1")
cell.put_value(1234567890123456.001234567890123456)

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CellsHelper

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Set significant digits to 15 like MS-Excel
CellsHelper.set_significant_digits(15)

# Create workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Access cell A1
c = worksheet.cells.get("A1")

# Put double value with 15 significant digits
c.put_value(1234567890.123451711)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "out_SignificantDigits.xlsx"))
```
