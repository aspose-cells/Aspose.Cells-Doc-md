---
title: Skapa, ta bort och få kommentarer för GridCell
type: docs
weight: 10
url: /sv/java/create-remove-and-get-gridcell-comments/
---

## **Möjliga användningsscenario**
Följande artikel förklarar hur man skapar, tar bort och hämtar GridCell-kommentarer i GridWeb-kalkylarket. Det är värt att notera att GridWeb visar kommentaren som en verktygstips liknande MS-Excel när du sveper musen över cellen som visas i denna skärmbild.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Skapa kommentarsobjekt inuti cellen**
Använd metoden GridCell.CreateComment för att skapa ett kommentarsobjekt inuti cellen. Följande exempelkod skapar en provkommentar i cell B4 på den första arbetsbladet av GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Ta bort kommentarsobjekt från cellen**
Använd GridCell.RemoveComment-metoden för att ta bort ett kommentarobjekt från en cell. Följande exempelkod tar bort kommentaren från cell B4 i den första kalkylbladet i GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Få kommentarsobjekt från cellen**
Använd GridCell.GetComment()-metoden för att hämta kommentarobjekt från en cell. Följande exempelkod hämtar kommentarobjektet från cell B4 och får sedan åtkomst till dess olika egenskaper som författare, anteckning, synlighet osv.

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




