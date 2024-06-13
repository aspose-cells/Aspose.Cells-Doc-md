---
title: 分线评论
type: docs
weight: 140
url: /zh/java/threaded-comments/
---

# **线程化的批注**
MS Excel 365提供了一个添加分线评论的功能。这些评论可以用作对话，并可用于讨论。现在的评论带有一个回复框，允许进行分线对话。Excel 365中的旧注释称为注释。下面的截图显示了在Excel中打开分线评论时的显示方式。

![todo:image_alt_text](threaded-comments_1.jpg)

在较旧版本的Excel中，分线评论显示如下。以下图片是打开在Excel 2016中的样本文件时拍摄的。

![todo:image_alt_text](threaded-comments_2.jpg)



![todo:image_alt_text](threaded-comments_3.jpg)



Aspose.Cells还提供了管理分线评论的功能。 
## **添加分线评论**
### **使用Excel添加分线评论**
在Excel 365中添加分线评论，请按照以下步骤进行。

- 方法1
  - 单击**审阅**选项卡
  - 单击**新建评论**按钮
  - 这将打开一个对话框，以输入活动单元格中的评论。
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- 方法2
  - 右键单击要插入评论的单元格。
  - 单击**新建评论**选项。
  - 这将打开一个对话框，以输入活动单元格中的评论。
  - ![todo:image_alt_text](threaded-comments_5)
### **使用Aspose.Cells添加分线评论**
Aspose.Cells提供[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\))方法来添加分线程评论。[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\))方法接受以下三个参数。

- 单元格名称：要插入评论的单元格的名称。
- 评论文本：评论的文本。
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor)：评论的作者

以下代码示例演示了如何使用[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\))方法向单元格A1添加分线程评论。请参阅代码生成的 [输出Excel文件](AddThreadedComments_out.xlsx) 以供参考。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **读取分线评论**
### **使用Excel读取分线评论**
要在Excel中读取分线评论，只需将鼠标悬停在包含评论的单元格上以查看评论。评论视图将类似于以下图像中的视图。

![todo:image_alt_text](threaded-comments_1.jpg)
### **使用Aspose.Cells读取分线评论**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))方法来检索指定列的分线程评论。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))方法接受列名作为参数，并返回[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)。您可以遍历[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)以查看评论。

以下示例演示了通过加载 [sample Excel File](ThreadedCommentsSample.xlsx) 从A1列读取评论。请参考代码生成的控制台输出。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **控制台输出**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **读取线程评论的创建时间**
Aspose.Cells 提供 [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法来检索指定列的线程化评论。 [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法接受列名作为参数，并返回 [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)。 您可以遍历 [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)，并使用 [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime) 属性。

以下示例演示了通过加载 [sample Excel File](ThreadedCommentsSample.xlsx) 读取线程化评论的创建时间。请参考代码生成的控制台输出。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **控制台输出**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **编辑线程评论**
### **使用Excel编辑线程评论**
要在 Excel 中编辑线程化评论，单击评论上显示的 **编辑** 链接，如下图所示。

![todo:image_alt_text](threaded-comments_7.jpg)
### **使用Aspose.Cells编辑线程评论**
Aspose.Cells 提供 [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法来检索指定列的线程化评论。 [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) 方法接受列名作为参数，并返回 [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)。 您可以更新 [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) 中所需的评论，并保存工作簿。

以下示例演示了通过加载 [sample Excel File](ThreadedCommentsSample.xlsx) 编辑A1列中的第一个线程化评论。请参考代码生成的 [output Excel file](EditThreadedComments.xlsx)，显示更新后的评论。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **删除线程评论**
### **使用Excel删除线程评论**
要在 Excel 中删除线程化评论，右键单击包含评论的单元格，然后单击 **删除评论** 选项，如下图所示。

![todo:image_alt_text](threaded-comments_8.jpg)
### **使用Aspose.Cells删除线程评论**
Aspose.Cells 提供 [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) 方法来删除指定列的评论。 [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) 方法接受列名作为参数，删除该列中的评论。 

下面的示例演示了如何通过加载 [示例 Excel 文件](ThreadedCommentsSample.xlsx) 来删除 A1 列中的注释。请参考代码生成的 [输出 Excel 文件](ThreadedCommentsSample_Out.xlsx)。
#### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

请注意，通过 Aspose.Cells 删除评论时，作者不会自动删除。如果您也需要删除作者，请使用 [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) 方法，就像上面的示例中所示的那样。

{{% /alert %}}
