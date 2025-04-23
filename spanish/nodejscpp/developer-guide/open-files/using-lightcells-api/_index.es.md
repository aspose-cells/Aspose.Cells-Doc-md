---  
title: Usando la API LightCells con Node.js a través de C++  
linktitle: Utilizando la API de LightCells  
type: docs  
weight: 160  
url: /es/nodejs-cpp/using-lightcells-api/  
description: Aprende cómo leer y escribir archivos Excel grandes usando la API LightCells en Node.js a través de C++. Mejora el rendimiento y la eficiencia con menor consumo de memoria.  
---  

{{% alert color="primary" %}}  

A veces necesitas leer y escribir archivos de Excel de Microsoft grandes con una enorme lista de datos o contenido en la hoja de cálculo. La API de LightCells es útil para crear hojas de cálculo de Excel extensas: con ella, necesita menos memoria y obtiene un mejor rendimiento y eficiencia.  

{{% /alert %}}  
# Arquitectura Orientada a Eventos  
Aspose.Cells proporciona la API de LightCells, diseñada principalmente para manipular los datos de las celdas una por una sin construir un modelo completo de datos (usando la colección de Celdas, etc.) en la memoria. Funciona en modo de eventos.  

Para guardar libros de trabajo, proporciona el contenido de la celda una por una al guardar, y el componente lo guarda directamente en el archivo de salida.  

Al leer archivos de plantilla, el componente analiza cada celda y proporciona su valor uno por uno.  

En ambos procedimientos, se procesa y luego descarta un objeto Cell; el objeto Workbook no mantiene la colección. En este modo, por lo tanto, se ahorra memoria al importar y exportar archivos de Microsoft Excel que tienen un conjunto de datos grande que de otra manera usaría mucha memoria.  

Aunque la API de LightCells procesa las celdas de la misma manera para archivos XLSX y XLS (no carga todas las celdas en la memoria sino que procesa una celda y luego la descarta), ahorra memoria de manera más efectiva para archivos XLSX que para archivos XLS debido a los diferentes modelos de datos y estructuras de los dos formatos.  

Sin embargo, **para archivos XLS**, para ahorrar más memoria, los desarrolladores pueden especificar una ubicación temporal para guardar los datos temporales generados durante el proceso de guardado. Comúnmente, **usar la API LightCells para guardar archivos XLSX puede ahorrar un 50% o más de memoria** que usar la forma común; **guardar XLS puede ahorrar aproximadamente un 20-40% de memoria**.  

## Escribir un Archivo de Excel Grande  
Aspose.Cells proporciona una interfaz, `LightCellsDataProvider`, que debe ser implementada en tu programa. La interfaz representa el proveedor de datos para guardar archivos de hojas de cálculo grandes en modo liviano.  

Al guardar un libro en este modo, `StartSheet(int)` se verifica al guardar cada hoja del libro. Para una hoja, si `StartSheet(int)` es verdadero, entonces todos los datos y propiedades de filas y celdas de esa hoja son proporcionados por esta implementación. Primero, se llama a `NextRow()` para obtener el siguiente índice de fila a guardar. Si se devuelve un índice de fila válido (el índice de fila debe estar en orden ascendente para las filas a guardar), entonces se proporciona un objeto Row que representa esa fila para que la implementación establezca sus propiedades mediante `StartRow(Row)`.  

Para una fila, primero se verifica `NextCell()`. Si se devuelve un índice de columna válido (el índice de columna debe estar en orden ascendente para todas las celdas de una fila a guardar), entonces se proporciona un objeto Cell que representa esa celda para que la implementación establezca sus datos y propiedades mediante `StartCell(Cell)`. Después de establecer los datos de la celda, la celda se guarda directamente en el archivo de hoja de cálculo generado y se verifica y procesa la siguiente celda.  
### Escribir un archivo Excel grande: ejemplo  
Consulte el siguiente código de muestra para ver el funcionamiento de la API LightCells. Agregue, elimine o actualice los segmentos de código según sus necesidades.  

El programa crea un archivo enorme con **10,000 (matriz 10000x30) registros** en una hoja y los llena con datos ficticios. Puedes especificar tu propia matriz cambiando las variables `rowsCount` y `colsCount` en el método `Main()`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## Leer Archivos de Excel Grandes  
Aspose.Cells proporciona una interfaz, `LightCellsDataHandler`, que debe ser implementada en tu programa. La interfaz representa el proveedor de datos para leer archivos de hojas de cálculo grandes en modo liviano.  

Al leer un libro en este modo, `StartSheet` se verifica al leer cada hoja del libro. Para una hoja, si `StartSheet` devuelve true, entonces todos los datos y propiedades de las celdas en filas y columnas de la hoja son verificadas y procesadas por la implementación de esta interfaz. Para cada fila, se llama a `StartRow` para verificar si necesita ser procesada. Si una fila necesita ser procesada, primero se leen sus propiedades y el desarrollador puede acceder a sus propiedades con `ProcessRow`. Si las celdas de esa fila también necesitan ser procesadas, entonces `ProcessRow` debe devolver true, y se llama a `StartCell` para cada celda existente en la fila para verificar si una celda necesita ser procesada. Si una celda necesita ser procesada, entonces `ProcessCell` se llama para procesar la celda por la implementación de esta interfaz.  
### Leer archivos Excel grandes: ejemplo  
Consulte el siguiente código de muestra para ver el funcionamiento de la API LightCells. Agregue, elimine o actualice los segmentos de código según sus necesidades.  

El programa lee un archivo enorme con millones de registros en una hoja. Toma poco tiempo leer cada hoja del libro. El código de ejemplo lee el archivo y obtiene el número total de celdas, la cantidad de cadenas y la cantidad de fórmulas en cada hoja.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

