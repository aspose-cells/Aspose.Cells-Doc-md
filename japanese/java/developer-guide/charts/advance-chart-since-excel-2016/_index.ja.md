---
title: Excel 2016 グラフの読み取りと操作
type: docs
weight: 150
url: /ja/java/read-and-manipulate-excel-2016-charts/
---
## **考えられる使用シナリオ**
Aspose.Cells は、Microsoft Excel 2013 以前のバージョンには存在しない Microsoft Excel 2016 チャートの読み取りと操作をサポートします。
## **Excel 2016 グラフの読み取りと操作**
次のサンプル コードは、[ソースエクセルファイル](23166980.xlsx)最初のワークシートに Microsoft Excel 2016 グラフが含まれています。すべてのチャートを 1 つずつ読み取り、チャートの種類に応じてタイトルを変更します。次のスクリーンショットは、コード実行前のソース Excel ファイルを示しています。ご覧のとおり、チャート タイトルはすべてのチャートで同じです。

![todo:画像_代替_文章](read-and-manipulate-excel-2016-charts_1.png)

次のスクリーンショットは、[出力エクセルファイル](23166978.xlsx)コードの実行後。ご覧のとおり、チャートのタイトルはチャートの種類ごとに変更されています。

![todo:画像_代替_文章](read-and-manipulate-excel-2016-charts_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ReadManipulateExcel2016Charts-ReadManipulateExcel2016Charts.java" >}}
## **コンソール出力**
上記のサンプル コードを提供されたコマンドで実行した場合のコンソール出力は次のとおりです。[ソースエクセルファイル](23166980.xlsx).

{{< highlight "java" >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}

## **先行トピック**
- [ウォーターフォール チャートの作成](/cells/ja/java/creating-waterfall-chart/)
