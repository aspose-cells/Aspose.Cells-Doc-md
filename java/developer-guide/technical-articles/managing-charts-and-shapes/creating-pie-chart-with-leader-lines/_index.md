---
title: Creating Pie Chart with Leader Lines
type: docs
weight: 170
url: /java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}} 

This article explains how to create a pie chart with leader lines from scratch while using Aspose.Cells for Java API. In Excel, the 'Show leader lines' option is set by default so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells APIs, you have to explicitly set the [Series.HasLeaderLines](https://apireference.aspose.com/java/cells/com.aspose.cells/series#HasLeaderLines) property.

{{% /alert %}} 
### **Creating Pie Chart with Leader Lines**
In order to demonstrate the usage of Aspose.Cells for Java API to create a pie chart with leader lines, we will first create a new [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) and input some data that will serve as series data source. Once the data is in place, we will add a [Chart](https://apireference.aspose.com/java/cells/com.aspose.cells/Chart) of type [Pie](https://apireference.aspose.com/java/cells/com.aspose.cells/charttype#PIE) to the collection of charts and set it's different aspects to get the desired chart view.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}





**Resultant Pie Chart** 

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)
