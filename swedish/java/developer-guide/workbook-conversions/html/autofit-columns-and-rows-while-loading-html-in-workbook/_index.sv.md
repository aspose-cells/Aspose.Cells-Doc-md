---
title: Autopassa kolumner och rader när HTML laddas i arbetsboken
type: docs
weight: 70
url: /sv/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Möjliga användningsscenarier**

 Du kan automatiskt anpassa kolumner och rader medan du laddar din HTML-fil inuti**[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Arbetsbok)**objekt. Vänligen ställ in**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** egendom till**Sann**för detta ändamål.

## **Autopassa kolumner och rader när HTML laddas i arbetsboken**

 Följande exempelkod läser först in exemplet HTML i arbetsboken utan några laddningsalternativ och sparar det i formatet XLSX. Den laddar sedan återigen provet HTML i arbetsboken men den här gången laddar den HTML efter att ha ställt in**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** egendom till**Sann**och sparar den i XLSX-format. Ladda ner båda utdata Excel-filerna, dvs[Utdata Excel-fil utan AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och[Utdata Excel-fil med AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . Följande skärmdump visar effekten av**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)**egenskap på båda utdata Excel-filerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
