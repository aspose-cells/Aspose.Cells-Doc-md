---
title: CSV を JSON に変換
type: docs
weight: 220
url: /ja/net/convert-csv-to-json/
description: 使いやすい Aspose.Cells for .NET API を使用して、CSF ファイルを JSON に変換します。
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **CSV を JSON に変換**

Aspose.Cells は、CSV から JSON への変換をサポートします。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**と**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**クラス。の**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**クラスは、範囲を JSON にエクスポートするためのオプションを提供します。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**クラスには次のプロパティがあります。

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**: これにより、セルの文字列値が JSON にエクスポートされます。
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: 範囲にヘッダー行が含まれているかどうかを示します。
- **[インデント](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**インデントを示します。

の**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**クラスは、で設定されたエクスポート オプションを使用して JSON をエクスポートします**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**クラス。

次のコード サンプルは、**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**と**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**ロードするクラス[ソース CSV ファイル](104398879.csv)コンソールに JSON 出力を出力します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **コンソール出力**
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