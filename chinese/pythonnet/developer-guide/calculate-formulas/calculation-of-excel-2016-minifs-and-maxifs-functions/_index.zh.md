---
title: 使用Python.NET计算Excel 2016的MINIFS和MAXIFS函数
linktitle: 计算Excel 2016 MINIFS和MAXIFS函数
type: docs
weight: 300
url: /zh/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: 了解如何使用Aspose.Cells for Python via .NET API计算Excel 2016的MINIFS和MAXIFS函数，并附有示例代码。
keywords: python excel，minifs maxifs，公式计算，aspore.cells
---

## **可能的使用场景**
Microsoft Excel 2016支持MINIFS和MAXIFS函数。这些函数在Excel 2013或更早版本中不支持。Aspose.Cells也支持这些函数的计算。下图显示了这些函数的用法。请阅读图片中的红色注释以理解这些函数的工作机制。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **计算Excel 2016的MINIFS和MAXIFS函数**
以下示例代码加载[样例Excel文件](5115149.xlsx)，调用[workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)方法，通过Aspose.Cells进行公式计算，然后将结果保存在[输出PDF](5115154.pdf)。


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
