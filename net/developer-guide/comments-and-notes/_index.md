---
title: Comments and Notes
type: docs
weight: 128
url: /net/comments-and-notes/
aliases: [/net/managing-comments/]
description: How to insert a comment or note in CSharp.
keywords: insert comment, insert note
---

## **Introduction**

Comments are used to add additional information to cells. Aspose.Cells provides two methods for adding comments to cells. The first is to create comments in a designer file manually. These comments are then imported using Aspose.Cells. The second is to add comments using the Aspose.Cells API at runtime. This topic discusses adding comments to cells using the Aspose.Cells API. Formatting comments will also be explained.

## **Adding a Comment**

Add a comment to a cell by calling the [**Comments**](https://apireference.aspose.com/cells/net/aspose.cells/commentcollection) collection's [**Add**](https://apireference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) method (encapsulated in the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) object). The new [**Comment**](https://apireference.aspose.com/cells/net/aspose.cells/comment) object can be accessed from the [**Comments**](https://apireference.aspose.com/cells/net/aspose.cells/commentcollection) collection by passing the comment index. After accessing the [**Comment**](https://apireference.aspose.com/cells/net/aspose.cells/comment) object, customize the comment note by using the [**Comment**](https://apireference.aspose.com/cells/net/aspose.cells/comment) object's [**Note**](https://apireference.aspose.com/cells/net/aspose.cells/comment/properties/note) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Comment Formatting**

It is also possible to format comments' appearance by configuring their height, width and font settings.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Add an Image to Comment**

With Microsoft Excel 2007, it is also possible to have an image as the background to a cell comment. In Excel 2007 this is accomplished by doing the following steps. (They suppose that you have already added a cell comment.)

1. Right-click the cell that contains the comment.
1. Select **Show/Hide Comments**, and clear any text from the comment.
1. Click on the border of the comment to select it.
1. Select **Format**, then **Comment**.
1. On the **Colors and Lines** tab, expand the **Color** list.
1. Click **Fill Effects**.
1. On the **Picture** tab, click **Select Picture**.
1. Locate and select the picture.
1. Click **OK** until all dialogs have closed.

Aspose.Cells also provides this feature. Below is a code sample that creates an XLSX file from scratch, adding a comment to cell "A1" with a picture set as its background.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}
