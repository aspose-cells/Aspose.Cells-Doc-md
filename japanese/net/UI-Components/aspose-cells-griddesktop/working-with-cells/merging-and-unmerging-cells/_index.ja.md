---
title: GridDesktopでのセルの結合と解除
linktitle: セルの結合と解除
type: docs
weight: 90
url: /ja/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop、結合、解除
description: この記事ではGridDesktopでのセルの結合と解除について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、ワークシートのセルを結合および解除する便利な機能について説明します。この機能は、データの可読性を向上させるために一部の行または列を広げる必要がある場合に役立ちます。

{{% /alert %}} 
## **セルの結合**
次の手順に従ってセルを1つの大きなセルに結合します：

- 任意の **Worksheet** にアクセスします
- 結合される**セル範囲**を作成します
- **セル範囲**を1つの大きなセルに**結合**します

**ワークシート**の**Merge**メソッドを使用してセルを結合できます。ただし、**CellRange**オブジェクトを使用してセル範囲を定義できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **セルの解除**
次の手順に従って大きなセルを複数のセルに解除します：

- 任意の **Worksheet** にアクセスします
- 解除する必要がある結合されたセルにアクセスします
- 結合されたセルの位置を使用して、大きなセルを複数のセルに**解除**します

**ワークシート**の**Unmerge**メソッドを使用して、セルの位置を使用してセルを解除できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

セルを1つのセルに結合すると、セルの希望の範囲の左上のセルの書式設定が結合されたセルに適用されますが、セルが解除されると、すべての解除されたセルはその書式設定を保持します。

{{% /alert %}}
