---
title: 在工作表中管理注释
type: docs
weight: 110
url: /zh/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop,评论,评论
description: 本文介绍了如何在GridDesktop中处理评论。
---

{{% alert color="primary" %}} 

在MS Excel中，您必须熟悉评论功能，该功能允许用户向单元格添加评论。在需要向用户提供一些信息以供其在单元格中输入值时，此功能非常有用。每当用户将鼠标指针放在评论单元格上时，都会弹出一个小窗口消息，向用户提供一些信息。使用Aspose.Cells.GridDesktop，开发人员可以在单元格上创建评论。在本主题中，我们将详细解释此功能的用法。

{{% /alert %}} 
## **添加评论**
要使用Aspose.Cells.GridDesktop向单元格添加注释，请按照以下步骤执行：

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 通过指定要添加注释的单元格（使用名称或行和列号）向工作表添加**注释**

下面的代码将向工作表的**b2**和**b4**单元格添加评论。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**工作表**对象中的**Comments**集合提供了重载的**Add**方法。开发人员可以根据其特定需求使用**Add**方法的任何重载版本。
## **访问评论**
要访问和修改工作表中的现有注释，开发人员可以通过指定要访问的工作表的**Comments**集合（使用单元格名称或其行和列号的位置）来访问注释。一旦访问了注释，开发人员可以在运行时修改其文本。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **移除评论**
要删除现有的评论，开发人员可以简单地访问所需的工作表，然后通过指定包含评论的单元格（使用其名称或行和列号）在**工作表**的**Comments**集合中**移除**评论。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
