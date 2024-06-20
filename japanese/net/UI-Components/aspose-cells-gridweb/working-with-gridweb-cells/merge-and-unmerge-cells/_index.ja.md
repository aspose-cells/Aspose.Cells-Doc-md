---
title: セルの結合と解除
type: docs
weight: 60
url: /ja/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb でのセルの結合、解除
description: この記事では、GridWeb でセルを結合/解除する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb にはセルを 1 つの大きなセルに結合する便利なユーティリティ機能があります。このトピックでは、プログラムでセルを結合する方法について説明します。

{{% /alert %}} 
## **セルの結合**
ワークシート内の複数のセルを 1 つのセルに結合するために、Cells コレクションの Merge メソッドを呼び出します。Merge メソッドを呼び出す際に、結合するセルの範囲を指定します。

{{% alert color="primary" %}} 

複数のセルを結合し、各セルにデータが含まれている場合、結合後も範囲内の左上のセルの内容のみが保持されます。他のセルのデータは失われません。セルを解除すると、各セルがそのデータを回復します。

{{% /alert %}} 

**4 つのセルが 1 つに結合されました** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **セルの結合解除**
セルを結合解除するには、Merge メソッドと同じパラメータを取る Cells コレクションの UnMerge メソッドを使用します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
