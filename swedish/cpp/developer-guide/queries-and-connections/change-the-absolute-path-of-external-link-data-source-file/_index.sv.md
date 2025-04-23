---
title: Ändra den absoluta sökvägen för externt länk datakällfil med C++
linktitle: Ändra den absoluta sökvägen för extern länkdatakällfil
type: docs
weight: 290
url: /sv/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Ändra den absoluta sökvägen för externt länk datakällfil i Aspose.Cells med C++.
---

## Möjliga användningsfall

Om du vill ändra den absoluta sökvägen för den externa länk datakällfilen, använd då [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) metoden. Initialt sätts denna egenskap till den sökväg där Excel-filen laddades. Men du kan sätta den till en tom sträng eller till en lokal mappväg eller fjärrnätverksväg. När du ändrar denna egenskap, ändras även sökvägen för den externa länk datakällfilen.

## Ändra den absoluta sökvägen för extern länkdatakällfil

Följande exempel laddar [exempel Excel-fil](5115146.xlsx) som innehåller en extern länk. Den skriver först ut den externa länkens datakälla, vilken visar den fjärrväg. Den tar bort den fjärrvägen och skriver ut igen, denna gång med den lokala sökvägen. Sedan ändrar den [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) metoden till en lokal och fjärrväg och skriver ut den externa länkens datakälla igen, och förändringarna reflekteras i konsolutmatningen.

Här är konsol- eller felsökningsutdata efter att ovanstående exempelkod har utförts med [exempel_excelfil](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
