---
title: GridDesktopのコンテキストメニューの管理
type: docs
weight: 40
url: /ja/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop、context、context menu
description: この記事では、GridDesktopのコンテキストメニューのカスタマイズ方法について紹介しています。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktopには、一般に使用されるすべてのコマンドを持つコンテキストメニューがあります。このコントロールでは、メニューアイテムを非表示または表示することができます。さらに、イベントハンドラを持つ新しいメニューアイテムを追加することも可能です。

{{% /alert %}} 
## **紹介**
ContextMenuManagerクラスは、コンテキストメニューアイテムを管理するために使用されます。GridDesktop.ContextMenuManager属性は、ContextMenuManagerオブジェクトのインスタンスを取得します。たとえば、ContextMenuManager.MenuItemAvailable_Copy属性は、コンテキストメニューアイテムの 'Copy' が利用可能かどうかを取得または設定します。同様に、異なるコンテキストメニューアイテムに対応する属性があります。

**重要：**デフォルトでは、すべてのコンテキストメニューアイテムがリストに表示されます。
## **コンテキストメニューの管理**
### **コンテキストメニューアイテムの非表示**
このタスクを実行するには、最初にGridDesktopのデフォルトのコンテキストメニューを確認します。

GridDeskopのデフォルトメニュー 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

以下のコードを使用して、いくつかのメニューアイテムを非表示にします:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



上記のコードを実行した後、一部のメニューアイテムがユーザーには表示されなくなります:

一部のメニューアイテムが非表示になります 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **新しいメニューアイテムの追加**
以下のコードスニペットを使用してリストに新しいコンテキストメニューアイテムを追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


新しいコマンド/オプションのイベントハンドラも指定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



上記のコードを実行した後、コンテキストメニューに新しいメニューアイテムが表示されます。セルをクリックするとメッセージも表示されます。

リストに新しいメニューアイテムが追加されます 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
