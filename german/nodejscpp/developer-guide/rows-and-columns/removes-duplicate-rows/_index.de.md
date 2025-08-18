---
title: Doppelte Zeilen in einem Arbeitsblatt mit Node.js via C++ entfernen
linktitle: Doppelte Zeilen in einem Arbeitsblatt entfernen
type: docs
weight: 370
url: /de/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Lernen Sie, wie Sie doppelte Zeilen in einem Arbeitsblatt mit Aspose.Cells for Node.js via C++ entfernen und bestimmte Spalten für Duplikatprüfungen auswählen.
---


Das Entfernen doppelter Zeilen ist eine der vielen nützlichen Funktionen von Microsoft Excel. Es ermöglicht Benutzern, doppelte Zeilen in einem Arbeitsblatt zu entfernen, und Sie können auswählen, welche Spalten auf doppelte Informationen überprüft werden sollen.

Aspose.Cells for Node.js via C++ stellt die Methode `Cells.removeDuplicates()` bereit, um dies zu tun. Sie können auch `startRow`, `startColumn`, `endRow` und `endColumn` festlegen, um den Bereich der zu überprüfenden Spalten anzugeben.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
