---
title: Cálculo de fórmula de matriz de tablas de datos con Node.js vía C++
linktitle: Cálculo de la fórmula de arreglo de tablas de datos
description: Cómo usar la biblioteca Aspose.Cells para calcular fórmulas de matriz para una tabla de datos en Microsoft Excel usando Node.js vía C++. Carga o crea un archivo de Excel, calcula la fórmula de matriz y guarda el archivo modificado.
keywords: Aspose.Cells, Excel, tablas de datos, fórmulas de matriz, cálculos Node.js vía C++
type: docs
weight: 70
url: /es/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Puedes crear una Tabla de Datos en Microsoft Excel usando Datos > Análisis de hipótesis > Tabla de datos... Ahora Aspose.Cells te permite calcular la fórmula de matriz de una tabla de datos. Por favor, usa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) como normal para calcular cualquier tipo de fórmulas.

{{% /alert %}}

En el siguiente código de ejemplo, usamos el [archivo de Excel de origen](5115535.xlsx). Si cambia el valor de la celda B1 a 100, los valores de la tabla de datos que están llenos con color amarillo se convertirán en 120 como se muestra en las siguientes imágenes. El código de ejemplo genera el [PDF de salida](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

A continuación se muestra el código de ejemplo utilizado para generar el [PDF de salida](5115538.pdf) a partir del [archivo de Excel de origen](5115535.xlsx). Por favor, lea los comentarios para más información.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
