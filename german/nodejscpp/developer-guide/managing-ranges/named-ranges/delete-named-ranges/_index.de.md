---
title: Benannte Bereiche mit Node.js über C++ löschen
linktitle: Benannte Bereiche löschen
type: docs
weight: 90
url: /de/nodejs-cpp/Delete-named-ranges/
description: Sie können lernen, wie man definierte Namen oder benannte Bereiche aus Excel oder OpenOffice Dateien mit Aspose.Cells for Node.js via C++ entfernt.
---

## **Einführung**
Wenn es zu viele definierte Namen oder benannte Bereiche in den Excel-Dateien gibt, müssen wir einige davon löschen, da sie nicht mehr referenziert werden.

## **Benannten Bereich in MS Excel entfernen**

Um einen benannten Bereich aus Excel zu entfernen, können Sie folgende Schritte befolgen:
1. Öffnen Sie Microsoft Excel und die Arbeitsmappe, die den benannten Bereich enthält.
2. Gehen Sie zum Register "Formeln" in der Excel-Menüleiste.
3. Klicken Sie auf die Schaltfläche "Namensmanager" in der Gruppe "Definierte Namen". Dadurch wird das Dialogfeld Namensmanager geöffnet.
4. Wählen Sie im Dialogfeld Namensmanager den benannten Bereich aus, den Sie entfernen möchten.
5. Klicken Sie auf die Schaltfläche "Löschen". Bestätigen Sie die Löschung beim Auffordern.
6. Klicken Sie auf die Schaltfläche "Schließen", um das Dialogfeld Namensmanager zu schließen.
7. Speichern Sie die Arbeitsmappe, um die Änderungen beizubehalten.

## **Löscht benannten Bereich mit Aspose.Cells for Node.js via C++**
Mit Aspose.Cells for Node.js via C++ können Sie benannte Bereiche oder definierte Namen über [Text](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) oder [Index](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) in der Liste entfernen.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Hinweis: Wenn der definierte Name sich auf Formeln bezieht, kann er nicht entfernt werden. Wir können nur die Formel des definierten Namens entfernen.

## **Einige benannte Bereiche entfernen**
Beim Entfernen eines definierten Namens müssen wir überprüfen, ob er von allen Formeln in der Datei referenziert wird.
Um die Leistung beim Entfernen benannter Bereiche zu verbessern, können wir einige gleichzeitig entfernen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Doppelte definierte Namen entfernen**
Einige Excel-Dateien sind beschädigt, weil einige definierte Namen doppelt vorhanden sind. Daher können wir diese doppelten Namen entfernen, um die Datei zu reparieren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



{{< app/cells/assistant language="nodejs-cpp" >}}
