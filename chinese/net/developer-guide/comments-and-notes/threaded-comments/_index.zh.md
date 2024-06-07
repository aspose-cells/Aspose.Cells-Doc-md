---
title: 线程化评论
type: docs
weight: 140
url: /zh/net/threaded-comments/
---

## **线程化评论**

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
  - 单击**审阅**选项卡
  - 单击**新注释**按钮
  - 这将打开对话框，可在活动单元格中输入评论。
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- 方法2
  - 在要插入评论的单元格上右键单击。
  - 单击**新评论**选项。
  - 这将打开对话框，可在活动单元格中输入评论。
  - ![todo:image_alt_text](threaded-comments_5)

### **使用Aspose.Cells添加线程化评论**

Aspose.Cells提供[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)方法来添加线程化评论。 [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)方法接受以下三个参数。

- 单元格名称: 将插入评论的单元格的名称。
- 评论文本: 评论的文本。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): 评论的作者

以下代码示例演示了使用 [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) 方法向单元格 A1 添加分线评论。请参阅代码生成的 [输出 Excel 文件](89849859.xlsx) 以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **阅读分线评论**

### **使用 Excel 阅读分线评论**

要在 Excel 中阅读分线评论，只需将鼠标悬停在包含评论的单元格上即可查看评论。评论视图将类似于以下图片中的视图。

![todo:image_alt_text](threaded-comments_1.jpg)

### **使用 Aspose.Cells 读取分线评论**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法来检索指定列的分线评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法接受列名作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)。您可以遍历 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) 来查看评论。

以下示例演示了通过加载 [示例 Excel 文件](89849861.xlsx) 从列 A1 读取备注。请参阅代码生成的控制台输出以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **控制台输出**

备注: 测试分线注释

作者: Aspose 测试

### **阅读分线评论的创建时间**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法来检索指定列的分线评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法接受列名作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)。您可以遍历 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) 并使用 [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) 属性。

以下示例演示了通过加载 [示例 Excel 文件](89849861.xlsx) 读取分线评论的创建时间。请参阅代码生成的控制台输出以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **控制台输出**

备注: 测试分线注释

作者: Aspose 测试

创建时间: 2019年5月15日 下午12:46:23

## **编辑分线评论**

### **使用 Excel 编辑分线评论**

要在 Excel 中编辑分线评论，请单击评论上显示的 **编辑** 链接，如下图所示。

![todo:image_alt_text](threaded-comments_7.jpg)

### **使用 Aspose.Cells 编辑分线评论**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法来检索指定列的分线评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法接受列名作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)。您可以在 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) 中更新所需的评论并保存工作簿。

以下示例演示了通过加载 [示例 Excel 文件](89849861.xlsx) 编辑列 A1 中的第一个分线评论。请参阅代码生成的 [输出 Excel 文件](89849862.xlsx) 以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **删除分线评论**

### **使用 Excel 删除分线评论**

要在 Excel 中删除分线评论，请右键单击包含评论的单元格，然后单击下面图片中显示的 **删除评论** 选项。

![todo:image_alt_text](threaded-comments_8.jpg)

### **使用 Aspose.Cells 删除分线评论**

Aspose.Cells 提供 [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) 方法来移除指定列的评论。[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) 方法接受列名作为参数，并移除该列中的评论。

以下示例演示了通过加载 [示例 Excel 文件](89849861.xlsx) 在列 A1 中移除评论。请参阅代码生成的 [输出 Excel 文件](89849864.xlsx) 以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

请注意，使用 Aspose.Cells 删除评论时，作者不会自动删除。如果您需要同时删除作者，请像上面的示例中所示使用 [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) 类的 RemoveAt 方法。

{{% /alert %}}
