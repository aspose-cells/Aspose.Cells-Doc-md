---
title: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format
type: docs
weight: 110
url: /sv/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**

Aspose.Cells ger möjligheten att behålla radavgränsare när du konverterar kalkylblad till CSV-format. För detta kan du använda [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) egenskapen av [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions) klassen. [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) är en boolesk egenskap. För att behålla avgränsarna för blanka rader när du konverterar excelfilen till CSV, ställ in [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) egenskapen till **true**.

Följande exempelkod laddar den [källa Excel-filen](KeepSeparatorsForBlankRow.xlsx). Det ställer in [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) egenskapen till **true** och sparar den som [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). Skärmbilden visar jämförelsen mellan källa Excel-filen, standardutdatan som genererats vid konvertering av kalkylbladet till CSV och utdatan som genererats genom att ställa in [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) till **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
{{< app/cells/assistant language="java" >}}
