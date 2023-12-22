---
title: 複数のエンコーディングを持つ CSV ファイルの読み取り
type: docs
weight: 200
url: /ja/python-net/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for Python via .NET API を使用して、複数のエンコーディングを持つ CSV ファイルを読み取ります。
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

CSV ファイルに複数のエンコーディング (Unicode、ANSI、UTF8、UTF7 など) が含まれている場合があります。 Aspose.Cells を使用すると、このような CSV ファイルをロードし、他の形式 (PDF や XLSX など) に変換できます。

{{% /alert %}}

 Aspose.Cells は、[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)に設定する必要があるプロパティ**真実**複数のエンコーディングを使用して CSV ファイルを適切にロードするには、

次のスクリーンショットは、2 行を含むサンプル CSV ファイルを示しています。最初の行は次のとおりです**ANSI**エンコーディングと2行目は**ユニコード**エンコーディング

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

次のスクリーンショットは、上記の CSV ファイルを設定せずに変換した XLSX ファイルを示しています。[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)プロパティを *true** に設定します。ご覧のとおり、Unicode テキストは正しく変換されませんでした。

|**出力ファイル 1: 複数のエンコードに対応していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

次のスクリーンショットは、設定後に上記の CSV ファイルから変換された XSLX ファイルを示しています。[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)プロパティを *true** に設定します。ご覧のとおり、Unicode テキストが適切に変換されるようになりました。

|**出力ファイル 2: IsMultiEncoded が true に設定されます**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記の CSV ファイルを XLSX 形式に正しく変換するサンプルコードです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
