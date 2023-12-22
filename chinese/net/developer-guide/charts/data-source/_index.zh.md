---
title: 设置图表的数据源
description: 了解 Aspose.Cells for .NET 支持的各种数据源。我们的指南将引导您了解可用的不同类型的数据源，并向您展示如何连接它们并从中检索数据以填充您的工作表。
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: 数据源
type: docs
weight: 10
url: /zh/net/data-formatting-in-charts/
---
在之前的主题中，我们已经提供了许多示例来演示如何为图表设置数据源，但在本主题中，我们将提供有关可为图表设置的数据类型的更多详细信息。

##  **设置图表数据**

使用 Aspose.Cells 处理图表时需要处理两种类型的数据，如下所示：

- 图表数据。
- 类别数据。

###  **图表数据**

图表数据是我们用作构建图表的数据源的数据。我们可以通过调用添加一系列单元格（包含图表数据）[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象的[**添加**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **类别数据**

类别数据用于图表数据的标注，可以添加到[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)通过使用其[**类别数据**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)财产。下面给出一个完整的例子来演示图表和类别数据的使用。执行上述示例代码后，柱形图将添加到工作表中，如下所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **高级主题**
- [复制行或范围时将图表的数据源更改为目标工作表](/cells/zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [创建动态图表](/cells/zh/net/create-dynamic-charts/)
- [使用 Chart.SetChartDataRange 方法进行图表设置的简单方法](/cells/zh/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中点的 X 和 Y 值类型](/cells/zh/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
