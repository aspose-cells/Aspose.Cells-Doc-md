---
title: Leer hojas de cálculo numéricas desarrolladas por Apple Inc. usando Aspose.Cells for Node.js via C++
linktitle: Leer Hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells
type: docs
weight: 140
url: /es/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Aprenda cómo leer hojas de cálculo de Numbers desarrolladas por Apple Inc. usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Numbers es una aplicación de hoja de cálculo desarrollada por Apple Inc. Aspose.Cells puede leer hojas de cálculo de Numbers, pero no soporta escribir en ellas. Puede leer datos, estilos y fórmulas de hojas de cálculo de Numbers.

## **Leer hoja de cálculo de Números desarrollada por Apple Inc. usando Aspose.Cells for Node.js via C++**

El siguiente código de ejemplo carga la [Hoja de cálculo de Números de muestra](sampleNumbersByAppleInc.numbers) y la convierte en [Formato PDF de salida](outputNumbersByAppleInc.pdf). Tendrás que usar la clase [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) y especificar [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) como parámetro en su constructor para cargarla correctamente. Por favor, descarga ambos desde los enlaces proporcionados. Puedes probar el código con cualquier hoja de cálculo de Numbers. También lee los comentarios del código para más ayuda.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

