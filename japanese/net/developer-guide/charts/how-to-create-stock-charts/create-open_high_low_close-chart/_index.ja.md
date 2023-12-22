---
title: 始値・高値・安値・終値(OHLC)株価チャートの作成
description: Aspose.Cells for .NET を使用して、始値、高値、安値、終値の株価チャートを作成する方法を学びます。このガイドでは、分析と視覚化を改善するために、始値、高値、安値、終値などの株式市場データをチャートにプロットする方法を説明します。
keywords: Aspose.Cells for .NET, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /ja/net/create-open-high-low-close-stock-chart/
---
##  **考えられる使用シナリオ**
始値-高値-安値-終値 (OHLC) チャートでは、カテゴリ、始値、高値、安値、終値の順に 5 列のデータが使用されます。各カテゴリの価格の範囲は再び垂直線で示され、始値と終値の間の範囲は幅の広い浮動バーで示されます。カテゴリ内の価格が上昇すると (終値が始値よりも高くなります)、バーは 1 つの色で塗りつぶされ、価格が下がると、バーは別の色で塗りつぶされます。このタイプのチャートは、多くの場合、ローソク足チャートと呼ばれます。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
##  **チャートの視認性の向上**
価格の増減を示すために、白黒ではなく色を使用することがよくあります。以下の最初のローソク足セットでは、赤は価格の上昇を示し、緑は価格の低下を示します。

![todo:image_alt_text](sample2.png)
##  **サンプルコード**
次のサンプルコードは、[サンプル Excel ファイル](Open-High-Low-Close.xlsx)そして、[Excelファイルを出力](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
