---
title: Dokumentenstruktur beim Konvertieren in PDF mit Node.js via C++ exportieren
linktitle: Exportieren der Dokumentstruktur beim Konvertieren in PDF
type: docs
weight: 360
url: /de/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Erfahren Sie, wie Sie die Dokumentenstruktur beim Konvertieren einer Excel Datei in ein getaggtes PDF mit Aspose.Cells for Node.js via C++ exportieren. 
---

Die Funktionalitäten der PDF-Logikstruktur bieten einen Mechanismus, um Informationen über die Dokumentenstruktur in eine PDF-Datei einzubinden. Aspose.Cells for Node.js via C++ bewahrt Informationen über die Struktur eines Microsoft Excel-Dokuments, wie Zellen, Zeilen, Tabellen, Arbeitsblätter, Bilder, Formen, Kopf- und Fußzeilen usw.

Mit der Option [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) können Sie in eine markierte PDF mit exportierter Dokumentenstruktur speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
