---
title: ワークシートへの行の追加または挿入
type: docs
weight: 30
url: /ja/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

前のトピックの 1 つと同様に、このトピックでは、Aspose.Cells.GridDesktop の API を使用して、実行時にワークシートに行を追加および挿入する機能について説明します。追加と挿入の基本的な違いは、さらに、ワークシートの行コレクションの最後に行が追加されることです。挿入と同様に、行はワークシートの指定された位置に追加できます。

{{% /alert %}} 
## **ワークシートへの行の追加**
ワークシートに新しい行を追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**行**に**ワークシート**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **ワークシートへの行の挿入**
ワークシートの指定した位置に新しい行を挿入するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 入れる**行**の中へ**ワークシート**（挿入する行のインデックスを指定して特定の位置に）

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
