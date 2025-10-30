---
title: JSONをCSVに変換(C++) via Golang
linktitle: JSONをCSVに変換する
type: docs
weight: 210
url: /ja/go-cpp/convert-json-to-csv/
description: シンプルなJSON例とネストされたJSON例を使用して、Aspose.Cells for C++でJSONをCSVに変換する方法を学びます。
---

## **JSONをCSVに変換**

Aspose.CellsはシンプルなJSONとネストされたJSONの両方をCSVに変換するのをサポートしています。APIは[**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスを提供します。[**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/)クラスは、[**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/)（配列がオブジェクトのプロパティの場合にタイトルを無視）や[**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/)（配列を表として処理）などのJSONレイアウトオプションを提供し、[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスは[**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/)クラスで設定されたレイアウトオプションを使用してJSONを処理します。

次のコード例では、[**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスを使用して[ソースJSONファイル](104398869.json)を読み込み、[出力CSVファイル](104398870.csv)を生成します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
