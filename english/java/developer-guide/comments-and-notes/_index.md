---
title: Manage Comments and Notes
linktitle: Comments and Notes
type: docs
weight: 128
url: /java/comments-and-notes/
description: Insert and manage comments or notes with Aspose.Cells for java.
keywords: insert comments, insert notes
---

## **Introduction**

Comments are used to add additional information to cells. Aspose.Cells provides two methods for adding comments to cells. The first is to create comments in a designer file manually. These comments are then imported using Aspose.Cells. The second is to add comments using the Aspose.Cells API at runtime. This topic discusses adding comments to cells using the Aspose.Cells API. Formatting comments will also be explained.

## **Adding a Comment**

Add a comment to a cell by calling the [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) collection's **Add** method (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) object). The new [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) object can be accessed from the [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) collection by passing the comment index. After accessing the [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) object, customize the comment note by using the [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) object's [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Comment Formatting**

It is also possible to format comments' appearance by configuring their height, width and font settings.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Advance topics**
- [Change Text Direction of the Comment](/cells/java/change-text-direction-of-the-comment/)
- [How to change the Comment Font Color](/cells/java/how-to-change-the-comment-font-color/)
- [How to set comment background](/cells/java/how-to-set-comment-background/)
- [Threaded Comments](/cells/java/threaded-comments/)

{{< app/cells/assistant language="java" >}}