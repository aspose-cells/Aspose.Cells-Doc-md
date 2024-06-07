---
title: 创建、移除和获取GridCell注释
type: docs
weight: 10
url: /zh/java/create-remove-and-get-gridcell-comments/
---

## **可能的使用场景**
以下文章解释了如何在GridWeb工作表内创建、移除和获取GridCell注释。值得注意的是，GridWeb在您将鼠标悬停在单元格上时显示注释，就像MS-Excel那样，如本屏幕截图所示。

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **在单元格内创建评论对象**
请使用 GridCell.CreateComment 方法在单元格内创建评论对象。以下示例代码在第一个 GridWeb 工作表的 B4 单元格创建一个示例评论。

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **从单元格中移除评论对象**
请使用 GridCell.RemoveComment 方法从单元格中移除注释对象。以下示例代码将删除GridWeb第一个工作表中单元格B4的注释。



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **从单元格获取评论对象**
请使用 GridCell.GetComment() 方法从单元格中获取注释对象。以下示例代码从单元格B4获取注释对象，然后访问其各种属性，如作者、备注、可见性等。

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Get comment of this cell

GridComment gridComm = cell.getComment();

// Access its various properties

String strAuth = gridComm.getAuthor();

String strNote = gridComm.getNote();

boolean isVis = gridComm.isVisible();


{{< /highlight >}}




