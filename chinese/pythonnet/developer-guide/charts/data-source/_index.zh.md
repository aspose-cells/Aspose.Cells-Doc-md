---
title: 为图表设置数据源
description: 了解Aspose.Cells for Python via .NET支持的各种数据源。我们的指南将带你了解不同类型的数据源，以及如何连接和获取数据以填充你的工作表。
keywords: Aspose.Cells for Python via .NET、图表、数据格式、标签、颜色、字体、外观、易用性。
linktitle: 数据源
type: docs
weight: 10
url: /zh/python-net/data-formatting-in-charts/
---

在我们之前的主题中，我们已经提供了许多示例，演示了如何为图表设置数据源，但在本主题中，我们将提供有关可为图表设置的数据类型的更多详细信息。

## **设置图表数据**

在使用Aspose.Cells for Python via .NET制作图表时，有两种类型的数据需要处理：

 - 图表数据。
 - 类别数据。

### **图表数据**

图表数据是我们用作图表数据源的数据。我们可以通过调用 [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) 对象的 [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) 方法来添加包含图表数据的单元格范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **分类数据**

类别数据用于标记图表数据，并且可以通过其 [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data) 属性添加到 [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) 中。下面提供了一个完整的示例，演示了如何使用图表和分类数据。执行以上示例代码后，工作表将添加一个柱状图，如下所示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **高级主题**
- [复制行或区域时更改图表的数据源到目标工作表](/cells/zh/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [创建动态图表](/cells/zh/python-net/create-dynamic-charts/)
- [使用 Chart.SetChartDataRange 方法设置图表的简单方法](/cells/zh/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中点的X和Y值类型](/cells/zh/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="python-net" >}}
