---
title: ワークシートに保護を追加
type: docs
weight: 130
url: /ja/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop、プロテクト
description: 本記事では、GridDesktopのワークシート内のセルを保護する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells for GridDesktopを使用すると、ワークシートのセルを保護できます。 まず、ワークシートを保護し、次にワークシート内の特定のセルを保護できます。 ワークシートを保護するには、**Worksheet.Protected**プロパティをtrueに設定し、その後に**Worksheet.SetProtected()**メソッドを使用してセルの範囲を保護します。

{{% /alert %}} 
## **Aspose.Cells.GridDesktopを使用してセルを保護**
以下のサンプルコードでは、GridDesktopのアクティブなワークシートの範囲**A1:B1**のすべてのセルを保護しています。 この範囲のセルをダブルクリックすると、編集ができなくなります。 これにより、これらのセルは読み取り専用になります。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
