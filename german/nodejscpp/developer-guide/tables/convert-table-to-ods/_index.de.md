---  
title: Tabelle in ODS mit Node.js über C++ konvertieren  
linktitle: Tabelle in ODS konvertieren  
type: docs  
weight: 70  
url: /de/nodejs-cpp/convert-table-to-ods/  
description: Erfahren Sie, wie Sie eine Excel Datei mit Tabelle in das ODS Format mit Aspose.Cells for Node.js via C++ konvertieren.  
---  

Aspose.Cells unterstützt die Konvertierung einer Excel-Datei mit einer Tabelle in das ODS-Format. Sie müssen die Datei nur im ODS-Format speichern, und die generierte ODS-Datei wird eine funktionierende Tabelle enthalten.

## Beispielcode

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

Die Ausgabedatei ODS, die durch den Beispielcode generiert wurde, ist im Anhang zu Ihrer Referenz.

[**Output ODS File**](ConvertTableToOds_out.ods)  

