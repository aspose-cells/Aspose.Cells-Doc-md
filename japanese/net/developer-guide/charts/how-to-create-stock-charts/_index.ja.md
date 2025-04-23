---
title: 株価チャートの作成方法
description: 株価チャートは、取引資産の価格の変化を追跡するために使用される特定のタイプのチャートです。このセクションでは、Aspose.Cells APIを使用してさまざまな種類の株価チャートを簡単に作成する方法を示します。具体的には、次の種類の株価チャートをカバーします：High Low Close（HLC）株価チャート、Open High Low Close（OHLC）チャート、Volume High Low Close（VHLC）株価チャート、Volume Open High Low Close（VOHLC）株価チャート。 
keywords: 株価チャートを作成、Aspose.Cells、マーケットデータの視覚化、株式市場分析、ステップバイステップガイド
type: docs
weight: 71
url: /ja/net/how-to-create-stock-charts/
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

以下のデータセットは、株式の日次取引情報を示しています。このデータを使用して、4種類の株価チャートを作成します：高値-安値-終値(HLC)株価チャート、始値-高値-安値-終値(OHLC)チャート、出来高-高値-安値-終値(VHLC)株価チャート、および出来高-始値-高値-安値-終値(VOHLC)株価チャート。 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="csharp" >}}
