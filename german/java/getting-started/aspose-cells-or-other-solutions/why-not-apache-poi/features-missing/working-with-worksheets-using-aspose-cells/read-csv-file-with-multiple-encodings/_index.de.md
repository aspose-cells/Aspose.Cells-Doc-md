---
title: Lesen Sie die Datei CSV mit mehreren Codierungen
type: docs
weight: 70
url: /de/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - CSV-Datei mit mehreren Codierungen lesen**
Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Mit Aspose.Cells können Sie solche CSV-Dateien laden und in andere Formate konvertieren, z. B. PDF oder XLSX.

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
## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Lesen von CSV-Datei mit mehreren Codierungen](/cells/de/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
