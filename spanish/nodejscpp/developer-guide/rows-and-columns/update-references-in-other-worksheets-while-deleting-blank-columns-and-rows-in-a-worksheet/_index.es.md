---
title: Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo
linktitle: Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo
type: docs
weight: 5000
url: /es/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Aprenda cómo mantener las referencias en otras hojas de cálculo al eliminar columnas y filas vacías en una hoja usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Cuando eliminas columnas y filas en blanco en una hoja de cálculo, sus referencias en otras hojas de cálculo se vuelven inválidas. Si deseas evitar este comportamiento y que esas referencias de la hoja de cálculo actual en otras hojas de cálculo también se actualicen, entonces por favor utiliza la propiedad [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) y configúrala como **true**.

{{% /alert %}}

## **Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo**

Por favor, vea el siguiente código de ejemplo y su salida en consola. La celda E3 en la segunda hoja tiene una fórmula =Sheet1!C3 que hace referencia a la celda C3 en la primera hoja. Si establece la propiedad [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) como **true**, esta fórmula será actualizada y se convertirá en =Sheet1!A1 al eliminar columnas y filas vacías en la primera hoja. Sin embargo, si establece la propiedad [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) como **false**, la fórmula en la celda E3 de la segunda hoja permanecerá como =Sheet1!C3 y será inválida.

### **Ejemplo de Programación**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add second sheet with name Sheet2
wb.getWorksheets().add("Sheet2");

// Access first sheet and add some integer value in cell C1
// Also add some value in any cell to increase the number of blank rows and columns
const sht1 = wb.getWorksheets().get(0);
sht1.getCells().get("C1").putValue(4);
sht1.getCells().get("K30").putValue(4);

// Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
const sht2 = wb.getWorksheets().get(1);
sht2.getCells().get("E3").setFormula("'Sheet1'!C1");

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
console.log("Cell E3 before deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());

// If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
const opts = new AsposeCells.DeleteOptions();
opts.setUpdateReference(true);

// Delete all blank rows and columns with delete options
sht1.getCells().deleteBlankColumns(opts);
sht1.getCells().deleteBlankRows(opts);

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
console.log("");
console.log("");
console.log("Cell E3 after deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());
```

### **Salida de la consola**

Esta es la salida de consola del código de ejemplo anterior cuando la propiedad [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) ha sido establecida como **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Esta es la salida de consola del código de ejemplo anterior cuando la propiedad [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) ha sido establecida como **false**. Como puede ver, la fórmula en la celda E3 de la segunda hoja no se actualiza y su valor de celda ahora es 0 en lugar de 4, lo cual es inválido.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
