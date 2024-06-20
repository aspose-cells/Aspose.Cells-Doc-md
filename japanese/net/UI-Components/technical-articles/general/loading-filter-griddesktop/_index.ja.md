---
title: GridDesktopでワークブックをローディングする際のフィルターオブジェクト
type: docs
weight: 1060
url: /ja/net/aspose-cells-griddesktop/loading-filter
description: この記事では、GridDesktopでのローディングフィルタの使用方法について説明します。
keywords: GridDesktop,loading,loading filter,filter
---

## **可能な使用シナリオ**
[GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)プロパティを使用してワークブックからデータをフィルタリングしてください。

[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)列挙型には、以下の値があります。
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
## **ワークブックのデータの読み込み中にデータをフィルタリングする**
次のサンプルコードは、ワークブックから図をフィルタリングする方法を示しています。[サンプルのExcelファイル](5472489.xlsx)を参照してください。すべてのチャート/図形/画像がワークブックからフィルタリングされていることがわかります。
![画像なしのワークブック](nodrawing.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}

