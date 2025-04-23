---
title: 创建分类汇总
type: docs
weight: 800
url: /zh/net/creating-subtotals/
description: 学习如何通过 Aspose.Cells for .NET API 为电子表格中重复值创建小计。
keywords: 应用小计、设置小计、添加小计、创建小计、如何向工作表添加小计 
---

{{% alert color="primary" %}}

您可以自动为电子表格中的任何重复值创建小计。Aspose.Cells提供了API功能，帮助您以编程方式向电子表格添加小计。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中添加小计：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为 Book1.xls。
1. 选择列表中的任何单元格。
1. 从**数据**菜单中选择**小计**。将显示小计对话框。定义要使用的函数和放置小计的位置。

## **使用Aspose.Cells API**

Aspose.Cells提供了一个代表Microsoft Excel文件的类,[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。该类提供了广泛的属性和方法来管理工作表和其他对象。每个工作表都包含一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合。要向工作表添加小计，请使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)类的[**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。向该方法提供参数值以指定如何计算和放置小计。

在下面的示例中，我们使用Aspose.Cells API向模板文件（Book1.xls）的第一个工作表添加了小计。执行代码时，将创建一个带有小计的工作表。

以下代码片段展示了如何使用 Aspose.Cells for .NET 向工作表添加小计。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **高级主题**
- [应用小计和更改概要行的方向，使之位于详细信息下方](/cells/zh/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
{{< app/cells/assistant language="csharp" >}}
