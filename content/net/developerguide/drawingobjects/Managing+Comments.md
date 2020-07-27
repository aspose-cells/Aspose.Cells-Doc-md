+++
title = "Managing Comments" 
description = "" 
weight = 12286 
+++

Aspose.Cells for .NET : Managing Comments  

# Aspose.Cells for .NET : Managing Comments


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#ManagingComments-Introduction)
*   2 [Adding a Comment](#ManagingComments-AddingaComment)
*   3 [Comment Formatting](#ManagingComments-CommentFormatting)
*   4 [Add an Image to Comment](#ManagingComments-AddanImagetoComment)
{{< /panel >}}
 

## Introduction

Comments are used to add additional information to cells. Aspose.Cells provides two methods for adding comments to cells. The first is to create comments in a designer file manually. These comments are then imported using Aspose.Cells. The second is to add comments using the Aspose.Cells API at runtime. This topic discusses adding comments to cells using the Aspose.Cells API. Formatting comments will also be explained.

## Adding a Comment

Add a comment to a cell by calling the [Comments](https://apireference.aspose.com/net/cells/aspose.cells/commentcollection) collection's [Add](https://apireference.aspose.com/net/cells/aspose.cells/commentcollection/methods/add/index) method (encapsulated in the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) object). The new [Comment](https://apireference.aspose.com/net/cells/aspose.cells/comment) object can be accessed from the [Comments](https://apireference.aspose.com/net/cells/aspose.cells/commentcollection) collection by passing the comment index. After accessing the [Comment](https://apireference.aspose.com/net/cells/aspose.cells/comment) object, customize the comment note by using the [Comment](https://apireference.aspose.com/net/cells/aspose.cells/comment) object's [Note](https://apireference.aspose.com/net/cells/aspose.cells/comment/properties/note) property.

## Comment Formatting

It is also possible to format comments' appearance by configuring their height, width and font settings.

## Add an Image to Comment

With Microsoft Excel 2007, it is also possible to have an image as the background to a cell comment. In Excel 2007 this is accomplished by doing the following steps. (They suppose that you have already added a cell comment.)

1.  Right-click the cell that contains the comment.
2.  Select **Show/Hide Comments**, and clear any text from the comment.
3.  Click on the border of the comment to select it.
4.  Select **Format**, then **Comment**.
5.  On the **Colors and Lines** tab, expand the **Color** list.
6.  Click **Fill Effects**.
7.  On the **Picture** tab, click **Select Picture**.
8.  Locate and select the picture.
9.  Click **OK** until all dialogs have closed.

Aspose.Cells also provides this feature. Below is a code sample that creates an XLSX file from scratch, adding a comment to cell "A1" with a picture set as its background.

