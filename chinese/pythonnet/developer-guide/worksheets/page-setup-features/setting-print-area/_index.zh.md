---
title: 如何用 Python.NET 设置打印区域
linktitle: 如何设置打印区域
type: docs
weight: 200
url: /zh/python-net/how-to-set-print-area/
description: 学习如何使用 Aspose.Cells for Python 在 Excel 文件中设置和清除打印区域 via .NET。
keywords: python 设置打印区域，清除打印范围，python Excel 打印设置，aspose.cells python 打印区域，python 限制打印范围
---

## **可能的使用场景**

在文档中设置打印区域有助于控制打印内容。主要原因包括：

1. 聚焦特定数据：仅打印相关部分
1. 改善布局：整齐排列内容跨多个页面
1. 节省资源：减少纸张/墨水消耗
1. 专业表现：确保输出更佳
1. 一致性：保持统一的打印输出

## ** 如何在 Excel 中设置打印区域**

编程方式设置打印区域：

1. 访问工作表的页面设置属性
1. 使用单元格范围符号定义打印区域
1. 保存已修改的工作簿

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **如何在Excel中清除打印区域**

要删除打印区域限制：

1. 访问页面设置属性
1. 将打印区域重置为空字符串
1. 保存更改

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **清除打印区域后会发生什么**

清除打印区域会导致：

1. 默认打印整个工作表
1. 移除之前的范围限制
1. 包含所有已格式化单元格

## **如何使用Aspose.Cells设置打印区域**

通过工作表的页面设置设置打印区域：

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"

# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```

```python
# Output image reference
<img src="1.png" width=60% />
```

## **如何使用Aspose.Cells清除打印区域**

删除现有的打印区域定义：

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear print area
worksheet.page_setup.print_area = ""

# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```

```python
# Output image reference
<img src="2.png" width=60% />
```

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"

# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the print area
worksheet.page_setup.print_area = ""

# Save the workbook
workbook.save("clear_print_area.pdf")
```
