---
title: Erstellen, Entfernen und Abrufen von GridCell Kommentaren
type: docs
weight: 100
url: /de/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: In diesem Artikel wird erläutert, wie Sie mit Kommentaren in GridWeb arbeiten.
---

## **Mögliche Verwendungsszenarien**
Im folgenden Artikel wird erläutert, wie Sie einen Kommentar aus einer Zelle (GridCell) innerhalb des GridWeb-Arbeitsblatts erstellen, entfernen und abrufen. Es ist erwähnenswert, dass GridWeb den Kommentar als Tooltip wie MS-Excel anzeigt, wenn Sie mit der Maus über die Zelle fahren, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Erstellen eines Kommentarobjekts in der Zelle**
Bitte verwenden Sie die Methode GridCell.CreateComment zum Erstellen eines Kommentarobjekts in der Zelle. Der folgende Beispielcode erstellt einen Beispielkommentar in Zelle B4 des ersten Arbeitsblatts von GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Kommentarobjekt aus der Zelle entfernen**
Bitte verwenden Sie die Methode GridCell.RemoveComment, um ein Kommentarobjekt aus einer Zelle zu entfernen. Der folgende Beispielcode entfernt den Kommentar der Zelle B4 im ersten Arbeitsblatt von GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Kommentarobjekt aus der Zelle abrufen**
Bitte verwenden Sie die Methode GridCell.GetComment(), um das Kommentarobjekt aus der Zelle zu erhalten. Der folgende Beispielscode ruft das Kommentarobjekt aus der Zelle B4 ab und greift dann auf verschiedene Eigenschaften wie Autor, Notiz, Sichtbarkeit usw. zu.

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
