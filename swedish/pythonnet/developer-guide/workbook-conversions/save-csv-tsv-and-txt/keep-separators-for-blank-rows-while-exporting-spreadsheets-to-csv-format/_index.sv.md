---
title: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format
type: docs
weight: 160
url: /sv/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format med Aspose.Cells för Python via .NET API.
keywords: Python Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format, Behåll avskiljare för tomma rader vid sparande excelfilen till CSV format i Python via NET, Python Behåll avskiljare för tomma rader vid export av excelfil till CSV format.
---

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**

Aspose.Cells för Python via .NET ger möjlighet att behålla radavskiljare vid konvertering av kalkylblad till CSV-format. För detta kan du använda [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)-egenskapen av [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/)-klassen. [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) är en boolesk egenskap. För att behålla avskiljarna för tomma rader vid konvertering av Excelfil till CSV, ställ in [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)-egenskapen till **true**.

Den följande exempelkoden laddar [käll-excelfilen](84378743.xlsx). Den ställer in [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)-egenskapen till **true** och sparar den som [output.csv](84378744.csv). Skärmdumpen visar jämförelsen mellan käll-excelfilen, standardutdata genererad vid konvertering av kalkylblad till CSV och utdata som genereras genom att ställa in [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) till **true**.

![todo:image_alt_text](result.jpg)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
