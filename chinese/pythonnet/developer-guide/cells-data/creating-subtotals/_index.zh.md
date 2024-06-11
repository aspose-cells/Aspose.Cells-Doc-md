---
title: 创建小计
type: docs
weight: 800
url: /zh/python-net/creating-subtotals/
description: 通过 .NET 的 Aspose.Cells for Python API 学习如何在电子表格中为任何重复值创建小计。
keywords: Python Excel 库，应用小计，设置小计，增加小计，创建小计，如何在工作表中添加小计 
---

{{% alert color="primary" %}}

您可以在电子表格中自动为任何重复值创建小计。Aspose.Cells for Python 通过 .NET 提供的 API 功能可以帮助您在电子表格中程序化地添加小计。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中添加小计：

1.在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为Book1.xls。
1.选择列表中的任何单元格。
1.从**数据**菜单中选择**小计**。 将显示小计对话框。 定义要使用的功能以及放置小计的位置。

## **通过 .NET 的 Aspose.Cells for Python API**

通过 .NET 的 Aspose.Cells for Python 提供了一个代表 Microsoft Excel 文件的类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个允许访问 Excel 文件中每个工作表的 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) 集合。

通过[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示工作表。 该类提供了用于管理工作表和其他对象的各种属性和方法。 每个工作表都包含一个[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合。 要向工作表添加小计，请使用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)类的[**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list)方法。 向该方法提供参数值以指定应如何计算和放置小计。

在下面的示例中，我们使用 Aspose.Cells for Python 通过 .NET API 为模板文件的第一个工作表（Book1.xls）添加了小计。当代码被执行时，将创建一个带有小计的工作表。

以下代码段示例展示如何使用Aspose.Cells for Python通过.NET向工作表添加小计。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **高级主题**
- [应用小计并更改概述详细行的方向](/cells/zh/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
