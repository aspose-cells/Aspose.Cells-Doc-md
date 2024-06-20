---
title: Aspose.Cells.GridWebでコンテキストメニューのアイテムを追加または削除する
type: docs
weight: 130
url: /ja/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, contextmenu, menu
description: この記事では、GridWebにコンテキストメニューアイテムを追加または削除する方法について説明します。
---

{{% alert color="primary" %}} 

ASP.NETマークアップを使用するか、.NETコードを使用してコンテキストメニューアイテムを追加できます。.NETコードを使用してコンテキストメニューアイテムを削除することもできます。

{{% /alert %}} 
## **ASP.NETマークアップを使用してコンテキストメニューアイテムを追加**
次のASP.NETマークアップは、GridWebにコンテキストメニューアイテムを追加します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



上記のASP.NETマークアップでコンテキストメニューアイテムを追加した場合の全体的なASP.NETマークアップを以下に示します。"OnCustomCommand="GridWeb1_CustomCommand""属性に注意してください。これは、コンテキストメニューアイテムがクリックされたときに呼び出されるイベントハンドラの名前です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



上記のASP.NETマークアップを使用してコンテキストメニューアイテムを追加した後のコンテキストメニューアイテムの外観です。

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

コンテキストメニューアイテムがクリックされたときに実行されるイベントハンドラコードです。コードはまずコマンド名をチェックし、マッチする場合は、アクティブなGridWebワークシートのセルA1にテキストを追加し、テキストが見えるように最初の列の幅を40ユニットに設定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


上記のASP.NETマークアップを使用してコンテキストメニューアイテムを追加した後のGridWebの外観です。

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **コードを使用してAspose.Cells.GridWebにコンテキストメニューアイテムを追加する**
このコードは、コードを使用してGridWeb内にコンテキストメニューアイテムを追加する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **コードを使用してAspose.Cells.GridWebからコンテキストメニューアイテムを削除する**
このコードは、CustomCommandButtons.Remove()およびCustomCommandButtons.RemoveAt()メソッドを使用してコンテキストメニューアイテムを削除する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
