---
title: Go言語を介したC++による複数エンコーディングのCSVファイル読み取り
linktitle: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 200
url: /ja/go-cpp/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for C++を使用して、複数のエンコーディング（Unicode、ANSI、UTF8、UTF7など）を持つCSVファイルの読み取り方法を学びます。
---

{{% alert color="primary" %}}

時には、CSVファイルに複数のエンコーディング（Unicode、ANSI、UTF8、UTF7など）が含まれている場合があります。Aspose.Cellsを使えば、そのようなCSVファイルをロードして、PDFやXLSXなどの他のフォーマットに変換できます。

{{% /alert %}}

Aspose.Cellsは[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)プロパティを提供しており、これを**true**に設定する必要があります。そうすることで、複数エンコーディングのCSVファイルを正しく読み込むことができます。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。最初の行は**ANSI**エンコーディングで、2行目は**Unicode**エンコーディングです。

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下のスクリーンショットは、上記のCSVファイルから変換されたXLSXファイルを、[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)プロパティを**true**に設定しなかった場合を示しています。ご覧のとおり、Unicodeテキストは正しく変換されませんでした。

|**出力ファイル1: 複数のエンコーディングを考慮していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下のスクリーンショットは、[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)プロパティを**true**に設定した後の、上記のCSVファイルから変換されたXLSXファイルを示しています。ご覧のとおり、Unicodeテキストは正しく変換されています。

|**出力ファイル2: IsMultiEncodedをtrueに設定**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## 関連記事

- [CSV ファイルを開く](/cells/ja/cpp/opening-files-with-different-formats/#opening-csv-files)
