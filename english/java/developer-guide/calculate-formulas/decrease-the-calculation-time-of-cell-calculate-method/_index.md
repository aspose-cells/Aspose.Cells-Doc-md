---
title: Decrease the Calculation Time of Cell.Calculate method
type: docs
weight: 860
url: /java/decrease-the-calculation-time-of-cell-calculate-method/
---


Possible Usage Scenarios

Normally, we recommend users to call [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate entire workbook. They just want to calculate a single cell. Aspose.Cells provides [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) property which you can set **false** and it will decrease the calculation time of individual cell significantly. Because when the recursive property is set to **true**, then all the dependents of cells are recalculated on each call. But when the recursive property is set to **false**, then dependent cells are calculated only once and are not calculated again on subsequent calls.
## **Decrease the Calculation Time of Cell.Calculate() method**
The following sample code illustrates the usage of [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) property. Please execute this code with the given [sample excel file](5472288.xlsx) and check its console output. You will find that setting the recursive property to **false** has decreased the calculation time significantly. Please also read the comments for a better understanding of this property.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Console Output**
This is the console output of the above sample code when executed with the given [sample excel file](5472288.xlsx) on our machine. Please note, your output may differ but the elapsed time after setting the recursive property to **false** will always be less than setting it to **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}