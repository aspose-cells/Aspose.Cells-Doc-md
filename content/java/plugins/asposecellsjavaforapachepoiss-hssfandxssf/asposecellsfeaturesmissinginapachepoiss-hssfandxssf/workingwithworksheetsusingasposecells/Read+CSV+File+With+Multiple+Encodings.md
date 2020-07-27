+++
title = "Read CSV File With Multiple Encodings" 
description = "" 
weight = 20642 
+++

Aspose.Cells for Java : Read CSV File With Multiple Encodings  

# Aspose.Cells for Java : Read CSV File With Multiple Encodings


## Aspose.Cells - Read CSV File With Multiple Encodings

Sometime, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7 etc). Aspose.Cells allows you to load such CSV files and converting them into other formats, for example PDF or XLSX.

**Java**

{{< code lang="java" >}}
//Set Multi Encoded Property to True
TxtLoadOptions options = new TxtLoadOptions();
options.setMultiEncoded(true);

//Load the CSV file into Workbook
Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format
workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

For more details, visit [Reading CSV File with Multiple Encodings](http://docs.aspose.com:8082/docs/display/cellsjava/Reading+CSV+File+with+Multiple+Encodings).

