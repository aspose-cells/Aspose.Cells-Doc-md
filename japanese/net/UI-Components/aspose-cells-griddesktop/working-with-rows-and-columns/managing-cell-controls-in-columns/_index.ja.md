---
title: 列での Cell コントロールの管理
type: docs
weight: 100
url: /ja/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop API を使用して列内のセル コントロールを管理することに関するいくつかの重要な概念について説明します。開発者がワークシートの列からセル コントロールにアクセス、変更、および削除する方法について説明します。それを見てみましょう。

{{% /alert %}} 
## **Cell コントロールへのアクセス**
開発者は、列内の既存のセル コントロールにアクセスして変更するために、**Aspose.Cells.GridDesktop.Data.GridColumn** .セル コントロールにアクセスすると、開発者は実行時にそのプロパティを変更できます。たとえば、以下の例では、既存の**チェックボックス**特定の細胞制御**Aspose.Cells.GridDesktop.Data.GridColumn**その Checked プロパティを変更しました。

**重要：** CellControl プロパティは、セル コントロールを次の形式で提供します。**セルコントロール**物体。したがって、特定の種類のセル コントロールにアクセスする必要がある場合は、**チェックボックス**次に、型キャストする必要があります**セルコントロール**異議を唱える**チェックボックス**クラス。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Cell コントロールの削除**
既存のセル コントロールを削除するには、開発者は目的のワークシートにアクセスしてから、**削除する**を使用して、特定の列からのセル コントロール**削除セル コントロール**方法**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

の各列**コラム**のコレクション**ワークシート**のインスタンスで表されます**Aspose.Cells.GridDesktop.Data.GridColumn**クラス。

{{% /alert %}}
