---
title: Microsoft Excelの数式監視ウィンドウにセルを追加（Python.NET）
linktitle: 数式の監視ウィンドウにセルを追加
type: docs
weight: 60
url: /ja/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Aspose.Cells for Python via .NETを使用して、Excelの数式監視ウィンドウのセルを監視する方法を学びます。コード例とAPIリファレンスを含みます。
keywords: python excel、数式監視ウィンドウ、セル監視、aspose.cells、python.net
---

## **可能な使用シナリオ**

Microsoft Excelの監視ウィンドウは、セルの値や数式を便利に監視できるツールです。*監視ウィンドウ*は、`数式 > 監視ウィンドウ`に移動して開けます。*追加監視*ボタンでセルを追加でき、同様に、[**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/)メソッドを用いてAspose.Cells APIでプログラム的にセルを監視ウィンドウに追加できます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

次のサンプルコードは、セルC1とE1に数式を設定し、それらをウォッチウィンドウに追加します。ワークブックを [出力Excelファイル](67338481.xlsx) として保存します。Excelで出力ファイルを開くと、両方のセルが次のようにウォッチウィンドウに表示されます：

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
