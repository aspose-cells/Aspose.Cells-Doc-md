---  
title: Detección de hojas de cálculo vacías con Node.js a través de C++  
linktitle: Detectar hojas de cálculo vacías  
type: docs  
weight: 410  
url: /es/nodejs-cpp/detecting-empty-worksheets/  
description: Este artículo muestra un código que explica cómo detectar programáticamente hojas de cálculo vacías en libros de Excel usando la API de Node.js con la biblioteca C++.  
keywords: detectar hoja de cálculo vacía Node.js a través de C++, encontrar hoja de cálculo vacía en Excel Node.js a través de C++  
---  

## **Buscar celdas pobladas**

Las hojas de cálculo pueden tener una o más celdas llenas con valores, donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En tal caso, es fácil detectar si una hoja de cálculo dada está vacía o no. Todo lo que tenemos que verificar son las propiedades [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) o [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--). Si las propiedades mencionadas devuelven cero o valores positivos, eso significa que una o más celdas han sido llenadas; sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas ha sido llenada en la hoja de cálculo dada.

{{% alert color="primary" %}}

Las colecciones de filas y columnas tienen índices basados en cero; por lo tanto, una celda en la fila 0 y columna 0 significa la primera celda en la hoja de cálculo, que es A1.

{{% /alert %}}

## **Comprobar celdas inicializadas vacías**

Todas las celdas que tienen valores se inicializan automáticamente; sin embargo, existe la posibilidad de que una hoja de cálculo tenga celdas solo con formato aplicado. En tal escenario, las propiedades [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) o [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) devolverán -1 indicando la ausencia de valores poblados, pero las celdas inicializadas debido al formato no se pueden detectar usando este método. Para verificar si una hoja de cálculo tiene celdas inicializadas vacías, se recomienda usar el método `Enumerator.MoveNext` en el enumerador adquirido de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Si el método `Enumerator.MoveNext` devuelve **true**, eso significa que hay una o más celdas inicializadas en la hoja de cálculo dada.

## **Comprobar formas**

Es posible que una hoja de cálculo dada no tenga celdas llenas; sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos verificar si una hoja de cálculo contiene alguna forma, podemos hacerlo inspeccionando la propiedad [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--). Cualquier valor positivo indica la presencia de forma(s) en la hoja de cálculo.

## **Ejemplo de Programación**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

