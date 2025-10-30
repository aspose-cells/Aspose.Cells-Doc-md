---
title: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 200
url: /ja/python-net/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for Python via .NET APIを使用して、複数のエンコーディングを持つCSVファイルの読み込み。
keywords: 複数のエンコーディングを持つCSVファイルを読み込むPython via NET、複数のエンコーディングを持つCSVファイルをExcelに変換する、複数のエンコーディングを持つCSVファイルをExcelに変換する。
---

{{% alert color="primary" %}}

CSVファイルには複数のエンコーディング（Unicode、ANSI、UTF8、UTF7など）が含まれることがあります。Aspose.Cellsを使用すると、このようなCSVファイルをロードし、PDFやXLSXなどの他の形式に変換することができます。

{{% /alert %}}

Aspose.Cellsは[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)プロパティを提供しており、複数のエンコーディングでCSVファイルを正しくロードするには**true**に設定する必要があります。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。1行目は**ANSI**エンコーディングで、2行目は**Unicode**エンコーディングです

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

|**入力ファイル**|

|**出力ファイル1: 複数のエンコーディングを考慮していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

上記のCSVファイルから変換されたXLSXファイルを、[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)プロパティを**true**に設定した後のスクリーンショットは以下の通りです。Unicodeテキストが正しく変換されていることがわかります。

|**出力ファイル2: IsMultiEncodedをtrueに設定**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
