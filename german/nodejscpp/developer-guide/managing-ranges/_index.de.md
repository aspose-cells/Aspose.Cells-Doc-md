---
title: Verwaltung von Bereichen mit Node.js über C++
linktitle: Bereiche
type: docs
weight: 105
url: /de/nodejs-cpp/managing-ranges/
description: Erfahren Sie, wie Sie Bereiche in Excel mit Aspose.Cells for Node.js via C++ verwalten. Erstellen Sie Bereiche, setzen Sie Werte, Stile und führen Sie verschiedene Operationen aus.
---

## **Einführung**

In Excel können Sie mehrere Zellen mit einer Mausschablon-Auswahl auswählen; die Menge der ausgewählten Zellen wird als "Bereich" bezeichnet.

Zum Beispiel können Sie in Excel mit der linken Maustaste in Zelle "A1" klicken und dann bis zu Zelle "C4" ziehen. Der rechteckige Bereich, den Sie ausgewählt haben, kann ebenfalls einfach als Objekt erstellt werden mit Aspose.Cells for Node.js via C++.

Hier ist beschrieben, wie man einen Bereich erstellt, Werte eingibt, einen Stil setzt und weitere Operationen auf dem "Range"-Objekt durchführt.

## **Verwaltung von Bereichen mit Aspose.Cells for Node.js via C++**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung.

### **Bereich erstellen**

Wenn Sie einen rechteckigen Bereich erstellen möchten, der über A1:C4 reicht, können Sie den folgenden Code verwenden:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Wert in die Zellen des Bereichs eingeben**

Angenommen, Sie haben einen Zellenbereich, der sich über A1:C4 erstreckt. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequenziell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0], Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Das folgende Beispiel zeigt, wie man einige Werte in die Zellen des Bereichs eingibt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Stellen Sie den Stil der Zellen des Bereichs ein**

Das folgende Beispiel zeigt, wie man den Stil der Zellen im Bereich festlegt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Aktuelles Gebiet des Bereichs erhalten**

CurrentRegion ist eine Eigenschaft, die ein Range-Objekt zurückgibt, das die aktuelle Region darstellt. 

Die aktuelle Region ist ein Bereich, der durch eine beliebige Kombination von leeren Zeilen und leeren Spalten begrenzt ist. Schreibgeschützt.

In Excel können Sie den CurrentRegion-Bereich durch folgende Methode erhalten:
1. Wählen Sie einen Bereich (range1) mit der Mausschablon aus.
2. Klicken Sie auf "Start - Bearbeiten - Suchen & Auswählen - Gehe zu Spezial - Aktuelle Region" oder verwenden Sie "Strg+Shift+*". Sie sehen, wie Excel automatisch einen Bereich (Bereich2) auswählt. Jetzt haben Sie es gemacht, Bereich2 ist die Aktuelle Region von Bereich1.

Bitte laden Sie die folgende Testdatei herunter, öffnen Sie sie in Excel, wählen Sie mit der Maus den Bereich "A1:D7" aus und klicken Sie dann auf "Strg+Shift+*". Sie werden sehen, dass der Bereich "A1:C3" ausgewählt ist.

[current_region.xlsx](current_region.xlsx)

Führen Sie nun das folgende Beispiel aus, um zu sehen, wie es in Aspose.Cells funktioniert:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Erweiterte Themen**
- [Autofüllbereich der Excel-Datei](/cells/de/nodejs-cpp/autofill-ranges/)
- [Bereiche von Excel kopieren](/cells/de/nodejs-cpp/copy-ranges-of-Excel/)
- [Nur Datenbereich kopieren](/cells/de/nodejs-cpp/copy-range-data-only/)
- [Datenbereich mit Stil kopieren](/cells/de/nodejs-cpp/copy-range-data-with-style/)
- [Nur Bereichsstil kopieren](/cells/de/nodejs-cpp/copy-range-style-only/)
- [Union Range erstellen](/cells/de/nodejs-cpp/create-union-range/)
- [Bereich ausschneiden und einfügen](/cells/de/nodejs-cpp/cut-and-paste-cells/)
- [Bereiche löschen](/cells/de/nodejs-cpp/delete-ranges-from-Excel/)
- [Adresse, Zellenanzahl, Versatz, Gesamte Spalte und Gesamte Zeile des Bereichs abrufen](/cells/de/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Bereiche einfügen](/cells/de/nodejs-cpp/insert-ranges-to-Excel/)
- [Zellbereich zusammenführen oder trennen](/cells/de/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Bereich von Zellen in einem Arbeitsblatt verschieben](/cells/de/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Arbeitsbuch- und arbeitsblattübergreifende benannte Bereiche erstellen](/cells/de/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Suchen und Ersetzen von Daten in einem Bereich](/cells/de/nodejs-cpp/search-and-replace-data-in-a-range/)
