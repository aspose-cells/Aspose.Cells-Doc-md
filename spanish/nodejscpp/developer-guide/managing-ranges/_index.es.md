---
title: Gestión de rangos con Node.js a través de C++
linktitle: Rangos
type: docs
weight: 105
url: /es/nodejs-cpp/managing-ranges/
description: Aprende cómo gestionar rangos en Excel usando Aspose.Cells for Node.js via C++. Crea rangos, establece valores, estilos y realiza varias operaciones.
---

## **Introducción**

En Excel, puedes seleccionar múltiples celdas con una selección de caja con ratón; el conjunto de celdas seleccionadas se llama "Rango".

Por ejemplo, puedes hacer clic con el botón izquierdo del ratón en la celda "A1" de Excel y luego arrastrar hasta la celda "C4". La área rectangular que seleccionaste también puede ser creada fácilmente como un objeto usando Aspose.Cells for Node.js via C++.

Aquí tienes cómo crear un rango, poner un valor, establecer un estilo y realizar más operaciones en el objeto "Rango".

## **Gestión de rangos usando Aspose.Cells for Node.js via C++**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite el acceso a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

### **Crear rango**

Cuando quieras crear un área rectangular que se extienda sobre A1:C4, puedes usar el siguiente código:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Poner valor en las celdas del rango**

Digamos que tienes un rango de celdas que se extiende sobre A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

El siguiente ejemplo muestra cómo introducir algunos valores en las celdas del rango.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Establecer estilo de las celdas del rango**

El ejemplo siguiente muestra cómo establecer el estilo de las celdas del rango.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Obtener la región actual del rango**

CurrentRegion es una propiedad que devuelve un objeto Range que representa la región actual. 

La región actual es un rango delimitado por cualquier combinación de filas y columnas en blanco. Solo lectura.

En Excel, puedes obtener el área de CurrentRegion mediante:
1. Selecciona un área (rango1) con el cuadro del ratón.
2. Haz clic en "Inicio - Edición - Buscar y Seleccionar - Ir a especial - Región actual", o usa "Ctrl+Shift+*", verás que Excel te ayuda automáticamente a seleccionar un área (rango2). Ahora lo has logrado, rango2 es la RegiónActual de rango1.

Por favor, descarga el siguiente archivo de prueba, ábrelo en Excel, usa el cuadro del ratón para seleccionar un área "A1:D7", luego presiona "Ctrl+Shift+*", verás que el área "A1:C3" está seleccionada.

[current_region.xlsx](current_region.xlsx)

Ahora por favor ejecuta el siguiente ejemplo para ver cómo funciona en Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Temas avanzados**
- [Rango de AutoFill del archivo de Excel](/cells/es/nodejs-cpp/autofill-ranges/)
- [Copiar rangos de Excel](/cells/es/nodejs-cpp/copy-ranges-of-Excel/)
- [Copiar solo datos de rango](/cells/es/nodejs-cpp/copy-range-data-only/)
- [Copiar datos de rango con estilo](/cells/es/nodejs-cpp/copy-range-data-with-style/)
- [Copiar solo estilo de rango](/cells/es/nodejs-cpp/copy-range-style-only/)
- [Crear rango de unión](/cells/es/nodejs-cpp/create-union-range/)
- [Cortar y pegar rango](/cells/es/nodejs-cpp/cut-and-paste-cells/)
- [Eliminar rangos](/cells/es/nodejs-cpp/delete-ranges-from-Excel/)
- [Obtener dirección Celda Contar Desplazamiento Toda la columna y Toda la fila del Rango](/cells/es/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insertar rangos](/cells/es/nodejs-cpp/insert-ranges-to-Excel/)
- [Combinar o dividir rango de celdas](/cells/es/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Mover rango de celdas en una hoja de cálculo](/cells/es/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Crear rangos con nombre con ámbito de libro de trabajo y hoja de cálculo](/cells/es/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Buscar y reemplazar datos en un rango](/cells/es/nodejs-cpp/search-and-replace-data-in-a-range/)
