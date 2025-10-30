---
title: Rendern von Office Add Ins beim Konvertieren von Excel zu PDF mit Node.js via C++
linktitle: Office Add Ins beim Konvertieren von Excel in PDF rendern
type: docs
weight: 100
url: /de/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Mögliche Verwendungsszenarien**

Früher konnte Aspose.Cells Office-Add-Ins beim Speichern einer Excel-Datei in PDF-Format nicht rendern. Jetzt funktioniert es einwandfrei. Es sind keine speziellen Methoden oder Eigenschaften erforderlich, um Office-Add-Ins im Ausgabe-PDF zu rendern. Speichern Sie einfach Ihre Excel-Datei im PDF-Format, und die Office-Add-Ins werden gerendert.

## **Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen**

Das folgende Beispiel speichert die [Beispiel-Excel-Datei](60489769.xlsx), die Office-Add-Ins enthält. Bitte sehen Sie sich das [Ausgabe-PDF, das mit der früheren Version (z.B. 17.11) generiert wurde](60489770.pdf), und das [Ausgabe-PDF, das mit der neueren Version (z.B. 17.12 und später) erstellt wurde](60489771.pdf). Das Ausgabe-PDF der vorherigen Version ist Leer, während das neuere eine Office-Add-In anzeigt.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
