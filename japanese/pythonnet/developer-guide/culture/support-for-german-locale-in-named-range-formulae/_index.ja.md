---
title: Python.NETによるドイツ語ロケール対応の名前付き範囲式のサポート
linktitle: 名前付き範囲式におけるドイツ語ロケールのサポート
type: docs
weight: 60
url: /ja/python-net/support-for-german-locale-in-named-range-formulae/
description: Aspose.Cells for Pythonを使用して、エクセルの名前付き範囲式でドイツ語ロケール設定を処理する方法について学びます。via .NET。
---

英語の式は名前付き領域に書き込まれます。このExcelファイルは、システムがドイツ語ロケールに設定されている環境で開くことができ、英語の式はドイツ語に翻訳されます。この例では、ドイツ語環境のExcelとシステムロケール設定が必要です。

この機能のテスト用のサンプルファイルは以下からダウンロードできます：  
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
{{< app/cells/assistant language="python-net" >}}
