---
title: Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells for Node.js via C++
linktitle: Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells
type: docs
weight: 350
url: /es/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aprende cómo renderizar caracteres suplementarios Unicode en el PDF de salida usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientra que los caracteres Unicode suplementarios tienen una longitud de 4 bytes. Ahora, Aspose.Cells admite la renderización de estos caracteres Unicode de 4 bytes.

En el Estándar de Caracteres Unicode, los Caracteres Suplementarios son los caracteres asignados a puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8 estos caracteres tienen cada uno una longitud de 4 bytes.
- En UTF-16 estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

## Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells for Node.js via C++

La siguiente captura muestra cómo Aspose.Cells renderizó el [archivo de Excel de origen](5115563.xlsx) en el [PDF de salida](5115564.pdf). Como puedes ver, los tres caracteres suplementarios Unicode se han renderizado exactamente igual que en Microsoft Excel.

![todo:image_alt_text](output.png)

## Código de Muestra

Puede usar este código de ejemplo para convertir [archivo de Excel fuente](5115563.xlsx) en [PDF de salida](5115564.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
