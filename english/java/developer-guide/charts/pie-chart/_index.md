---
title: Creating Pie Chart with Leader Lines
linktitle: Pie Chart
type: docs
weight: 170
url: /java/creating-pie-chart-with-leader-lines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article explains how to create a pie chart with leader lines from scratch while using Aspose.Cells for Java API. In Excel, the 'Show leader lines' option is set by default so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells APIs, you have to explicitly set the [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#setHasLeaderLines-boolean-) property.

{{% /alert %}}

## **Creating Pie Chart with Leader Lines**

In order to demonstrate the usage of Aspose.Cells for Java API to create a pie chart with leader lines, we will first create a new [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) and input some data that will serve as series data source. Once the data is in place, we will add a [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) of type [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) to the collection of charts and set it's different aspects to get the desired chart view.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Resultant Pie Chart**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Related Articles

- [Creating and Customizing Charts](/cells/java/creating-and-customizing-charts/)
- [Chart Formatting](/cells/java/chart-formatting/)
{{< app/cells/assistant language="java" >}}
