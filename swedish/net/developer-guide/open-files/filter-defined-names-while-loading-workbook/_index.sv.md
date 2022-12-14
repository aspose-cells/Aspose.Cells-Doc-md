---
title: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/net/filter-defined-names-while-loading-workbook/
---
## **Möjliga användningsscenarier**

Aspose.Cells låter dig filtrera eller ta bort definierade namn som finns i arbetsboken. Snälla använd[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)för att ladda definierade namn och använda ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)för att ta bort dem medan du laddar arbetsboken. Observera att om du tar bort definierade namn kan formler i arbetsboken gå sönder.

## **Filtrera definierade namn när arbetsboken laddas**

 Följande exempelkod laddar[exempel på Excel-fil](61767860.xlsx)som har en formel i cellen**C1** som innehåller de definierade namnen, dvs*=SUMMA(Mitt Namn1, Mitt Namn2)*. Eftersom vi använder ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) för att ta bort de definierade namnen när du laddar arbetsboken, formeln i cell C1 in[utdata Excel-fil](61767861.xlsx) bryter upp och du ser*#NAME?*istället. Se följande skärmdump som visar effekten av koden på exemplet på Excel-filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
