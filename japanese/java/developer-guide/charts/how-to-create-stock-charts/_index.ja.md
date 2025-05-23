---
title: 株価チャートの作成方法
type: docs
weight: 71
url: /ja/java/how-to-create-stock-charts/
description: 株価チャートの作成方法、株価チャートの追加方法、株価チャートの生成方法。
keywords: 株価チャートの追加、株価チャートの作成、株価チャートの生成。
---

{{% alert color="primary" %}}

この段落では、4種類の株価チャートの作成方法が示されます。
- **HLC** – 高値-安値-終値。
- **OHLC** – 始値-高値-安値-終値。
- **VHLC** – 出来高-高値-安値-終値。
- **VOHLC** – 出来高-始値-高値-安値-終値。

{{% /alert %}}

## **株価チャートとは何ですか？**

株価チャートは、取引資産の価格変動を追跡するために使用される特定のチャートで、商品や株式、暗号通貨などの資産などが該当します。これらは1つのチャートで、時間による高値と安値、オープンとクローズの値を見ることができます。Aspose.Cellsでは4つの株価チャートが提供され、これらを使用するには適切なデータセットを持っていることと、正しい順序で列を選択する必要があります。

以下のデータセットは株式の日次取引情報を示しています。このデータを使用して、Aspose.Cellsで利用可能な4つの株価チャートを作成します。 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="java" >}}
