---
title: Erstellen, Entfernen und Abrufen von GridCell Kommentaren
type: docs
weight: 10
url: /de/java/create-remove-and-get-gridcell-comments/
---

## **Mögliche Verwendungsszenarien**
Der folgende Artikel erläutert, wie GridCell-Kommentare innerhalb des GridWeb-Arbeitsblatts erstellt, entfernt und abgerufen werden können. Es ist erwähnenswert, dass GridWeb Kommentare als Tooltip wie MS-Excel anzeigt, wenn Sie mit der Maus über die Zelle fahren, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Erstellen eines Kommentarobjekts in der Zelle**
Bitte verwenden Sie die Methode GridCell.CreateComment zum Erstellen eines Kommentarobjekts in der Zelle. Der folgende Beispielcode erstellt einen Beispielkommentar in Zelle B4 des ersten Arbeitsblatts von GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Kommentarobjekt aus der Zelle entfernen**
Verwenden Sie bitte die Methode GridCell.RemoveComment zum Entfernen eines Kommentarobjekts aus der Zelle. Der folgende Beispielcode entfernt den Kommentar in Zelle B4 im ersten Arbeitsblatt von GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Kommentarobjekt aus der Zelle abrufen**
Bitte verwenden Sie die Methode GridCell.GetComment(), um das Kommentarobjekt aus der Zelle zu erhalten. Der folgende Beispielcode erhält das Kommentarobjekt aus Zelle B4 und greift dann auf verschiedene Eigenschaften wie Autor, Notiz, Sichtbarkeit usw. zu.

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




