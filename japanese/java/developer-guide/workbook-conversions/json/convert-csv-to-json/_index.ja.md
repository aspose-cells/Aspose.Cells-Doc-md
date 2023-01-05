---
title: CSV を JSON に変換
type: docs
weight: 170
url: /ja/java/convert-csv-to-json/
---
## **CSV を JSON に変換**

Aspose.Cells は、CSV から JSON への変換をサポートします。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)と[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラス。の[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)クラスは、範囲を JSON にエクスポートするためのオプションを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)クラスには次のプロパティがあります。

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): これにより、セルの文字列値が JSON にエクスポートされます。
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): 範囲にヘッダー行が含まれているかどうかを示します。
- [**インデント**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent)インデントを示します。

の[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスは、で設定されたエクスポート オプションを使用して JSON をエクスポートします[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)クラス。

次のコード サンプルは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)と[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)ロードするクラス[ソース CSV ファイル](SampleCsv.csv)そして印刷します[JSON](SampleJson_out.csv)コンソールに出力します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **コンソール出力**

[ { "id": 1, "言語": "Java", "版": "3 番目", "著者": "ハーバート シルト", "streetAddress": 126, "都市": "San Jone", "state": "CA", "postalCode": 394221 }, { "id": 2, "language": "C++", "edition": "second", "著者": "EAAAA", "streetAddress": 126, "都市": "サン ジョーン", "都道府県": "CA", "郵便番号": 394221 }, { "id": 3 , "language": ".Net", "edition": "second", "author": "E.Balagurusamy", "streetAddress": 126, "city": "San Jone", "状態": "CA", "郵便番号": 394221 } ]