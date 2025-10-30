---
title: Ändra den absoluta sökvägen för extern länkdatakällfil
type: docs
weight: 290
url: /sv/python-net/change-the-absolute-path-of-external-link-data-source-file/
---

## Möjliga användningsfall

Om du vill ändra den absoluta sökvägen för extern länkdatakällfilen, använd [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) egenskapen. Initialt kommer denna egenskap att sättas till sökvägen från vilken Excel-filen lästes in. Men du kan sätta den till en tom sträng eller så kan du sätta den till någon lokal mapp sökväg eller fjärrnätverk sökväg. Varje gång du ändrar denna egenskap kommer även sökvägen för extern länkdatakällfilen att ändras.

## Ändra den absoluta sökvägen för extern länkdatakällfil

Följande exempelkod läser in [exempel_excelfil](5115146.xlsx) som innehåller en extern länk. Först skriver den ut den externa länkdatakällan som skriver ut fjärrsökvägen. Sedan tar den bort fjärrsökvägen och skriver ut igen, denna gången skriver den ut den externa länkdatakällan med den lokala sökvägen. Sedan ändrar den [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) egenskapen till en lokal och fjärr sökväg och skriver ut den externa länkdatakällan igen och ändringarna återspeglas i konsoloutputen.

Här är konsol- eller felsökningsutdata efter att ovanstående exempelkod har utförts med [exempel_excelfil](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
