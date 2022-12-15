---
title: 管理 GridDesktops 上下文菜单
type: docs
weight: 40
url: /zh/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop 有一个包含所有常用命令的上下文菜单。该控件允许您隐藏/显示菜单项。此外，可以向菜单添加带有事件处理程序的新菜单项。

{{% /alert %}} 
## **介绍**
ContextMenuManager 类用于管理上下文菜单项。 GridDesktop.ContextMenuManager 属性获取 ContextMenuManager 对象的实例。例如，ContextMenuManager.MenuItemAvailable_Copy 属性获取或设置一个值，该值指示上下文菜单项 **Copy** 是否可用。同样，我们拥有不同上下文菜单项的所有相应属性。

**重要的：**默认情况下，所有上下文菜单项都在列表中可见。
## **管理上下文菜单**
### **隐藏上下文菜单项**
要执行此任务，我们首先看一下 GridDesktop 的默认上下文菜单。

**GridDeskop 的默认菜单** 

![待办事项：图像_替代_文本](managing-griddesktops-context-menu_1.png)

现在，使用以下代码隐藏一些菜单项：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



执行上述代码后，一些菜单项将对用户不可见：

**一些菜单项被隐藏** 

![待办事项：图像_替代_文本](managing-griddesktops-context-menu_2.png)
### **添加新菜单项**
使用以下代码片段将新的上下文菜单项添加到列表中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


我们还为新命令/选项指定一个事件处理程序。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



执行上述代码后，可以在上下文菜单中看到一个新的菜单项。单击单元格时也会出现一条消息。

**一个新的菜单项被添加到列表中** 

![待办事项：图像_替代_文本](managing-griddesktops-context-menu_3.png)
