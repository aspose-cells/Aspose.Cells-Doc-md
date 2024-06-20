---
title: Ändra den absoluta sökvägen för extern länkdatakällfil
type: docs
weight: 1020
url: /sv/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Möjliga användningsscenario**
Om du vill ändra den absoluta sökvägen för externa länkdatakällfilen, använd [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) egenskapen. Initialt kommer denna egenskap att vara inställd på sökvägen från vilken excelfilen laddades. Men du kan ställa in den till en tom sträng eller till någon lokal mappväg eller fjärrnätverksväg. När du ändrar denna egenskap kommer sökvägen för externa länkdatakällanfilen också att ändras.
## **Ändra den absoluta sökvägen för extern länkdatakällfilen**
Följande exempelkod laddar [provexcelfilen](5472589.xlsx) som innehåller en extern länk. Det skriver först ut den externa länkdatakällan som skriver ut den fjärranslutna sökvägen. Sedan tar den bort den fjärra sökvägen och skriver ut den igen, den här gången skriver den den externa länkdatakällan med den lokala sökvägen. Sedan ändras [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) egenskapen till en lokal och fjärr sökväg och skriver ut den externa länkdatakällan igen och ändringarna återspeglas i konsolresultatet.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Konsoloutput**
Här är konsol- eller felsökningsresultatet efter att ovanstående exempelkod har körts med [provexcelfilen](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
