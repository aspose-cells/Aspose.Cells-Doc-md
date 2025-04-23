---
title: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 70
url: /de/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - CSV-Datei mit mehreren Codierungen lesen**
Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht es Ihnen, solche CSV-Dateien zu laden und in andere Formate wie z.B. PDF oder XLSX zu konvertieren.

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
## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

Besuchen Sie für weitere Details [Lesen einer CSV-Datei mit mehreren Codierungen](/cells/de/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
