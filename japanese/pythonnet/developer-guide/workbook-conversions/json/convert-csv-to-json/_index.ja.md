---
title: CSVをJSONに変換
type: docs
weight: 220
url: /ja/python-net/convert-csv-to-json/
description: Aspose.Cells for Python via .NET APIを使用してCSVをJSONに変換します。
keywords: CSVをJSONに変換する、PythonでCSVをJSONに変換するvia NET、PythonでCSVをJSONに変換する、CSVをJSONに保存する。
---

## **CSVをJSONに変換**

Aspose.Cells for Python via .NETは、CSVをJSONに変換する機能をサポートしています。このために、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)および[**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)クラスを提供しています。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)クラスはJSONをエクスポートするためのオプションを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)クラスには次のプロパティがあります。

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): セルの文字列値をJSONにエクスポートします。
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/):範囲にヘッダー行が含まれているかどうかを示します。
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): インデントを示します。

この[**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)クラスで設定されたエクスポートオプションを使用してJSONをエクスポートします。

以下のコードサンプルは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)および[**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)クラスを使用して[ソースのCSVファイル](104398879.csv)をロードし、コンソールにJSON出力を出力する方法を示しています。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

### **コンソール出力**
{{< highlight java >}}

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

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
