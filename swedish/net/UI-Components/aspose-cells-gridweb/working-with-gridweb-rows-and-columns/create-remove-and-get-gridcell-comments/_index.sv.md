---
title: Skapa Ta bort och få GridCell-kommentarer
type: docs
weight: 100
url: /sv/net/create-remove-and-get-gridcell-comments/
---
## **Möjliga användningsscenarier**
Följande artikel förklarar hur du skapar, tar bort och får GridCell-kommentarer i GridWeb-kalkylbladet. Det är värt att notera att GridWeb visar kommentarer som verktygstips som MS-Excel när du håller muspekaren över cellen som visas i den här skärmdumpen.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Skapa kommentarsobjekt i Cell**
Använd metoden GridCell.CreateComment för att skapa ett kommentarsobjekt inuti cellen. Följande exempelkod skapar en exempelkommentar i cell B4 i det första kalkylbladet i GridWeb.

{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Ta bort kommentarobjekt från Cell**
Använd metoden GridCell.RemoveComment för att ta bort ett kommentarobjekt från cellen. Följande exempelkod tar bort kommentar från cell B4 i det första kalkylbladet i GridWeb.



{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Få kommentarobjekt från Cell**
Använd metoden GridCell.GetComment() för att hämta kommentarobjekt från cellen. Följande exempelkod hämtar kommentarsobjektet från cell B4 och kommer sedan åt dess olika egenskaper som författare, anteckning, synlighet etc.

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
