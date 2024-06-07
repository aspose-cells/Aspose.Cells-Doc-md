---
title: 在工作表中管理评论
type: docs
weight: 110
url: /zh/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb，评论
description: 本文介绍了在GridWeb中处理评论的方法。
---

{{% alert color="primary" %}} 

本主题讨论了如何向工作表添加、访问和移除批注。批注可用于为将使用工作表的用户添加注释或有用信息。开发人员可以灵活地向工作表的任何单元格添加批注。

{{% /alert %}} 
## **处理批注**
### **添加批注**
要向工作表添加批注，请按照以下步骤进行：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单。
1. 访问要添加批注的工作表。
1. 向单元格添加注释。
1. 为新的批注设置备注。

**已向工作表添加批注** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **访问评论**
要访问批注：

1. 访问包含批注的单元格。
1. 获取单元格的引用。
1. 将引用传递给Comment集合以访问批注。
1. 现在可以修改批注的属性。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **删除评论**
要移除批注：

1. 如上所述访问单元格。
1. 使用Comment集合的RemoveAt方法删除评论。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
