---
title: Läsning av CSV fil med flera kodningar
type: docs
weight: 140
url: /sv/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7 osv). Aspose.Cells tillåter dig att ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}} 

Aspose.Cells tillhandahåller metoden TxtLoadOptions.setMultiEncoded(), som du behöver sätta till **true** för att korrekt ladda din CSV-fil med flera kodningar.

Följande skärmdump visar en exempel-CSV-fil som innehåller två rader. Första raden är i **ANSI**-kodning och andra raden är i **Unicode**-kodning.

**Ingångsfil** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

Följande skärmdump visar XLSX-filen konverterad från ovanstående CSV-fil utan att ha satt TxtLoadOptions.setMultiEncoded() metoden till true. Som du kan se blev den Unicode-texten inte korrekt konverterad.

**Utdata fil 1: ingen hänsyn tas till flera kodningar** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

Följande skärmdump visar XSLX-filen konverterad från ovanstående CSV-fil efter att ha satt TxtLoadOptions.setMultiEncoded() metoden till true. Som du kan se, är nu Unicode-texten korrekt konverterad.

**Utgångsfil 2: IsMultiEncoded är inställd på true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

Nedan är det exempelkod som konverterar ovanstående CSV-fil till XLSX-format korrekt.

**Java**

{{< highlight csharp >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
