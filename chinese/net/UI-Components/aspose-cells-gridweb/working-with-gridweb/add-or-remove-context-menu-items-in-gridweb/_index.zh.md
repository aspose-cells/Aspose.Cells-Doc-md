---
title: 在 GridWeb 中添加或移除上下文菜单项
type: docs
weight: 130
url: /zh/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb,上下文菜单,菜单
description: 本文介绍如何在 GridWeb 中添加或删除上下文菜单项。
---

{{% alert color="primary" %}} 

您可以使用 ASP.NET 标记或使用 .NET 代码添加上下文菜单项。您还可以使用 .NET 代码来删除上下文菜单项。请使用GridWeb.CustomCommandButtons.Add() 和 GridWeb.CustomCommandButtons.Remove() 或 RemoveAt() 方法进行这些操作。

{{% /alert %}} 
## **使用 ASP.NET 标记添加上下文菜单项**
以下 ASP.NET 标记在 GridWeb 中添加上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



以下是完整的 ASP.NET 标记，创建了一个带有上述上下文菜单项的 GridWeb。请注意OnCustomCommand="GridWeb1_CustomCommand" 属性。这是单击上下文菜单项时调用的事件处理程序名称。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



使用上述 ASP.NET 标记添加上下文菜单项后的效果。

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

当使用上述的 ASP.NET 标记添加上下文菜单项时，执行的事件处理代码。该代码首先检查命令名称，如果匹配我们的命令，它会将文本添加到活动 GridWeb 工作表的A1单元格，并将第一列宽度设置为40个单位以使文本可见。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


单击上下文菜单项时 GridWeb 的外观。

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **使用代码在 Aspose.Cells.GridWeb 中添加上下文菜单项**
此代码展示了如何使用代码在 GridWeb 内部添加上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **使用代码在 Aspose.Cells.GridWeb 中移除上下文菜单项**
此代码展示了如何使用 CustomCommandButtons.Remove() 和 CustomCommandButtons.RemoveAt() 方法移除上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
