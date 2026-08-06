---
title: Modificar el diseño del campo de página en una tabla dinámica
linktitle: Modificar el diseño del campo de página en una tabla dinámica
description: Aprenda a controlar el diseño del área de campos de página en una tabla dinámica con Aspose.Cells for Node.js via Java, incluyendo la configuración del orden de visualización, el número de saltos y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells, biblioteca de Node.js vía Java, hoja de cálculo, tabla dinámica, campo de página, orden del campo de página, número de saltos del campo de página, mover campo de página
type: docs
weight: 191
url: /es/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Este artículo es una continuación del tema **Agregar campo de página en tabla dinámica**. Demuestra cómo controlar el diseño del área de campos de página, la franja de controles de filtro en la parte superior de una tabla dinámica, incluyendo el orden de visualización, el número de saltos y el reordenamiento de campos.
{{% /alert %}}
## **Introducción**
Una tabla dinámica en Microsoft Excel expone un **área de campos de página** dedicada que se sitúa encima del cuerpo de filas, columnas y datos de la tabla. Esta área se representa como una franja de controles de filtro desplegables (uno por cada campo de página) y es donde los usuarios finales hacen clic para segmentar la dinámica por criterios como el año o la región. Aspose.Cells modela esta área mediante la colección `PivotTable.PageFields` y expone tres propiedades que controlan cómo se distribuye visualmente la franja:
- `PivotTable.PageFieldOrder` (un valor de `Aspose.Cells.PrintOrderType`) decide si los campos de página adicionales se colocan *al lado* de los existentes o *debajo* de ellos.
- `PivotTable.PageFieldWrapCount` establece cuántos campos de página se colocan por fila o columna antes de saltar.
- `PivotTable.PageFields.Move(currIndex, destIndex)` reordena los campos de página sin cambiar el modo de orden.
Este artículo recorre tres ejemplos de código que demuestran cada una de estas operaciones sobre un conjunto de datos compartido, de modo que pueda comparar los diseños resultantes uno junto al otro.
## **Datos de origen**
Los tres ejemplos siguientes cargan estas ocho filas de datos de ventas en una hoja de cálculo llamada `PivotData`. Los datos contienen dos candidatos a campo de página (`Year`, `Region`), un candidato a campo de fila (`Fruit`) y una medida (`Amount`), lo que hace que la franja de campos de página sea significativa para inspeccionar.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Las ocho filas se rellenan en cada ejemplo de código, en el mismo orden, por lo que los datos de origen nunca difieren entre escenarios, solo lo hacen las propiedades del diseño de campos de página.
## **Ejemplo 1: Horizontal y luego vertical**
En el primer escenario configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **uno al lado del otro en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, ubicamos `Year` en primer lugar y `Region` en segundo lugar en el eje de páginas (el orden de las llamadas a `addFieldToArea` determina el índice de inicio), añadimos `Amount` (Sum) como campo de datos y luego establecemos `PageFieldOrder` en `PrintOrderType.OVER_THEN_DOWN` con `PageFieldWrapCount = 2`. Con `OVER_THEN_DOWN` y un número de saltos de 2, los dos campos de página se colocan horizontalmente uno al lado del otro en una sola fila en la parte superior de la tabla dinámica, de modo que la franja ocupa una fila de ancho dos.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// Encabezados (fila 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Fila 1: Manzana, 2022, Norte, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Fila 2: Manzana, 2023, Norte, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Fila 3: Plátano, 2022, Sur, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Fila 4: Plátano, 2023, Sur, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Fila 5: Cereza, 2022, Este, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Fila 6: Cereza, 2023, Este, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Fila 7: Uva, 2022, Oeste, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Fila 8: Uva, 2023, Oeste, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Agregar hoja PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Crear tabla dinámica con origen en PivotData!A1:D9 ubicada en A1 de PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Agregar campos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruta
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Año
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Región
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Cantidad
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Configurar disposición del área de campos de página: colocar los campos de página primero en horizontal, ajustar cada 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Actualizar y calcular
pivotTable.calculateData();

// Guardar
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **Ejemplo 2: Vertical y luego horizontal**
En este ejemplo ubicamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de páginas (con `Year` primero) y `Amount` (Sum) como campo de datos, exactamente como en el Ejemplo 1. Luego establecemos `PageFieldOrder` en `PrintOrderType.DOWN_THEN_OVER` y `PageFieldWrapCount` en `2`. Con `DOWN_THEN_OVER` y un número de saltos de 2, los dos campos de página se apilan verticalmente: `Year` arriba y `Region` directamente debajo, formando una sola columna en la parte superior de la tabla dinámica. Por lo tanto, la franja ocupa dos filas de ancho uno, en contraste con el Ejemplo 1.
```javascript
var workbook = new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);

var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Ejemplo 3: Mover un campo de página**
En el tercer escenario mantenemos este conjunto de datos y la asignación de campos, establecemos un diseño neutral (`OVER_THEN_DOWN` con número de saltos `2`) y luego demostramos la operación `PageFields.Move`. La llamada a `Move(0, 1)` mueve el campo de página en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) se desplaza a la posición 0. Tras esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El modo de saltos y el orden quedan sin cambios, por lo que la franja sigue representándose horizontalmente uno al lado del otro, solo se ha intercambiado el orden de los dos desplegables.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();

const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);

const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **Artículos relacionados**
- [Agregar campo de página en tabla dinámica](/cells/es/nodejs-java/add-page-field-in-pivot-table/) — la página principal que presenta cómo se agregan los campos de página a una tabla dinámica.
- [Campos de filas y columnas en una tabla dinámica](/cells/es/nodejs-java/row-and-column-fields/) — cubre la asignación de campos a los ejes de filas y columnas, complementando el trabajo del eje de páginas mostrado aquí.
- [Administrar campos de valor en una tabla dinámica](/cells/es/nodejs-java/manage-value-fields/) — describe cómo configurar el área de datos (valor), incluida la agregación `Sum` utilizada en este artículo.
- [Actualizar tabla dinámica](/cells/es/nodejs-java/refresh-pivot-table/) — explica `refreshData` y `calculateData`, que son necesarios después de reordenar los campos de página.
- [Aplicar estilo a una tabla dinámica](/cells/es/nodejs-java/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica renderizada después de que la franja de campos de página se haya dispuesto.
{{< app/cells/assistant language="nodejs-java" >}}