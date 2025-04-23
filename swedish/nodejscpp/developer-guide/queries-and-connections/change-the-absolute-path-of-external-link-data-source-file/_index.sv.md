---
title: Ändra den absoluta sökvägen för extern länk datakällfil med Node.js via C++
linktitle: Ändra den absoluta sökvägen för extern länkdatakällfil
type: docs
weight: 290
url: /sv/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Lär dig att ändra den absoluta sökvägen för den externa länken datakällfil med Aspose.Cells for Node.js via C++. 
---

## Möjliga användningsfall

Om du vill ändra den absoluta sökvägen för den externa länken datakällfilen, använd då egenskapen [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). Initialt är denna egenskap inställd på sökvägen från vilken Excel-filen laddades. Men du kan ställa in den på en tom sträng, eller till en lokal mapp eller en fjärrnätverksväg. När du ändrar denna egenskap, kommer sökvägen för den externa länken datakällfilen också att ändras.

## Ändra den absoluta sökvägen för extern länkdatakällfil

Följande exempel kod laddar den [exempel Excel-filen](5115146.xlsx) som innehåller en extern länk. Den skriver först ut den externa länken datakälla som visar den fjärranslutna sökvägen. Sedan tar den bort den fjärranslutna sökvägen och skriver ut igen; den här gången visar den den externa länken datakälla med den lokala sökvägen. Sedan ändrar den [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--)-egenskapen till en lokal och fjärransluten sökväg och skriver ut den externa länken datakälla igen, och ändringarna återspeglas i konsolutmatningen.

Här är konsol- eller felskrivningsutgången efter körning av ovanstående exempel med den [exempel Excel-filen](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
