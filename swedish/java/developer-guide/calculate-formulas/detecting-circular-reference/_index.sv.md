---
title: Upptäcka en cirkulär referens
type: docs
weight: 70
url: /sv/java/detecting-circular-reference/
---

## **Introduktion**

Arbetsböcker kan ha cirkulära referenser och ibland finns det ett behov av att avgöra om cirkulära referenser finns eller inte.

## **Konceptet bakom att upptäcka den cirkulära referensen**

Cirkulära referenser kan bara upptäckas när formeln beräknas eftersom referenserna i en formel vanligtvis beror på det beräknade resultatet av andra delar eller andra formler. Så tillhandahåller vi nya API:er för detta krav (att samla celler med cirkulära referenser) i processen för formelberäkning:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Representerar beräkningen av relevant data om en cell som beräknas

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): kommer att anropas av formelberäkningsmotorn när cirkulära referenser upptäcks, elementet i uppräknaren är [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) objekt som representerar alla celler i en cirkel. Det returnerade värdet anger om formel-motorn behöver beräkna de cellerna i cirkulären efter detta anrop.

Användaren kan samla in dessa cirkulära referenser i implementeringen av metoden [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)).

Den angivna provfilen kan laddas ner från följande länk:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Definition av *CircularMonitor* klassen som är härledd från [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) klassen är följande:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
