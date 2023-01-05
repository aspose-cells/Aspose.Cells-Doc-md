---
title: GridDesktop での Cells のマージとマージ解除
linktitle: マージとアンマージ Cells
type: docs
weight: 90
url: /ja/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

このトピックでは、ワークシートのセルを結合および結合解除するユーティリティ機能について説明します。この機能は、データの読みやすさを向上させるために、いくつかの行または列にまたがる必要がある場合に役立ちます。

{{% /alert %}} 
## **合併 Cells**
セルを 1 つの大きなセルに結合するには、次の手順に従ってください。

- 任意のアクセス**ワークシート**
- 作成する**Cellsの範囲**合併する
- **マージ**セルの範囲を大きなセルに

使用できます**マージ**方法**ワークシート**セルを結合します。ただし、セルの範囲は次を使用して定義できます。**セル範囲**物体。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **アンマージ Cells**
大きなセルを多くのセルに結合解除するには、次の手順に従ってください。

- 任意のアクセス**ワークシート**
- 結合を解除する必要がある結合セルにアクセスする
- **マージ解除**結合されたセルの位置を使用して、大きなセルを多くのセルに

使用できます**マージ解除**方法**ワークシート**その場所を使用してセルの結合を解除します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

セルを 1 つのセルに結合すると、左上のセル (セルの範囲内) の書式設定が結合されたセルに適用されますが、セルが結合解除されると、結合されていないすべてのセルの書式設定が維持されます。

{{% /alert %}}
