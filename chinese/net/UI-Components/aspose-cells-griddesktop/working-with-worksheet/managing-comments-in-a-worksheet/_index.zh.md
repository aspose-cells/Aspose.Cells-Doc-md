---
title: 管理工作表中的评论
type: docs
weight: 110
url: /zh/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

在 MS Excel 中，您必须熟悉允许用户向单元格添加注释的注释功能。当需要在用户将要向单元格中输入值时向其提供一些信息时，此功能非常有用。每当用户将鼠标光标放在注释单元格上时，就会出现一个小的弹出消息，向用户提供一些信息。使用 Aspose.Cells.GridDesktop，开发人员可以在单元格上创建注释。在本主题中，我们将详细解释此功能的用法。

{{% /alert %}} 
## **添加评论**
要使用 Aspose.Cells.GridDesktop 向单元格添加评论，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**评论**通过指定要在其中添加注释的单元格（使用其名称或行号和列号）到工作表。

下面的代码将注释添加到**b2**和**b4**工作表的单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**注释**收集在**工作表**对象提供重载**添加**方法。开发人员可以使用任何重载版本**添加**方法根据自己的具体需要。
## **访问评论**
要访问和修改工作表中的现有评论，开发人员可以从**注释**的集合**工作表**通过指定插入注释的单元格（使用单元格名称或其在行号和列号方面的位置）。访问评论后，开发人员可以在运行时修改其文本。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **删除评论**
要删除现有评论，开发人员只需访问所需的工作表，然后**消除**来自的评论**注释**的集合**工作表**通过指定包含注释的单元格（使用其名称或行号和列号）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
