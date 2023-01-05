---
title: Ändra den absoluta sökvägen för datakällfilen för extern länk
type: docs
weight: 1020
url: /sv/java/change-the-absolute-path-of-external-link-data-source-file/
---
## **Möjliga användningsscenarier**
 Om du vill ändra den absoluta sökvägen för den externa länkdatakällfilen, använd[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)fast egendom. Inledningsvis kommer den här egenskapen att ställas in på sökvägen varifrån excel-filen laddades. Men du kan ställa in den på en tom sträng eller så kan du ställa in den på någon lokal mappsökväg eller fjärrnätverkssökväg. Närhelst du ändrar den här egenskapen ändras även sökvägen till den externa länkdatakällfilen.
## **Ändra den absoluta sökvägen för datakällfilen för extern länk**
 Följande exempelkod laddar[exempel på excel-fil](5472589.xlsx) som innehåller en extern länk. Den skriver först ut den externa länkdatakällan som skriver ut fjärrsökvägen. Sedan tar den bort fjärrsökvägen och skriver ut igen, den här gången skriver den ut extern länkdatakälla med den lokala sökvägen. Sedan ändrar det[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)egenskapen till en lokal och fjärrsökväg och skriver ut den externa länkdatakällan igen och ändringarna återspeglas i konsolens utdata.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Konsolutgång**
Här är konsolen eller felsökningsutgången efter exekveringen av ovanstående exempelkod med[exempel på excel-fil](5472589.xlsx).

{{< highlight "java" >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
