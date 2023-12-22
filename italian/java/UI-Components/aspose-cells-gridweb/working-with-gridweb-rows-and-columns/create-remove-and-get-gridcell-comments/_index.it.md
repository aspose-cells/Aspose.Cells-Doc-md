---
title: Crea Rimuovi e ottieni commenti GridCell
type: docs
weight: 10
url: /it/java/create-remove-and-get-gridcell-comments/
---
##  **Possibili scenari di utilizzo**
Il seguente articolo spiega come creare, rimuovere e ottenere commenti GridCell all'interno del foglio di lavoro GridWeb. Vale la pena notare che GridWeb visualizza il commento come descrizione comando come MS-Excel quando si passa il mouse sopra la cella, come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](create-remove-and-get-gridcell-comments_1.png)
##  **Crea oggetto commento all'interno di Cell**
Utilizza il metodo GridCell.CreateComment per creare un oggetto commento all'interno della cella. Il seguente codice di esempio crea un commento di esempio nella cella B4 del primo foglio di lavoro di GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
##  **Rimuovi l'oggetto Commento da Cell**
Utilizzare il metodo GridCell.RemoveComment per rimuovere un oggetto commento dalla cella. Il seguente codice di esempio rimuove il commento della cella B4 all'interno del primo foglio di lavoro di GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
##  **Ottieni oggetto commento da Cell**
Utilizzare il metodo GridCell.GetComment() per ottenere l'oggetto commento dalla cella. Il seguente codice di esempio ottiene l'oggetto commento dalla cella B4 e quindi accede alle sue varie proprietà come Autore, Nota, Visibilità ecc.

{{< highlight "java" >}}

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




