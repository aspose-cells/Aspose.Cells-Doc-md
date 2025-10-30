---
title: GO言語とC++経由でワークブックまたはワークシートの読み込み時にオブジェクトをフィルタリングします
linktitle: ワークブックまたはワークシートをロードする際にオブジェクトをフィルタリングする
type: docs
weight: 330
url: /ja/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aspose.Cells for C++を用いて、ワークブックやシートの読み込み時にチャートや図形、条件付き書式などのオブジェクトをフィルタリングする方法を学習します。
---

## **可能な使用シナリオ**
[LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) プロパティを使用してワークブックからデータをフィルタリングしてください。ただし、個々のワークシートからデータをフィルタリングしたい場合は、[LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) メソッドをオーバーライドする必要があります。[LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) 列挙体から適切な値を設定して [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/) を作成または操作してください。

[LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) 列挙体には以下の可能な値があります。

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **ワークシートの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、[ソースエクセルファイル](5115255.xlsx)を読み込み、カスタムフィルタを使用してそのワークシートから以下のデータをフィルタリングする方法を説明しています。

- NoChartsという名前のワークシートからグラフをフィルタリングします。
- NoShapesという名前のワークシートから形状をフィルタリングします。
- NoConditionalFormattingという名前のワークシートから条件付き書式をフィルタリングします。

1つのカスタムフィルタで[ソースエクセルファイル](5115255.xlsx)を読み込むと、ワークシートを1つずつ画像化します。以下は参照用の出力画像です。最初の画像にはグラフがなく、2番目の画像には形状がなく、3番目の画像には条件付き書式がないことが分かります。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
ワークシート名に従ってCustomLoadFilterクラスを使用する方法

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
