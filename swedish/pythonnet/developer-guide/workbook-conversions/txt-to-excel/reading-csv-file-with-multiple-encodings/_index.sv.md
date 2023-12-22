---
title: Läser CSV Fil med flera kodningar
type: docs
weight: 200
url: /sv/python-net/reading-csv-file-with-multiple-encodings/
description: Läser CSV Fil med flera kodningar genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells låter dig ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

 Aspose.Cells tillhandahåller[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) egenskap som du måste ställa in på**Sann** för att ladda din CSV-fil med flera kodningar korrekt.

 Följande skärmdump visar ett exempel på CSV-fil som innehåller två rader. Första raden är inne**ANSI** kodning och den andra raden är inne**Unicode** kodning

|**Indatafil**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Följande skärmdump visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)egendom till *sant**. Som du kan se konverterades inte Unicode-texten korrekt.

|**Utdatafil 1: inget boende gjort för multipelkodning**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 Följande skärmdump visar XSLX-filen konverterad från ovanstående CSV-fil efter att ha ställt in[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)egendom till *sant**. Som du kan se är Unicode-texten nu konverterad på rätt sätt.

|**Utdatafil 2: IsMultiEncoded är satt till true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är exempelkoden som konverterar ovanstående CSV-fil till XLSX-format korrekt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
