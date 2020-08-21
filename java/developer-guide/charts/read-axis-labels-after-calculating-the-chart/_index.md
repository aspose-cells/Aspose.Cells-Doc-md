---
title: Read Axis Labels after Calculating the Chart
type: docs
weight: 90
url: /java/read-axis-labels-after-calculating-the-chart/
---

## **Possible Usage Scenarios**
You can read axis labels of your chart after calculating its values using the [Chart.calculate()](https://apireference.aspose.com/java/cells/com.aspose.cells/chart#calculate\(\)) method. Please use the [Axis.AxisLabels](https://apireference.aspose.com/java/cells/com.aspose.cells/axis#AxisLabels) property for this purpose that will return the list of axis labels. 
## **Read Axis Labels after Calculating the Chart**
Please see the following sample code that loads the [sample Excel file](64716829.xlsx) and reads the category axis labels of the chart in the first worksheet. It then prints the values of the axis labels on the console. Please see the console output of the sample code given below for a reference.
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}
## **Console Output**
{{< highlight java >}}

 Category Axis Labels: 

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
