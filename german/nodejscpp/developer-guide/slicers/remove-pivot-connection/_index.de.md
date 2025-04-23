---
title: Entfernen der Pivot Verbindung mit Node.js über C++
linktitle: Pivot Verbindung entfernen
type: docs
weight: 30
url: /de/nodejs-cpp/remove-pivot-connection/
description: Erfahren Sie, wie Sie die Pivot Verbindung mit Aspose.Cells for Node.js via C++ entfernen.
keywords: Entfernen der Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365 Node.js über C++.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer und eine Pivot-Tabelle in Excel trennen möchten, klicken Sie mit der rechten Maustaste auf den Slicer und wählen Sie "Bericht Verbindungen...". In der Optionsliste können Sie die Checkbox aktivieren oder deaktivieren. Wenn Sie einen Slicer und eine Pivot-Tabelle programmatisch mit der Aspose.Cells API trennen möchten, verwenden Sie bitte die [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-)-Methode. Dadurch wird der Slicer und die Pivot-Tabelle getrennt.

## **Slicer und Pivot-Tabelle dissoziieren**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](remove-pivot-connection.xlsx), die einen bestehenden Slicer enthält. Er greift auf die Slicer zu und trennt dann den Slicer von der Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabedatei Excel](remove-pivot-connection-out.xlsx).

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
