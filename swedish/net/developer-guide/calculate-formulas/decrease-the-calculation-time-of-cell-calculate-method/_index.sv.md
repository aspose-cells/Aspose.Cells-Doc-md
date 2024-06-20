---
title: Minska beräkningstiden för Cell.Calculate metoden
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att minska beräkningstiden för cellberäkningsmetoder i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att optimera cellberäkningsmetoden och förbättra dess prestanda. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, Cellberäkningsmetoder, optimering, prestanda, minskning av beräkningstid
type: docs
weight: 100
url: /sv/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Möjliga användningsscenario**

Normalt rekommenderar vi användare att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)-metoden en gång och sedan få de beräknade värdena för enskilda celler. Men ibland vill användare inte beräkna hela arbetsboken. De vill bara beräkna en enda cell. Aspose.Cells tillhandahåller [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)-egenskapen som du kan ställa in till **false** och det minskar beräkningstiden för enskilda celler betydligt. Eftersom när den rekursiva egenskapen är inställd på **true**, beräknas alla beroende av celler vid varje anrop. Men när den rekursiva egenskapen är **false**, beräknas beroende celler endast en gång och beräknas inte igen vid efterföljande anrop.

## **Minska beräkningstiden för Cell.Calculate() metoden**

Följande exempelkod illustrerar användningen av [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)-egenskapen. Kör denna kod med den angivna [exempel på excelfil](5113710.xlsx) och kontrollera dess konsolresultat. Du kommer att märka att beräkningstiden har minskat avsevärt efter att den rekursiva egenskapen har ställts in till **false**. Läs även kommentarerna för en bättre förståelse av denna egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Konsoloutput**

Detta är konsoloutputen för ovannämnda exempelkod när den körs med den angivna [exempel på excelfil](5113710.xlsx) på vår maskin. Observera att din utdata kan skilja sig, men den förflutna tiden efter att den rekursiva egenskapen har ställts in till **false** kommer alltid att vara mindre än när den är inställd till **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
