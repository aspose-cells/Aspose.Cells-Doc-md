---
title: Cómo verificar el Estado de Congelamiento sin Excel usando Node.js a través de C++
linktitle: Estado congelado
type: docs
weight: 190
url: /es/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: En este artículo, aprenderás cómo verificar el estado de congelamiento de una hoja de cálculo de Excel programáticamente usando Node.js con la biblioteca C++.

---

## **Introducción**

En este artículo, aprenderemos cómo verificar el estado de congelamiento de una hoja de Excel programáticamente. Podemos simplemente determinar si la hoja está congelada o dividida en MS Excel. Pero, ¿existe una forma de saber si está congelada o dividida con Node.js? Podemos hacerlo fácilmente con Aspose.Cells for Node.js via C++.

## **¿Están congelados los paneles de la ventana?**
Con Aspose.Cells for Node.js via C++, podemos verificar si la ventana está congelada y cuántas filas y columnas están bloqueadas.

Utilice la propiedad [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) para verificar el estado de los paneles de ventana y obtener filas y columnas bloqueadas con el método [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--).
1. Construir un libro de trabajo para abrir el archivo.
2. Verificar si la hoja de cálculo está congelada.
3. Obtener filas y columnas bloqueadas.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
