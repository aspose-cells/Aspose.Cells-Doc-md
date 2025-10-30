---
title: Leeren Seite im Ausgabepdf vermeiden, wenn nichts zu drucken ist mit Node.js via C++
linktitle: Leere Seite im Ausgabe PDF vermeiden, wenn nichts gedruckt werden soll
type: docs
weight: 30
url: /de/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Lernen Sie, wie Sie leere Seiten im Ausgabepdf vermeiden, wenn nichts zum Drucken vorhanden ist, mit Aspose.Cells for Node.js via C++.
---

## **Mögliche Verwendungsszenarien**

 Wenn die Excel-Datei leer ist und der Benutzer sie mit Aspose.Cells for Node.js via C++ in PDF speichert, wird eine leere Seite im Ausgabepdf gerendert. Dieses Standardverhalten ist manchmal unerwünscht. Aspose.Cells bietet die [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--)-Eigenschaft, um dieses Problem zu beheben. Wenn Sie sie auf **false** setzen, tritt eine Ausnahme auf, wann immer nichts zum Drucken im PDF vorhanden ist.

## **Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll**

 Das folgende Beispiel erstellt eine leere Arbeitsmappe und speichert sie dann als PDF, nachdem die [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--)-Eigenschaft auf **false** gesetzt wurde. Da im Ausgabepdf nichts gedruckt werden kann, tritt die Ausnahme wie unten gezeigt auf.

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **Ausnahme**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
