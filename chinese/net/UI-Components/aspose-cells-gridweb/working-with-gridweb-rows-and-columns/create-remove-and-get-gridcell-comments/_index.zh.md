---
title: 创建、移除和获取GridCell注释
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb，评论
description: 本文介绍了在GridWeb中处理评论的方法。
---

## **可能的使用场景**
以下文章解释了如何在 GridWeb 工作表内创建、移除和获取单元格 (GridCell) 的评论。值得注意的是，当您将鼠标悬停在单元格上时，GridWeb 会将评论显示为工具提示，就像 MS-Excel 中的效果一样，如下方截图所示。

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **在单元格内创建评论对象**
请使用 GridCell.CreateComment 方法在单元格内创建评论对象。以下示例代码在第一个 GridWeb 工作表的 B4 单元格创建一个示例评论。

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **从单元格中移除评论对象**
请使用 GridCell.RemoveComment 方法从单元格中移除评论对象。以下示例代码在第一个 GridWeb 工作表内移除 B4 单元格的评论。



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **从单元格获取评论对象**
请使用 GridCell.GetComment() 方法从单元格中获取评论对象。以下示例代码从 B4 单元格获取评论对象，然后访问其作者、注释、可见性等各种属性。

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Get comment of this cell

GridComment gridComm = cell.GetComment();

//Access its various properties

string strAuth = gridComm.Author;

string strNote = gridComm.Note;

bool isVis = gridComm.IsVisible;

{{< /highlight >}}
