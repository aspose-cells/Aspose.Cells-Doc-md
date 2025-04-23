---
title: Ocultar la visualización de valores cero en la hoja de cálculo con Node.js a través de C++
linktitle: Ocultar la visualización de los valores cero en la hoja de cálculo
type: docs
weight: 50
url: /es/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Este artículo te mostrará código de ejemplo que explica cómo ocultar programáticamente los valores cero en una hoja de Excel usando la biblioteca Node.js a través de C++.
keywords: Ocultar valores cero en la hoja de Excel en Node.js a través de C++
---

{{% alert color="primary" %}} 

A veces, es necesario ocultar los valores cero en una hoja de cálculo. Puede ser una preferencia personal o un estándar de formato.

{{% /alert %}} 

Para ocultar los valores cero en una hoja de cálculo en Microsoft Excel (por ejemplo, Microsoft Excel 2003):

1. Desde el menú **Herramientas**, seleccione **Opciones**, y luego seleccione la pestaña **Ver**.
1. Desmarque la opción **Valores de cero**.
1. Haz clic en **Aceptar**.

Por favor, mira el siguiente código de ejemplo que demuestra cómo ocultar ceros usando Aspose.Cells for Node.js via C++.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
