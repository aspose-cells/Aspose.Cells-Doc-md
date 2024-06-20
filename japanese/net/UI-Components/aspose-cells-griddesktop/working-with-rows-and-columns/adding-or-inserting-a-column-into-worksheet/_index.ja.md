---
title: ワークシートへの列の追加または挿入
type: docs
weight: 10
url: /ja/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,insert,add,column,insert column,insert row
description: この記事では、GridDesktopで列を挿入または追加する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktopのAPIを使用して、ワークシートに列を動的に追加および挿入する基本的な機能について説明します。追加と挿入の基本的な違いは、追加では列がワークシートの列コレクションの最後に追加されるのに対して、挿入では任意の指定位置に列を追加できることです。

{{% /alert %}} 
## **ワークシートへの列の追加**
ワークシートに新しい列を追加するには、以下の手順に従ってください：

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **ワークシート**に**列**を追加します



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **ワークシートに列を挿入**
指定された位置に新しい列をワークシートに挿入するには、以下の手順に従ってください：

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **ワークシート**に**列**を**挿入**します（挿入する位置の列のインデックスを指定することで）

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
