---
title: Interrupt or Cancel the Formula Calculation of Workbook
type: docs
weight: 30
url: /java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Possible Usage Scenarios**

Aspose.Cells provides a mechanism to interrupt or cancel the formula calculation of the workbook using the interrupt() method of the [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) class. This is useful when the formula calculation of workbook is taking too much time and you want to cancel its processing.

## **Interrupt or Cancel the Formula Calculation of Workbook**

The following sample code implements the [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate-int-int-int-) method of the [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) class. Inside this method, it finds the cell name using row and column index parameters. If the cell name is B8, it interrupts the calculation process by calling the AbstractCalculationMonitor.interrupt() method. Once, the concrete class of [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) class is implemented, its instance is assigned to [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor) property. Finally, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-) is called by passing [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) as a parameter. Please see the [sample Excel file](51740744.xlsx) used inside the code as well as the console output of the code given below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Console Output**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}