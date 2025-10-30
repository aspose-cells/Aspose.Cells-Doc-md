---
title: CSVをJSONに変換(C++) via Golang
linktitle: CSVをJSONに変換
type: docs
weight: 220
url: /ja/go-cpp/convert-csv-to-json/
description: シンプルなAPIAspose.Cells for C++を使用してCSVファイルをJSONに変換します。
keywords: CSVからJSON、JPEGからJSONArray、CSVをJSONに変換するC++コード例。
---

## **CSVをJSONに変換**

Aspose.CellsはCSVからJSONへの変換をサポートしています。このため、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)クラスはエクスポート範囲をJSONに設定するオプションを提供し、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)クラスには以下のプロパティがあります。

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): セルの文字列値をJSONにエクスポートします。
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): これが範囲にヘッダ行が含まれるかどうかを示します。
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): インデントを示します。

[**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)クラスで設定されたエクスポートオプションを使用してJSONを出力します。

次のコード例は、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスを使用して[ソースCSVファイル](104398879.csv)を読み込み、JSON出力をコンソールに表示します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
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
