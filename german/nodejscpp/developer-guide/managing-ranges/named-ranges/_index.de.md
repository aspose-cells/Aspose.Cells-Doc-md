---
title: Arbeitsmappe und Arbeitsblatt Scoped Named Ranges mit Node.js über C++ erstellen
linktitle: Benannten Bereich
type: docs
weight: 40
url: /de/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Erfahren Sie, wie Sie workbooks und worksheet gebundene benannte Bereiche mit Aspose.Cells for Node.js via C++ erstellen. 
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, benannte Bereiche mit zwei verschiedenen Bereichen zu definieren: arbeitsmappe (auch als globaler Bereich bekannt) und tabellenblatt.

- Benannte Bereiche mit arbeitsmappenbereich können von jedem Arbeitsblatt innerhalb dieser Arbeitsmappe aus durch einfaches Verwenden ihres Namens aufgerufen werden.
- Auf tabellenblattbeschränkte benannte Bereiche werden mithilfe des Verweises auf das bestimmte Arbeitsblatt, in dem sie erstellt wurden, aufgerufen.

Aspose.Cells for Node.js via C++ bietet die gleiche Funktionalität wie Microsoft Excel zum Hinzufügen von benannten Bereichen, die nach Arbeitsmappe und Arbeitsblatt abgegrenzt sind. Beim Erstellen eines benannten Bereichs, der auf das Arbeitsblatt beschränkt ist, sollte die Arbeitsblattreferenz im Namen verwendet werden, um ihn als auf das Arbeitsblatt beschränkten Bereich zu kennzeichnen.

{{% /alert %}} 
## **Hinzufügen eines benannten Bereichs mit arbeitsmappenbereich**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Hinzufügen eines benannten Bereichs mit tabellenblattbereich**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Erweiterte Themen**
- [Zugriff erstellen und benannte Bereiche kopieren](/cells/de/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Benannte Bereiche formatieren und ändern](/cells/de/nodejs-cpp/format-and-modify-named-ranges/)
- [Bereich mit externen Links abrufen](/cells/de/nodejs-cpp/get-range-with-external-links/)
- [Implementierung nicht aufeinanderfolgender Bereiche](/cells/de/nodejs-cpp/implementing-non-sequential-ranges/)


