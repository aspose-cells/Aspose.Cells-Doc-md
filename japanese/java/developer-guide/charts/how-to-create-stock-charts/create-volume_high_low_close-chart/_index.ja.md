---
title: 出来高 高値 安値 終値（VHLC）株価チャートを作成する
type: docs
weight: 183
url: /ja/java/create-volume-high-low-close-stock-chart/
description: ボリューム ハイ ロー クローズ（VHLC）株価チャートを作成する方法、ボリューム ハイ ロー クローズ（VHLC）株価チャートを追加する方法、ボリューム ハイ ロー クローズ（VHLC）株価チャートを生成する方法。
keywords: ボリューム ハイ ロー クローズ（VHLC）株価チャートを追加する、ボリューム ハイ ロー クローズ（VHLC）株価チャートを作成する、ボリューム ハイ ロー クローズ（VHLC）株価チャートを生成する。
---

## **可能な使用シナリオ**
私たちが見る3番目の株価チャートは、出来高高安終チャートです。再度、データを正しい順序で持っていることが重要であることを繰り返すことは重要です。データテーブルを再配置する必要がある場合は、チャートを設定する前に行う必要があります。
このチャートには、最初の（カテゴリ）列の直後に出来高の列が含まれており、チャートにはこの出来高を示す主軸の列チャートが含まれます。価格は副軸に移動します。

![todo:image_alt_text](data.png)
## **出来高-高値-安値-終値（VHLC）株価チャート**

![todo:image_alt_text](sample.png)
## **サンプルコード**
[サンプルExcelファイル](Volume-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-create-volume-high-low-close-stock-chart.java" >}}
{{< app/cells/assistant language="java" >}}
