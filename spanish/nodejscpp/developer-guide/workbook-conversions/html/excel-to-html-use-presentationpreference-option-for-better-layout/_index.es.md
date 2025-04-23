---
title: Excel a HTML  Usa la opción PresentationPreference para mejor disposición con Node.js a través de C++
linktitle: De Excel a HTML  Usa la Opción PresentationPreference para un Mejor Diseño
type: docs
weight: 220
url: /es/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells ofrece la propiedad HtmlSaveOptions.presentationPreference, útil para desarrolladores que necesitan un mejor diseño al guardar un archivo de Excel en HTML o formato MHT. Su valor predeterminado es false. Recomendamos configurarla en true para una presentación más atractiva de los informes de Excel.

{{% /alert %}} 

Consulta el código de ejemplo a continuación que demuestra cómo renderizar un archivo HTML desde un informe de Excel con preferencia de presentación activada.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
