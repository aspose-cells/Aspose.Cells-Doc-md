---
title: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format
type: docs
weight: 160
url: /sv/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**

Aspose.Cells ger möjligheten att behålla radavgränsare när du konverterar kalkylblad till CSV-format. För detta kan du använda [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) egenskapen av [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions) klassen. [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) är en boolesk egenskap. För att behålla avgränsarna för blanka rader när du konverterar excelfilen till CSV, ställ in [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) egenskapen till **true**.

Den följande exempelkoden laddar [käll-excelfilen](84378743.xlsx). Den ställer in [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)-egenskapen till **true** och sparar den som [output.csv](84378744.csv). Skärmdumpen visar jämförelsen mellan käll-excelfilen, standardutdata genererad vid konvertering av kalkylblad till CSV och utdata som genereras genom att ställa in [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) till **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
