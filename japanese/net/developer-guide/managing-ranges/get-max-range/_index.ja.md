---
title: ワークシート内の最大範囲を取得する
type: docs
weight: 360
url: /ja/net/get-max-range-in-a-worksheet/
description: この記事では、.Net ライブラリの Aspose.Cells を使用して Excel ファイルの最大範囲、最大データ範囲、最大表示範囲を取得する方法について説明します。
---
{{% alert color="primary" %}} 

ワークシートからデータを読み取るときは、最大領域を知る必要があります。

ワークシートからすべてのデータをコピーするときは、最大領域を知る必要があります。

指定した領域を html や pdf にエクスポートする場合、最大領域を知る必要があります。

 .Net の Aspose.Cells には、ワークシート内の最大範囲を見つけるためのさまざまな方法が含まれています。


{{% /alert %}} 



##  **最大射程距離を取得する**
Aspose.Cells の場合、[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)そして[**カラム**](https://reference.aspose.com/cells/net/aspose.cells/column)オブジェクトが初期化されると、空の行や列にデータがない場合でも、これらの行と列が最大領域までカウントされます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **最大データ範囲の取得**
ほとんどの場合、範囲外の空のセルが書式設定されている場合でも、すべてのデータを含むすべての範囲を取得するだけで済みます。
また、シェイプ、テーブル、ピボットテーブルに関する設定は無視されます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **最大表示範囲の取得**
ワークシートのすべてのデータを HTML、PDF、または画像にエクスポートする場合、データ、スタイル、グラフィックス、テーブル、ピボット テーブルを含むすべての表示オブジェクトを含む領域を取得する必要があります。
次のコードは、最大表示範囲を HTML にレンダリングする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

ここは[ソースエクセルファイル](Book1.xlsx).
