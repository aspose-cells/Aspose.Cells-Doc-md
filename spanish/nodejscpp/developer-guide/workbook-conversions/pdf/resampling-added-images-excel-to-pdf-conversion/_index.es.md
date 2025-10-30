---
title: Agregando imágenes con remuestreo  Conversión de Excel a PDF con Node.js vía C++
linktitle: Resampling Added Images
type: docs
weight: 150
url: /es/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aprende cómo comprimir las imágenes añadidas en archivos Excel para reducir el tamaño del PDF y mejorar el rendimiento de conversión usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Al trabajar con archivos grandes de Microsoft Excel con muchas imágenes, puede que necesites comprimir las imágenes que se hayan añadido para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento general de la conversión. Aspose.Cells for Node.js via C++ soporta el resampling de las imágenes añadidas para reducir el tamaño del archivo PDF de salida y mejorar el rendimiento en cierta medida.

{{% /alert %}}

Consulte el siguiente código de ejemplo que describe cómo realizar la tarea utilizando la API de Aspose.Cells. El ejemplo convierte un archivo de Microsoft Excel a un archivo PDF mientras comprime las imágenes en el archivo.

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

Usar la [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) opción minimiza el tamaño del PDF de salida, pero puede afectar un poco la calidad de la imagen.

{{% /alert %}} {{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
