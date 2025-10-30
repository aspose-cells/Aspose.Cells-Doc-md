---
title: Behåll separatorer för tomma rader vid export av kalkylblad till CSV format med Golang via C++
linktitle: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format
type: docs
weight: 160
url: /sv/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Lär dig hur du behåller separatorer för tomma rader vid export av kalkylblad till CSV format med Aspose.Cells med Golang via C++.
---

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**

Aspose.Cells ger möjlighet att behålla radseparatorer vid konvertering av kalkblad till CSV-format. För detta kan du använda [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)-egenskapen hos [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/)-klass. [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) är en boolesk egenskap. För att behålla separatorerna för tomma rader vid konvertering av Excel-fil till CSV, ställ in [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)-egenskapen till **true**.

Följande kod laddar [käll-Excel-filen](84378743.xlsx). Den ställer in [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/)-egenskapen till **true** och sparar den som [utdata.csv](84378744.csv). Skärmbilden visar jämförelsen mellan käll-Excel-filen, standardutdata som genereras vid konvertering av kalkblad till CSV och den utdata som genereras när [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) ställs in på **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
