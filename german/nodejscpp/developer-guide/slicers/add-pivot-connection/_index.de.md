---
title: Pivot Verbindung mit Node.js via C++ hinzufügen
linktitle: Pivot Verbindung hinzufügen
type: docs
weight: 30
url: /de/nodejs-cpp/add-pivot-connection/
description: Erfahren Sie, wie Sie eine Pivot Verbindung mit Aspose.Cells for Node.js via C++ hinzufügen.
keywords: Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365 mit Node.js via C++ hinzufügen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Slicer und eine Pivot-Tabelle in Excel verknüpfen möchten, klicken Sie mit der rechten Maustaste auf den Slicer und wählen Sie „Berichtverbindungen...“. In der Optionenliste können Sie die Kontrollkästchen aktivieren. Bitte verwenden Sie auch die Methode [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-), um eine Slicer mit einer Pivot-Tabelle programmgesteuert mit der Aspose.Cells API zu verknüpfen.

## **Slicer und PivotTable verknüpfen**

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](add-pivot-connection.xlsx), die einen vorhandenen Slicer enthält. Es greift auf den Slicer zu und verknüpft ihn mit der Pivot-Tabelle. Abschließend wird die Arbeitsmappe als [Ausgabedatei](add-pivot-connection-out.xlsx) gespeichert.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
