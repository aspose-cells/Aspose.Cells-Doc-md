---
title: 管理评论和附注
linktitle: 评论和笔记
type: docs
weight: 128
url: /zh/net/comments-and-notes/
description: 使用 Aspose.Cells for .Net 插入和管理评论或附注。
keywords: 插入评论，插入附注
---

## **介绍**

评论用于向单元格添加额外信息。Aspose.Cells 提供两种方法来向单元格添加评论。第一种是在设计文件中手动创建评论，然后使用 Aspose.Cells 导入这些评论。第二种是在运行时使用 Aspose.Cells API 添加评论。本主题将讨论使用 Aspose.Cells API 向单元格添加评论。还将解释格式化评论。

## **添加评论**

调用 [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) 集合的 [**Add**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) 方法（封装在 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 对象中）向单元格添加备注。可以通过传递注释索引从 [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) 集合访问新的 [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) 对象。访问 [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) 对象后，可以使用 [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) 对象的 [**Note**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note) 属性自定义评论备注。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **评论格式设置**

还可以通过配置其高度、宽度和字体设置来格式化评论的外观。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **为评论添加图像**

在 Microsoft Excel 2007 中，还可以将图像添加为单元格备注的背景。在 Excel 2007 中，您可以通过以下步骤实现。（假设您已经添加了单元格备注。）

1. 右键单元格中的备注。
1. 选择 **显示/隐藏备注**，并清除备注中的任何文本。
1. 单击备注的边框选择它。
1. 选择 **格式**，然后选择 **备注**。
1. 在 **颜色和线条** 选项卡上展开 **颜色** 列表。
1. 单击 **填充效果**。
1. 在 **图片** 选项卡上，单击 **选择图片**。
1. 定位并选择图片。
1. 单击 **确定** 直到所有对话框关闭。

Aspose.Cells还提供了此功能。以下是创建XLSX文件的代码示例，从头开始添加一个备注到单元格“A1”，并设置图片作为其背景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **高级主题**
- [更改备注文本方向](/cells/zh/net/change-text-direction-of-the-comment/)
- [如何更改备注字体颜色](/cells/zh/net/how-to-change-the-comment-font-color/)
- [如何设置备注背景](/cells/zh/net/how-to-set-comment-background/)
- [线程化评论](/cells/zh/net/threaded-comments/)

