---
title: 线程评论
type: docs
weight: 140
url: /zh/java/threaded-comments/
---
# **线程评论**
MS Excel 365 提供了添加线程注释的功能。这些评论作为对话，可用于讨论。评论现在带有一个回复框，允许进行线程对话。旧注释在 Excel 365 中称为注释。下面的屏幕截图显示了在 Excel 中打开时线程注释的显示方式。

![待办事项：图像_替代_文本](threaded-comments_1.jpg)

线程注释在旧版本的 Excel 中显示如下。以下图像是在 Excel 2016 中打开示例文件拍摄的。

![待办事项：图像_替代_文本](threaded-comments_2.jpg)



![待办事项：图像_替代_文本](threaded-comments_3.jpg)



Aspose.Cells 还提供了管理线程评论的功能。
## **添加主题评论**
### **使用 Excel 添加线程评论**
若要在 Excel 365 中添加线程注释，请按照以下步骤操作。

- 方法一
 点击**审查**标签
 点击**新评论**按钮
 这将打开一个对话框以在活动单元格中输入评论。
  - ![待办事项：图像_替代_文本](threaded-comments_4.jpg)
- 方法二
 右键单击要插入评论的单元格。
 点击**新评论**选项。
 这将打开一个对话框以在活动单元格中输入评论。
  - ![待办事项：图像_替代_文本](threaded-comments_5)
### **使用 Aspose.Cells 添加主题评论**
Aspose.Cells提供[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) 方法添加线程评论。[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) 方法接受以下三个参数。

- Cell 名称：将插入注释的单元格的名称。
- 评论文本：评论的文本。
- [线程评论作者](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor)评论作者

下面的代码示例演示了使用[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)方法将线程注释添加到单元格 A1。请参阅[输出Excel文件](AddThreadedComments_out.xlsx)生成的代码供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **阅读线程评论**
### **使用 Excel 阅读线程评论**
要在 Excel 中阅读线程注释，只需将鼠标悬停在包含注释的单元格上即可查看注释。评论视图将如下图所示。

![待办事项：图像_替代_文本](threaded-comments_1.jpg)
### **使用 Aspose.Cells 阅读线程评论**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法来检索指定列的线程注释。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法接受列名作为参数并返回[线程评论集合](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection).你可以遍历[线程评论集合](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)查看评论。

以下示例演示了通过加载[示例 Excel 文件](ThreadedCommentsSample.xlsx).请查看代码生成的控制台输出以供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **控制台输出**
评论：测试线程评论

作者：Aspose 测试
### **读取线程评论的创建时间**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法来检索指定列的线程注释。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法接受列名作为参数并返回[线程评论集合](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection).你可以遍历[线程评论集合](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)并使用[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)财产。

下面的例子演示了通过加载[示例 Excel 文件](ThreadedCommentsSample.xlsx).请查看代码生成的控制台输出以供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **控制台输出**
评论：测试线程评论

作者：Aspose 测试

创建时间：2019-05-15T12:46:23
## **编辑线程评论**
### **使用 Excel 编辑线程评论**
要在 Excel 中编辑线程注释，请单击**编辑**评论上的链接，如下图所示。

![待办事项：图像_替代_文本](threaded-comments_7.jpg)
### **使用 Aspose.Cells 编辑线程评论**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法来检索指定列的线程注释。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法接受列名作为参数并返回[线程评论集合](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection).您可以在[线程评论集合](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)并保存工作簿。

以下示例演示了通过加载[示例 Excel 文件](ThreadedCommentsSample.xlsx).请参阅[输出Excel文件](EditThreadedComments.xlsx)由显示更新评论的代码生成以供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **删除线程评论**
### **使用 Excel 删除线程评论**
要在 Excel 中删除线程注释，请右键单击包含注释的单元格，然后单击**删除评论**选项如下图所示。

![待办事项：图像_替代_文本](threaded-comments_8.jpg)
### **使用 Aspose.Cells 删除线程评论**
Aspose.Cells提供[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) 方法删除指定列的注释。[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) 方法接受列名作为参数，删除该列中的注释。

以下示例演示通过加载[示例 Excel 文件](ThreadedCommentsSample.xlsx).请参阅[输出Excel文件](ThreadedCommentsSample_Out.xlsx)生成的代码供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

请注意，通过删除带有 Aspose.Cells 的评论，作者不会自动删除。如果您还需要删除作者，请使用[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) 方法如上例所示。

{{% /alert %}}
