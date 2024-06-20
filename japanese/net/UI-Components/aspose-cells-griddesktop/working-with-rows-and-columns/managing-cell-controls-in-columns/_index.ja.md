---
title: 列のセルコントロールの管理
type: docs
weight: 100
url: /ja/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop,コントロール,制御
description: この記事では、GridDesktopで列にコントロールを設定する方法について紹介します
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop APIを使用して列のセルコントロールを管理する際の重要な概念について説明します。開発者がワークシートの列からセルコントロールにアクセスし、変更、削除する方法について説明します。ぜひご覧ください。

{{% /alert %}} 
## **セルコントロールへのアクセス**
列内の既存のセルコントロールにアクセスして変更するには、開発者は**Aspose.Cells.GridDesktop.Data.GridColumn**の**CellControl**プロパティを使用できます。一度セルコントロールにアクセスすると、開発者はそのプロパティを実行時に変更できます。たとえば、以下の例では、特定の**Aspose.Cells.GridDesktop.Data.GridColumn**から既存の**CheckBox**セルコントロールにアクセスし、そのCheckedプロパティを変更しました。

**重要:** CellControlプロパティは**CellControl**オブジェクトとしてセルコントロールを提供します。そのため、特定のタイプのセルコントロール（例えば**CheckBox**）にアクセスする必要がある場合は、**CellControl**オブジェクトを**CheckBox**クラスにキャストする必要があります。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **セルコントロールの削除**
既存のセルコントロールを削除するには、開発者は単純に目的のワークシートにアクセスし、**Aspose.Cells.GridDesktop.Data.GridColumn**の**RemoveCellControl**メソッドを使用して特定の列からセルコントロールを削除できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

ワークシートの**Columns**コレクション内の各列は、**Aspose.Cells.GridDesktop.Data.GridColumn**クラスのインスタンスによって表されます。

{{% /alert %}}
