---
title: Data Formatting in Charts
linktitle: Data Source
type: docs
weight: 50
url: /java/data-formatting-in-charts/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In our previous topics, we have already provided many examples to demonstrate that how can you set a data source for your chart but in this topic, we are going to provide more details about the types of data that can be set for a chart.

{{% /alert %}}

## **Setting Chart Data**

There are two types of data to deal with while working on charts using Aspose.Cells as follows:

- [Chart data](/cells/java/data-formatting-in-charts/#chart-data).
- [Category data](/cells/java/data-formatting-in-charts/#category-data).

### **Chart Data**

Chart data is that data that we use as a data source to build our charts. We can add a range of the cells (containing chart data) by calling the [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) object's [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add-java.lang.Object-) method.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Category Data**

Category data is used for the labeling of chart data and can be added to [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) by using its [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#setCategoryData-java.lang.String-) method.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Column chart with chart & category data** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Advance topics**
- [Create Dynamic Charts](/cells/java/create-dynamic-charts/)
- [Easy way for Chart Setup using Chart.setChartDataRange method](/cells/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Find Type of X and Y Values of Points in Chart Series](/cells/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Set the Values Format Code of Chart Series](/cells/java/set-the-values-format-code-of-chart-series/)
{{< app/cells/assistant language="java" >}}
