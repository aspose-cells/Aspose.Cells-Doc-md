---
title: Autoajustar la altura de fila automáticamente al cargar un archivo con Node.js vía C++
linktitle: Ajustar automáticamente la altura de la fila cuando se carga el archivo
type: docs
weight: 120
url: /es/nodejs-cpp/autofit-row-height/
description: Aprenda cómo ajustar automáticamente la altura de filas cuyo tamaño no está personalizado al cargar un archivo usando Aspose.Cells for Node.js via C++.
keywords: Autoajustar la altura de fila al cargar un archivo Node.js vía C++, ajustando automáticamente la altura de fila al abrir un archivo de Excel con Node.js vía C++ 
---

## **Escenarios de uso posibles**
La altura de la fila se ajusta automáticamente para coincidir con la fuente del contenido, pero cuando la altura de la fila almacenada en caché no coincide con la altura del contenido en el archivo, MS Excel ajustará automáticamente la altura de la fila al cargar el archivo, mientras que Aspose.Cells for Node.js via C++ no lo hará automáticamente para mejorar el rendimiento. Si necesita usar el programa Aspose.Cells para ajustar automáticamente las alturas de línea al cargar archivos, puede lograrlo mediante el parámetro [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) en su código.

Por favor, consulte la siguiente imagen. Observamos que la altura de fila almacenada en caché en la línea 11 es 15, pero Excel ajustó automáticamente la altura de la fila al cargar el archivo.
<br>
<img src="1.png" width=70% />

## **Ajustar la altura de fila usando Aspose.Cells for Node.js via C++**
Si carga el archivo directamente y lo guarda en PDF, los datos no se mostrarán completamente en el PDF porque su altura en caché es solo 15.
<br>
<img src="2.png" width=70% />
<br>
Si establece el parámetro [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) en verdadero al cargar el archivo, Aspose.Cells ajustará automáticamente la altura de la fila. La altura ajustada puede cumplir eficazmente los requisitos de visualización del texto.
<br>
<img src="3.png" width=70% />

## **Código de ejemplo en Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
