---
title: グラフシリーズの値フォーマットコードを設定する
description: チャート シリーズの値の書式コードを Aspose.Cells for Java に設定する方法を学習します。このガイドは、適切な書式コードを使用してチャート シリーズのデータを書式設定する方法を理解し、データを正確かつ専門的に表示できるようにするのに役立ちます。
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: 数値の形式
type: docs
weight: 100
url: /ja/java/set-the-values-format-code-of-chart-series/
---
##  **考えられる使用シナリオ**
チャートシリーズの値形式コードを設定するには、[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)方法。この方法は、ワークシート内の範囲に基づく系列だけでなく、値の配列で作成された系列にも有効です。
##  **グラフシリーズの値フォーマットコードを設定する**
次のサンプル コードでは、これまで系列のなかった空のグラフに系列を追加します。値の配列を使用して系列を追加します。シリーズを追加したら、次のコマンドを使用してコード $#,##0 でフォーマットします。[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)メソッドを使用すると、数値 10000 は $10,000 になります。スクリーンショットは、コードによる影響を示しています。[サンプル Excel ファイル](51740712.xlsx)そして[Excelファイルを出力](51740713.xlsx)処刑後。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
