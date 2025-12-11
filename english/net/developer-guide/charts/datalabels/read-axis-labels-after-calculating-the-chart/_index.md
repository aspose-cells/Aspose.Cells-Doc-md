---  
title: Read Axis Labels after Calculating the Chart  
description: Learn how to read axis labels in Aspose.Cells for .NET after calculating the chart. Our guide will show you how to access and retrieve axis labels, including their formatting and positioning.  
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.  
type: docs  
weight: 90  
url: /net/read-axis-labels-after-calculating-the-chart/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**

You can read axis labels of your chart after calculating its values using the [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/) method. Please use the [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) method for this purpose, which will return the list of axis labels.

## **Read Axis Labels after Calculating the Chart**

Please see the following sample code that loads the [sample Excel file](ReadAxisLabels.xlsx) and reads the category‑axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Refer to the console output of the sample code below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

## **Console Output**

{{< highlight csharp >}}

 Category Axis Labels:

---------------------

Iran  

China  

USA  

Brazil  

England  

{{< /highlight >}}

{{< app/cells/assistant language="csharp" >}}
