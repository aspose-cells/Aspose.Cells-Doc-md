---
title: Decrease the Calculation Time of Cell.Calculate method
description: This article introduces how to use the Aspose.Cells library to reduce the calculation time of cell calculation methods in Microsoft Excel. By loading an existing Excel file or creating a new one, we can use the methods provided by Aspose.Cells to optimize the cell calculation method and improve its performance. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /net/decrease-the-calculation-time-of-cell-calculate-method/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Normally, we recommend that users call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate the entire workbook; they just want to calculate a single cell. Aspose.Cells provides [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) property, which you can set to **false**, and it will decrease the calculation time of an individual cell significantly. Because when the Recursive property is set to **true**, all dependent cells are recalculated on each call. When the Recursive property is **false**, dependent cells are calculated only once and are not recalculated again on subsequent calls.

## **Decrease the Calculation Time of Cell.Calculate() method**

The following sample code illustrates the usage of [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) property. Please execute this code with the given [sample Excel file](5113710.xlsx) and check its console output. You will find that setting the Recursive property to **false** decreases the calculation time significantly. Please also read the comments for a better understanding of this property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Console Output**

This is the console output of the above sample code when executed with the given [sample Excel file](5113710.xlsx) on our machine. Please note that your output may differ, but the elapsed time after setting the Recursive property to **false** will always be less than when it is set to **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
