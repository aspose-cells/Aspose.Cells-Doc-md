---
title: GolangからC++を使って、Open High Low Close（OHLC）株価チャートを作成する
description: Aspose.Cells for C++を使った始値高値安値終値の株式チャートの作成方法を学びます。株式市場データ（始値、高値、安値、終値）をチャートにプロットし、分析と可視化を向上させます。
keywords: Aspose.Cells for C++、始値高値安値終値株式チャート、株式市場データ、分析、可視化。
type: docs
weight: 182
url: /ja/go-cpp/create-open-high-low-close-stock-chart/
---

## **可能な使用シナリオ**
Open-High-Low-Close（OHLC）チャートは、カテゴリ、オープン、ハイ、ロー、クローズのデータを使用し、価格の範囲は垂直線で示され、オープンからクローズまでの範囲はより広い浮動バーで示されます。カテゴリ内で価格が上昇する場合（クローズがオープンより高い場合）、バーは1つの色で塗りつぶされ、価格が下落する場合は別の色で塗りつぶされます。この種のチャートは、ローソク足チャートと呼ばれることがよくあります。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **チャートの可視性の改善**
価格の上昇と下降を示すために黒白よりも色をよく使用します。下の最初のキャンドルスティックのセットでは、赤は上昇、緑は下降を示しています。

![todo:image_alt_text](sample2.png)

## **サンプルコード**
[サンプルExcelファイル](Open-High-Low-Close.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成するサンプルコードは、以下の通りです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
