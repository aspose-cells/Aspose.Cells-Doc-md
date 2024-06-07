---
title: 线程化评论
type: docs
weight: 140
url: /zh/java/threaded-comments/
---

# **线程化评论**
MS Excel 365提供了添加线程化评论的功能。这些评论可以作为对话使用，可用于讨论。现在的评论带有一个回复框，用于线程化对话。Excel 365中的老评论称为“备注”。下图显示了打开Excel时线程化评论的显示方式。

![todo:image_alt_text](threaded-comments_1.jpg)

较旧版本的Excel中线程化评论显示的方式如下。以下图像是通过在Excel 2016中打开示例文件获取的。

![todo:image_alt_text](threaded-comments_2.jpg)



![todo:image_alt_text](threaded-comments_3.jpg)



Aspose.Cells还提供了管理线程化评论的功能。 
## **添加线程化评论**
### **使用Excel添加线程化注释**
要在Excel 365中添加线程化注释，请按照以下步骤进行。

- 方法1
  - 点击**审阅**选项卡
  - 点击**新建批注**按钮
  - 这将打开对话框，可在活动单元格中输入评论。
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- 方法2
  - 在要插入评论的单元格上右键单击。
  - 点击**新建批注**选项。
  - 这将打开对话框，可在活动单元格中输入评论。
  - ![todo:image_alt_text](threaded-comments_5)
### **使用Aspose.Cells添加线程化评论**
Aspose.Cells提供[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor))方法以添加分线评论。[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor))方法接受以下三个参数。

- 单元格名称: 将插入评论的单元格的名称。
- 评论文本: 评论的文本。
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor)：评论的作者

以下代码示例演示了使用[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor))方法向单元格A1添加分线评论。请参见代码生成的[输出Excel文件](AddThreadedComments_out.xlsx)。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **阅读分线评论**
### **使用 Excel 阅读分线评论**
要在 Excel 中阅读分线评论，只需将鼠标悬停在包含评论的单元格上即可查看评论。评论视图将类似于以下图片中的视图。

![todo:image_alt_text](threaded-comments_1.jpg)
### **使用 Aspose.Cells 读取分线评论**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments(java.lang.String))方法来检索指定列的分线评论。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments(java.lang.String))方法接受列名作为参数，并返回[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)。您可以遍历[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)以查看评论。

以下示例演示了通过加载[sample Excel文件](ThreadedCommentsSample.xlsx)从A1列中读取注释。请参见代码生成的控制台输出以供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **控制台输出**
备注: 测试分线注释

作者: Aspose 测试
### **阅读分线评论的创建时间**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments(java.lang.String))方法来检索指定列的分线评论。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments(java.lang.String))方法接受列名作为参数，并返回[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)。您可以遍历[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)并使用[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)属性。

以下示例演示了通过加载[sample Excel文件](ThreadedCommentsSample.xlsx)读取分线评论的创建时间。请参见代码生成的控制台输出以供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **控制台输出**
备注: 测试分线注释

作者: Aspose 测试

创建时间：2019-05-15T12:46:23
## **编辑分线评论**
### **使用 Excel 编辑分线评论**
要在Excel中编辑分线评论，请点击评论中的**编辑**链接，如下图所示。

![todo:image_alt_text](threaded-comments_7.jpg)
### **使用 Aspose.Cells 编辑分线评论**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments(java.lang.String))方法来检索指定列的分线评论。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments(java.lang.String))方法接受列名作为参数，并返回[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)。您可以更新[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)中所需的评论，然后保存工作簿。

以下示例演示了通过加载[sample Excel文件](ThreadedCommentsSample.xlsx)编辑A1列中的第一条分线评论。请参见代码生成的[输出Excel文件](EditThreadedComments.xlsx)以查看更新后的评论。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **删除分线评论**
### **使用 Excel 删除分线评论**
要在Excel中删除分线评论，请右键单击包含评论的单元格，然后单击**删除评论**选项，如下图所示。

![todo:image_alt_text](threaded-comments_8.jpg)
### **使用 Aspose.Cells 删除分线评论**
Aspose.Cells提供[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt(int))方法来移除指定列的评论。[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt(int))方法接受列名作为参数并移除该列中的评论。 

以下示例演示了通过加载[sample Excel文件](ThreadedCommentsSample.xlsx)移除A1列中的评论。请参见代码生成的[输出Excel文件](ThreadedCommentsSample_Out.xlsx)。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

请注意，通过Aspose.Cells移除评论时，并不会自动移除作者。如果需要同时移除作者，请使用[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt(int))方法，如上面的示例所示。

{{% /alert %}}
