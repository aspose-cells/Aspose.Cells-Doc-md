---
title: Evitar página en blanco en PDF de salida cuando no hay nada que imprimir con Node.js a través de C++
linktitle: Evitar Página en Blanco en el PDF de Salida cuando no hay Nada que Imprimir
type: docs
weight: 30
url: /es/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aprende cómo evitar páginas en blanco en PDF de salida cuando no hay nada que imprimir usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Cuando el archivo de Excel está vacío y el usuario lo guarda como PDF usando Aspose.Cells for Node.js via C++, se renderiza una página en blanco en el PDF de salida. A veces, este comportamiento predeterminado no es deseable. Aspose.Cells proporciona la propiedad [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) para manejar este problema. Si la configuras en **false**, entonces ocurrirá una excepción cuando no haya nada que imprimir en el PDF de salida.

## **Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir**

El siguiente ejemplo de código crea un libro vacío y luego lo guarda como PDF tras configurar la propiedad [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) en **false**. Como no hay nada que imprimir en el PDF de salida, ocurre la excepción como se muestra abajo.

## **Código de muestra**

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

## **Excepción**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
