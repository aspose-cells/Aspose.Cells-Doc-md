---
title: ワークシートでセルコントロールの管理
type: docs
weight: 130
url: /ja/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop、cell control、control、controls
description: この記事では、GridDesktopでのセルコントロールの操作方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktopのAPIを使用してセルコントロールを管理する重要な概念について説明します。開発者がワークシートからセルコントロールにアクセスし、そのプロパティを実行時に変更および削除する方法について説明します。

{{% /alert %}} 
## **セルコントロールへのアクセス**
ワークシート内の既存のセルコントロールにアクセスして変更するには、開発者は**Controls**コレクション内の**Worksheet**から特定のセルコントロールにアクセスできます（セルの名前または行および列番号を使用して）。セルコントロールにアクセスしたら、開発者は実行時にそのプロパティを変更することができます。たとえば、以下の例では、ワークシートから既存の**CheckBox**セルコントロールにアクセスし、そのCheckedプロパティを変更しました。

**重要:** **Controls**コレクションには、**CellControl**オブジェクトとしてすべてのタイプのセルコントロールが含まれています。したがって、特定のタイプのセルコントロールにアクセスする必要がある場合は、**CellControl**オブジェクトを**CheckBox**クラスに変換する必要があります。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **セルコントロールの削除**
既存のセルコントロールを削除するには、開発者は単に希望のワークシートにアクセスし、**Controls**コレクションからセルコントロールを指定して削除します（その名前または行＆列番号を使用して）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
