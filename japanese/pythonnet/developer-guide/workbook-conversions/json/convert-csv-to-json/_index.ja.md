---
title: CSV を JSON に変換します
type: docs
weight: 220
url: /ja/python-net/convert-csv-to-json/
description: Aspose.Cells for Python via .NET API を使用して、CSV を JSON に変換します。
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **CSV を JSON に変換します**

Aspose.Cells for Python via .NET は、CSV から JSON への変換をサポートしています。このために、API は以下を提供します。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**そして**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**クラス。の**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**クラスは、範囲を JSON にエクスポートするためのオプションを提供します。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**クラスには次のプロパティがあります。

- *[文字列としてエクスポート](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: これにより、セルの文字列値が JSON にエクスポートされます。
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: これは、範囲にヘッダー行が含まれるかどうかを示します。
- *[インデント](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: インデントを示します。

の**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**クラスは、で設定されたエクスポート オプションを使用して JSON をエクスポートします。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**クラス。

次のコードサンプルは、の使用法を示しています。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**そして**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**をロードするクラス[ソース CSV ファイル](104398879.csv)そして、コンソールに JSON 出力を出力します。

###  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **コンソール出力**
```json
[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]
```