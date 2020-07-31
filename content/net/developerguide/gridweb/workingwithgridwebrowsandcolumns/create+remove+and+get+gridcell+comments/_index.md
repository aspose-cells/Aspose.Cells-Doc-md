---
title : "Create Remove and Get GridCell Comments" 
description : "" 
weight : 16708 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebrowsandcolumns/create+remove+and+get+gridcell+comments/
---

# Aspose.Cells for .NET : Create Remove and Get GridCell Comments


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Create Comment object inside Cell](#create-comment-object-inside-cell)
*   3 [Remove Comment object from Cell](#remove-comment-object-from-cell)
*   4 [Get Comment object from Cell](#get-comment-object-from-cell)
{{< /panel >}}
 

## Possible Usage Scenarios

The following article explains how to create, remove and get GridCell comments inside the GridWeb worksheet. It is worth noting that GridWeb displays comment as Tooltip like MS-Excel when you hover mouse over the cell as shown in this screenshot.

![](https://docs2.aspose.com/cells/net/attachments/50266181/50528371.png)

## Create Comment object inside Cell

Please use the `GridCell.CreateComment` method to create a comment object inside cell. The following sample code creates a sample comment in cell B4 of the first worksheet of GridWeb.

{{< code lang="cs" >}}
//Access first worksheet of GridWeb
GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4
GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters
//i.e. note, author, isvisible
cell.CreateComment("This is a B4 note.", "Peter", true);
{{< /code >}}

## Remove Comment object from Cell

Please use the `GridCell.RemoveComment` method to remove a comment object from cell. The following sample code removes cell B4 comment inside the first worksheet of GridWeb.

{{< code lang="cs" >}}
//Access first worksheet of GridWeb
GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4
GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.
cell.RemoveComment();
{{< /code >}}

## Get Comment object from Cell

Please use the `GridCell.GetComment()` method to get comment object from cell. The following sample code gets the comment object from cell B4 and then accesses its various properties like Author, Note, Visibility etc.

{{< code lang="cs" >}}
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
{{< /code >}}

