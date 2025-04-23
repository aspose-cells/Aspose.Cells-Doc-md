---
title: Avbryt eller avbryt formelberäkningen i arbetsbok
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att bryta eller avbryta formelberäkningar av arbetsböcker i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att avbryta eller avbryta formelberäkningen och få resultatet. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, arbetsböcker, formelberäkningar, bryter, avbrott
type: docs
weight: 50
url: /sv/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en mekanism för att avbryta eller avbryta formelberäkningen av arbetsboken med hjälp av [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)-metoden. Detta är användbart när arbetsbokens formelberäkning tar för lång tid och du vill avbryta dess bearbetning.

## **Avbryt eller avbryt formelberäkningen i arbetsbok**

Följande exempelkod implementerar [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)-metoden i [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)-klassen. Inne i denna metod hittar den cellnamnet med hjälp av rad- och kolumnindexparametrarna. Om cellnamnet är B8, avbryter den beräkningsprocessen genom att anropa [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)-metoden. När [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)-klassens konkreta klass väl har implementerats, tilldelas dess instans till [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)-egenskapen. Slutligen anropas [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) genom att skicka [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) som en parameter. Se även den [exempel på excelfil](51740731.xlsx) som används i koden samt konsolresultatet av koden nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
