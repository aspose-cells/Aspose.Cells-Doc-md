---
title: Modificar el diseño del campo de página en una tabla dinámica
linktitle: Modificar el diseño del campo de página en una tabla dinámica
description: Aprenda a controlar el diseño del área de campos de página en una tabla dinámica usando Aspose.Cells for C++, incluyendo el establecimiento del orden de visualización, el recuento de ajuste y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, tabla dinámica, campo de página, orden de campo de página, recuento de ajuste de campo de página, mover campo de página
type: docs
weight: 191
url: /es/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Este artículo es una continuación del tema **Añadir campo de página en una tabla dinámica**. Muestra cómo controlar el diseño del área de campos de página — la franja de controles de filtro en la parte superior de una tabla dinámica — incluyendo el orden de visualización, el recuento de ajuste y la reordenación de campos.
{{% /alert %}}
## **Introducción**
Una tabla dinámica en Microsoft Excel expone un **área de campos de página** dedicada que se sitúa encima del cuerpo de filas/columnas/datos de la tabla. Esta área se representa como una franja de controles desplegables de filtro (uno por cada campo de página) y es donde los usuarios finales hacen clic para segmentar la tabla dinámica por criterios como año o región. Aspose.Cells for C++ modela esta área a través de la colección `PivotTable.PageFields` y expone tres propiedades que controlan cómo se dispone visualmente la franja:
- `PivotTable.PageFieldOrder` (un valor de `Aspose.Cells.PrintOrderType`) decide si los campos de página adicionales se colocan *junto a* los existentes o *debajo* de ellos.
- `PivotTable.PageFieldWrapCount` establece cuántos campos de página se colocan por fila o columna antes de ajustar.
- `PivotTable.PageFields.Move(currIndex, destIndex)` reordena los campos de página sin cambiar el modo de orden.
Este artículo recorre tres ejemplos de código que muestran cada una de estas operaciones sobre un conjunto de datos compartido, para que pueda comparar los diseños resultantes uno al lado del otro.
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
Las ocho filas se rellenan en cada ejemplo de código, en orden idéntico, de modo que los datos de origen nunca difieren entre escenarios — solo lo hacen las propiedades del diseño del campo de página.
## **Ejemplo 1: Sobre y luego abajo (Over Then Down)**
En el primer escenario configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **uno al lado del otro en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, colocamos `Year` primero y `Region` después en el eje de página (el orden de las llamadas `AddFieldToArea` determina el índice inicial), añadimos `Amount` (Suma) como campo de datos y luego establecemos `PageFieldOrder` como `PrintOrderType.OverThenDown` con `PageFieldWrapCount = 2`. Con `OverThenDown` y un recuento de ajuste de 2, los dos campos de página se disponen horizontalmente uno al lado del otro en una sola fila en la parte superior de la tabla dinámica, por lo que la franja ocupa una fila de ancho dos.
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // Encabezados (fila 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Fila 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Fila 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Fila 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Fila 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Fila 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Fila 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Fila 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Fila 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // Agregar hoja PivotTableReport
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Crear tabla dinámica con origen en PivotData!A1:D9 ubicada en A1 en PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Agregar campos
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruta
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Año
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Región
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Monto
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Configurar el diseño del área de campos de página: colocar los campos de página primero en horizontal, ajustar después de cada 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Refrescar y calcular
    pivotTable.CalculateData();

    // Guardar
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Ejemplo 2: Abajo y luego sobre (Down Then Over)**
En este ejemplo colocamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de página (con `Year` primero), y `Amount` (Suma) como el campo de datos — exactamente como en el Ejemplo 1. Luego establecemos `PageFieldOrder` como `PrintOrderType.DownThenOver` y `PageFieldWrapCount` como `2`. Con `DownThenOver` y un recuento de ajuste de 2, los dos campos de página se apilan verticalmente — `Year` arriba, `Region` directamente debajo — formando una sola columna en la parte superior de la tabla dinámica. Por lo tanto, la franja ocupa dos filas de ancho uno, en contraste con el Ejemplo 1.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Ejemplo 3: Mover un campo de página**
En el tercer escenario conservamos este conjunto de datos y asignación de campos, establecemos un diseño neutro (`OverThenDown` con recuento de ajuste `2`) y luego demostramos la operación `PageFields.Move`. La llamada `Move(0, 1)` mueve el campo de página en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) se desplaza a la posición 0. Tras esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El ajuste y el modo de orden no se modifican, por lo que la franja sigue mostrándose horizontalmente uno al lado del otro — solo se ha intercambiado el orden de los dos desplegables.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Artículos relacionados**
- [Añadir campo de página en una tabla dinámica](/cells/es/cpp/add-page-field-in-pivot-table/) — la página principal que presenta cómo se añaden campos de página a una tabla dinámica.
- [Campos de fila y columna en una tabla dinámica](/cells/es/cpp/row-and-column-fields/) — cubre la asignación de campos a los ejes de fila y columna, complementando el trabajo del eje de página mostrado aquí.
- [Administrar campos de valor en una tabla dinámica](/cells/es/cpp/manage-value-fields/) — describe cómo configurar el área de datos (valores), incluida la agregación `Sum` utilizada en este artículo.
- [Actualizar tabla dinámica](/cells/es/cpp/refresh-pivot-table/) — explica `RefreshData` y `CalculateData`, que son necesarios después de reordenar los campos de página.
- [Aplicar estilo a una tabla dinámica](/cells/es/cpp/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica renderizada después de haber dispuesto la franja de campos de página.
{{< app/cells/assistant language="" >}}