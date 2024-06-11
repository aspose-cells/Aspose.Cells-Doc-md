---
title: 使用多种编码读取CSV文件
type: docs
weight: 70
url: /zh/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - 使用多种编码读取CSV文件**
有时，您的CSV文件包含多种编码（Unicode、ANSI、UTF8、UTF7等）。 Aspose.Cells允许您加载此类CSV文件并将其转换为其他格式，例如PDF或XLSX。

Java

{{< highlight java >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

有关更多详情，请访问[使用多种编码读取CSV文件](/cells/zh/java/reading-csv-file-with-multiple-encodings)。

{{% /alert %}}
