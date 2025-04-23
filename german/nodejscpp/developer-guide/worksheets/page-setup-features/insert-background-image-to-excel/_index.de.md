---
title: Heben Sie Hintergrundbild in Excel mit Node.js über C++ ein
linktitle: Hintergrundbild in Excel einfügen
type: docs
weight: 90
url: /de/nodejs-cpp/insert-background-image-to-excel/
description: "Wie man Hintergrundbild in Excel mit Aspose.Cells for Node.js via C++ einfügt."
---

{{% alert color="primary" %}} 

Sie können ein Arbeitsblatt attraktiver gestalten, indem Sie ein Bild als Hintergrundbild hinzufügen. Diese Funktion kann sehr effektiv sein, wenn Sie eine spezielle Unternehmensgrafik haben, die einen Hauch des Hintergrunds hinzufügt, ohne die Daten auf dem Blatt zu verdecken. Sie können mithilfe der Aspose.Cells-API ein Hintergrundbild für ein Blatt festlegen.

{{% /alert %}} 

## **Blatthintergrund in Microsoft Excel festlegen**

Um ein Hintergrundbild für ein Blatt in Microsoft Excel festzulegen (z. B. Microsoft Excel 2019):

1. Wählen Sie im Menü **Seitenlayout** die Option **Seiteneinrichtung** und anschließend die Option **Hintergrund**.
1. Wählen Sie ein Bild aus, um das Hintergrundbild des Blatts festzulegen.

   **Festlegen eines Blatthintergrunds**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Hintergrundbild im Arbeitsblatt mit Aspose.Cells for Node.js via C++ einstellen**

Der unten stehende Code legt ein Hintergrundbild mithilfe eines Bildes aus einem Stream fest.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Verwandte Artikel

- [Arbeiten mit Hintergründen in ODS-Dateien](/cells/de/nodejs-cpp/working-with-background-in-ods-files/)

