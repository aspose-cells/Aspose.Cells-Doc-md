---
title: ワークブックまたはワークシートをロードする際にオブジェクトをフィルタリングする
type: docs
weight: 330
url: /ja/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能な使用シナリオ**
データのフィルタリングには、[LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter)プロパティを使用してください。ただし、個々のワークシートからデータをフィルターしたい場合は、[LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet)メソッドをオーバーライドする必要があります。[LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions)列挙体から適切な値を提供してください。

[LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions)列挙体には以下の値があります。

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

{{< app/cells/assistant language="python-net" >}}
