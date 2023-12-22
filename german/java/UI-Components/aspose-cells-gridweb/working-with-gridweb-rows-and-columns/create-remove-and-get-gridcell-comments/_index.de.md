---
title: Erstellen Sie GridCell-Kommentare zum Entfernen und Abrufen
type: docs
weight: 10
url: /de/java/create-remove-and-get-gridcell-comments/
---
##  **Mögliche Nutzungsszenarien**
Im folgenden Artikel wird erläutert, wie Sie GridCell-Kommentare im GridWeb-Arbeitsblatt erstellen, entfernen und abrufen. Es ist erwähnenswert, dass GridWeb Kommentare als Tooltip wie MS-Excel anzeigt, wenn Sie mit der Maus über die Zelle fahren, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
##  **Erstellen Sie ein Kommentarobjekt in Cell**
Bitte verwenden Sie die Methode GridCell.CreateComment, um ein Kommentarobjekt innerhalb der Zelle zu erstellen. Der folgende Beispielcode erstellt einen Beispielkommentar in Zelle B4 des ersten Arbeitsblatts von GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
##  **Entfernen Sie das Kommentarobjekt aus Cell**
Bitte verwenden Sie die Methode GridCell.RemoveComment, um ein Kommentarobjekt aus der Zelle zu entfernen. Der folgende Beispielcode entfernt den Kommentar der Zelle B4 im ersten Arbeitsblatt von GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
##  **Holen Sie sich das Kommentarobjekt von Cell**
Bitte verwenden Sie die Methode GridCell.GetComment(), um das Kommentarobjekt aus der Zelle abzurufen. Der folgende Beispielcode ruft das Kommentarobjekt aus Zelle B4 ab und greift dann auf seine verschiedenen Eigenschaften wie Autor, Notiz, Sichtbarkeit usw. zu.

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




