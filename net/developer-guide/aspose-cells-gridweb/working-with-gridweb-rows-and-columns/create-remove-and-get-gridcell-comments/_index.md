---
title: Create Remove and Get GridCell Comments
type: docs
weight: 100
url: /net/create-remove-and-get-gridcell-comments/
---

## **Possible Usage Scenarios**
The following article explains how to create, remove and get GridCell comments inside the GridWeb worksheet. It is worth noting that GridWeb displays comment as Tooltip like MS-Excel when you hover mouse over the cell as shown in this screenshot.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Create Comment object inside Cell**
Please use the GridCell.CreateComment method to create a comment object inside cell. The following sample code creates a sample comment in cell B4 of the first worksheet of GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Remove Comment object from Cell**
Please use the GridCell.RemoveComment method to remove a comment object from cell. The following sample code removes cell B4 comment inside the first worksheet of GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Get Comment object from Cell**
Please use the GridCell.GetComment() method to get comment object from cell. The following sample code gets the comment object from cell B4 and then accesses its various properties like Author, Note, Visibility etc.

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
