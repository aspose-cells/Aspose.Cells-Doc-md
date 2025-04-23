---
title: 在Python.NET中指定要存储的有效数字
linktitle: 指定有效数字
type: docs
weight: 30
url: /zh/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: 了解如何使用Aspose.Cells for Python via .NET API控制存储在Excel文件中的有效数字。
---

## **可能的使用场景**

默认情况下，Aspose.Cells在Excel文件中存储双精度值时保留17位有效数字，不同于Microsoft Excel仅存储15位有效数字。你可以通过[**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/)属性将此行为从17位改为15位有效数字。

## **指定要在Excel文件中存储的有效数字**

以下示例代码强制Aspose.Cells在存储双精度值时使用15位有效数字。请查看[输出Excel文件](22774105.xlsx)（将扩展名改为.zip以检查存储的值）。下图显示了此设置如何影响存储的值：

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

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
