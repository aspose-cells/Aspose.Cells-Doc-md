---
title: Läs en CSV fil med flera kodningar
type: docs
weight: 70
url: /sv/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - Läs en CSV-fil med flera kodningar**
Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7 osv). Aspose.Cells tillåter dig att ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

**Java**

{{< highlight java >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

För mer information, besök [Läsning av CSV-fil med flera kodningar](/cells/sv/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
