---
title: Detekterar cirkulär referens
type: docs
weight: 70
url: /sv/net/detecting-circular-reference/
---
## **Introduktion**

Arbetsböcker kan ha cirkulära referenser och ibland finns det ett behov av att upptäcka om cirkulära referenser finns där eller inte.

## **Konceptet bakom att detektera den cirkulära referensen**

Cirkulära referenser kan bara upptäckas när formeln beräknas eftersom referenserna för en formel vanligtvis beror på det beräknade resultatet av andra delar eller andra formler. Så vi tillhandahåller nya API:er för detta krav (för att samla celler med cirkulära referenser) i processen för formelberäkning:

[**Beräkningscell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Representerar beräkningen av relevant data om en cell som beräknas

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): kommer att anropas av formelberäkningsmotorn när cirkulära referenser påträffas, elementet i enumeratorn är[**Beräkningscell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) objekt som representerar alla celler i en cirkel. Det returnerade värdet anger om formelmotorn behöver beräkna dessa celler i cirkulär efter detta anrop.

 Användare kan samla in dessa cirkulära referenser i implementeringen av[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) metod.

Källexempelfilen kan laddas ner från följande länk:

[Cirkulära formler.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition av*CircularMonitor* klass som härrör från[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) klass är som följer:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
