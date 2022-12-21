---
title: GridDesktops コンテキスト メニューの管理
type: docs
weight: 40
url: /ja/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop には、一般的に使用されるすべてのコマンドを含むコンテキスト メニューがあります。コントロールを使用すると、メニュー項目を非表示/表示できます。さらに、イベント ハンドラーを使用して新しいメニュー項目をメニューに追加することもできます。

{{% /alert %}} 
## **序章**
ContextMenuManager クラスは、コンテキスト メニュー項目を管理するために使用されます。 GridDesktop.ContextMenuManager 属性は、ContextMenuManager オブジェクトのインスタンスを取得します。たとえば、ContextMenuManager.MenuItemAvailable_Copy 属性は、コンテキスト メニュー項目 **Copy** が使用可能かどうかを示す値を取得または設定します。同様に、さまざまなコンテキスト メニュー項目に対応するすべての属性があります。

**重要：**デフォルトでは、すべてのコンテキスト メニュー項目がリストに表示されます。
## **コンテキスト メニューの管理**
### **コンテキスト メニュー項目の非表示**
このタスクを実行するには、まず GridDesktop にあるデフォルトのコンテキスト メニューを確認します。

**GridDeskop のデフォルト メニュー** 

![todo:画像_代替_文章](managing-griddesktops-context-menu_1.png)

次に、以下のコードを使用していくつかのメニュー項目を非表示にします。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



上記のコードを実行すると、一部のメニュー項目がユーザーに表示されなくなります。

**一部のメニュー項目が非表示になっています** 

![todo:画像_代替_文章](managing-griddesktops-context-menu_2.png)
### **新しいメニュー項目の追加**
次のコード スニペットを使用して、新しいコンテキスト メニュー項目をリストに追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


また、新しいコマンド/オプションのイベント ハンドラーも指定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



上記のコードを実行すると、コンテキスト メニューに新しいメニュー項目が表示されます。セルをクリックするとメッセージも表示されます。

**リストに新しいメニュー項目が追加されました** 

![todo:画像_代替_文章](managing-griddesktops-context-menu_3.png)
