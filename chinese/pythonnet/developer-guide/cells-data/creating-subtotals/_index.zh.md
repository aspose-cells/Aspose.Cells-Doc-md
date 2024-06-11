---
title: 创建分类汇总
type: docs
weight: 800
url: /zh/python-net/creating-subtotals/
description: 学习如何使用Aspose.Cells for Python via .NET API为电子表格中的任何重复值创建小计。
keywords: Python Excel库，应用小计，设置小计，添加小计，创建小计，如何向工作表添加小计 
---

{{% alert color="primary" %}}

您可以在电子表格中自动生成重复数值的小计。Aspose.Cells for Python via .NET提供API功能，可帮助您以编程方式向电子表格添加小计。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中添加小计：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为 Book1.xls。
1. 选择列表中的任何单元格。
1. 从**数据**菜单中选择**小计**。将显示小计对话框。定义要使用的函数和放置小计的位置。

## **使用Aspose.Cells for Python via .NET API**

Aspose.Cells for Python via .NET提供一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。该类提供了广泛的属性和方法来管理工作表和其他对象。每个工作表都包含一个[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合。要向工作表添加小计，请使用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)类的[**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list)方法。向该方法提供参数值以指定如何计算和放置小计。

在下面的示例中，我们使用Aspose.Cells for Python via .NET API向模板文件（Book1.xls）的第一个工作表添加了小计。当执行代码时，将创建一个带有小计的工作表。

接下来的代码片段展示了如何使用Aspose.Cells for Python via .NET向工作表添加小计。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **高级主题**
- [应用小计和更改概要行的方向，使之位于详细信息下方](/cells/zh/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
