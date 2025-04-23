---  
title: Jedes Arbeitsblatt in eine separate PDF Datei speichern mit Node.js über C++  
linktitle: Jede Arbeitsblatt in eine separate PDF Datei speichern  
type: docs  
weight: 130  
url: /de/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for Node.js via C++ kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren, und Sie müssen dafür nicht Aspose.PDF für Node.js über C++ verwenden. Die Konvertierung erfordert keine Software, um temporäre Dateien zu erstellen oder zu verwenden, da der gesamte Vorgang im Arbeitsspeicher erfolgen kann.  
{{% /alert %}}  

## **Jedes Arbeitsblatt in eine separate PDF-Datei speichern**  
Wenn Sie jede Tabelle in Ihrer Vorlage-Exceldatei in verschiedene PDF-Dateien speichern möchten, können Sie dies einfach erreichen. Versuchen Sie, einen Tabellenindex mit [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet)-Option festzulegen, um diese in PDF zu rendern.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.  
{{% /alert %}}  

