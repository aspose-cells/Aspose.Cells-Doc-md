---
title: ワークブックまたはワークシートをロードする際にオブジェクトをフィルタリングする
type: docs
weight: 330
url: /ja/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能な使用シナリオ**
ワークブックからデータをフィルタリングする際は、[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)プロパティを使用してください。ただし、個々のワークシートからデータをフィルタリングする場合は、[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)メソッドをオーバーライドする必要があります。[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)を作成または使用する際は、[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)の列挙型から適切な値を指定してください。

[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)列挙型には、以下の可能な値があります。

- 全て
- ブック設定
- 空白セル
- ブールセル
- データセル
- エラーセル
- 数値セル
- 文字列セル
- 値セル
- Chart
- 条件付き書式
- データの検証
- 定義された名前
- ドキュメントのプロパティ
- 数式
- ハイパーリンク
- 結合エリア
- ピボットテーブル
- 設定
- 図形
- シートデータ
- シート設定
- 構造
- スタイル
- テーブル
- VBA
- XmlMap
## **ワークブックの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、ワークブックからグラフをフィルタリングする方法を示しています。このコードで使用されている[サンプルエクセルファイル](5115258.xlsx)とその生成された[出力PDF](5115257.pdf)を確認してください。出力PDFでは、すべてのグラフがワークブックからフィルタリングされていることが分かります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **ワークシートの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、[ソースエクセルファイル](5115255.xlsx)を読み込み、カスタムフィルタを使用してそのワークシートから以下のデータをフィルタリングする方法を説明しています。

- NoChartsという名前のワークシートからグラフをフィルタリングします。
- NoShapesという名前のワークシートから形状をフィルタリングします。
- NoConditionalFormattingという名前のワークシートから条件付き書式をフィルタリングします。

1つのカスタムフィルタで[ソースエクセルファイル](5115255.xlsx)を読み込むと、ワークシートを1つずつ画像化します。以下は参照用の出力画像です。最初の画像にはグラフがなく、2番目の画像には形状がなく、3番目の画像には条件付き書式がないことが分かります。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


ワークシート名に従ってCustomLoadFilterクラスを使用する方法

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
