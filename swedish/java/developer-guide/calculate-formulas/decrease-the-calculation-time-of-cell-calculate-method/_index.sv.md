---
title: Minska beräkningstiden för Cell. Beräkna metod
type: docs
weight: 860
url: /sv/java/decrease-the-calculation-time-of-cell-calculate-method/
---
Möjliga användningsscenarier

 Normalt rekommenderar vi användare att ringa[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) metod en gång och få sedan de beräknade värdena för de enskilda cellerna. Men ibland vill användare inte beräkna hela arbetsboken. De vill bara beräkna en enda cell. Aspose.Cells tillhandahåller[Beräkningsalternativ.Rekursiv](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) egenskap som du kan ställa in**falsk**och det kommer att minska beräkningstiden för individuell cell avsevärt. För när den rekursiva egenskapen är inställd på**Sann**sedan räknas alla beroenden av celler om på varje samtal. Men när den rekursiva egenskapen är inställd på**falsk**, sedan beräknas beroende celler endast en gång och beräknas inte igen vid efterföljande samtal.
## **Minska beräkningstiden för Cell.Calculate()-metoden**
 Följande exempelkod illustrerar användningen av[Beräkningsalternativ.Rekursiv](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) fast egendom. Vänligen kör den här koden med den givna[exempel på excel-fil](5472288.xlsx) och kontrollera dess konsolutgång. Du kommer att upptäcka att inställningen av den rekursiva egenskapen till**falsk**har minskat beräkningstiden avsevärt. Läs även kommentarerna för en bättre förståelse av denna fastighet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsolutgång**
 Detta är konsolutgången för ovanstående exempelkod när den körs med den givna[exempel på excel-fil](5472288.xlsx) på vår maskin. Observera att din utdata kan skilja sig men den förflutna tiden efter att den rekursiva egenskapen ställts in på**falsk** kommer alltid att vara mindre än att ställa in den på**Sann**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
