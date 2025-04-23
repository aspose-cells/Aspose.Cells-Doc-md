---
title: Python.NETを使用した配列数式のデータテーブルの計算
linktitle: データテーブルの配列式の計算
type: docs
weight: 70
url: /ja/python-net/calculation-of-array-formula-of-data-tables/
description: Aspose.Cells for Python via .NET APIを使用してExcelデータテーブルの配列数式を計算する方法を学習します。 プログラムでスプレッドシートを変更し、保存します。
keywords: Python Excelデータテーブル、Python配列数式、Aspose.Cells Python、データテーブル計算Python、Excel自動化Python
---

{{% alert color="primary" %}}

Microsoft Excelでは、Data > What-If Analysis > Data Table...を使ってデータテーブルを作成できます。Aspose.Cells for Python via .NETは、データテーブルの配列数式を計算することを可能にします。 任意の数式を計算する場合は [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) を使用してください。

{{% /alert %}}

以下の例では、[ソースExcelファイル](5115535.xlsx)を使用しています。セルB1の値を100に変更すると、ハイライトされた黄色のデータテーブルの値が120に更新され、以下のスクリーンショットのようになります。Pythonコードはこの [出力PDF](5115538.pdf) を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下は、[ソースExcelファイル](5115535.xlsx)から[出力PDF](5115538.pdf)を生成するPythonの実装例です：

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Pythonコードの解説:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
