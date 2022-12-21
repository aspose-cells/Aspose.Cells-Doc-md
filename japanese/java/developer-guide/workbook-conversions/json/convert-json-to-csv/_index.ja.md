---
title: JSON を CSV に変換する
type: docs
weight: 160
url: /ja/java/convert-json-to-csv/
---
Aspose.Cells は、単純な JSON とネストされた JSON の CSV への変換をサポートしています。このために、API が提供します。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)と[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラス。の[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラスは、次のような JSON レイアウトのオプションを提供します[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(配列がオブジェクトのプロパティである場合、タイトルは無視されます) または[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(配列をテーブルとして処理します)。の[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスは、で設定されたレイアウト オプションを使用して JSON を処理します。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラス。

次のコード サンプルは、[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)と[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)ロードするクラス[ソース JSON ファイル](SampleJson.json)を生成し、[出力CSVファイル](SampleJson_out.csv).

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
