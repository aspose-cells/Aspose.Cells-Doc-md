---
title: Upptäcka en cirkulär referens
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att upptäcka cirkulära referenser i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda metoden som tillhandahålls av Aspose.Cells för att upptäcka cirkulära referenser och få resultaten. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, cirkulära referenser, upptäckt
type: docs
weight: 70
url: /sv/net/detecting-circular-reference/
---

## **Introduktion**

Arbetsböcker kan ha cirkulära referenser och ibland finns det ett behov av att avgöra om cirkulära referenser finns eller inte.

## **Konceptet bakom att upptäcka den cirkulära referensen**

Cirkulära referenser kan bara upptäckas när formeln beräknas eftersom referenserna i en formel vanligtvis beror på det beräknade resultatet av andra delar eller andra formler. Så tillhandahåller vi nya API:er för detta krav (att samla celler med cirkulära referenser) i processen för formelberäkning:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Representerar beräkningen av relevant data om en cell som beräknas

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): kommer att anropas av formelberäkningsmotorn när cirkulära referenser upptäcks, elementet i uppräknaren är [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) objekt som representerar alla celler i en cirkel. Det returnerade värdet anger om formel-motorn behöver beräkna de cellerna i cirkulären efter detta anrop.

Användaren kan samla in dessa cirkulära referenser i implementeringen av metoden [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular).

Den angivna provfilen kan laddas ner från följande länk:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition av *CircularMonitor* klassen som är härledd från [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) klassen är följande:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
