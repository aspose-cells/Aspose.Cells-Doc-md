---
title: Python.NETを使用したワークブックの数式計算モード設定
linktitle: ワークブックの式の計算モードを設定する
type: docs
weight: 110
url: /ja/python-net/setting-formula-calculation-mode-of-workbook/
description: Aspose.Cells for Python via .NET APIを使用して、Excelワークブックの数式計算モード（自動、手動）の設定方法を段階的に解説したコード例とともに学びます。
keywords: Python, Aspose.Cells, Excel, ワークブック, 数式計算モード, 自動, 手動, 設定
---

## **ワークブック内での数式計算モードの設定**

{{% alert color="primary" %}}

Microsoft Excelは次の3つの計算モードを提供します：
- **自動**：変更およびワークブックのオープン時に計算を再実行
- **データテーブルを除く自動**：変更時にデータテーブルを除く数式を再計算
- **手動**：ユーザーの要求（F9/CTRL+ALT+F9）または保存時のみ再計算

{{% /alert %}}

### **Aspose.Cellsを使用した計算モード設定**

Aspose.Cells for Python via .NETは[**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/)設定を[**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/)プロパティを通じて提供します。[**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/)属性を使用して計算動作を制御します。

[**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/)列挙型で利用可能なモード：
- `AUTOMATIC`
- `AUTOMATIC_EXCEPT_TABLE`
- `MANUAL`

**実装手順:**
1. 既存のワークブックを読み込むか、新規に作成
2. ワークブック設定にアクセス
3. `formula_settings.calculation_mode`を使用して計算モードを設定
4. 変更したワークブックを保存

```python
from aspose.cells import Workbook, CalcModeType

# Load source workbook
workbook = Workbook("source.xlsx")

# Configure manual calculation mode
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CalcModeType, SaveFormat

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create a workbook
workbook = Workbook()

# Set the Formula Calculation Mode to Manual
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save the workbook
output_path = os.path.join(data_dir, "output_out.xlsx")
workbook.save(output_path, SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
