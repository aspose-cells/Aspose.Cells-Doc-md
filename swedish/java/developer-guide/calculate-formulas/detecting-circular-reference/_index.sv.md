---
title: Detekterar cirkulär referens
type: docs
weight: 70
url: /sv/java/detecting-circular-reference/
---
## **Introduktion**

Arbetsböcker kan ha cirkulära referenser och ibland finns det ett behov av att upptäcka om cirkulära referenser finns där eller inte.

## **Konceptet bakom att detektera den cirkulära referensen**

Cirkulära referenser kan bara upptäckas när formeln beräknas eftersom referenserna för en formel vanligtvis beror på det beräknade resultatet av andra delar eller andra formler. Så vi tillhandahåller nya API:er för detta krav (för att samla celler med cirkulära referenser) i processen för formelberäkning:

[**Beräkningscell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Representerar beräkningen av relevant data om en cell som beräknas

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): kommer att anropas av formelberäkningsmotorn när cirkulära referenser påträffas, elementet i enumeratorn är[**Beräkningscell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) objekt som representerar alla celler i en cirkel. Det returnerade värdet anger om formelmotorn behöver beräkna dessa celler i cirkulär efter detta anrop.

 Användare kan samla in dessa cirkulära referenser i implementeringen av[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) metod.

Källexempelfilen kan laddas ner från följande länk:

[Cirkulära formler.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Definition av*CircularMonitor* klass som härrör från[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) klass är som följer:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
