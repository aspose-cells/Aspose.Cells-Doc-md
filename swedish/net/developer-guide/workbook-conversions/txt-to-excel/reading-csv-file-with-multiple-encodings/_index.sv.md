---
title: Läsning av CSV fil med flera kodningar
type: docs
weight: 200
url: /sv/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera krypteringar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells tillåter dig att ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

Aspose.Cells tillhandahåller egenskapen [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded), som du måste ställa in på **true** för att korrekt ladda din CSV-fil med flera krypteringar.

Följande skärmbild visar en prov-CSV-fil som innehåller två rader. Den första raden är kodad med **ANSI** och den andra raden är kodad med **Unicode**

|**Ingående fil**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Följande skärmbild visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in egenskapen [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) till **true**. Som du kan se konverterades inte den Unicode-texten ordentligt.

|**Utgående fil 1: ingen anpassning gjord för flera krypteringar**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Följande skärmbild visar XSLX-filen konverterad från ovanstående CSV-fil efter att ha ställt in egenskapen [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) till **true**. Som du kan se har den Unicode-texten nu konverterats korrekt.

|**Utgående fil 2: IsMultiEncoded är satt till true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är det exempelkod som konverterar ovanstående CSV-fil till XLSX-format korrekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Relaterade artiklar

- [Öppning av CSV-filer](/cells/sv/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
