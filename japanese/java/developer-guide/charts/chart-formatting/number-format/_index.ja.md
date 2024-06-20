---
title: チャートシリーズの値の形式コードを設定する
description: Aspose.Cells for Javaのチャートシリーズの値のフォーマットコードの設定方法を学びます。当ガイドにより、適切なフォーマットコードを使用してチャートシリーズデータをフォーマットし、正確でプロフェッショナルなデータを提供する方法を理解できます。
keywords: Aspose.Cells for Java, チャートシリーズ, 値のフォーマットコード, フォーマット, データプレゼンテーション, 正確さ, プロフェッショナリズム。
linktitle: 数値形式
type: docs
weight: 100
url: /ja/java/set-the-values-format-code-of-chart-series/
---

## **可能な使用シナリオ**
チャートシリーズの値のフォーマットコードを[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)メソッドを使用して設定できます。このメソッドはワークシート内の範囲に基づくシリーズだけでなく、値の配列で作成されたシリーズにも適用できます。
## **チャートシリーズの値の形式コードを設定する**
次のサンプルコードは、以前にシリーズがない空のチャートにシリーズを追加します。値の配列を使用してシリーズを追加した後、[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)メソッドを使用してコード$#,##0でフォーマットします。この方法で、数値10000が$10,000になります。スクリーンショットは、コードの効果を示し、実行後の[sample Excelファイル](51740712.xlsx)と[出力Excelファイル](51740713.xlsx)を表示しています。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
