+++
title = "Interrupt or Cancel the Formula Calculation of Workbook" 
description = "" 
weight = 12228 
+++

Aspose.Cells for .NET : Interrupt or Cancel the Formula Calculation of Workbook  

# Aspose.Cells for .NET : Interrupt or Cancel the Formula Calculation of Workbook


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#InterruptorCanceltheFormulaCalculationofWorkbook-PossibleUsageScenarios)
*   2 [Interrupt or Cancel the Formula Calculation of Workbook](#InterruptorCanceltheFormulaCalculationofWorkbook-InterruptorCanceltheFormulaCalculationofWorkbook)
*   3 [Sample Code](#InterruptorCanceltheFormulaCalculationofWorkbook-SampleCode)
*   4 [Console Output](#InterruptorCanceltheFormulaCalculationofWorkbook-ConsoleOutput)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells provides a mechanism to interrupt or cancel the formula calculation of workbook using the [AbstractCalculationMonitor.Interrupt()](https://apireference.aspose.com/net/cells/aspose.cells/abstractcalculationmonitor/methods/interrupt) method. This is useful when the formula calculation of workbook is taking too much time and you want to cancel its processing.

## Interrupt or Cancel the Formula Calculation of Workbook

The following sample code implements the [BeforeCalculate()](https://apireference.aspose.com/net/cells/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) method of [AbstractCalculationMonitor](https://apireference.aspose.com/net/cells/aspose.cells/abstractcalculationmonitor) class. Inside this method, it finds the cell name using row and column index parameters. If the cell name is B8, it interrupts the calculation process by calling the [AbstractCalculationMonitor.Interrupt()](https://apireference.aspose.com/net/cells/aspose.cells/abstractcalculationmonitor/methods/interrupt) method. Once, the concrete class of [AbstractCalculationMonitor](https://apireference.aspose.com/net/cells/aspose.cells/abstractcalculationmonitor) class is implemented, its instance is assigned to [CalculationOptions.CalculationMonitor](https://apireference.aspose.com/net/cells/aspose.cells/calculationoptions/properties/calculationmonitor) property. Finally, [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula/index) is called by passing [CalculationOptions](https://apireference.aspose.com/net/cells/aspose.cells/calculationoptions) as a parameter. Please see the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/51479989/51740731.xlsx) used inside the code as well as the console output of the code given below for a reference.

## Sample Code

## Console Output

{{< code lang="cs" >}}
0----1----3----D2
0----4----6----G5
0----7----1----B8
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleCalculationMonitor.xlsx](https://docs2.aspose.com/cells/net/attachments/51479989/51740731.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

