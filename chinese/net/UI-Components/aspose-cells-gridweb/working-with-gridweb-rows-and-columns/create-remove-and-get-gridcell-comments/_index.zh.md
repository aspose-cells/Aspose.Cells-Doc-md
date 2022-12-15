---
title: 创建删除和获取 GridCell 注释
type: docs
weight: 100
url: /zh/net/create-remove-and-get-gridcell-comments/
---
## **可能的使用场景**
以下文章介绍了如何在 GridWeb 工作表中创建、删除和获取 GridCell 注释。值得注意的是，当您将鼠标悬停在单元格上时，GridWeb 会像 MS-Excel 一样将注释显示为工具提示，如此屏幕截图所示。

![待办事项：图像_替代_文本](create-remove-and-get-gridcell-comments_1.png)
## **在 Cell 内创建 Comment 对象**
请使用 GridCell.CreateComment 方法在单元格内创建评论对象。以下示例代码在 GridWeb 的第一个工作表的单元格 B4 中创建示例注释。

{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **从 Cell 中删除 Comment 对象**
请使用 GridCell.RemoveComment 方法从单元格中删除注释对象。以下示例代码删除 GridWeb 第一个工作表中的单元格 B4 注释。



{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **从 Cell 获取 Comment 对象**
请使用 GridCell.GetComment() 方法从单元格中获取注释对象。以下示例代码从单元格 B4 获取评论对象，然后访问其各种属性，如作者、注释、可见性等。

{{< highlight "java" >}}

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
