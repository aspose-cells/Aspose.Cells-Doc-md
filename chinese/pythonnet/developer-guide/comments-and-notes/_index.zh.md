---
title: 管理注释和备注
linktitle: 注释和备注
type: docs
weight: 128
url: /zh/python-net/comments-and-notes/
description: 使用Aspose.Cells for Python插入和管理评论或笔记 via .NET。
keywords: 插入注释，插入备注
---

## **介绍**

注释用于向单元格添加额外信息。Aspose.Cells提供两种方法来向单元格添加注释。第一种是手动在设计文件中创建注释，然后使用Aspose.Cells导入这些注释。第二种是在运行时使用Aspose.Cells API添加注释。本主题讨论使用Aspose.Cells API向单元格添加注释。还将介绍注释的格式设置。

## **添加注释**

通过调用[**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection)集合的[**add**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add)方法（封装在[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)对象中）向一个单元格添加评论。可以通过传递评论索引访问新的[**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment)对象。在访问[**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment)对象后，可以使用[**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment)对象的[**note**](https://reference.aspose.com/cells/python-net/aspose.cells/comment/note)属性自定义评论注释。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **注释格式设置**

还可以通过配置其高度、宽度和字体设置来格式化注释的外观。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **向注释添加图像**

在Microsoft Excel 2007中，还可以将图像添加为单元格注释的背景。在Excel 2007中，可以通过以下步骤完成这一操作。（假设您已经添加了单元格注释。）

1.右键单元格，然后选择**显示/隐藏注释**，清除注释中的任何文本。
1.点击注释的边框进行选择。
1.选择**格式**，然后选择**注释**。
1.在**颜色和线条**选项卡上，展开**颜色**列表。
1.单击**填充效果**。
1.单击**图片**选项卡。
1.在**图片**选项卡上，单击**选择图片**。
1.定位并选择图片。
1. 点击 **确定** 直到所有对话框都关闭。

Aspose.Cells 也提供了这个功能。下面是一个代码示例，从头开始创建一个 XLSX 文件，并在单元格"A1"中添加一个以图片作为背景的评论。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **高级主题**
- [更改批注的文本方向](/cells/zh/python-net/change-text-direction-of-the-comment/)
- [如何更改批注字体颜色](/cells/zh/python-net/how-to-change-the-comment-font-color/)
- [如何设置评论背景](/cells/zh/python-net/how-to-set-comment-background/)
- [线程化的批注](/cells/zh/python-net/threaded-comments/)

{{< app/cells/assistant language="python-net" >}}
