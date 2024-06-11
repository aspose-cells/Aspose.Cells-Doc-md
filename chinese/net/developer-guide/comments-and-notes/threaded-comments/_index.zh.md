---
title: 分线评论
type: docs
weight: 140
url: /zh/net/threaded-comments/
---

## **线程化的批注**

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

Aspose.Cells提供[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)方法来添加分线评论。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)方法接受以下三个参数。

- 单元格名称：要插入评论的单元格的名称。
- 评论文本：评论的文本。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor)：评论的作者

以下代码示例演示了使用[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)方法向单元格A1添加分线评论。请参考代码生成的[输出Excel文件](89849859.xlsx)。

#### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **读取分线评论**

### **使用Excel读取分线评论**

要在Excel中读取分线评论，只需将鼠标悬停在包含评论的单元格上以查看评论。评论视图将类似于以下图像中的视图。

![todo:image_alt_text](threaded-comments_1.jpg)

### **使用Aspose.Cells读取分线评论**

Aspose.Cells提供[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)方法来检索指定列的分线评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)方法接受列名称作为参数，并返回[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)。您可以遍历[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)以查看评论。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 从A1列读取评论。请查看生成的代码控制台输出以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **控制台输出**

评论: 测试线程评论

作者: Aspose 测试

### **读取线程评论的创建时间**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法来检索指定列的线程评论。 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法接受列名称作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)。您可以遍历 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) 并使用 [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) 属性。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 读取线程评论的创建时间。请查看生成的代码控制台输出以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **控制台输出**

评论: 测试线程评论

作者: Aspose 测试

创建时间: 2019年5月15日 下午12:46:23

## **编辑线程评论**

### **使用Excel编辑线程评论**

要在Excel中编辑线程评论，请单击评论上显示的**编辑**链接，如下图所示。

![todo:image_alt_text](threaded-comments_7.jpg)

### **使用Aspose.Cells编辑线程评论**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法来检索指定列的线程评论。 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) 方法接受列名称作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)。您可以更新 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) 中所需的评论并保存工作簿。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 编辑A1列中的第一个线程评论。请查看生成的代码以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **删除线程评论**

### **使用Excel删除线程评论**

要在Excel中删除线程评论，请右键单击包含评论的单元格，然后单击下图所示的**删除评论**选项。

![todo:image_alt_text](threaded-comments_8.jpg)

### **使用Aspose.Cells删除线程评论**

Aspose.Cells 提供 [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) 方法来删除指定列的评论。 [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) 方法接受列名称作为参数并删除该列中的评论。

以下示例演示了通过加载[sample Excel File](89849861.xlsx)文件来删除A1列中的注释。请参考代码生成的[output Excel file](89849864.xlsx)。

#### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

请注意，使用Aspose.Cells删除注释时，作者不会自动删除。如果您需要同时删除作者，请像上面的示例中所示使用[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection)类的RemoveAt方法。

{{% /alert %}}
