---
title: Läser CSV-fil med flera kodningar
type: docs
weight: 200
url: /sv/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells låter dig ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

 Aspose.Cells tillhandahåller[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) egenskap som du måste ställa in på**Sann** för att ladda din CSV-fil med flera kodningar korrekt.

 Följande skärmdump visar ett exempel på en CSV-fil som innehåller två rader. Första raden är inne**ANSI** kodning och den andra raden är inne**Unicode** kodning

|**Indatafil**|
|:- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 Följande skärmdump visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) egendom till**Sann**. Som du kan se konverterades inte Unicode-texten korrekt.

|**Utdatafil 1: inget boende gjort för multipelkodning**|
|:- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 Följande skärmdump visar XSLX-filen konverterad från ovanstående CSV-fil efter att ha ställt in[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) egendom till**Sann**. Som du kan se är Unicode-texten nu konverterad på rätt sätt.

|**Utdatafil 2: IsMultiEncoded är satt till true**|
|:- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är exempelkoden som konverterar ovanstående CSV-fil till XLSX-format på rätt sätt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## relaterade artiklar

- [Öppna CSV-filer](/cells/sv/net/opening-files-with-different-formats/#opening-csv-files)
