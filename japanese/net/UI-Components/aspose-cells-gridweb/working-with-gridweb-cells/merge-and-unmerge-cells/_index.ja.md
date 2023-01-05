---
title: マージとアンマージ Cells
type: docs
weight: 60
url: /ja/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb には、セルを 1 つの大きなセルに結合できる便利なユーティリティ機能があります。このトピックでは、セルをプログラムで結合する方法について説明します。

{{% /alert %}} 
## **合併 Cells**
Cells コレクションの Merge メソッドを呼び出して、ワークシート内の複数のセルを 1 つのセルに結合します。 Merge メソッドを呼び出すときに結合するセルの範囲を指定します。

{{% alert color="primary" %}} 

複数のセルを結合し、各セルにデータが含まれている場合、結合後に範囲内の左上のセルの内容のみが保持されます。他のセルのデータは失われません。セルの結合を解除すると、各セルのデータが復元されます。

{{% /alert %}} 

**4 つのセルが 1 つに結合されました** 

![todo:画像_代替_文章](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **アンマージ Cells**
セルの結合を解除するには、Cells コレクションの UnMerge メソッドを使用します。このメソッドは、Merge メソッドと同じパラメーターを取り、セルの結合解除を実行します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
