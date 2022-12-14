---
title: Crea Rimuovi e ottieni commenti GridCell
type: docs
weight: 100
url: /it/net/create-remove-and-get-gridcell-comments/
---
## **Possibili scenari di utilizzo**
Il seguente articolo spiega come creare, rimuovere e ottenere commenti GridCell all'interno del foglio di lavoro GridWeb. Vale la pena notare che GridWeb visualizza i commenti come Tooltip come MS-Excel quando passi il mouse sopra la cella come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](create-remove-and-get-gridcell-comments_1.png)
## **Crea oggetto commento all'interno di Cell**
Utilizzare il metodo GridCell.CreateComment per creare un oggetto commento all'interno della cella. Il seguente codice di esempio crea un commento di esempio nella cella B4 del primo foglio di lavoro di GridWeb.

{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Rimuovere l'oggetto commento da Cell**
Utilizzare il metodo GridCell.RemoveComment per rimuovere un oggetto commento dalla cella. Il codice di esempio seguente rimuove il commento della cella B4 all'interno del primo foglio di lavoro di GridWeb.



{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Ottieni l'oggetto commento da Cell**
Utilizzare il metodo GridCell.GetComment() per ottenere l'oggetto commento dalla cella. Il seguente codice di esempio ottiene l'oggetto commento dalla cella B4 e quindi accede alle sue varie proprietà come Autore, Nota, Visibilità ecc.

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
