---
title: 使用Python.NET计算数据表的数组公式
linktitle: 数据表的数组公式计算
type: docs
weight: 70
url: /zh/python-net/calculation-of-array-formula-of-data-tables/
description: 了解如何使用Aspose.Cells for Python via .NET API计算Excel数据表的数组公式。编程修改和保存电子表格。
keywords: Python Excel数据表、Python数组公式、Aspose.Cells Python、Python中计算数据表、Excel自动化Python
---

{{% alert color="primary" %}}

你可以在Microsoft Excel中使用数据 > 假设分析 > 数据表来创建数据表…… Aspose.Cells for Python via .NET允许你计算数据表的数组公式。请像平常一样使用 [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) 进行任何类型公式的计算。

{{% /alert %}}

在下面的示例中，我们使用[源Excel文件](5115535.xlsx)。如果你将单元格B1的值改为100，数据表（用黄色突出显示）的值将更新为120，如下图所示。Python代码生成了这个[输出PDF](5115538.pdf)。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下是演示如何从[源Excel文件](5115535.xlsx)生成[输出PDF](5115538.pdf)的Python实现：

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

**Python代码说明：**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
