---
title: 管理工作表中的评论
type: docs
weight: 110
url: /zh/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

本主题讨论在工作表中添加、访问和删除注释。注释对于为将使用工作表的用户添加注释或有用信息很有用。开发人员可以灵活地向工作表的任何单元格添加注释。

{{% /alert %}} 
## **使用评论**
### **添加评论**
要向工作表添加评论，请按照以下步骤操作：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要添加评论的工作表。
1. 向单元格添加注释。
1. 为新评论设置注释。

**评论已添加到工作表** 

![待办事项：图像_替代_文本](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **访问评论**
要访问评论：

1. 访问包含评论的单元格。
1. 获取单元格的引用。
1. 将引用传递给 Comment 集合以访问评论。
1. 现在可以修改评论的属性。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **删除评论**
要删除评论：

1. 如上所述访问单元格。
1. 使用 Comment 集合的 RemoveAt 方法删除评论。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
