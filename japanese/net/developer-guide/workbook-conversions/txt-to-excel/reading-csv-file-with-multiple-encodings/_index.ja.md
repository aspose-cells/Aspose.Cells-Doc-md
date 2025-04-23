---
title: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 200
url: /ja/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

CSVファイルには複数のエンコーディング（Unicode、ANSI、UTF8、UTF7など）が含まれることがあります。Aspose.Cellsを使用すると、このようなCSVファイルをロードし、PDFやXLSXなどの他の形式に変換することができます。

{{% /alert %}}

Aspose.Cellsは[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)プロパティを提供しており、複数のエンコーディングでCSVファイルを正しくロードするには**true**に設定する必要があります。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。1行目は**ANSI**エンコーディングで、2行目は**Unicode**エンコーディングです

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

|**入力ファイル**|

|**出力ファイル1: 複数のエンコーディングを考慮していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

上記のCSVファイルから変換されたXLSXファイルを、[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)プロパティを**true**に設定した後のスクリーンショットは以下の通りです。Unicodeテキストが正しく変換されていることがわかります。

|**出力ファイル2: IsMultiEncodedをtrueに設定**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## 関連記事

- [CSV ファイルを開く](/cells/ja/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
