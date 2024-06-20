---
title: Avbryt eller avbryt formelberäkningen i arbetsbok
type: docs
weight: 30
url: /sv/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en mekanism för att avbryta eller avbryta formelberäkningen i arbetsboken med hjälp av metoden interrupt() i [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) klassen. Detta är användbart när formelberäkningen i arbetsboken tar för lång tid och du vill avbryta dess bearbetning.

## **Avbryt eller avbryt formelberäkningen i arbetsbok**

Följande provkod implementerar [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) metoden i [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) klassen. Inne i denna metod letar den reda på cellnamnet med hjälp av rad- och kolumnindexparametrarna. Om cellnamnet är B8, avbryter den beräkningsprocessen genom att anropa AbstractCalculationMonitor.interrupt() metoden. När [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) -klassens konkreta klass är implementerad, tilldelas dess instans [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor) egenskap. Slutligen, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) anropas genom att skicka [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) som parameter. Vänligen se den [provmallen Excel-fil](51740744.xlsx) som används i koden samt konsolens utmatning av koden nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Konsoloutput**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
