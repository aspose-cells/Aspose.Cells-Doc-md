---
title: 启用不同的 GridWeb 模式
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb，EditMode，SessionMode
description: 本文介绍如何在 GridWeb 中使用 EditMode 和 SessionMode。
---

{{% alert color="primary" %}} 

本文描述了 Aspose.Cells.GridWeb 的不同模式。这些模式在逻辑上由于其不同的特点和行为而有所区别。我们已经确定了几种模式：

- 编辑模式
- 查看模式
- 会话模式
- 无会话模式

所有这些模式都有其自己的特点。开发人员可以根据自己的需求在任何模式下使用Aspose.Cells.GridWeb。我们将逐个查看每种模式。

{{% /alert %}} 
## **编辑模式**
默认情况下，Aspose.Cells.GridWeb控件处于编辑模式。在编辑模式下，您可以使用Aspose.Cells.GridWeb控件提供的所有功能完全编辑或修改网格内容。这些功能包括：

- 将网格内容保存为Microsoft Excel文件。
- 将数据提交到服务器。
- 计算公式。
- 撤消或放弃之前的操作。
- 管理行和列。
- 剪切、复制或粘贴数据。
- 格式化单元格等。

**编辑模式下的GridWeb控件** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

开发人员还可以通过将GridWeb控件的EditMode属性设置为true来以编程方式切换到编辑模式。

下面的示例显示如何以编程方式启用编辑模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

每当用户单击 **撤消** 按钮时，它会将 GridWeb 恢复到先前的状态（在最后一次向服务器发出回发之前的状态）。它不会逐个取消先前的操作。

{{% /alert %}} 
## **查看模式**
当 GridWeb 控件处于查看模式时，用户无法编辑或修改网格内容，意味着用户只能查看网格内容。这就是为什么这种模式被称为查看模式。在查看模式下，一些按钮（**提交**、**保存** 和 **撤销**）是隐藏的，右键单击弹出的菜单只包含 **复制** 选项。

**GridWeb控件的查看模式** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

如果开发人员希望他们的用户只能查看数据，那么他们可以通过将 GridWeb 控件的 EditMode 属性设置为 false 在编程上切换到查看模式。

下面的示例显示如何在编程上启用查看模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

即使在查看模式下，用户也可以更改行和列的高度和宽度。

{{% /alert %}} 
## **会话模式**
Aspose.Cells.GridWeb 控件在网页用户每个请求之间通过 Web 服务器的用户会话中保存工作表数据。这意味着 GridWeb 控件默认始终在会话模式下工作。但是，如果您不希望在会话模式下工作，可以通过将 GridWEb 控件的 SessionMode 属性设置为 SessionMode.Session 来启用。

下面的示例显示如何在编程上启用会话模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **无会话模式**
我们已经讨论过，会话模式方法通过使用用户会话来加载和存储工作表数据来提供最佳性能。但是，这样做会消耗服务器内存。因此，如果有大量并发用户，则可能会出现内存问题。为了节省服务器内存并支持大量并发用户，请考虑无会话模式。

可以通过将 GridWeb 控件的 SessionMode 属性设置为 SessionMode.ViewState 来启用无会话模式。

下面的示例显示如何在编程上启用无会话模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

重要提示：当 GridWeb 的 SessionMode 属性设置为 SessionMode.ViewState 时，网格会在页面的 ViewState 中存储数据。这意味着呈现的页面会更大，消耗更多的网络流量。

{{% /alert %}} {{% alert color="primary" %}} 

如果要使用 SQL Server 或状态服务器来保存会话，请使用会话模式。GridWeb 控件支持将其数据序列化到 SQL Server 或状态服务器。

请查看以下文章以获取更多帮助。

- [ASP.NET会话状态模式为SQL Server时的GridWeb的工作](/cells/zh/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
