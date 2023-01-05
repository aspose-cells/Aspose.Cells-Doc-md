---
title: Autopassa kolumner och rader när HTML laddas i arbetsboken
type: docs
weight: 120
url: /sv/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Möjliga användningsscenarier**

Du kan automatiskt anpassa kolumner och rader medan du laddar din HTML-fil inuti Workbook-objektet. Vänligen ställ in**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** egendom till**Sann**för detta ändamål.

## **Autopassa kolumner och rader när HTML laddas i arbetsboken**

 Följande exempelkod läser först in exemplet HTML i arbetsboken utan några laddningsalternativ och sparar det i formatet XLSX. Den laddar sedan återigen provet HTML i arbetsboken men den här gången laddar den HTML efter att ha ställt in**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** egendom till**Sann**och sparar den i XLSX-format. Ladda ner båda utdata Excel-filerna, dvs[Utdata Excel-fil utan AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och[Utdata Excel-fil med AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . Följande skärmdump visar effekten av**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**egenskap på båda utdata Excel-filerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

