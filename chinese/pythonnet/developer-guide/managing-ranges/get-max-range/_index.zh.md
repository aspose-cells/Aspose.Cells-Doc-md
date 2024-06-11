---
title: 获取工作表中的最大范围
type: docs
weight: 360
url: /zh/python-net/get-max-range-in-a-worksheet/
description: 本文介绍如何使用Aspose.Cells for Python via .NET库获取Excel文件的最大范围、最大数据范围和最大显示范围。
keywords: Python Excel库，Python获取最大范围，Python获取最大数据范围，Python获取最大显示范围。
---

{{% alert color="primary" %}} 

在从工作表读取数据时，我们需要知道最大的区域。

在从工作表复制所有数据时，我们需要知道最大的区域。

在将指定区域导出到html和pdf时，我们需要知道最大的区域。

Aspose.Cells for Python via .NET包含查找工作表中最大范围的不同方法。 


{{% /alert %}} 



## **如何获取最大范围**
在Aspose.Cells for Python via .NET中，如果初始化了[**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)和[**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)对象，这些行和列将被计算到最大的区域，即使空行或空列中没有数据。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **如何获取最大数据范围**
在大多数情况下，我们只需要获取包含所有数据的所有范围，即使范围外的空单元格被格式化。
关于形状、表格和数据透视表的设置将被忽略。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **如何获取最大显示范围**
当我们将工作表中的所有数据导出到 HTML、PDF 或图像时，需要获取一个包含所有可见对象的区域，包括数据、样式、图形、表格和数据透视表。
以下代码展示了如何将最大显示范围呈现为 HTML:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

这是 [源 Excel 文件](Book1.xlsx)。
