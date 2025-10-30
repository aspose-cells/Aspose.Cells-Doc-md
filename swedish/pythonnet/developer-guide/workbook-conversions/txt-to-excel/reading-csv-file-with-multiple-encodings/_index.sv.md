---
title: Läsning av CSV fil med flera kodningar
type: docs
weight: 200
url: /sv/python-net/reading-csv-file-with-multiple-encodings/
description: Läsning av CSV fil med flera kodningar med Aspose.Cells för Python via .NET API.
keywords: Python Läsa CSV fil med flera krypteringar, Konvertera CSV fil med flera krypteringar till Excel i Python via NET, Python konvertera CSV fil med flera krypteringar till xlsx, Ladda CSV fil med flera krypteringar till Excel fil.
---

{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera krypteringar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells tillåter dig att ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

Aspose.Cells tillhandahåller egenskapen [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/), som du måste ställa in på **true** för att korrekt ladda din CSV-fil med flera krypteringar.

Följande skärmbild visar en prov-CSV-fil som innehåller två rader. Den första raden är kodad med **ANSI** och den andra raden är kodad med **Unicode**

|**Ingående fil**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Följande skärmbild visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in egenskapen [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) till **true**. Som du kan se konverterades inte den Unicode-texten ordentligt.

|**Utgående fil 1: ingen anpassning gjord för flera krypteringar**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Följande skärmbild visar XSLX-filen konverterad från ovanstående CSV-fil efter att ha ställt in egenskapen [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) till **true**. Som du kan se har den Unicode-texten nu konverterats korrekt.

|**Utgående fil 2: IsMultiEncoded är satt till true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är det exempelkod som konverterar ovanstående CSV-fil till XLSX-format korrekt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
