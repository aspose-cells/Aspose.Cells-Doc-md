---
title: Find Type of X and Y Values of Points in Chart Series
type: docs
weight: 110
url: /java/find-type-of-x-and-y-values-of-points-in-chart-series/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#getXValueType--) and [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#getYValueType--) properties that can be used for this purpose. Please note, you will have to call [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) method before you could use these properties effectively.

## **Find Type of X and Y Values of Points in Chart Series**

The following sample code loads the [sample Excel file](64716920.xlsx) and accesses the first chart inside the first worksheet. It then calls the [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) method and finds the type of X and Y values of first chart point and prints them on the console. Please see the console output shown below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Console Output**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
