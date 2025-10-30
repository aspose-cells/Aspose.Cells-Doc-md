---
title: XLS Datei mit Bildern oder Diagrammen in PDF mit Node.js via C++ umwandeln
linktitle: Konvertierung von XLS Datei mit Bildern oder Diagrammen in PDF
type: docs
weight: 50
url: /de/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien, die Bilder und Diagramme enthalten, in PDF-Dokumente. Aspose.Cells for Node.js via C++ kann eigenständig eine Tabelle in PDF umwandeln: Aspose.PDF für Node.js via C++ ist für die Konvertierung nicht erforderlich. Der Vorgang kann im Arbeitsspeicher durchgeführt werden, da er nicht von temporären oder Zwischen-XML-Dateien abhängt. Dies bedeutet, dass große Excel-Dateien, zum Beispiel mit Bildern, Diagrammen und anderen Zeichnungsobjekten, schnell und effizient konvertiert werden können.

{{% /alert %}} 
## **Beispielcode**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

Falls die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern in PDF aufzurufen. So werden formelabhängige Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
