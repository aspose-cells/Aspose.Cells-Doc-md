---
title: Formato de una parte de una tabla dinámica
description: Formato de una parte de una tabla dinámica en Aspose.Cells for C++ aplicando estilos a regiones semánticas PivotArea o a rectángulos CellArea mediante PivotTable.Format, con formatos almacenados en PivotTable.GetPivotFormats y preservados cuando se actualiza la tabla dinámica.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, tabla dinámica, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /es/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
`PivotTable.FormatAll` aplica un solo estilo a toda la tabla dinámica y se cubre en la página principal. No distingue entre etiquetas, valores, totales o regiones particulares del informe.  
En la práctica, solo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valores producidas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de elementos.  
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de registros de estilo de celda ordinarios. Un formato de área de pivote permanece vinculado a una región, como las etiquetas o los valores de datos de un campo, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Por otro lado, un estilo escrito directamente en una celda pertenece a esa posición de celda y no es rastreado por el modelo de pivote.  
Aspose.Cells expone la familia completa de sobrecargas `PivotTable.Format` para que ambos tipos de formato estén disponibles:
- `Format(const PivotArea&, const Style&)` ancla un estilo a una región semántica que se construye con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` ancla un estilo a un rectángulo de hoja de cálculo dentro de la tabla dinámica.
- `Format(int32_t row, int32_t column, const Style&)` apunta a una sola celda.
- `FormatAll(const Style&)` formatea toda la tabla dinámica.

## **Formatear un área de pivote**
El flujo de trabajo de área semántica es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Crear un `PivotArea` con `PivotArea pivotArea(pivotTable);`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.  
2. Seleccionar un campo por su posición basada en cero en un eje dado con `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType::DataAndLabel` selecciona tanto las etiquetas como los datos del campo.  
   - `PivotTableSelectionType::LabelOnly` selecciona solo las etiquetas del campo.  
   - `PivotTableSelectionType::DataOnly` selecciona solo las celdas de datos del campo.  
3. Seleccionar un campo por nombre con `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve en las celdas de valores producidas por los elementos de ese campo.  
4. Crear un `Style` con `Workbook.CreateStyle()`, configurar su fuente, color de primer plano y patrón de fondo sólido, y pasar el estilo a `PivotTable.Format(pivotArea, style)`.  
5. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.GetPivotFormats()`.  
6. Los formatos anclados a campos se aplican cuando se calculan los datos de la tabla dinámica. Por lo tanto, llame a `PivotTable.CalculateData()` después de aplicar los formatos para que los estilos sean visibles.  
El siguiente ejemplo construye una pequeña tabla dinámica de ventas de frutas, formatea las etiquetas de fila `Fruit` con `PivotArea.Select` y `PivotTableSelectionType::LabelOnly`, formatea las celdas de valores producidas por ese mismo campo de fila con `PivotArea.SelectField`, y luego recalcula la tabla dinámica para que ambos estilos se apliquen.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Formatear un área de celdas de la tabla dinámica**
Use `PivotTable.Format(const CellArea&, const Style&)` cuando la zona de interés sea un rectángulo simple de la hoja de cálculo en lugar de una región semántica de pivote.  
Un `CellArea` se describe mediante los campos públicos `StartRow`, `StartColumn`, `EndRow` y `EndColumn`. Los valores son coordenadas de hoja basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, de modo que el área cubre las celdas desde la posición inicial hasta la final, inclusive.  
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas de inmediato. No se necesita otra llamada a `CalculateData()` para que el estilo aparezca.  
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor al mismo tiempo. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.  
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursivo y azul claro y guarda el libro de trabajo sin realizar una recalculación adicional.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Cómo se mapean las áreas de pivote y las áreas de celda**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros de estilo de celda ordinarios. El mismo modelo lo utiliza Aspose.Cells, por lo que una solicitud de formato se traduce en áreas de pivote al registrarse.  
La relación entre el `CellArea` proporcionado por el usuario y las áreas de pivote almacenadas internamente es de muchos a muchos en ambas direcciones.  
- Un `CellArea` puede producir varias áreas de pivote. Si el rectángulo abarca tanto celdas de etiqueta como de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo de pivote trata el formato de etiquetas y de datos de forma independiente.  
- Una área de pivote puede resolverse en varias instancias disjuntas de `CellArea`. Una región semántica como una fila de total general, o un campo cuyos elementos no son contiguos, puede cubrir varios rectángulos. Por eso `PivotArea.GetCellAreas()` devuelve un `Vector<CellArea>` en lugar de un único rectángulo.  
Cada operación de formato realizada a través de `PivotTable.Format` se registra en `PivotTable.GetPivotFormats()`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga de `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene distintas regiones semánticas puede agregar varias entradas.  
Para distinguir las regiones almacenadas, cada `PivotArea` expone las banderas `GetOnlyLabel()` y `GetOnlyData()`. El ejemplo a continuación formatea un solo rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.GetPivotFormats()` e imprime las coordenadas `CellArea` que cada área de pivote almacenada resuelve.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Porque los formatos se almacenan como áreas de pivote en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y a la actualización. Cuando la tabla dinámica se actualiza con `PivotTable.RefreshData`, se recalcula con `CalculateData`, o se guarda y recarga, cada área de pivote almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Use un `PivotArea` construido con `Select` o `SelectField` cuando un resaltado deba permanecer vinculado a un campo o a una región semántica a través de actualizaciones, y use un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `Format(int32_t row, int32_t column, const Style&)` apunta a una celda individual. Use `FormatAll`, cubierto en la página principal, cuando toda la tabla dinámica deba restilarse de una sola vez.

## **Artículos relacionados**
- [Aplicar estilo a una tabla dinámica](/cells/es/cpp/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/cpp/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valores en la tabla dinámica](/cells/es/cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}