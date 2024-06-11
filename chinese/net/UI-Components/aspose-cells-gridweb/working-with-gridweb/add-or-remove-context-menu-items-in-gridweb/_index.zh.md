---
title: 在GridWeb中添加或删除上下文菜单项
type: docs
weight: 130
url: /zh/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb,上下文菜单,菜单
description: 本文介绍如何在GridWeb中添加或删除上下文菜单项。
---

{{% alert color="primary" %}} 

您可以使用ASP.NET标记或.NET代码添加上下文菜单项。也可以使用.NET代码删除上下文菜单项。请使用GridWeb.CustomCommandButtons.Add() 和GridWeb.CustomCommandButtons.Remove() 或RemoveAt() 方法进行这些操作。

{{% /alert %}} 
## **使用ASP.NET标记添加上下文菜单项**
以下ASP.NET标记在GridWeb中添加了上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



这里是创建带有上述上下文菜单项的GridWeb的完整ASP.NET标记。请注意OnCustomCommand="GridWeb1_CustomCommand"属性。这是当单击上下文菜单项时将调用的事件处理程序名称。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



这是使用上述ASP.NET标记添加上下文菜单项后的效果。

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

这是当单击上下文菜单项时执行的事件处理程序代码。代码首先检查命令名称，如果符合我们的命令，它会在活动GridWeb工作表的A1单元格中添加文本，并将第一列宽度设置为40个单位，以便使文本可见。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


这是单击上下文菜单项时GridWeb的外观。

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **使用代码在Aspose.Cells.GridWeb中添加上下文菜单项**
此代码显示了如何在GridWeb中使用代码添加上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **使用代码在Aspose.Cells.GridWeb中删除上下文菜单项**
此代码显示了如何使用CustomCommandButtons.Remove()和CustomCommandButtons.RemoveAt()方法移除上下文菜单项。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
