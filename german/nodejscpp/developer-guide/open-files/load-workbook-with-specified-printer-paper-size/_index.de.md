---  
title: Laden einer Arbeitsmappe mit gesetzter Printer Papiergröße mit Node.js und C++  
linktitle: Arbeitsbuch mit spezifischer Druckerpapiergröße laden  
type: docs  
weight: 430  
url: /de/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Erfahren Sie, wie Sie die Papiergröße des Druckers beim Laden einer Arbeitsmappe mit Aspose.Cells for Node.js via C++ festlegen.  
---  

{{% alert color="primary" %}}  
Sie können die Druckerpapiergröße Ihrer Wahl beim Laden Ihres Arbeitsbuches mit der [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-)-Methode angeben. Bitte beachten Sie, wenn Sie eine neue Datei in MS Excel erstellen, finden Sie die Papiergröße ist dieselbe wie die Einstellung des Standarddruckers in Ihrem Gerät.  
{{% /alert %}}  

Der folgende Beispielcode zeigt die Verwendung der Methode [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Zuerst wird eine Arbeitsmappe erstellt, dann in einem Speicher-Stream im XLSX-Format gespeichert. Anschließend wird sie mit A5-Papiergröße geladen und im PDF-Format gespeichert. Dann wird sie erneut mit A3-Papiergröße geladen und erneut im PDF-Format gespeichert. Wenn Sie die Ausgabedateien öffnen und die Papiergrößen überprüfen, sehen Sie, dass sie unterschiedlich sind. Eine ist A5, die andere A3. Bitte laden Sie die [A5-Ausgabedatei](5115234.pdf) und die [A3-Ausgabedatei](5115233.pdf), die vom Code generiert wurden, für Ihren Vergleich herunter.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
