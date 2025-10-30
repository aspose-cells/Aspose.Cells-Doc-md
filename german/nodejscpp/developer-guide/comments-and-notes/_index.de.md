---
title: Kommentare und Notizen mit Node.js via C++ verwalten
linktitle: Kommentare und Notizen
type: docs
weight: 128
url: /de/nodejs-cpp/comments-and-notes/
description: Kommentare oder Notizen mit Aspose.Cells for Node.js via C++ einfügen und verwalten.
keywords: Kommentare einfügen, Notizen einfügen Node.js über C++
---

## **Einführung**

Kommentare werden verwendet, um zusätzliche Informationen zu Zellen hinzuzufügen. Aspose.Cells for Node.js via C++ bietet zwei Methoden zum Hinzufügen von Kommentaren zu Zellen. Die erste besteht darin, Kommentare manuell in einer Designer-Datei zu erstellen. Diese Kommentare werden anschließend mit Aspose.Cells importiert. Die zweite Möglichkeit besteht darin, Kommentare mithilfe der Aspose.Cells API zur Laufzeit hinzuzufügen. Dieses Thema beschreibt, wie Kommentare mit der Aspose.Cells API zu Zellen hinzugefügt werden. Das Formatieren von Kommentaren wird ebenfalls erklärt.

## **Einen Kommentar hinzufügen**

Fügen Sie einem Zellkommentar hinzu, indem Sie die [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)-Sammlung mit ihrer [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-)-Methode aufrufen (eingeschlossen im [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Objekt). Das neue [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)-Objekt kann aus der [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)-Sammlung durch Übergabe des Kommentar-Index abgerufen werden. Nach Zugriff auf das [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)-Objekt passen Sie die Kommentarnotiz mit der [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--)-Eigenschaft an.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Kommentarformatierung**

Es ist auch möglich, das Erscheinungsbild von Kommentaren zu formatieren, indem ihre Höhe, Breite und Schriftarteneinstellungen konfiguriert werden.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Ein Bild zum Kommentar hinzufügen**

Mit Microsoft Excel 2007 ist es auch möglich, ein Bild als Hintergrund für einen Zellenkommentar zu haben. In Excel 2007 wird dies durch die folgenden Schritte erreicht. (Es wird davon ausgegangen, dass bereits ein Zellenkommentar hinzugefügt wurde.)

1. Klicken Sie mit der rechten Maustaste auf die Zelle, die den Kommentar enthält.
1. Wählen Sie **Kommentare einblenden/ausblenden** und löschen Sie jeglichen Text aus dem Kommentar.
1. Klicken Sie auf den Rand des Kommentars, um ihn auszuwählen.
1. Wählen Sie **Format** und dann **Kommentar** aus.
1. Auf der Registerkarte **Farben und Linien** die **Farbe**-Liste erweitern.
1. Klicken Sie auf **Fülleffekte**.
1. Klicken Sie auf der Registerkarte **Bild** auf **Bild auswählen**.
1. Suchen Sie das Bild und wählen Sie es aus.
1. Klicken Sie auf **OK**, bis alle Dialogfelder geschlossen sind.

Auch Aspose.Cells bietet diese Funktion. Im Folgenden finden Sie einen Beispielcode, der eine XLSX-Datei von Grund auf erstellt und einem Zelle "A1" einen Kommentar mit einem Bild als Hintergrund hinzufügt.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Erweiterte Themen**
- [Ändern der Textrichtung des Kommentars](/cells/de/nodejs-cpp/change-text-direction-of-the-comment/)
- [Ändern der Kommentarschriftfarbe](/cells/de/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Wie man den Kommentarhintergrund einstellt](/cells/de/nodejs-cpp/how-to-set-comment-background/)
- [Antwortkommentare](/cells/de/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
