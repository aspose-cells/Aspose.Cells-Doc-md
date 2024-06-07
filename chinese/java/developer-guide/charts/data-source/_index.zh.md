---
title: 图表中的数据格式化
linktitle: 数据源
type: docs
weight: 50
url: /zh/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

在之前的主题中，我们已经提供了许多示例，演示了如何为图表设置数据源，但在本主题中，我们将提供有关可以为图表设置的数据类型的更多详细信息。

{{% /alert %}}

## **设置图表数据**

使用Aspose.Cells处理图表时要处理的数据类型有两种:

- [图表数据](/cells/zh/java/data-formatting-in-charts/#chart-data)
- [分类数据](/cells/zh/java/data-formatting-in-charts/#category-data)

### **图表数据**

图表数据是用作构建图表的数据源。我们可以通过调用[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)对象的[**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)方法添加一系列包含图表数据的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **分类数据**

分类数据用于标记图表数据，可以通过使用其[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)方法添加到[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**带图表和类别数据的柱状图** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **高级主题**
- [创建动态图表](/cells/zh/java/create-dynamic-charts/)
- [使用Chart.setChartDataRange方法进行图表设置的简便方法](/cells/zh/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中X和Y值的类型](/cells/zh/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [设置图表系列的值格式代码](/cells/zh/java/set-the-values-format-code-of-chart-series/)
