---
title: Wie man mit Node.js via C++ ein Textfeld zu einem Arbeitsblatt hinzufügt/einfügt
linktitle: Fügen Sie eine Textbox in ein Arbeitsblatt ein
type: docs
weight: 10
url: /de/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Wie man in Aspose.Cells for Node.js via C++ ein Textfeld zu einem Arbeitsblatt hinzufügt/einfügt.
keywords: Textfeld hinzufügen/einfügen, TextBox Arbeitsblatt Excel Aspose Node.js via C++
---

## Fügen Sie ein Textfeld in das Arbeitsblatt in Excel ein

In den Excel-Programmen (Version 07 und höher) gibt es zwei Stellen, an denen Sie Textfelder einfügen können. Einmal in "Einfügen-Formen", dann auf der rechten Seite des oberen Menüs unter der Option "Einfügen".

### Methode eins:

![1](1.png)

### Methode zwei:

![2](2.png)

## Wie man erstellt

Sie können Textfelder mit horizontal oder vertikal ausgerichtetem Text erstellen.

- Wählen Sie die entsprechende Option (horizontal oder vertikal)
- Klicken Sie links auf die Seite
- Halten Sie die linke Taste gedrückt und ziehen Sie eine Entfernung auf der Seite
- Lassen Sie die linke Taste los

Nun haben Sie ein Textfeld.

## Textfeld zu Arbeitsblatt in Aspose.Cells for Node.js via C++ hinzufügen

Wenn Sie eine große Anzahl von Textfeldern in das Arbeitsblatt einfügen müssen, ist die manuelle Einfügung offensichtlich problematisch. Wenn Sie dies stört, wird dieses Dokument Ihnen sicherlich helfen. [Aspose.Cells](https://products.aspose.com/cells/) bietet eine API, mit der Sie einfache Masseninserts in Ihrem Code durchführen können.

Der folgende Beispielcode erstellt ein Textfeld.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Sie erhalten eine Datei, die der [Ergebnisdatei](result.xlsx) ähnlich ist. In der Datei werden Sie Folgendes sehen:

![](52449.png)

