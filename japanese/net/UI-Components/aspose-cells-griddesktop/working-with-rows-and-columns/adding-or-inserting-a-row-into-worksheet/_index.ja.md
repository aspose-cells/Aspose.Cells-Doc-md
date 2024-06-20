---
title: ワークシートに行を追加または挿入する
type: docs
weight: 30
url: /ja/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: この記事では、GridDesktopで行を追加または挿入する方法について紹介します。
---

{{% alert color="primary" %}} 

以前のトピックの1つと同様に、このトピックでは、Aspose.Cells.GridDesktopのAPIを使用して、ワークシートに行を動的に追加および挿入する機能について説明します。追加と挿入の基本的な違いは、追加では行がワークシートの行コレクションの最後に追加されるのに対して、挿入では任意の指定位置に行を追加できることです。

{{% /alert %}} 
## **ワークシートに行を追加**
ワークシートに新しい行を追加するには、以下の手順に従ってください：

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **ワークシート**に**行**を追加します



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **ワークシートに行を挿入**
指定された位置に新しい行をワークシートに挿入するには、以下の手順に従ってください：

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **ワークシート**に**行**を**挿入**します（挿入する位置の行のインデックスを指定することで）

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
