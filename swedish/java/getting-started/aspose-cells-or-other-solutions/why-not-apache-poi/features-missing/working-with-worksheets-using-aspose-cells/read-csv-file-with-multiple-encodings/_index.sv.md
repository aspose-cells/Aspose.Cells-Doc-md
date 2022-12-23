---
title: Läs CSV Fil med flera kodningar
type: docs
weight: 70
url: /sv/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - Läs CSV fil med flera kodningar**
Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7 etc). Aspose.Cells låter dig ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

**Java**

{{< highlight "java" >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

 För mer information, besök[Läser CSV Fil med flera kodningar](/cells/sv/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
