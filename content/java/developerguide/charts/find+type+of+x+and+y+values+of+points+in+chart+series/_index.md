---
title : "Find Type of X and Y Values of Points in Chart Series" 
description : "" 
weight : 12212 
toc : false
type: docs
url: /java/developerguide/charts/find+type+of+x+and+y+values+of+points+in+chart+series/
---

# Aspose.Cells for Java : Find Type of X and Y Values of Points in Chart Series


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Find Type of X and Y Values of Points in Chart Series](#find-type-of-x-and-y-values-of-points-in-chart-series)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides [ChartPoint.XValueType](https://apireference.aspose.com/java/cells/com.aspose.cells/chartpoint#XValueType) and [ChartPoint.YValueType](https://apireference.aspose.com/java/cells/com.aspose.cells/chartpoint#YValueType) properties that can be used for this purpose. Please note, you will have to call [Chart.calculate()](https://apireference.aspose.com/java/cells/com.aspose.cells/chart#calculate()) method before you could use these properties effectively.

## Find Type of X and Y Values of Points in Chart Series

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/64456365/64716920.xlsx) and accesses the first chart inside the first worksheet. It then calls the [Chart.calculate()](https://apireference.aspose.com/java/cells/com.aspose.cells/chart#calculate()) method and finds the type of X and Y values of first chart point and prints them on the console. Please see the console output shown below for a reference.

## Sample Code

## Console Output

{{< code lang="cs" >}}
X Value Type: IsString
Y Value Type: IsNumeric
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleFindTypeOfXAndYValuesOfPoints.xlsx](https://docs2.aspose.com/cells/java/attachments/64456365/64716920.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

