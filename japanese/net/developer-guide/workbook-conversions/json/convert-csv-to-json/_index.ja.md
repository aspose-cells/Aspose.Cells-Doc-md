---
title: CSVをJSONに変換
type: docs
weight: 220
url: /ja/net/convert-csv-to-json/
description: 簡単に使用できるAspose.Cells for .NET APIを使用して、CSFファイルをJSONに変換する。
keywords: 変換、CSVからJSONへの変換、CSVからJSON、CSV、JSON、CSVからJSON CSharpへの変換、CSVをJSONに変換するためのc#コード
---

## **CSVをJSONに変換**

Aspose.Cellsでは、CSVをJSONに変換する機能がサポートされています。このために、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)および[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)クラスはJSONへの範囲のエクスポートオプションを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)クラスには以下のプロパティがあります。

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): セルの文字列値をJSONにエクスポートします。
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow):範囲にヘッダー行が含まれているかどうかを示します。
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): インデントを示します。

この[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)クラスで設定されたエクスポートオプションを使用してJSONをエクスポートします。

以下のコードサンプルは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)および[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスを使用して[ソースのCSVファイル](104398879.csv)をロードし、コンソールにJSON出力を出力する方法を示しています。

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
