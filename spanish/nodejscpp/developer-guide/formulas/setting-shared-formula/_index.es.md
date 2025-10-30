---
title: Establecimiento de fórmula compartida con Node.js mediante C++
linktitle: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Si deseas agregar una función en una hoja de cálculo que realice algunos cálculos, este artículo explica cómo lograrlo usando Aspose.Cells for Node.js via C++.

{{% /alert %}}

## Establecer fórmula compartida usando Aspose.Cells for Node.js via C++

Supongamos que tienes una hoja de trabajo llena de datos con el formato que se muestra en la siguiente hoja de cálculo de ejemplo.

|Archivo de entrada con una columna de datos|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Quieres agregar una función en B2 que calculará el impuesto sobre las ventas para la primera fila de datos. El impuesto es del **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

Aspose.Cells te permite especificar una fórmula utilizando la propiedad [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--). Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, y así sucesivamente) en la columna.

O haga lo que hizo para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de la celda en consecuencia (A3*0.09, A4*0.09, A5*0.09 y así sucesivamente). Esto requiere que las referencias de celda para cada fila se actualicen. También requiere que Aspose.Cells analice cada fórmula individualmente, lo cual puede ser lento para hojas de cálculo grandes y fórmulas complejas. Además, agrega líneas adicionales de código, aunque los bucles pueden reducirlas en cierta medida.

Otro enfoque es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. El método [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
