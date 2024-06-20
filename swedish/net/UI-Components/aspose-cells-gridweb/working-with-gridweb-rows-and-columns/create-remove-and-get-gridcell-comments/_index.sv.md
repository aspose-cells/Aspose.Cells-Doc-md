---
title: Skapa, ta bort och få kommentarer för GridCell
type: docs
weight: 100
url: /sv/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: Denna artikel visar hur man arbetar med kommentarer i GridWeb.
---

## **Möjliga användningsscenario**
Följande artikel förklarar hur man skapar, tar bort och får kommentarer från en cell (GridCell) inuti GridWeb-kalkylbladet. Det är värt att nämna att GridWeb visar kommentaren som en verktygstips som MS-Excel när du sveper musen över cellen, som visas på denna skärmbild.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Skapa kommentarsobjekt inuti cellen**
Använd metoden GridCell.CreateComment för att skapa ett kommentarsobjekt inuti cellen. Följande exempelkod skapar en provkommentar i cell B4 på den första arbetsbladet av GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Ta bort kommentarsobjekt från cellen**
Använd metoden GridCell.RemoveComment för att ta bort ett kommentarsobjekt från cellen. Följande exempelkod tar bort kommentaren i cell B4 på den första arbetsbladet av GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Få kommentarsobjekt från cellen**
Använd metoden GridCell.GetComment() för att få kommentarsobjekt från cellen. Följande exempelkod får kommentarsobjektet från cell B4 och får sedan åtkomst till dess olika egenskaper som författare, anteckning, synlighet etc.

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
