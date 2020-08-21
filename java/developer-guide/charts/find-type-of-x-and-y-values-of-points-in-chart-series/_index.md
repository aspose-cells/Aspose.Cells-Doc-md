---
title: Find Type of X and Y Values of Points in Chart Series
type: docs
weight: 110
url: /java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possible Usage Scenarios**
Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides [ChartPoint.XValueType](https://apireference.aspose.com/java/cells/com.aspose.cells/chartpoint#XValueType) and [ChartPoint.YValueType](https://apireference.aspose.com/java/cells/com.aspose.cells/chartpoint#YValueType) properties that can be used for this purpose. Please note, you will have to call [Chart.calculate()](https://apireference.aspose.com/java/cells/com.aspose.cells/chart#calculate\(\)) method before you could use these properties effectively.
## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716920.xlsx) and accesses the first chart inside the first worksheet. It then calls the [Chart.calculate()](https://apireference.aspose.com/java/cells/com.aspose.cells/chart#calculate\(\)) method and finds the type of X and Y values of first chart point and prints them on the console. Please see the console output shown below for a reference.
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}
## **Console Output**
{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
