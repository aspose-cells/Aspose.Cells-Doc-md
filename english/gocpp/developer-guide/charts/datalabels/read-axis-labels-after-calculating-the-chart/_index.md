---  
title: Read Axis Labels after Calculating the Chart with Golang via C++  
linktitle: Read Axis Labels after Calculating the Chart  
description: Learn how to read axis labels in Aspose.Cells for C++ after calculating the chart. Our guide will show you how to access and retrieve axis labels, including their formatting and positioning.  
keywords: Aspose.Cells for C++, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.  
type: docs  
weight: 90  
url: /go-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Possible Usage Scenarios**  

You can read the axis labels of your chart after calculating its values using the [**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/) method. Please use the [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) method for this purpose, which returns the list of axis labels.  

## **Read Axis Labels after Calculating the Chart**  

Please see the following sample code that loads the [sample Excel file](ReadAxisLabels.xlsx) and reads the category axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Please see the console output of the sample code given below for reference.  

## **Sample Code**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}  

## **Console Output**  

{{< highlight cpp >}}  

 Category Axis Labels:  

---------------------

Iran  

China  

USA  

Brazil  

England  

{{< /highlight >}}