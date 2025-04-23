---
title: 在 Python.NET 中对德语区域设置的支持，用于命名范围公式
linktitle: 支持在命名范围公式中使用德国区域设置
type: docs
weight: 60
url: /zh/python-net/support-for-german-locale-in-named-range-formulae/
description: 了解如何使用 Aspose.Cells for Python 处理 Excel 中德语区域设置的命名范围公式，编号 via .NET。
---

 英文公式以文本形式写入命名区域。这个Excel文件可以在系统配置为德语区域的环境中打开，英文公式将被翻译成德语。此示例需要安装配置为德语的Excel以及系统区域设置为德语。

 测试此功能的示例文件可从以下网址下载：  
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
