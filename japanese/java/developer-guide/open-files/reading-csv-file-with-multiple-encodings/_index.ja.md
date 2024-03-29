﻿---
title: 複数のエンコーディングを持つ CSV ファイルの読み取り
type: docs
weight: 140
url: /ja/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

CSV ファイルに複数のエンコーディング (Unicode、ANSI、UTF8、UTF7 など) が含まれている場合があります。 Aspose.Cells を使用すると、そのような CSV ファイルをロードして、PDF や XLSX などの他の形式に変換できます。

{{% /alert %}} 

 Aspose.Cells は TxtLoadOptions.setMultiEncoded() メソッドを提供します。これを設定する必要があります。**真実**複数のエンコーディングで CSV ファイルを適切にロードします。

次のスクリーンショットは、2 行を含むサンプル CSV ファイルを示しています。最初の行は**ANSI**エンコーディングと2行目は**ユニコード**エンコーディング

**入力ファイル** 

![todo:画像_代替_文章](reading-csv-file-with-multiple-encodings_1.png)

次のスクリーンショットは、TxtLoadOptions.setMultiEncoded() メソッドを true に設定せずに、上記の CSV ファイルから変換された XLSX ファイルを示しています。ご覧のとおり、Unicode テキストは適切に変換されていません。

**出力ファイル 1: 複数のエンコードに対応していません** 

![todo:画像_代替_文章](reading-csv-file-with-multiple-encodings_2.png)

次のスクリーンショットは、TxtLoadOptions.setMultiEncoded() メソッドを true に設定した後、上記の CSV ファイルから変換された XSLX ファイルを示しています。ご覧のとおり、Unicode テキストは適切に変換されています。

**出力ファイル 2: IsMultiEncoded が true に設定されている** 

![todo:画像_代替_文章](reading-csv-file-with-multiple-encodings_3.png)

以下は、上記の CSV ファイルを XLSX 形式に正しく変換するサンプル コードです。

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
