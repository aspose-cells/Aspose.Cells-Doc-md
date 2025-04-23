---
title: División de la vista en Excel con Node.js vía C++
linktitle: Pantalla dividida
type: docs
weight: 190
url: /es/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: En este artículo, aprenderás cómo mostrar ciertas filas y/o columnas en paneles separados dividiendo la hoja en dos o cuatro partes programáticamente usando Node.js C++ Addon.
keywords: Congelar filas superiores, Congelar fila superior.
---

## **Introducción**

En este artículo, aprenderemos cómo mostrar en paneles separados ciertas filas y/o columnas dividiendo la hoja de cálculo en dos o cuatro partes. Cuando se trabaja con conjuntos de datos grandes, necesitamos ver algunas áreas de la misma hoja de cálculo a la vez para comparar diferentes subconjuntos de datos. La función de pantalla dividida puede satisfacer sus necesidades.

## **Cómo dividir la pantalla en Excel**
Para dividir una hoja de cálculo en dos o cuatro partes, haz lo siguiente:

1. Selecciona la fila/columna/celda antes de la cual deseas colocar la división.
2. En la pestaña de Vista, en el grupo de Ventanas, haz clic en el botón Dividir.

**![Pantalla dividida](Split-Screen.png)**

## **Dividir la hoja de cálculo verticalmente en columnas**

Para separar dos áreas de la hoja de cálculo verticalmente, selecciona la columna a la derecha de la columna donde deseas que aparezca la división y haz clic en el botón Dividir en Excel.

Es fácil dividir la hoja de cálculo verticalmente en columnas programáticamente con Aspose.Cells for Node.js via C++, solo necesitamos seleccionar una celda en la fila superior como celda activa, luego dividir con [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Dividir la hoja de cálculo horizontalmente en filas**
Para separar tu ventana de Excel horizontalmente, selecciona la fila debajo de la fila donde deseas que ocurra la división en Excel.

Es fácil dividir la hoja horizontalmente en filas programáticamente con Aspose.Cells for Node.js via C++, solo necesitamos seleccionar una celda en la columna izquierda como celda activa, luego dividir con [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Dividir la hoja de cálculo en cuatro partes**
Para ver cuatro secciones diferentes de la misma hoja de cálculo simultáneamente, divide tu pantalla tanto vertical como horizontalmente en Excel.

Es fácil dividir la hoja verticalmente en columnas programáticamente con Aspose.Cells for Node.js via C++, solo necesitamos seleccionar una celda que no esté en la primera fila y columna como celda activa, luego dividir con [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **Cómo quitar la división**
Para eliminar la división de la hoja de cálculo, simplemente haz clic en el botón Dividir nuevamente.

Aspose.Cells for Node.js via C++ proporciona un método [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) para eliminar la configuración de división.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

