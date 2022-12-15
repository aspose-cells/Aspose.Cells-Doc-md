---
title: 图表中的数据格式
linktitle: 数据源
type: docs
weight: 50
url: /zh/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

在我们之前的主题中，我们已经提供了许多示例来演示如何为图表设置数据源，但在本主题中，我们将提供有关可以为图表设置的数据类型的更多详细信息。

{{% /alert %}}

## **设置图表数据**

在使用 Aspose.Cells 处理图表时，有两种类型的数据需要处理，如下所示：

- [图表数据](/cells/zh/java/data-formatting-in-charts/#chart-data).
- [类别数据](/cells/zh/java/data-formatting-in-charts/#category-data).

### **图表数据**

图表数据是我们用作构建图表的数据源的数据。我们可以通过调用[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象的[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **类别数据**

分类数据用于图表数据的标注，可以添加到[**系列合集**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)通过使用其[**设置类别数据**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**包含图表和类别数据的柱形图** 

![待办事项：图像_替代_文本](data-formatting-in-charts_1.png)

## **推进主题**
- [创建动态图表](/cells/zh/java/create-dynamic-charts/)
- [使用 Chart.setChartDataRange 方法设置图表的简便方法](/cells/zh/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中点的 X 和 Y 值类型](/cells/zh/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [设置图表系列的值格式代码](/cells/zh/java/set-the-values-format-code-of-chart-series/)
