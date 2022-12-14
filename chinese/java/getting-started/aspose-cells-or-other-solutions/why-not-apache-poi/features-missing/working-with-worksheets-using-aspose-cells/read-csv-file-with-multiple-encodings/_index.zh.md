---
title: 读取具有多种编码的 CSV 文件
type: docs
weight: 70
url: /zh/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - 读取具有多种编码的 CSV 文件**
有时，您的 CSV 文件包含多个编码（Unicode、ANSI、UTF8、UTF7 等）。 Aspose.Cells 允许您加载此类 CSV 文件并将其转换为其他格式，例如 PDF 或 XLSX。

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
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[读取具有多种编码的 CSV 文件](/cells/zh/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
