---
title: 创建、删除和获取GridCell注释
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: 本文介绍了如何在GridWeb中处理评论。
---

## **可能的使用场景**
以下文章解释了如何在GridWeb工作表中创建、删除并获取单元格（GridCell）中的注释。特别值得注意的是，当您将鼠标悬停在单元格上时，GridWeb会像MS-Excel一样将注释显示为工具提示，如此屏幕截图所示。

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **在单元格内创建注释对象**
请使用GridCell.CreateComment方法在单元格内创建注释对象。以下示例代码在GridWeb的第一个工作表的B4单元格中创建了一个示例注释。

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **从单元格中移除注释对象**
请使用GridCell.RemoveComment方法从单元格中移除注释对象。以下示例代码删除GridWeb第一个工作表中单元格B4的注释。



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **从单元格中获取注释对象**
请使用GridCell.GetComment()方法从单元格中获取注释对象。以下示例代码从单元格B4获取注释对象，然后访问其各种属性，如作者、注释、可见性等。

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
