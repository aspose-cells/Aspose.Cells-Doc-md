---
title: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 140
url: /ja/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

CSVファイルにはUnicode、ANSI、UTF8、UTF7など複数のエンコーディングが含まれる場合があります。Aspose.Cellsを使用すると、これらのCSVファイルを読み込んで他の形式（例：PDFまたはXLSX）に変換することができます。

{{% /alert %}} 

Aspose.CellsはTxtLoadOptions.setMultiEncoded()メソッドを提供しており、複数のエンコーディングを持つCSVファイルを適切に読み込むには**true**に設定する必要があります。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。最初の行は**ANSI**エンコーディングで、2番目の行は**Unicode**エンコーディングです。

**入力ファイル** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

以下のスクリーンショットは、TxtLoadOptions.setMultiEncoded()メソッドをtrueに設定せずに上記のCSVファイルから変換されたXLSXファイルを示しています。Unicodeテキストが正しく変換されていないことがわかります。

**出力ファイル1： 複数のエンコーディングに対する対応なし** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

以下のスクリーンショットは、TxtLoadOptions.setMultiEncoded()メソッドをtrueに設定した後、上記のCSVファイルから変換されたXSLXファイルを示しています。Unicodeテキストが正しく変換されていることがわかります。

**出力ファイル2：IsMultiEncodedがtrueに設定されています** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

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
