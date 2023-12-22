---
title: 出来高-高値-安値-終値(VHLC)株価チャートの作成
type: docs
weight: 183
url: /ja/java/create-volume-high-low-close-stock-chart/
description: 出来高・高値・安値・終値(VHLC)株価チャートを作成する方法、出来高・高値・安値・終値(VHLC)株価チャートを追加する方法、出来高・高値・安値・終値(VHLC)株価チャートを生成する方法。
keywords: Add Volume-High-Low-Close(VHLC) Stock Chart, Create Volume-High-Low-Close(VHLC) Stock Chart, Generate Volume-High-Low-Close(VHLC) Stock Chart.
---
##  **考えられる使用シナリオ**
3 つ目の株価チャートは、出来高高値安値終値チャートです。データを正しい順序で指定する必要があることを繰り返します。データテーブルを再配置する必要がある場合は、グラフを設定する前に行う必要があります。
このチャートには、最初の (カテゴリー) 列の直後に出来高の列が含まれており、このチャートの主軸にはこの出来高を示す縦棒グラフが含まれており、価格は第 2 軸に移動しています。

![todo:image_alt_text](data.png)
##  **出来高・高値・安値・終値（VHLC）株価チャート**

![todo:image_alt_text](sample.png)
##  **サンプルコード**
次のサンプルコードは、[サンプル Excel ファイル](Volume-High-Low-Close.xlsx)そして、[Excelファイルを出力](out.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
