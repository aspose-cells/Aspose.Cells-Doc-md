---
title: JSON を CSV に変換する
type: docs
weight: 210
url: /ja/net/convert-json-to-csv/
---
## **JSON を CSV に変換する**

Aspose.Cells は、単純な JSON とネストされた JSON の CSV への変換をサポートしています。このために、API が提供します。**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**と**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**クラス。の**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**クラスは、次のような JSON レイアウトのオプションを提供します**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(配列がオブジェクトのプロパティである場合、タイトルは無視されます) または**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(配列をテーブルとして処理します)。の**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**クラスは、で設定されたレイアウト オプションを使用して JSON を処理します。**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**クラス。

次のコード サンプルは、**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**と**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**ロードするクラス[ソース JSON ファイル](104398869.json)を生成し、[出力CSVファイル](104398870.csv).

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
