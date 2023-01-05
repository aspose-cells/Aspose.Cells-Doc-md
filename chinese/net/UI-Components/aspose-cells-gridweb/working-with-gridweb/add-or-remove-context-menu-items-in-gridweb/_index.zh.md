---
title: 在 GridWeb 中添加或删除上下文菜单项
type: docs
weight: 130
url: /zh/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

您可以使用 ASP.NET 标记或使用 .NET 代码添加上下文菜单项。您还可以使用 .NET 代码删除上下文菜单项。为此，请使用 GridWeb.CustomCommandButtons.Add() 和 GridWeb.CustomCommandButtons.Remove() 或 RemoveAt() 方法。

{{% /alert %}} 
## **使用 ASP.NET 标记添加上下文菜单项**
以下 ASP.NET 标记在 GridWeb 中添加上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



这是创建具有上述上下文菜单项的 GridWeb 的完整 ASP.NET 标记。请注意 OnCustomCommand="GridWeb1_CustomCommand" 属性。它是单击上下文菜单项时将调用的事件处理程序名称。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



这是使用上述 ASP.NET 标记添加上下文菜单项后的样子。

![待办事项：图片_替代_文本](add-or-remove-context-menu-items-in-gridweb_1.png)

这是单击上下文菜单项时执行的事件处理程序代码。代码首先检查命令名称，如果它与我们的命令匹配，它会在活动 GridWeb 工作表的单元格 A1 中添加一个文本，并将第一列宽度设置为 40 个单位以使文本可见。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


这是单击上下文菜单项时 GridWeb 的外观。

![待办事项：图片_替代_文本](add-or-remove-context-menu-items-in-gridweb_2.png)
## **使用代码在 Aspose.Cells.GridWeb 中添加上下文菜单项**
此代码显示如何使用代码在 GridWeb 中添加上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **使用代码删除 Aspose.Cells.GridWeb 中的上下文菜单项**
此代码显示如何使用 CustomCommandButtons.Remove() 和 CustomCommandButtons.RemoveAt() 方法删除上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
