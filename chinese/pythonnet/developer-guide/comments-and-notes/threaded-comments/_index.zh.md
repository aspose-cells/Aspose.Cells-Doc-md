---
title: 分线评论
type: docs
weight: 140
url: /zh/python-net/threaded-comments/
---

## **线程化的批注**

MS Excel 365提供了一个添加分线评论的功能。这些评论可以用作对话，并可用于讨论。现在的评论带有一个回复框，允许进行分线对话。Excel 365中的旧注释称为注释。下面的截图显示了在Excel中打开分线评论时的显示方式。

![todo:image_alt_text](threaded-comments_1.jpg)

在较旧版本的Excel中，分线评论显示如下。以下图片是打开在Excel 2016中的样本文件时拍摄的。

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells for Python via .NET还提供管理线程评论的功能。

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

### **使用Aspose.Cells for Python via .NET添加线程评论**

Aspose.Cells for Python via .NET提供[**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/)方法以添加线程评论。[**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment)方法接受以下三个参数。

- 单元格名称：要插入评论的单元格的名称。
- 评论文本：评论的文本。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor)：评论的作者

以下代码示例演示了使用[**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment)方法向单元格A1添加分线评论。请参考代码生成的[输出Excel文件](89849859.xlsx)。

#### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **读取分线评论**

### **使用Excel读取分线评论**

要在Excel中读取分线评论，只需将鼠标悬停在包含评论的单元格上以查看评论。评论视图将类似于以下图像中的视图。

![todo:image_alt_text](threaded-comments_1.jpg)

### **使用Aspose.Cells for Python via .NET读取线程评论**

Aspose.Cells for Python via .NET提供[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)方法以检索指定列的线程评论。[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)方法接受列名作为参数并返回[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)。你可以遍历[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)以查看评论。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 从A1列读取评论。请查看生成的代码控制台输出以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **控制台输出**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **读取线程评论的创建时间**

Aspose.Cells for Python via .NET提供[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)方法以检索指定列的线程评论。[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)方法接受列名作为参数并返回[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)。你可以遍历[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)并使用[**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time)属性。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 读取线程评论的创建时间。请查看生成的代码控制台输出以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

#### **控制台输出**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **编辑线程评论**

### **使用Excel编辑线程评论**

要在Excel中编辑线程评论，请单击评论上显示的**编辑**链接，如下图所示。

![todo:image_alt_text](threaded-comments_7.jpg)

### **使用Aspose.Cells for Python via .NET编辑线程评论**

Aspose.Cells for Python via .NET提供[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)方法以检索指定列的线程评论。[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)方法接受列名作为参数并返回[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)。你可以在[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)中更新所需的评论并保存工作簿。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 编辑A1列中的第一个线程评论。请查看生成的代码以供参考。

#### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

