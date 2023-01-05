---
title: 为图表设置数据源
linktitle: 数据源
type: docs
weight: 10
url: /zh/net/data-formatting-in-charts/
---
在我们之前的主题中，我们已经提供了许多示例来演示如何为图表设置数据源，但在本主题中，我们将提供有关可以为图表设置的数据类型的更多详细信息。

## **设置图表数据**

在使用 Aspose.Cells 处理图表时，有两种类型的数据需要处理，如下所示：

- 图表数据。
- 类别数据。

### **图表数据**

图表数据是我们用作构建图表的数据源的数据。我们可以通过调用[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象的[**添加**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **类别数据**

分类数据用于图表数据的标注，可以添加到[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)通过使用其[**类别数据**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)财产。下面给出一个完整的例子来演示图表和类别数据的使用。执行上述示例代码后，工作表中将添加一个柱形图，如下所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **推进主题**
- [复制行或范围时将图表的数据源更改为目标工作表](/cells/zh/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [创建动态图表](/cells/zh/net/create-dynamic-charts/)
- [使用 Chart.SetChartDataRange 方法设置图表的简便方法](/cells/zh/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中点的 X 和 Y 值类型](/cells/zh/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
