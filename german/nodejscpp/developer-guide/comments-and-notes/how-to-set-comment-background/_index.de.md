---
title: Wie man den Hintergrund in Kommentaren in Excel mit Node.js über C++ ändert
linktitle: Kommentarhintergrund
type: docs
weight: 190
url: /de/nodejs-cpp/how-to-set-comment-background/
description: Wie man die Farbe in Kommentaren ändert und Bilder oder Bilder in Kommentaren in Excel mit Aspose.Cells for Node.js via C++ einfügt.
keywords: Bild, Hintergrund, Kommentar, Farbe, Excel, Node.js, C++ hinzufügen
---

{{% alert color="primary" %}}
Kommentare werden zu Zellen hinzugefügt, um Kommentare zu erfassen, sei es Details zur Funktionsweise einer Formel, Herkunft eines Wertes oder Fragen von Gutachtern. Kommentare spielen eine äußerst wichtige Rolle, wenn mehrere Personen dasselbe Dokument zu unterschiedlichen Zeiten diskutieren oder überprüfen. Wie kann man die Kommentare verschiedener Personen unterscheiden? Ja, wir können für jeden Kommentar eine andere Hintergrundfarbe festlegen. Aber wenn wir viele Dokumente und viele Kommentare verarbeiten müssen, ist manuelles Vorgehen eine Katastrophe. Glücklicherweise bietet [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) eine API, die dies im Code ermöglicht.
{{% /alert %}}

## **Wie ändere ich die Farbe in einem Kommentar in Excel**

Wenn Sie die Standard-Hintergrundfarbe für Kommentare nicht benötigen, möchten Sie diese durch eine Farbe ersetzen, die Sie interessiert. Wie ändere ich die Hintergrundfarbe des Kommentarfelds in Excel?

Der folgende Code zeigt Ihnen, wie Sie [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) verwenden, um Ihre bevorzugte Hintergrundfarbe zu den Kommentaren Ihrer Wahl hinzuzufügen.

Hier haben wir eine [Beispieldatei](exmaple.xlsx) für Sie vorbereitet. Diese Datei dient dazu, das Objekt Workbook im unten stehenden Code zu initialisieren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Führen Sie den obigen Code aus und Sie erhalten eine [Ausgabedatei](result.xlsx).

## **Wie füge ich ein Bild oder eine Grafik in einen Kommentar in Excel ein**

Microsoft Excel ermöglicht es Benutzern, Spreadsheets nach ihren Wünschen anzupassen. Es ist sogar möglich, Hintergrundbilder zu Kommentaren hinzuzufügen. Das Hinzufügen eines Hintergrundbildes kann eine ästhetische Wahl sein oder dazu dienen, das Branding zu stärken.

Der folgende Beispielcode erstellt eine XLSX-Datei von Grund auf mit der [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/)-API und fügt einem Zellkommentar mit Hintergrundbild ein Bild hinzu.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
