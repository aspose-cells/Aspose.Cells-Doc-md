---
title: Behåll avgränsare för tomma rader när du exporterar kalkylblad till CSV-format
type: docs
weight: 110
url: /sv/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Behåll avgränsare för tomma rader när du exporterar kalkylblad till CSV-format**

Aspose.Cells ger möjlighet att behålla radavgränsare samtidigt som kalkylblad konverteras till CSV-format. För detta kan du använda**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**egendom av**[TxtSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)**klass.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**är en boolesk egenskap. För att behålla avgränsarna för tomma rader när du konverterar Excel-filen till CSV, ställ in**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**egendom till**Sann**.

Följande exempelkod laddar[käll Excel-fil](KeepSeparatorsForBlankRow.xlsx). Det sätter sig**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**egendom till**Sann** och sparar den som[KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). Skärmdumpen visar jämförelsen mellan källfilen i Excel, standardutdata som genereras vid konvertering av kalkylarket till CSV och utdata som genereras genom inställning**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**till**Sann**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
