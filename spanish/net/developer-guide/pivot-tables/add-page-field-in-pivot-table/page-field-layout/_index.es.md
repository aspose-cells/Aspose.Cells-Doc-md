---
title: Modificar el diseño del campo de página en una tabla dinámica
linktitle: Modificar el diseño del campo de página en una tabla dinámica
description: Aprenda cómo controlar el diseño del área de campos de página en una tabla dinámica usando Aspose.Cells for .NET, incluyendo cómo configurar el orden de visualización, el recuento de ajuste y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells, biblioteca NET, hoja de cálculo, tabla dinámica, campo de página, orden de campos de página, recuento de ajuste de campos de página, mover campo de página
type: docs
weight: 191
url: /es/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Este artículo es una continuación del tema **Agregar campo de página en una tabla dinámica**. Demuestra cómo controlar el diseño del área de campos de página, es decir, la franja de controles de filtro situada en la parte superior de una tabla dinámica, lo que incluye el orden de visualización, el recuento de ajuste y la reordenación de campos.

{{% /alert %}}

## **Introducción**

Una tabla dinámica en Microsoft Excel expone un **área de campos de página** dedicada que se sitúa encima del cuerpo de filas, columnas y datos de la tabla. Esta área se representa como una franja de controles de filtro desplegables (uno por cada campo de página) y es sobre lo que los usuarios finales hacen clic para segmentar la tabla dinámica por criterios como el año o la región. Aspose.Cells modela esta área a través de la colección `PivotTable.PageFields` y expone tres propiedades que controlan cómo se dispone visualmente la franja:

- `PivotTable.PageFieldOrder` (un valor de `Aspose.Cells.PrintOrderType`) decide si los campos de página adicionales se colocan *junto a* los existentes o *debajo* de ellos.
- `PivotTable.PageFieldWrapCount` establece cuántos campos de página se colocan por fila o columna antes de ajustar.
- `PivotTable.PageFields.Move(currIndex, destIndex)` reordena los campos de página sin cambiar el modo de ordenamiento.

Este artículo recorre tres ejemplos de código que demuestran cada una de estas operaciones sobre un conjunto de datos compartido, para que pueda comparar lado a lado los diseños resultantes.

## **Datos de origen**

Los tres ejemplos siguientes cargan estas ocho filas de datos de ventas en una hoja de cálculo llamada `PivotData`. Los datos contienen dos candidatos a campos de página (`Year`, `Region`), un candidato a campo de fila (`Fruit`) y una medida (`Amount`), lo que hace que la franja de campos de página sea significativa para inspeccionar.

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

Las ocho filas se completan en cada ejemplo de código, en el mismo orden, de modo que los datos de origen nunca difieren entre escenarios; solo lo hacen las propiedades de diseño del campo de página.

## **Ejemplo 1: Over Then Down**

En el primer escenario configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **lado a lado en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, ubicamos `Year` en primer lugar y `Region` en segundo lugar en el eje de página (el orden de las llamadas a `AddFieldToArea` determina el índice inicial), agregamos `Amount` (Suma) como campo de datos y luego establecemos `PageFieldOrder` en `PrintOrderType.OverThenDown` con `PageFieldWrapCount = 2`. Con `OverThenDown` y un recuento de ajuste de 2, los dos campos de página se disponen horizontalmente lado a lado en una sola fila en la parte superior de la tabla dinámica, de modo que la franja ocupa una fila de ancho dos.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// Encabezados (fila 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Fila 1: Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Fila 2: Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Fila 3: Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Fila 4: Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Fila 5: Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Fila 6: Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Fila 7: Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Fila 8: Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// Agregar hoja PivotTableReport
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Crear tabla dinámica con origen PivotData!A1:D9 ubicada en A1 en PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Agregar campos
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Fruta
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Año
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Región
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Monto
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Configurar el diseño del área de campos de página: colocar los campos de página primero en horizontal, ajustar después de cada 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Actualizar y calcular
pivotTable.CalculateData();

// Guardar
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Ejemplo 2: Down Then Over**

En este ejemplo ubicamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de página (con `Year` en primer lugar) y `Amount` (Suma) como campo de datos, exactamente igual que en el Ejemplo 1. Luego establecemos `PageFieldOrder` en `PrintOrderType.DownThenOver` y `PageFieldWrapCount` en `2`. Con `DownThenOver` y un recuento de ajuste de 2, los dos campos de página se apilan verticalmente — `Year` arriba, `Region` directamente debajo — formando una sola columna en la parte superior de la tabla dinámica. Por lo tanto, la franja ocupa dos filas de ancho uno, a diferencia del Ejemplo 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Ejemplo 3: Move a Page Field**

En el tercer escenario mantenemos este conjunto de datos y la asignación de campos, establecemos un diseño neutral (`OverThenDown` con recuento de ajuste `2`) y luego demostramos la operación `PageFields.Move`. La llamada a `Move(0, 1)` mueve el campo de página en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) pasa a la posición 0. Tras esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El modo de orden y de ajuste no cambia, por lo que la franja sigue mostrándose horizontalmente lado a lado; solo se ha intercambiado el orden de los dos desplegables.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **Artículos relacionados**

- [Agregar campo de página en una tabla dinámica](/cells/es/net/add-page-field-in-pivot-table/) — la página principal que presenta cómo se agregan campos de página a una tabla dinámica.
- [Campos de fila y columna en una tabla dinámica](/cells/es/net/pivot-table-add-row-and-column-fields/) — cubre la asignación de campos a los ejes de fila y columna, lo que complementa el trabajo del eje de página mostrado aquí.
- [Administrar campos de valor en una tabla dinámica](/cells/es/net/manage-value-fields/) — describe cómo configurar el área de datos (valores), incluida la agregación `Sum` utilizada en este artículo.
- [Actualizar tabla dinámica](/cells/es/net/refresh-pivot-table/) — explica `RefreshData` y `CalculateData`, que son necesarios después de reordenar campos de página.
- [Aplicar estilo a tabla dinámica](/cells/es/net/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica ya renderizada una vez que se ha dispuesto la franja de campos de página.

{{< app/cells/assistant language="csharp" >}}