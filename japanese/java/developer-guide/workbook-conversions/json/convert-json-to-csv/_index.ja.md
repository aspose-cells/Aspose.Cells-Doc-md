---
title: JSONをCSVに変換する
type: docs
weight: 160
url: /ja/java/convert-json-to-csv/
---

Aspose.Cellsは、単純なJSONだけでなく、ネストされたJSONをCSVに変換することをサポートしています。このため、APIは[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)および[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスを提供します。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラスは、JSONレイアウトに関するオプションを提供します。たとえば、[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(オブジェクトのプロパティの配列の場合、タイトルを無視します)または[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(テーブルとして配列を処理します)。[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスは、[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラスで設定されたレイアウトオプションを使用してJSONを処理します。

次のコードサンプルは、[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)および[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスを使用して、[source JSON file](SampleJson.json)をロードし、[output CSV file](SampleJson_out.csv)を生成する方法を示しています。

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
