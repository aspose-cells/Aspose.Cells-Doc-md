---
title: ワークシート内の最大範囲を取得する
type: docs
weight: 360
url: /ja/net/get-max-range-in-a-worksheet/
description: この記事では、Aspose.Cells for .Netライブラリを使用してExcelファイルの最大範囲、最大データ範囲、最大表示範囲を取得する方法について説明します。
---

{{% alert color="primary" %}} 

ワークシートからデータを読み取る場合、最大範囲を知る必要があります。

ワークシートからすべてのデータをコピーする場合、最大範囲を知る必要があります。

指定された範囲をhtmlやpdfにエクスポートする場合、最大範囲を知る必要があります。

Aspose.Cells for .Netには、ワークシート内の最大範囲を見つけるための異なる方法が含まれています。 


{{% /alert %}} 



## **最大範囲を取得する**
Aspose.Cellsで、[**row**](https://reference.aspose.com/cells/net/aspose.cells/row)と[**column**](https://reference.aspose.com/cells/net/aspose.cells/column)オブジェクトが初期化されている場合、これらの行と列は、空の行や列にデータがなくても最大範囲としてカウントされます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **最大データ範囲を取得する**
ほとんどの場合、空のセルが範囲外にある場合でも、すべてのデータを含むすべての範囲を取得する必要があります。
そして、図形、テーブル、ピボットテーブルに関する設定は無視されます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **最大表示範囲を取得する**
ワークシートからすべてのデータをHTML、PDF、または画像にエクスポートする場合、データ、スタイル、グラフィック、表、およびピボットテーブルを含むすべての可視オブジェクトを含むエリアを取得する必要があります。
次のコードは、最大表示範囲をhtmlにレンダリングする方法を示しています：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

以下は[ソースエクセルファイル](Book1.xlsx)です。
