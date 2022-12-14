---
title: Avbryt eller avbryt formelberäkningen av arbetsboken
type: docs
weight: 50
url: /sv/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Möjliga användningsscenarier**

Aspose.Cells tillhandahåller en mekanism för att avbryta eller avbryta formelberäkningen av arbetsboken med[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)metod. Detta är användbart när formelberäkningen av arbetsboken tar för mycket tid och du vill avbryta behandlingen.

## **Avbryt eller avbryt formelberäkningen av arbetsboken**

Följande exempelkod implementerar[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)metod av[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) klass. Inuti den här metoden hittar den cellnamnet med hjälp av rad- och kolumnindexparametrar. Om cellnamnet är B8, avbryter det beräkningsprocessen genom att anropa[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)metod. En gång betongklassen av[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)klass implementeras, dess instans tilldelas[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)fast egendom. Till sist,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)kallas förbigående[**Beräkningsalternativ**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) som en parameter. Vänligen se[exempel på Excel-fil](51740731.xlsx) används inuti koden såväl som konsolutgången för koden som anges nedan som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
