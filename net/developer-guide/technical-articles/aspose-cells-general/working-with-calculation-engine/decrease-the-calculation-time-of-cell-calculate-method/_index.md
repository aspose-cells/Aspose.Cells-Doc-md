---
title: Decrease the Calculation Time of Cell.Calculate method
type: docs
weight: 100
url: /net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Possible Usage Scenarios**
Normally, we recommend users to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula/index) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate entire workbook. They just want to calculate a single cell. Aspose.Cells provides [CalculationOptions.Recursive](https://apireference.aspose.com/net/cells/aspose.cells/calculationoptions/properties/recursive) property which you can set to **false** and it will decrease the calculation time of individual cell significantly. Because when the recursive property is set to **true**, then all the dependents of cells are recalculated on each call. But when the recursive property is **false**, then dependent cells are calculated only once and are not calculated again on subsequent calls.
## **Decrease the Calculation Time of Cell.Calculate() method**
The following sample code illustrates the usage of [CalculationOptions.Recursive](https://apireference.aspose.com/net/cells/aspose.cells/calculationoptions/properties/recursive) property. Please execute this code with the given [sample excel file](5113710.xlsx) and check its console output. You will find that setting the recursive property to **false** has decreased the calculation time significantly. Please also read the comments for a better understanding of this property.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}
## **Console Output**
This is the console output of the above sample code when executed with the given [sample excel file](5113710.xlsx) on our machine. Please note, your output may differ but the elapsed time after setting the recursive property to **false** will always be less than setting it to **true**.



{{< highlight java >}}

 Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
