---
title: Deshacer bloqueo de filas o columnas con Node.js vía C++
linktitle: Descongelar paneles
type: docs
weight: 190
url: /es/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: En este artículo, aprenderás cómo desbloquear filas, columnas o paneles de hojas de cálculo de Excel programáticamente usando la API de Node.js con C++.
keywords: Desbloquear paneles, desbloquear filas, desbloquear columnas, deshacer bloqueo de ventana Node.js vía C++.
---

## **Introducción**

En este artículo, aprenderemos cómo desbloquear filas, columnas y paneles. Si las hojas en los archivos de Excel están congeladas, a veces queremos desbloquear la hoja o ajustar las filas, columnas o paneles congelados.


## **En Excel**

1. Haz clic en la pestaña Vista > Congelar paneles > Descongelar paneles.

**![descongelar paneles en Excel](Unfreeze-Panes.png)**




## **Desbloquear filas, columnas o paneles con Aspose.Cells for Node.js via C++**
Es simple desbloquear paneles con Aspose.Cells for Node.js via C++. Por favor, usa el método [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) para desbloquear paneles.

1. Construye el libro para abrir el archivo congelado.
2. Desbloquear paneles con el método Worksheet.unfreezePanes().
3. Guarda el archivo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Adjunto [archivo de Excel de origen de ejemplo](Frozen.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
