---
title: 启用不同的GridWeb模式
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb、EditMode、SessionMode
description: 本文介绍如何在GridWeb中使用EditMode和SessionMode。
---

{{% alert color="primary" %}} 

本文描述Aspose.Cells.GridWeb的不同模式。这些模式基于它们的不同特点和行为进行逻辑区分。我们已经确定了几种模式:

- 编辑模式
- 查看模式
- 会话模式
- 无会话模式

所有这些模式都有其特点。开发人员可以根据自己的需求在任何模式下使用Aspose.Cells.GridWeb。我们将在下面介绍每种模式。

{{% /alert %}} 
## **编辑模式**
默认情况下，Aspose.Cells.GridWeb控件处于编辑模式。在编辑模式下，您可以完全编辑或修改网格内容，使用Aspose.Cells.GridWeb控件提供的所有功能。这些功能包括:

- 将网格内容保存到Microsoft Excel文件中。
- 将数据提交到服务器。
- 计算公式。
- 撤销或放弃以前的操作。
- 管理行和列。
- 剪切、复制或粘贴数据。
- 设置单元格格式等。

**编辑模式中的GridWeb控件** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

开发人员还可以通过将GridWeb控件的EditMode属性设置为true来以编程方式切换到编辑模式。

下面的示例显示如何以编程方式启用编辑模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

每当用户单击**撤销**按钮时，它会将 GridWeb 恢复到其之前的状态（即上次回传到服务器之前的状态）。它不会逐个取消先前的操作。

{{% /alert %}} 
## **查看模式**
当 GridWeb 控件处于查看模式时，用户无法编辑或修改网格内容，这意味着用户只能查看网格内容。这就是为什么将此模式称为查看模式。在查看模式下，一些按钮（**提交**、**保存** 和 **撤销**）将被隐藏，右键单击时显示菜单中仅包含 **复制** 选项。

**GridWeb 控件处于查看模式** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

如果开发人员希望他们的用户只能查看数据，则可以通过将 GridWeb 控件的 EditMode 属性设置为 false 来在程序中切换到查看模式。

下面的示例显示了如何通过程序启用查看模式



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

即使在查看模式下，用户也可以更改行和列的高度和宽度。

{{% /alert %}} 
## **会话模式**
Aspose.Cells.GridWeb 控件在 web 服务器的用户会话中保存工作表数据，即在每个 web 用户请求之间。这意味着，GridWeb 控件默认始终以会话模式运行。但是，如果不在会话模式下工作，则通过将 GridWeb 控件的 SessionMode 属性设置为 SessionMode.Session 来切换到会话模式。

下面的示例显示了如何通过程序启用会话模式



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **无会话模式**
我们已经讨论过，会话模式方法通过使用用户会话加载和存储工作表数据提供最佳性能。但是，它确实会占用服务器内存。因此，如果有大量并发用户，则可能会出现内存问题。为了节省服务器内存并支持大量并发用户，请考虑 Sessionless 模式。

可以通过将 GridWeb 控件的 SessionMode 属性设置为 SessionMode.ViewState 来启用无会话模式。

下面的示例显示了如何通过程序启用无会话模式



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

重要提示：当 GridWeb 的 SessionMode 属性设置为 SessionMode.ViewState 时，网格会将数据存储在页面的 ViewState 中。这意味着渲染的页面会更大，消耗更多网络流量。

{{% /alert %}} {{% alert color="primary" %}} 

如果要使用 SQL Server 或 StateServer 来保存会话，请使用会话模式。GridWeb 控件支持将其数据序列化到 SQL Server 或 StateServer。

请查看以下文章以获取更多帮助。

- [ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作原理](/cells/zh/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
