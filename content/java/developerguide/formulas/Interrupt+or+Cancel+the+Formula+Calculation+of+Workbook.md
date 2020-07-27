+++
title = "Interrupt or Cancel the Formula Calculation of Workbook" 
description = "" 
weight = 12190 
+++

Aspose.Cells for Java : Interrupt or Cancel the Formula Calculation of Workbook  

# Aspose.Cells for Java : Interrupt or Cancel the Formula Calculation of Workbook


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#InterruptorCanceltheFormulaCalculationofWorkbook-PossibleUsageScenarios)
*   2 [Interrupt or Cancel the Formula Calculation of Workbook](#InterruptorCanceltheFormulaCalculationofWorkbook-InterruptorCanceltheFormulaCalculationofWorkbook)
*   3 [Sample Code](#InterruptorCanceltheFormulaCalculationofWorkbook-SampleCode)
*   4 [Console Output](#InterruptorCanceltheFormulaCalculationofWorkbook-ConsoleOutput)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells provides a mechanism to interrupt or cancel the formula calculation of the workbook using the interrupt() method of the [AbstractCalculationMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/AbstractCalculationMonitor) class. This is useful when the formula calculation of workbook is taking too much time and you want to cancel its processing.

## Interrupt or Cancel the Formula Calculation of Workbook

The following sample code implements the [beforeCalculate()](https://apireference.aspose.com/java/cells/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) method of the [AbstractCalculationMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/AbstractCalculationMonitor) class. Inside this method, it finds the cell name using row and column index parameters. If the cell name is B8, it interrupts the calculation process by calling the AbstractCalculationMonitor.interrupt() method. Once, the concrete class of [AbstractCalculationMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/AbstractCalculationMonitor) class is implemented, its instance is assigned to [CalculationOptions.CalculationMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/calculationoptions#CalculationMonitor) property. Finally, [Workbook.calculateFormula()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) is called by passing [CalculationOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/CalculationOptions) as a parameter. Please see the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/51480076/51740744.xlsx) used inside the code as well as the console output of the code given below for a reference.

## Sample Code

## Console Output

{{< code lang="cs" >}}
0----1----3----D2
0----4----6----G5
0----7----1----B8
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleCalculationMonitor.xlsx](https://docs2.aspose.com/cells/java/attachments/51480076/51740744.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

