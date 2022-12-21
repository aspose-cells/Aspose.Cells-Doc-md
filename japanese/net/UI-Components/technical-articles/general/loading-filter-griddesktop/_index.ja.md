---
title: GridDesktop でワークブックを読み込み中にオブジェクトをフィルタリングする
type: docs
weight: 1060
url: /ja/net/aspose-cells-griddesktop/loading-filter
description: この記事では、Aspose.Cells.GridDesktop ライブラリの読み込みフィルターの使用方法について説明します。
---
## **考えられる使用シナリオ**
使ってください[GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)ワークブックからデータをフィルタリングする際のプロパティ。

の[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)列挙には次の値があります。
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
## **ワークブックの読み込み中にデータをフィルタリングする**
次のサンプル コードは、ワークブックからの描画をフィルター処理する方法を示しています。を確認してください[サンプルエクセルファイル](5472489.xlsx).ご覧のとおり、すべてのグラフ/図形/画像がワークブックから除外されています。
![画像のないワークブック](nodrawing.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}
 