﻿---
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

[