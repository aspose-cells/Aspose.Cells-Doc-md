---
title: Evita pagine bianche nel PDF di output quando non c è nulla da stampare con Node.js tramite C++
linktitle: Evitare Pagina Vuota nel PDF di Output quando non c è Nulla da Stampare
type: docs
weight: 30
url: /it/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Scopri come evitare pagine bianche nel PDF di output quando non c è nulla da stampare usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Quando il file Excel è vuoto e l'utente lo salva come PDF usando Aspose.Cells for Node.js via C++, si verifica una pagina bianca nel PDF di output. A volte, questo comportamento predefinito è indesiderato. Aspose.Cells fornisce la proprietà [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) per gestire questo problema. Se la imposti su **false**, si verificherà un'eccezione ogni volta che non c'è nulla da stampare nel PDF di output.

## **Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare**

Il seguente esempio di codice crea un workbook vuoto e lo salva come PDF impostando la proprietà [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) su **false**. Poiché non c'è nulla da stampare nel PDF di output, si verifica l'eccezione come mostrato di seguito.

## **Codice di Esempio**

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

## **Eccezione**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
