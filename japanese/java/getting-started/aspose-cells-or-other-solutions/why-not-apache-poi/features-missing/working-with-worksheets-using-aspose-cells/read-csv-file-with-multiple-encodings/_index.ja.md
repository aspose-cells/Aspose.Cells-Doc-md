---
title: 複数のエンコーディングで CSV ファイルを読み込む
type: docs
weight: 70
url: /ja/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - 複数のエンコーディングで CSV ファイルを読み込む**
CSVファイルにはUnicode、ANSI、UTF8、UTF7など複数のエンコーディングが含まれる場合があります。Aspose.Cellsを使用すると、これらのCSVファイルを読み込んで他の形式（例：PDFまたはXLSX）に変換することができます。

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
## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

[複数のエンコーディングで CSV ファイルを読み込む](/cells/ja/java/reading-csv-file-with-multiple-encodings)の詳細については、こちらをご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
