---
title: Minska beräkningstiden för Cell.Calculate metoden
type: docs
weight: 860
url: /sv/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Möjliga användningsscenario

Normalt rekommenderar vi användare att anropa [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) metoden en gång och sedan få de beräknade värdena för enskilda celler. Men ibland vill användare inte beräkna hela arbetsboken. De vill bara beräkna en enskild cell. Aspose.Cells tillhandahåller [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) egenskap som du kan ställa in **falskt** och det kommer markant minska beräkningstiden för enskilda celler. Eftersom när den rekursiva egenskapen är inställd på **sant**, beräknas alla beroende celler om vid varje anrop. Men när den rekursiva egenskapen är inställd på **falskt**, beräknas beroende celler bara en gång och beräknas inte igen vid efterföljande anrop.
## **Minska beräkningstiden för Cell.Calculate() metoden**
Följande provkod illustrerar användningen av [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) egenskap. Kör denna kod med den angivna [prov excel-filen](5472288.xlsx) och kontrollera dess konsol utmatning. Du kommer att se att inställning av den rekursiva egenskapen till **falskt** har minskat beräkningstiden markant. Läs även kommentarerna för en bättre förståelse av denna egenskap.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsoloutput**
Detta är konsol utmatningen av ovanstående provkod när den körs med den angivna [prov excel-filen](5472288.xlsx) på vår maskin. Observera, din utmatning kan skilja sig men den passerade tiden efter att den rekursiva egenskapen har ställts till **falskt** kommer alltid att vara mindre än när den ställs till **sant**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
