---
title: Creare Rimuovere e Ottenere Commenti delle Celle di Grid
type: docs
weight: 10
url: /it/java/create-remove-and-get-gridcell-comments/
---

## **Possibili Scenari di Utilizzo**
L'articolo seguente spiega come creare, rimuovere e ottenere commenti delle celle di GridWeb. È importante notare che GridWeb visualizza il commento come un tooltip come MS-Excel quando si passa il mouse sopra la cella come mostrato in questa schermata.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Creare oggetto Commento all'interno della Cella**
Si prega di utilizzare il metodo GridCell.CreateComment per creare un oggetto commento all'interno della cella. Il seguente codice di esempio crea un commento di esempio nella cella B4 del primo foglio di lavoro di GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Rimuovere oggetto Commento dalla Cella**
Si prega di utilizzare il metodo GridCell.RemoveComment per rimuovere un oggetto commento dalla cella. Il seguente codice di esempio rimuove il commento della cella B4 all'interno del primo foglio di lavoro di GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Ottenere oggetto Commento dalla Cella**
Si prega di utilizzare il metodo GridCell.GetComment() per ottenere l'oggetto commento dalla cella. Il seguente codice di esempio ottiene l'oggetto commento dalla cella B4 e quindi accede alle sue varie proprietà come Autore, Nota, Visibilità etc.

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




