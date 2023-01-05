---
title: Läser CSV Fil med flera kodningar
type: docs
weight: 140
url: /sv/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7 etc). Aspose.Cells låter dig ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}} 

 Aspose.Cells tillhandahåller metoden TxtLoadOptions.setMultiEncoded() som du måste ställa in på**Sann** för att ladda din CSV-fil med flera kodningar korrekt.

 Följande skärmdump visar ett exempel på CSV-fil som innehåller två rader. Första raden är inne**ANSI** kodning och den andra raden är inne**Unicode** kodning

**Indatafil** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

Följande skärmdump visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in metoden TxtLoadOptions.setMultiEncoded() till true. Som du kan se konverterades inte Unicode-texten korrekt.

**Utdatafil 1: inget boende gjort för multipelkodning** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

Följande skärmdump visar XSLX-filen konverterad från ovanstående CSV-fil efter att ha ställt in metoden TxtLoadOptions.setMultiEncoded() till true. Som du kan se är Unicode-texten nu konverterad på rätt sätt.

**Utdatafil 2: IsMultiEncoded är satt till true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

Nedan är exempelkoden som konverterar ovanstående CSV-fil till XLSX-format korrekt.

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
