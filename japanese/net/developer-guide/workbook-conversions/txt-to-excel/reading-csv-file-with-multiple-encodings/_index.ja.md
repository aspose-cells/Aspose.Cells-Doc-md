---
title: 複数のエンコーディングを含む CSV ファイルの読み取り
type: docs
weight: 200
url: /ja/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

CSV ファイルに複数のエンコーディング (Unicode、ANSI、UTF8、UTF7 など) が含まれている場合があります。 Aspose.Cells を使用すると、そのような CSV ファイルを読み込んで、PDF や XLSX などの他の形式に変換できます。

{{% /alert %}}

Aspose.Cells は[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)に設定する必要があるプロパティ**真実**複数のエンコーディングを使用して CSV ファイルを適切にロードします。

次のスクリーンショットは、2 行を含むサンプル CSV ファイルを示しています。最初の行は**ANSI**エンコーディングと2行目は**ユニコード**エンコーディング

|**入力ファイル**|
|:- |
|![todo:画像_代替_文章](reading-csv-file-with-multiple-encodings_1.png)|

次のスクリーンショットは、上記の CSV ファイルから変換された XLSX ファイルを示しています。[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)プロパティへ**真実**.ご覧のとおり、Unicode テキストは適切に変換されていません。

|**出力ファイル 1: 複数のエンコードに対応していません**|
|:- |
|![todo:画像_代替_文章](reading-csv-file-with-multiple-encodings_2.png)|

次のスクリーンショットは、設定後に上記の CSV ファイルから変換された XSLX ファイルを示しています。[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)プロパティへ**真実**.ご覧のとおり、Unicode テキストは適切に変換されています。

|**出力ファイル 2: IsMultiEncoded が true に設定されている**|
|:- |
|![todo:画像_代替_文章](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記の CSV ファイルを XLSX 形式に正しく変換するサンプル コードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## 関連記事

- [CSV ファイルを開く](/cells/ja/net/opening-files-with-different-formats/#opening-csv-files)
