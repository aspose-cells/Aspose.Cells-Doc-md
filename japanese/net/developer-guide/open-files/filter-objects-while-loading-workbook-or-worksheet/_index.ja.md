---
title: ワークブックまたはワークシートの読み込み中にオブジェクトをフィルタリングする
type: docs
weight: 330
url: /ja/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **考えられる使用シナリオ**
使ってください[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)ワークブックからデータをフィルタリングする際のプロパティ。ただし、個々のワークシートからデータをフィルター処理する場合は、[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)方法。から適切な値を指定してください[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)作成中または操作中の列挙[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

の[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)列挙には、次の可能な値があります。

- 全て
- ブック設定
- セルブランク
- セルブール
- セルデータ
- セルエラー
- セル数値
- CellString
- セル値
- チャート
- 条件付き書式
- データ検証
- 定義済みの名前
- ドキュメント プロパティ
- 方式
- ハイパーリンク
- 合併面積
- ピボットテーブル
- 設定
- 形
- シートデータ
- シート設定
- 構造
- スタイル
- テーブル
- VBA
- XmlMap
## **ワークブックの読み込み中にオブジェクトをフィルタリングする**
次のサンプル コードは、ワークブックからグラフをフィルター処理する方法を示しています。を確認してください[サンプルエクセルファイル](5115258.xlsx)このコードと[出力 PDF](5115257.pdf)それによって生成されます。出力 PDF でわかるように、すべてのグラフがワークブックから除外されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **ワークシートの読み込み中にオブジェクトをフィルタリングする**
次のサンプル コードは、[ソースエクセルファイル](5115255.xlsx)カスタム フィルターを使用してワークシートから次のデータをフィルター処理します。

- NoCharts という名前のワークシートからチャートをフィルタリングします。
- NoShapes という名前のワークシートから Shapes をフィルター処理します。
- NoConditionalFormatting という名前のワークシートから条件付き書式をフィルター処理します。

一度、ロードします[ソースエクセルファイル](5115255.xlsx)カスタム フィルターを使用すると、すべてのワークシートの画像を 1 つずつ取得します。参考までに、出力イメージを次に示します。ご覧のとおり、最初の画像にはグラフがなく、2 番目の画像には図形がなく、3 番目の画像には条件付き書式がありません。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


これは、ワークシート名ごとに CustomLoadFilter クラスを使用する方法です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
