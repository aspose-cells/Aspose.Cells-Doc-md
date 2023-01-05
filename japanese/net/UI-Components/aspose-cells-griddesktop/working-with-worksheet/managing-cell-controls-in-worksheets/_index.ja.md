---
title: ワークシートでの Cell コントロールの管理
type: docs
weight: 130
url: /ja/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop の API を使用したセル コントロールの管理に関するいくつかの重要な概念について説明します。開発者がワークシートからセル コントロールにアクセス、変更、および削除する方法を説明します。それを見てみましょう。

{{% /alert %}} 
## **Cell コントロールへのアクセス**
ワークシート内の既存のセル コントロールにアクセスして変更するために、開発者は**コントロール**のコレクション**ワークシート**セル コントロールが表示されているセルを (セル名または行番号と列番号の観点からセルの位置を使用して) 指定します。セル コントロールにアクセスすると、開発者は実行時にそのプロパティを変更できます。たとえば、以下の例では、既存の**チェックボックス**からの細胞制御**ワークシート**その Checked プロパティを変更しました。

**重要：** **コントロール**コレクションには、すべてのタイプのセル コントロールが次の形式で含まれています。**セルコントロール**オブジェクト。したがって、特定の種類のセル コントロールにアクセスする必要がある場合は、**チェックボックス**次に、型キャストする必要があります**セルコントロール**異議を唱える**チェックボックス**クラス。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Cell コントロールの削除**
既存のセル コントロールを削除するには、開発者は目的のワークシートにアクセスしてから、**削除する**からのセルコントロール**コントロール**のコレクション**ワークシート**セル コントロールを含むセルを (その名前または行と列の番号を使用して) 指定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
