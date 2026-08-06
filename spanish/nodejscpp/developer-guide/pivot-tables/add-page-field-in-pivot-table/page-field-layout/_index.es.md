---
title: Modificar el diseño del campo de página en una tabla dinámica
linktitle: Modificar el diseño del campo de página en una tabla dinámica
description: Aprenda a controlar el diseño del área de campos de página en una tabla dinámica con Aspose.Cells for Node.js via C++, incluyendo el ajuste del orden de visualización, el número de ajuste y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells, biblioteca de Node.js via C++, hoja de cálculo, tabla dinámica, campo de página, orden del campo de página, número de ajuste del campo de página, mover campo de página
type: docs
weight: 191
url: /es/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Este artículo es una continuación del tema **Agregar campo de página en una tabla dinámica**. Muestra cómo controlar el diseño del área de campos de página — la franja de controles de filtro situada en la parte superior de una tabla dinámica — incluyendo el orden de visualización, el número de ajuste y la reordenación de campos.

{{% /alert %}}

## **Introducción**

Una tabla dinámica en Microsoft Excel expone un **área de campos de página** dedicada que se sitúa encima del cuerpo de filas/columnas/datos de la tabla. Esta área se representa como una franja de controles de filtro desplegables (uno por cada campo de página) y es donde los usuarios finales hacen clic para segmentar la tabla dinámica según criterios como el año o la región. Aspose.Cells for Node.js via C++ modela esta área a través de la colección `pivotTable.pageFields` y expone tres propiedades que controlan cómo se dispone visualmente la franja:

- `pivotTable.pageFieldOrder` (un valor de `Aspose.Cells.PrintOrderType`) decide si los campos de página adicionales se colocan *junto a* los existentes o *debajo* de ellos.
- `pivotTable.pageFieldWrapCount` establece cuántos campos de página se colocan por fila o columna antes de ajustar.
- `pivotTable.pageFields.move(currIndex, destIndex)` reordena los campos de página sin cambiar el modo de orden.

Este artículo recorre tres ejemplos de código que demuestran cada una de estas operaciones sobre un conjunto de datos compartido, de modo que pueda comparar los diseños resultantes uno al lado del otro.

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

Las ocho filas se rellenan en cada ejemplo de código, en el mismo orden, de modo que los datos de origen nunca difieren entre escenarios — solo lo hacen las propiedades del diseño del campo de página.

## **Ejemplo 1: Over Then Down**

En el primer escenario configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **uno al lado del otro en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, colocamos `Year` primero y `Region` después en el eje de página (el orden de las llamadas a `addFieldToArea` determina el índice inicial), añadimos `Amount` (Sum) como campo de datos y luego establecemos `pageFieldOrder` en `PrintOrderType.OverThenDown` con `pageFieldWrapCount = 2`. Con `OverThenDown` y un número de ajuste de 2, los dos campos de página se colocan horizontalmente uno al lado del otro en una sola fila en la parte superior de la tabla dinámica, de modo que la franja ocupa una fila de ancho dos.

```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

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

// Fila 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Fila 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Fila 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Fila 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Fila 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Fila 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Fila 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Fila 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Agregar hoja PivotTableReport
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Crear tabla dinámica con origen en PivotData!A1:D9 ubicada en A1 en PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Agregar campos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Configurar el diseño del área de campos de página: colocar los campos de página primero de izquierda a derecha, ajustar después de cada 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Refrescar y calcular
pivotTable.calculateData();

// Guardar
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Ejemplo 2: Down Then Over**

En este ejemplo colocamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de página (con `Year` primero) y `Amount` (Sum) como campo de datos — exactamente igual que en el Ejemplo 1. Luego establecemos `pageFieldOrder` en `PrintOrderType.DownThenOver` y `pageFieldWrapCount` en `2`. Con `DownThenOver` y un número de ajuste de 2, los dos campos de página se apilan verticalmente — `Year` arriba, `Region` directamente debajo — formando una sola columna en la parte superior de la tabla dinámica. Por lo tanto, la franja ocupa dos filas de ancho uno, en contraste con el Ejemplo 1.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

const data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Ejemplo 3: Mover un campo de página**

En el tercer escenario conservamos este conjunto de datos y la asignación de campos, establecemos un diseño neutro (`OverThenDown` con número de ajuste `2`) y luego demostramos la operación `pageFields.move`. La llamada a `move(0, 1)` mueve el campo de página en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) pasa a la posición 0. Tras esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El número de ajuste y el modo de orden no cambian, de modo que la franja sigue representándose horizontalmente uno al lado del otro — solo se ha intercambiado el orden de los dos desplegables.

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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```

## **Artículos relacionados**

- [Agregar campo de página en una tabla dinámica](/cells/es/nodejs-cpp/add-page-field-in-pivot-table/) — la página principal que presenta cómo se agregan campos de página a una tabla dinámica.
- [Campos de fila y columna en una tabla dinámica](/cells/es/nodejs-cpp/row-and-column-fields/) — cubre la asignación de campos a los ejes de fila y columna, complementando el trabajo del eje de página mostrado aquí.
- [Administrar campos de valor en una tabla dinámica](/cells/es/nodejs-cpp/manage-value-fields/) — describe cómo configurar el área de datos (valores), incluyendo la agregación `Sum` utilizada en este artículo.
- [Actualizar tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/) — explica `refreshData` y `calculateData`, que son necesarios tras reordenar los campos de página.
- [Aplicar estilo a una tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica renderizada una vez dispuesta la franja de campos de página.

{{< app/cells/assistant language="nodejs-cpp" >}}