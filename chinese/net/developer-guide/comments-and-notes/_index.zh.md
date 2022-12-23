---
title: 管理评论和注释
linktitle: 评论和注释
type: docs
weight: 128
url: /zh/net/comments-and-notes/
description: 使用 Aspose.Cells for .Net 插入和管理评论或注释。
keywords: insert comments, insert notes
---
## **介绍**

注释用于向单元格添加附加信息。 Aspose.Cells 提供了两种向单元格添加注释的方法。第一种是在设计器文件中手动创建注释。然后使用Aspose.Cells导入这些评论。第二个是在运行时使用Aspose.Cells API添加评论。本主题讨论使用 Aspose.Cells API 向单元格添加注释。还将解释格式化注释。

## **添加评论**

通过调用[**注释**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection)收藏的[**添加**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index)方法（封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的）。新的[**评论**](https://reference.aspose.com/cells/net/aspose.cells/comment)对象可以从[**注释**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection)通过传递评论索引进行收集。访问后[**评论**](https://reference.aspose.com/cells/net/aspose.cells/comment)对象，使用[**评论**](https://reference.aspose.com/cells/net/aspose.cells/comment)对象的[**笔记**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **评论格式**

还可以通过配置评论的高度、宽度和字体设置来格式化评论的外观。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **添加图像以评论**

使用 Microsoft Excel 2007，还可以将图像作为单元格注释的背景。在 Excel 2007 中，这是通过执行以下步骤完成的。 （他们假设您已经添加了单元格评论。）

1. 右键单击包含注释的单元格。
1. 选择**显示/隐藏评论**, 并清除评论中的任何文本。
1. 单击评论的边框以将其选中。
1. 选择**格式**， 然后**评论**.
1. 在**颜色和线条**选项卡，展开**颜色**列表。
1. 点击**填充效果**.
1. 在**图片**选项卡，单击**选择图片**.
1. 找到并选择图片。
1. 点击**好的**直到所有对话框都关闭。

Aspose.Cells也提供了这个功能。下面是一个代码示例，它从头开始创建一个 XLSX 文件，向单元格“A1”添加注释，并将图片集作为其背景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **推进主题**
- [更改评论的文本方向](/cells/zh/net/change-text-direction-of-the-comment/)
- [如何更改评论字体颜色](/cells/zh/net/how-to-change-the-comment-font-color/)
- [如何设置评论背景](/cells/zh/net/how-to-set-comment-background/)
- [线程评论](/cells/zh/net/threaded-comments/)

