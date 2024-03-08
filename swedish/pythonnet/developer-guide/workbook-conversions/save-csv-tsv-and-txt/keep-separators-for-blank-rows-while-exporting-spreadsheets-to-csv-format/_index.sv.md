---
title: Behåll avgränsare för tomma rader när du exporterar kalkylblad till CSV-format
type: docs
weight: 160
url: /sv/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Behåll separatorer för tomma rader när du exporterar kalkylark till CSV-formatet genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Keep Separators for Blank Rows while exporting spreadsheets to CSV format, Keep Separators for Blank Rows while saving excel to CSV format in Python via NET, Python Keep Separators for Blank Rows when exporting excel to CSV format.
---
##  **Behåll avgränsare för tomma rader när du exporterar kalkylblad till CSV-format**

Aspose.Cells for Python via .NET ger möjlighet att behålla radavgränsare samtidigt som kalkylblad konverteras till CSV-format. För detta kan du använda**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**egendom av**[TxtSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/)**klass.**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**är en boolesk egenskap. För att behålla avgränsarna för tomma rader när du konverterar Excel-filen till CSV, ställ in**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**egendom till *sant**.

Följande exempelkod laddar[käll Excel-fil](84378743.xlsx). Det sätter sig**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**egendom till**Sann** och sparar den som[output.csv](84378744.csv) . Skärmdumpen visar jämförelsen mellan källfilen i Excel, standardutdata som genereras vid konvertering av kalkylarket till CSV och utdata som genereras genom inställning**[keep_separators_for_blank_row](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/)**till *sant**.

![todo:image_alt_text](result.jpg)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
