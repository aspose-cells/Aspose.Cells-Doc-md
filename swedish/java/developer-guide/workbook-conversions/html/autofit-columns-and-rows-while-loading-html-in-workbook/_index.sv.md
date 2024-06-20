---
title: Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken
type: docs
weight: 70
url: /sv/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Möjliga användningsscenario**

Du kan justera kolumner och rader automatiskt vid inläsning av din HTML-fil i objektet [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Vänligen ställ in egenskapen [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) till **true** för detta ändamål.

## **Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken**

Följande kodexempel laddar först det provisoriska HTML-filen into arbetsboken utan några laddningsalternativ och sparar den i XLSX-format. Sedan laddar den igen det provisoriska HTML-filen in i arbetsboken, men den här gången laddas HTML-filen efter att ha ställt in egenskapen [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) till **true** och sparar den i XLSX-format. Vänligen ladda ner båda utdataexcel-filerna, dvs. [Utfil utan AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och [Utfil med AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Följande skärmbild visar effekten av egenskapen [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) på båda utdataexcel-filerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
