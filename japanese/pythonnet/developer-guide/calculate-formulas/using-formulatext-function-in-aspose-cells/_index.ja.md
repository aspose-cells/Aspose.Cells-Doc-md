---
title: Aspose.CellsとPython.NETを使用したFormulaText関数の利用例
linktitle: FormulaText関数の使用
type: docs
weight: 60
url: /ja/python-net/using-formulatext-function-in-aspose-cells/
description: Aspose.Cells for Python via .NET を使用したExcelのFORMULATEXT関数の使い方を学びましょう。スプレッドシートの整合性を保ちながらセルの数式をプログラムで取得・設定します。
keywords: Aspose.Cells、Python、Excel、FORMULATEXT、数式操作、スプレッドシート自動化
---

{{% alert color="primary" %}} 

FORMULATEXTはExcel 2013以降の関数です。Excel 2010や2007などの以前のバージョンではサポートされていません。その名前が示す通り、指定したセルに含まれる数式のテキストを表示します。この記事では、Aspose.Cells for Python via .NETを使用したこの関数の使い方を示します。

{{% /alert %}} 

以下のサンプルコードは、Aspose.Cellsを使用したFORMULATEXTの例です。まずセルA1に数式を書き込み、次にセルA2でFORMULATEXTを使って数式のテキストを表示します。

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **コンソール出力**
上記サンプルコードのコンソール出力は次のとおりです:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
