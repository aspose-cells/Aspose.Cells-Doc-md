---
title : "Creating Pie Chart with Leader Lines" 
description : "" 
weight : 20515 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngchartsandshapes/creating+pie+chart+with+leader+lines/
---

# Aspose.Cells for .NET : Creating Pie Chart with Leader Lines


This article explains how to create a pie chart with leader lines from scratch while using Aspose.Cells for .NET API. In Excel, the 'Show leader lines' option is set by default so when you create a pie chart in Excel the leader lines are shown. However, while creating a similar chart with Aspose.Cells APIs, you have to explicitly set the [Series.HasLeaderLines](https://apireference.aspose.com/net/cells/aspose.cells.charts/series/properties/hasleaderlines) property.

To demonstrate the usage of Aspose.Cells for .NET API to create a pie chart with leader lines, we will first create a new [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) and input some data that will serve as the series data source. Once the data is in place, we will add a [Chart](https://apireference.aspose.com/net/cells/aspose.cells.charts/chart) of type [ChartType.Pie](https://apireference.aspose.com/net/cells/aspose.cells.charts/charttype) to the collection of charts and set its different aspects to get the desired chart view.

So far we have created a pie chart and set its different aspects. Now we are going to turn on the leader lines for the chart. Please note, to show the leader lines, we have to move the data labels a little.

The following piece of code turns on the leader lines, refresh the chart and then calculates the data labels' positions to move them accordingly.

  
Finally, the following code saves the chart in image format and the workbook in XLSX format.

{{< table style="table-striped" >}}
|Resultant Pie Chart|
|:----|
|![image](https://docs2.aspose.com/cells/net/attachments/5017315/5112336.png)|
{{< /table >}}

