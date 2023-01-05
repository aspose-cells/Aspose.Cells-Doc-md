---
title: Avbryt eller avbryt formelberäkningen av arbetsboken
type: docs
weight: 30
url: /sv/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Möjliga användningsscenarier**

Aspose.Cells tillhandahåller en mekanism för att avbryta eller avbryta formelberäkningen av arbetsboken med hjälp av interrupt()-metoden i[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) klass. Detta är användbart när formelberäkningen av arbetsboken tar för mycket tid och du vill avbryta behandlingen.

## **Avbryt eller avbryt formelberäkningen av arbetsboken**

Följande exempelkod implementerar[**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) metod för[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)klass. Inuti den här metoden hittar den cellnamnet med hjälp av rad- och kolumnindexparametrar. Om cellnamnet är B8, avbryter det beräkningsprocessen genom att anropa metoden AbstractCalculationMonitor.interrupt(). En gång betongklassen av[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)klass implementeras, dess instans tilldelas[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)fast egendom. Till sist,[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) kallas förbigående[**Beräkningsalternativ**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)som en parameter. Vänligen se[exempel på Excel-fil](51740744.xlsx)används inuti koden såväl som konsolutgången för koden som anges nedan som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
