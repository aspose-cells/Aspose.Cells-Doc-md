---
title: 管理 GridDesktop 上下文菜单
type: docs
weight: 40
url: /zh/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop, 上下文, 上下文菜单
description: 本文介绍了如何自定义 GridDesktop 中的上下文菜单。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop 拥有一个包含所有常用命令的上下文菜单。该控件允许您隐藏/显示菜单项。此外，还可以通过事件处理程序向菜单添加新的菜单项。

{{% /alert %}} 
## **介绍**
ContextMenuManager 类用于管理上下文菜单项。GridDesktop.ContextMenuManager 属性获取 ContextMenuManager 对象的实例。例如，ContextMenuManager.MenuItemAvailable_Copy 属性获取或设置一个值，表示上下文菜单项“拷贝”是否可用。类似地，我们还有不同上下文菜单项的相应属性。

**重要提示：** 默认情况下，所有上下文菜单项都在列表中可见。
## **管理上下文菜单**
### **隐藏上下文菜单项**
要执行此任务，首先查看 GridDesktop 的默认上下文菜单。

**GridDesktop 的默认菜单** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

现在，使用下面的代码隐藏一些菜单项：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



执行上述代码后，某些菜单项对用户将不可见：

**部分菜单项被隐藏** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **添加新菜单项**
使用以下代码片段向列表中添加新的上下文菜单项。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


我们还为新命令/选项指定了一个事件处理程序。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



执行上述代码后，上下文菜单中将出现一个新的菜单项。单击单元格时还将出现一条消息。

**列表中添加了一个新菜单项** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
