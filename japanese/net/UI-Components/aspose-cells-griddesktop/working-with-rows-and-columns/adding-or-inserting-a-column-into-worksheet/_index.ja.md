---
title: ワークシートへの列の追加または挿入
type: docs
weight: 10
url: /ja/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop の API を使用して、実行時にワークシートに列を追加および挿入する基本機能について説明します。追加と挿入の基本的な違いは、さらに、ワークシートの列コレクションの最後に列が追加されるのに対し、挿入と同様に、列はワークシートの指定された位置に追加できることです。

{{% /alert %}} 
## **ワークシートへの列の追加**
ワークシートに新しい列を追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**桁**に**ワークシート**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **ワークシートへの列の挿入**
ワークシートの指定した位置に新しい列を挿入するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 入れる**桁**の中へ**ワークシート** （挿入する列のインデックスを指定して特定の位置に）

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
