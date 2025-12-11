---
title: Decrease the Calculation Time of Cell.Calculate method with Golang via C++
linktitle: Decrease the Calculation Time of Cell.Calculate
description: This article introduces how to use the Aspose.Cells library to reduce the calculation time of cell calculation methods in Microsoft Excel. By loading an existing Excel file or creating a new one, we can use the methods provided by Aspose.Cells to optimize the cell calculation method and improve its performance. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Possible Usage Scenarios**

Normally, we recommend that users call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate the entire workbook. They just want to calculate a single cell. Aspose.Cells provides the [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) property, which you can set to **false**, and it will decrease the calculation time of individual cells significantly. When the recursive property is set to **true**, all the dependent cells are recalculated on each call. When the recursive property is **false**, dependent cells are calculated only once and are not recalculated again on subsequent calls.

## **Decrease the Calculation Time of Cell.Calculate() method**

The following sample code illustrates the usage of the [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/) property. Please execute this code with the given [sample Excel file](5113710.xlsx) and check its console output. You will find that setting the recursive property to **false** has decreased the calculation time significantly. Please also read the comments for a better understanding of this property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}

## **Console Output**

This is the console output of the above sample code when executed with the given [sample Excel file](5113710.xlsx) on our machine. Please note that your output may differ, but the elapsed time after setting the recursive property to **false** will always be less than when it is set to **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}