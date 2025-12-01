---
title: Interrupt or Cancel the Formula Calculation of Workbook
description: This article introduces how to use Aspose.Cells library to break or cancel formula calculations of workbooks in Microsoft Excel. By loading an existing Excel file or creating a new one, we can use the methods provided by Aspose.Cells to interrupt or cancel the formula calculation and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /net/interrupt-or-cancel-the-formula-calculation-of-workbook/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells provides a mechanism to interrupt or cancel the formula calculation of workbook using the [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) method. This is useful when the formula calculation of workbook is taking too much time and you want to cancel its processing.

## **Interrupt or Cancel the Formula Calculation of Workbook**

The following sample code implements the [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) method of [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) class. Inside this method, it finds the cell name using row and column index parameters. If the cell name is B8, it interrupts the calculation process by calling the [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) method. Once, the concrete class of [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) class is implemented, its instance is assigned to [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor) property. Finally, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) is called by passing [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) as a parameter. Please see the [sample Excel file](51740731.xlsx) used inside the code as well as the console output of the code given below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Console Output**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
