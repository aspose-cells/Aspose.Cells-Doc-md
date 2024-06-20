---
title: Creare Rimuovere e Ottenere Commenti delle Celle di Grid
type: docs
weight: 100
url: /it/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: Questo articolo presenta come lavorare con i commenti in GridWeb.
---

## **Possibili Scenari di Utilizzo**
L'articolo seguente spiega come creare, rimuovere e ottenere commenti da una cella (GridCell) all'interno del foglio di lavoro GridWeb. È utile notare che GridWeb visualizza il commento come un Tooltip come MS-Excel quando si passa il mouse sopra la cella come mostrato in questa schermata.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Creare oggetto Commento all'interno della Cella**
Si prega di utilizzare il metodo GridCell.CreateComment per creare un oggetto commento all'interno della cella. Il seguente codice di esempio crea un commento di esempio nella cella B4 del primo foglio di lavoro di GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Rimuovere oggetto Commento dalla Cella**
Si prega di utilizzare il metodo GridCell.RemoveComment per rimuovere l'oggetto commento dalla cella. Il seguente codice di esempio rimuove il commento dalla cella B4 all'interno del primo foglio di lavoro di GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Ottenere oggetto Commento dalla Cella**
Si prega di utilizzare il metodo GridCell.GetComment() per ottenere l'oggetto commento dalla cella. Il seguente codice di esempio ottiene l'oggetto commento dalla cella B4 e poi accede alle sue varie proprietà come Autore, Nota, Visibilità, ecc.

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
