---
title: 创建小计
type: docs
weight: 800
url: /zh/net/creating-subtotals/
---
{{% alert color="primary" %}}

您可以为电子表格中的任何重复值自动创建小计。 Aspose.Cells 提供 API 功能，可帮助您以编程方式将小计添加到电子表格。

{{% /alert %}}

## **使用 Microsoft Excel**

要在 Microsoft Excel 中添加小计：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为Book1.xls。
1. 选择列表中的任何单元格。
1. 来自**数据**菜单，选择**小计**.将显示小计对话框。定义要使用的函数以及放置小计的位置。

## **使用 Aspose.Cells API**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。该类提供了广泛的属性和方法来管理工作表和其他对象。每个工作表由一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。要将小计添加到工作表，请使用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)班级'[**小计**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。向该方法提供参数值以指定应如何计算和放置小计。

在下面的示例中，我们使用 Aspose.Cells API 将小计添加到模板文件 (Book1.xls) 的第一个工作表。执行代码时，将创建一个包含小计的工作表。

下面的代码片段显示了如何将小计添加到包含 Aspose.Cells for .NET 的工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **推进主题**
- [应用小计和更改明细下方大纲汇总行的方向](/cells/zh/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
