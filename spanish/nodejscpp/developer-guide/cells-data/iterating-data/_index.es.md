---  
title: Cómo y dónde usar enumeradores con Node.js a través de C++  
linktitle: Iterar datos  
type: docs  
weight: 55  
url: /es/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Aprende cómo usar enumeradores mediante la API Aspose.Cells for Node.js via C++.  
keywords: Cómo usar enumeradores Node.js a través de C++, Enumerador de Celdas Node.js a través de C++, Enumerador de Filas Node.js a través de C++, Enumerador de Columnas Node.js a través de C++  
---  

{{% alert color="primary" %}}  

Un enumerador es un objeto que permite recorrer un contenedor o colección. Los enumeradores se usan para leer los datos en la colección, pero no para modificarla. La interfaz Array define un método `getEnumerator` que devuelve una interfaz `IEnumerator`, que a su vez permite acceso solo de lectura a una colección.  

Las API de Aspose.Cells proporcionan una serie de enumeradores, sin embargo, este artículo discute principalmente los tres tipos que se enumeran a continuación.  

1. Enumerador de celdas  
1. Enumerador de filas  
1. Enumerador de columnas  

{{% /alert %}}  

## **Cómo usar Enumeradores**  

### **Enumerador de celdas**  

Hay diversas formas de acceder al enumerador de celdas, y se puede utilizar cualquiera de estos métodos según los requisitos de la aplicación. Aquí están los métodos que devuelven el enumerador de celdas.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Todos los métodos mencionados anteriormente devuelven el enumerador que permite recorrer la colección de celdas que han sido inicializadas.  

{{% alert color="primary" %}}  

Mientras se recorren las celdas, la colección no debe modificarse (operaciones que causarán una nueva celda que se instancie o celda existente que se elimine). De lo contrario, es posible que el enumerador no pueda recorrer todas las celdas correctamente (algunos elementos pueden ser recorridos repetidamente o ignorados).  

{{% /alert %}}  

El siguiente ejemplo de código demuestra la implementación de la interfaz `IEnumerator` para una colección de Celdas.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Enumerador de filas**  

El enumerador de Filas se puede acceder al usar el método [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--). El siguiente ejemplo de código demuestra la implementación de la interfaz `IEnumerator` para [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Enumerador de columnas**  

El enumerador de Columnas se puede acceder al usar el método [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection). El siguiente ejemplo de código demuestra la implementación de la interfaz `IEnumerator` para [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Dónde usar Enumeradores**  

Para discutir las ventajas de usar enumeradores, tomemos un ejemplo en tiempo real.  

Escenario  

Un requisito de la aplicación es recorrer todas las celdas en un [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dado para leer sus valores. Podría haber varias formas de implementar este objetivo. Se demuestran algunas a continuación.  

### **Usando Rango de Visualización**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **Usando MaxDataRow y MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Como puedes observar, ambos enfoques mencionados anteriormente utilizan más o menos una lógica similar; es decir, recorrer todas las celdas en la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se discute a continuación.  

1. Las API como [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) y [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) requieren tiempo adicional para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, el uso de estas API podría imponer una penalización en el rendimiento.  
1. En la mayoría de los casos, no todas las celdas en un rango dado están instanciadas. En tales situaciones, verificar cada celda en la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.  
1. Acceder a una celda en un bucle como Cells fila, columna hará que se instancien todos los objetos de celda en un rango, lo que eventualmente podría causar OutOfMemoryException.  

## **Conclusión**  

Con base en los hechos mencionados anteriormente, los siguientes son los posibles escenarios en los que se deben usar los enumeradores.  

1. Se requiere acceso de solo lectura a la colección de celdas, es decir; el requisito es solo inspeccionar las celdas.  
1. Se deben recorrer un gran número de celdas.  
1. Solo se deben recorrer celdas/filas/columnas inicializadas.  

{{< app/cells/assistant language="nodejs-cpp" >}}
