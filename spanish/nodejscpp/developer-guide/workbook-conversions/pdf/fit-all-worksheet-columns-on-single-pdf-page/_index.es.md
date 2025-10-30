---
title: Ajustar todas las columnas de la hoja en una sola página de PDF con Node.js a través de C++
linktitle: Ajustar todas las columnas de la hoja de trabajo en una sola página de PDF
type: docs
weight: 160
url: /es/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

A veces deseas generar un archivo PDF que ajuste todas las columnas de una hoja de trabajo en una sola página. La propiedad [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) proporciona esta función de una manera muy fácil de usar. Los cálculos complejos como la altura y el ancho del PDF de salida se manejan internamente y se basan en los datos de la hoja de trabajo.

{{% /alert %}}

## **Ajustar las columnas de la hoja de trabajo en una sola página de PDF**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) asegura que todas las columnas de una hoja de cálculo se rendericen en una sola página de PDF, aunque las filas puedan expandirse en varias páginas dependiendo de los datos en la hoja.

El código de muestra a continuación muestra cómo utilizar la propiedad [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) para representar una hoja de cálculo grande de 100 columnas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

Cuando una hoja de trabajo determinada tiene muchas columnas, el archivo PDF generado puede mostrar el contenido en un tamaño muy pequeño. Aún será legible cuando se amplíe en una aplicación de visualización como Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
