---
title: Obtener dirección, celda, offset, toda columna y toda fila del rango con Node.js via C++
linktitle: Obtener dirección, contar celdas, desplazamiento, columna completa y fila completa del rango
type: docs
weight: 330
url: /es/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Escenarios de uso posibles**
Aspose.Cells for Node.js via C++ proporciona el objeto Range que tiene varios métodos útiles que facilitan al usuario trabajar con Rangos de Excel fácilmente. Este artículo ilustra el uso de los siguientes métodos o propiedades del objeto Range.

- **Dirección**

Obtiene la dirección del rango.

- **Recuento de celdas**

Obtiene el recuento de todas las celdas en el rango.

- **Desplazamiento**

Obtiene el rango mediante desplazamiento.

- **Columna completa**

Obtiene un objeto Range que representa toda la columna (o columnas) que contiene el rango especificado.

- **Fila completa**

Obtiene un objeto Range que representa toda la fila (o filas) que contiene el rango especificado.

## **Obtener Dirección, Recuento de celdas, Desplazamiento, Columna completa y Fila completa del Rango**
El siguiente código de ejemplo explica el uso de los métodos y propiedades como se discutió anteriormente. Consulte la salida de la consola del código que se muestra a continuación como referencia.

## **Código de muestra**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **Salida de la consola**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
