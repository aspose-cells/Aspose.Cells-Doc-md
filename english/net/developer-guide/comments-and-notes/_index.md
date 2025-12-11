---
title: Manage Comments and Notes
linktitle: Comments and Notes
type: docs
weight: 128
url: /net/comments-and-notes/
description: Insert and manage comments or notes with Aspose.Cells for .Net.
keywords: insert comments, insert notes
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Comments are used to add additional information to cells. Aspose.Cells provides two methods for adding comments to cells. The first is to create comments in a designer file manually. These comments are then imported using Aspose.Cells. The second is to add comments using the Aspose.Cells API at runtime. This topic discusses adding comments to cells using the Aspose.Cells API. Formatting comments will also be explained.

## **Adding a Comment**

Add a comment to a cell by calling the [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) collection's [**Add**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) method (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) object). The new [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) object can be accessed from the [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) collection by passing the comment index. After accessing the [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) object, customize the comment note by using the [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) object's [**Note**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Comment Formatting**

It is also possible to format comments' appearance by configuring their height, width and font settings.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Add an Image to Comment**

With Microsoft Excel 2007, it is also possible to have an image as the background of a cell comment. In Excel 2007 this is accomplished by following these steps. (It is assumed that you have already added a cell comment.)

1. Right‑click the cell that contains the comment.  
2. Select **Show/Hide Comments**, and clear any text from the comment.  
3. Click on the border of the comment to select it.  
4. Select **Format**, then **Comment**.  
5. On the **Colors and Lines** tab, expand the **Color** list.  
6. Click **Fill Effects**.  
7. On the **Picture** tab, click **Select Picture**.  
8. Locate and select the picture.  
9. Click **OK** until all dialogs have closed.

Aspose.Cells also provides this feature. Below is a code sample that creates an XLSX file from scratch, adding a comment to cell **A1** with a picture set as its background.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Advanced topics**
- [Change Text Direction of the Comment](/cells/net/change-text-direction-of-the-comment/)
- [How to change the Comment Font Color](/cells/net/how-to-change-the-comment-font-color/)
- [How to set comment background](/cells/net/how-to-set-comment-background/)
- [Threaded Comments](/cells/net/threaded-comments/)

{{< app/cells/assistant language="csharp" >}}
