---
title: 複数のエンコーディングを持つ CSV ファイルの読み取り
type: docs
weight: 70
url: /ja/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - 複数のエンコーディングを持つ CSV ファイルの読み取り**
CSV ファイルに複数のエンコーディング (Unicode、ANSI、UTF8、UTF7 など) が含まれている場合があります。 Aspose.Cells を使用すると、そのような CSV ファイルをロードして、PDF や XLSX などの他の形式に変換できます。

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
## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[複数のエンコーディングを持つ CSV ファイルの読み取り](/cells/ja/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
