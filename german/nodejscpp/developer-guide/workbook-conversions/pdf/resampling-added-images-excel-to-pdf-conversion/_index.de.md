---
title: Resampling hinzugefügter Bilder – Excel in PDF Konvertierung mit Node.js über C++
linktitle: Resampling hinzugefügter Bilder
type: docs
weight: 150
url: /de/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie Bilder, die in Excel Dateien eingefügt wurden, komprimieren, um die PDF Größe zu reduzieren und die Konvertierungsleistung mit Aspose.Cells for Node.js via C++ zu verbessern.
---

{{% alert color="primary" %}}

 Bei der Arbeit mit großen Microsoft Excel-Dateien mit vielen Bildern müssen Sie möglicherweise eingefügte Bilder komprimieren, um die Ausgabedateigröße zu verringern und die Gesamtleistung der Konvertierung zu verbessern. Aspose.Cells for Node.js via C++ unterstützt Resampling eingefügter Bilder, um die Ausgabedateigröße zu verringern und die Leistung etwas zu verbessern.

{{% /alert %}}

Bitte beachten Sie den folgenden Beispiellcode, der beschreibt, wie die Aufgabe mithilfe der Aspose.Cells-API ausgeführt wird. Das Beispiel konvertiert eine Microsoft Excel-Datei in eine PDF-Datei und komprimiert dabei die Bilder in der Datei.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

Die Verwendung der [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-)-Option minimiert die Größe der Ausgabedatei, kann aber die Bildqualität etwas beeinträchtigen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
