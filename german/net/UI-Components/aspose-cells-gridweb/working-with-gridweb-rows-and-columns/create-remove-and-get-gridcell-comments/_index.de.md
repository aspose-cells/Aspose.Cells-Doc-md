---
title: GridCell-Kommentare erstellen und abrufen
type: docs
weight: 100
url: /de/net/create-remove-and-get-gridcell-comments/
---
## **Mögliche Nutzungsszenarien**
Im folgenden Artikel wird erläutert, wie GridCell-Kommentare im GridWeb-Arbeitsblatt erstellt, entfernt und abgerufen werden. Es ist erwähnenswert, dass GridWeb Kommentare als Tooltip wie MS-Excel anzeigt, wenn Sie mit der Maus über die Zelle fahren, wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](create-remove-and-get-gridcell-comments_1.png)
## **Kommentarobjekt innerhalb von Cell erstellen**
Bitte verwenden Sie die GridCell.CreateComment-Methode, um ein Kommentarobjekt innerhalb der Zelle zu erstellen. Der folgende Beispielcode erstellt einen Beispielkommentar in Zelle B4 des ersten Arbeitsblatts von GridWeb.

{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Kommentarobjekt von Cell entfernen**
Bitte verwenden Sie die GridCell.RemoveComment-Methode, um ein Kommentarobjekt aus einer Zelle zu entfernen. Der folgende Beispielcode entfernt den Kommentar zu Zelle B4 im ersten Arbeitsblatt von GridWeb.



{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Holen Sie sich das Kommentarobjekt von Cell**
Bitte verwenden Sie die Methode GridCell.GetComment(), um das Kommentarobjekt aus der Zelle abzurufen. Der folgende Beispielcode ruft das Kommentarobjekt aus Zelle B4 ab und greift dann auf seine verschiedenen Eigenschaften wie Autor, Notiz, Sichtbarkeit usw. zu.

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
