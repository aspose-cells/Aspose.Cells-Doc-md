---
title: 为图表设置数据源
description: 了解Aspose.Cells for .NET支持的各种数据源。我们的指南将带你浏览可用的不同数据源类型，并向你展示如何连接和检索数据以填充你的工作表。
keywords: Aspose.Cells for .NET，图表，数据格式，标签，颜色，字体，外观，可用性。
linktitle: 数据源
type: docs
weight: 10
url: /zh/net/data-formatting-in-charts/
---

在之前的主题中，我们已经提供了许多示例，演示了如何为图表设置数据源，但在本主题中，我们将提供有关可以为图表设置的数据类型的更多详细信息。

## **设置图表数据**

使用Aspose.Cells处理图表时要处理的数据类型有两种:

- 图表数据。
- 分类数据。

### **图表数据**

图表数据是我们用作构建图表的数据源。我们可以通过调用[**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)方法添加包含图表数据的单元格的范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **分类数据**

分类数据用于对图表数据进行标记，并可以通过使用其[**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)属性将其添加到[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)中。下面给出一个完整的示例来演示图表和分类数据的使用。执行上述示例代码后，将向工作表添加一个柱形图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **高级主题**
- [将图表的数据源更改为目标工作表，同时复制行或范围](/cells/zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [创建动态图表](/cells/zh/net/create-dynamic-charts/)
- [使用Chart.SetChartDataRange方法设置图表的简单方法](/cells/zh/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中X和Y值的类型](/cells/zh/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
