---
title: 在工作表中管理批注
type: docs
weight: 110
url: /zh/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop，批注，批注
description: 这篇文章介绍了如何在GridDesktop中处理批注。
---

{{% alert color="primary" %}} 

在MS Excel中，您可能熟悉允许用户向单元格添加批注的功能。当用户在单元格中输入数值时，如果需要向用户提供一些信息，则此功能很有用。每当用户将鼠标光标放在带有批注的单元格上时，会出现一个小的弹出消息来向用户提供一些信息。使用Aspose.Cells.GridDesktop，开发人员可以在单元格上创建批注。在本主题中，我们将详细解释此功能的用法。

{{% /alert %}} 
## **添加批注**
要使用Aspose.Cells.GridDesktop向单元格添加批注，请按照以下步骤操作：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 通过指定要添加批注的单元格（使用其名称或行列号）向工作表添加**批注**。

以下代码将向工作表的**b2**和**b4**单元格添加批注。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Comments** 集合中的 **Worksheet** 对象提供了一个重载的 **Add** 方法。开发人员可以根据其特定需求使用任何重载版本的 **Add** 方法。
## **访问评论**
要访问和修改工作表中现有的评论，开发人员可以从**Comments**集合中的**Worksheet**访问评论，指定插入评论的单元格（使用单元格名称或其行和列号的位置）。一旦访问评论，开发人员可以在运行时修改其文本。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **删除评论**
要删除现有评论，开发人员可以简单地访问所需的工作表，然后从**Comments**集合的**Worksheet**中的**Remove**评论，指定包含评论的单元格（使用其名称或行和列号）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
