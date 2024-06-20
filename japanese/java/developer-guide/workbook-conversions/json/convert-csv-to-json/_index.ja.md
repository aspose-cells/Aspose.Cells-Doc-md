---
title: CSVをJSONに変換
type: docs
weight: 170
url: /ja/java/convert-csv-to-json/
---

## **CSVをJSONに変換**

Aspose.CellsはCSVをJSONに変換することをサポートしています。このために、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)および[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)クラスは、範囲をJSONにエクスポートするオプションを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)クラスには以下のプロパティがあります。

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): セルの文字列値をJSONにエクスポートします。
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow):範囲にヘッダー行が含まれているかどうかを示します。
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): インデントを示します。

この[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)クラスで設定されたエクスポートオプションを使用してJSONをエクスポートします。

次のコードサンプルは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)および[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスを使用して[ソースCSVファイル](SampleCsv.csv)をロードし、コンソールに[JSON](SampleJson_out.csv)出力を表示する方法を示しています。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

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
