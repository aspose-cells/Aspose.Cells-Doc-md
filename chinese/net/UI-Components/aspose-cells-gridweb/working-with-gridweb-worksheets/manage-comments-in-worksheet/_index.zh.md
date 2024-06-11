---
title: 管理工作表中的注释
type: docs
weight: 110
url: /zh/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: 本文介绍了如何在GridWeb中处理评论。
---

{{% alert color="primary" %}} 

本主题讨论了如何在工作表中添加、访问和移除评论。评论可用于为将要使用工作表的用户添加注释或有用信息。开发人员可以灵活地向工作表的任何单元格添加评论。

{{% /alert %}} 
## **处理评论**
### **添加评论**
要向工作表添加评论，请按照以下步骤进行：

1. 将Aspose.Cells.GridWeb控件添加到Web表单。
1. 访问要添加评论的工作表。
1. 向单元格添加评论。
1. 为新评论设置注释。

**已向工作表添加了评论** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **访问评论**
要访问评论：

1. 访问包含评论的单元格。
1. 获取单元格的引用。
1. 将引用传递给评论集合以访问评论。
1. 现在可以修改评论的属性。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **移除评论**
要移除评论：

1. 如上所述访问单元格。
1. 使用 Comment 集合的 RemoveAt 方法来移除评论。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
