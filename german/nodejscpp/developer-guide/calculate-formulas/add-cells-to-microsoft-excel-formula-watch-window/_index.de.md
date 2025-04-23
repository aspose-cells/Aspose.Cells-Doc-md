---
title: Zellen mit Node.js via C++ zum Microsoft Excel Formelüberwachungsfenster hinzufügen
linktitle: Zellen zur Microsoft Excel Formelüberwachung hinzufügen
description: So verwenden Sie die Aspose.Cells Bibliothek, um Zellen mit Node.js via C++ zum Formelüberwachungsfenster in Excel hinzuzufügen. Öffnen oder erstellen Sie eine Excel Datei, manipulieren Sie die Zellen und setzen Sie Formeln. Schließlich speichern wir die geänderte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Formelüberwachungsfenster, Zellen, Hinzufügen, Node.js via C++
type: docs
weight: 60
url: /de/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Mögliche Verwendungsszenarien**

Das Microsoft Excel Überwachungsfenster ist ein nützliches Tool, um Zellwerte und -formeln bequem in einem Fenster zu beobachten. Sie können das *Watch Window* in Microsoft Excel öffnen, indem Sie auf *Formeln > Überwachung > Überwachungsfenster* klicken. Es gibt einen *Überwachung hinzufügen*-Button, um Zellen zur Inspektion hinzuzufügen. Ebenso können Sie die Methode [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) verwenden, um Zellen mithilfe der Aspose.Cells API in das *Watch Window* hinzuzufügen.

## **Zellen zur Microsoft Excel-Formelüberwachung hinzufügen**

Das folgende Beispiel setzt die Formel der Zellen C1 und E1 und fügt beide im Überwachungsfenster hinzu. Anschließend wird die Arbeitsmappe als [Ausgabedatei für Excel](67338481.xlsx) gespeichert. Wenn Sie die Ausgabedatei öffnen und das *Watch Window* anzeigen, sehen Sie beide Zellen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
