---
title: 启用不同的 GridWeb 模式
type: docs
weight: 60
url: /zh/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

本文介绍 Aspose.Cells.GridWeb 的不同模式。这些模式因其不同的特征和行为而在逻辑上有所区别。我们已经确定了几种类型的模式：

- 编辑模式
- 查看模式
- 会话模式
- 无会话模式

所有这些模式都有自己的特点。开发人员可以根据自己的需要以任何模式使用 Aspose.Cells.GridWeb。我们将在下面查看每种模式。

{{% /alert %}} 
## **编辑模式**
默认情况下，Aspose.Cells.GridWeb 控件处于编辑模式。在编辑模式下，您可以使用 Aspose.Cells.GridWeb 控件提供的所有功能完全编辑或修改网格内容。这些功能包括：

- 将网格内容保存到 Microsoft Excel 文件。
- 向服务器提交数据。
- 计算公式。
- 撤消或放弃以前的操作。
- 管理行和列。
- 剪切、复制或粘贴数据。
- 格式化单元格等

**编辑模式下的 GridWeb 控件** 

![待办事项：图片_替代_文本](enable-different-gridweb-modes_1.png)

开发人员还可以通过将 GridWeb 控件的 EditMode 属性设置为 true，以编程方式切换到编辑模式。

下面的示例显示了如何以编程方式启用编辑模式。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

每当用户点击**撤消**按钮，它将 GridWeb 带到它以前的状态（最后一次回发到服务器之前的状态）。它不会一一取消先前的操作。

{{% /alert %}} 
## **查看模式**
当 GridWeb 控件处于 View 模式时，用户不能编辑或修改网格内容，这意味着用户只能查看网格内容。这就是为什么这种模式被称为查看模式。在查看模式下，一些按钮（**提交**, **节省**和**撤消** ) 被隐藏，右键单击时出现的菜单仅包含**复制**选项。

**视图模式下的 GridWeb 控件** 

![待办事项：图片_替代_文本](enable-different-gridweb-modes_1.png)

如果开发人员希望他们的用户只查看数据，那么他们可以通过将 GridWeb 控件的 EditMode 属性设置为 false 以编程方式切换到查看模式。

下面的示例显示了如何以编程方式启用视图模式



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

即使在查看模式下，用户也可以更改行和列的高度和宽度。

{{% /alert %}} 
## **会话模式**
Aspose.Cells.GridWeb 控件在网络用户的每次请求之间在网络服务器的用户会话中保存工作表数据。这意味着 GridWeb 控件默认总是工作在 Session 模式。但是，如果您不在会话模式下工作，请通过将 GridWEb 控件#s SessionMode 属性设置为 SessionMode.Session 来打开它。

下面的示例显示了如何以编程方式启用会话模式



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **无会话模式**
我们已经讨论过会话模式方法通过使用用户会话来加载和存储工作表数据来提供最佳性能。但是，它确实会消耗服务器内存。因此，如果有大量并发用户，则可能会出现内存问题。为了节省服务器内存并支持大量并发用户，可以考虑 Sessionless 模式。

可以通过将 GridWeb 控件的 SessionMode 属性设置为 SessionMode.ViewState 来打开无会话模式。

下面的示例显示了如何以编程方式启用无会话模式



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

重要提示：当 GridWeb 的 SessionMode 属性设置为 SessionMode.ViewState 时，网格将数据存储在页面的 ViewState 中。这意味着呈现的页面更大，消耗更多的网络流量。

{{% /alert %}} {{% alert color="primary" %}} 

如果要使用 SQL Server 或 StateServer 来保持会话，请使用 Session 模式。 GridWeb 控件支持将其数据序列化到 SQL Server 或 StateServer。

请查看以下文章以获得更多帮助。

- [ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作](/cells/zh/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
