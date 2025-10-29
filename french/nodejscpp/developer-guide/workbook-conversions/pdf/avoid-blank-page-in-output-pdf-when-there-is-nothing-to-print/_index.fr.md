---
title: Évitez la page blanche dans le PDF de sortie lorsqu il n y a rien à imprimer avec Node.js via C++
linktitle: Éviter une page vierge dans le PDF de sortie lorsqu il n y a rien à imprimer
type: docs
weight: 30
url: /fr/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Apprenez comment éviter les pages blanches dans le PDF de sortie lorsqu il n y a rien à imprimer en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur l'enregistre en PDF en utilisant Aspose.Cells for Node.js via C++, il affiche une page blanche dans le PDF de sortie. Parfois, ce comportement par défaut est indésirable. Aspose.Cells fournit la propriété [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) pour gérer ce problème. Si vous la définissez sur **false**, une exception sera levée lorsqu'il n'y aura rien à imprimer dans le PDF de sortie.

## **Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée un classeur vide puis le sauvegarde en PDF après avoir défini la propriété [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) sur **false**. Étant donné qu'il n'y a rien à imprimer dans le PDF de sortie, l'exception se produit comme montré ci-dessous.

## **Code d'exemple**

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

## **Exception**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
