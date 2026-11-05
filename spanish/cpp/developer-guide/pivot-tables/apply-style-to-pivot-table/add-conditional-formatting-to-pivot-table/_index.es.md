---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for C++ - anclar una regla a la región de datos con ApplyTo y un alcance PivotConditionFormatScopeType, o definir el objetivo con AddCellArea y PivotAreas, luego adjuntar reglas y estilos mediante FormatConditions.AddCondition.
keywords: Aspose.Cells for C++, tabla dinámica, formato condicional, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /es/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una sola vez y conserva su estilo sin importar los valores. El formato condicional es la contraparte basada en reglas: resaltar cada cantidad superior a 200, sombrear el cincuenta por ciento intermedio o marcar los elementos de menor rango, y el resaltado se actualiza conforme los valores cada vez que la tabla dinámica se recalcula o se actualiza.  
En Aspose.Cells, el formato condicional de una tabla dinámica se encuentra en la colección `pivotTable.GetConditionalFormats()`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región de destino se define ya sea mediante `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, que reproduce el selector de alcance de la interfaz de usuario de Excel, o mediante `AddCellArea(CellArea)` y la colección `GetPivotAreas()`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Una o más condiciones se añaden mediante `GetFormatConditions()` con `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, y cada condición lleva su propio `Style`.

{{% alert color="primary" %}}
No llame a `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ni a `FormatConditionCollection.AddArea(CellArea)` en el objeto `GetFormatConditions()` de un formato condicional de pivote. Estas dos sobrecargas provienen de la API de formato condicional de hoja de cálculo convencional y no funcionan para tablas dinámicas: el área de celda nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Defina siempre la región en el propio `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` o `GetPivotAreas()`) y añada la regla con una de las sobrecargas `AddCondition`.
{{% /alert %}}

## **Aplicar una regla con un alcance (de la forma de la interfaz de Excel)**
La primera forma posiciona la regla como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra por sus coordenadas de hoja de cálculo basadas en cero, y un alcance `PivotConditionFormatScopeType` indica an Aspose.Cells hasta dónde debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType::Data` - todas las celdas de valor que produce la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType::Field` - las celdas de valor que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType::Selection` - solo las celdas de valor en la intersección que la celda selecciona, típicamente una única celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el alcance `Data`, y resalta cada cantidad mayor a 200 en negrita blanca sobre rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla pinta F4, F5 y F7; la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Anclar la misma regla en la etiqueta del campo de fila E4 (fila 3, columna 4) con el alcance `Field` se resuelve en F4:F6 — la misma columna de datos sin la fila de total general — porque el alcance ahora describe el campo `Fruit` en lugar de todo el área de valores. El alcance `Selection` anclado en F4 se resuelve únicamente en F4.

## **Definir la región manualmente**
La segunda forma omite el selector de alcance y nombra la región explícitamente en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con AddCellArea**
`AddCellArea(CellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado, sin expansión a la columna de datos ni lógica de totales generales. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Una región semántica de pivote con PivotAreas**
`GetPivotAreas()` ofrece el mismo modelo de región semántica que la página hermana utiliza para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `Select` o `SelectField`, y añádalo con `GetPivotAreas().AddPivotArea(PivotArea)`. Una región semántica permanece vinculada a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y cambia el diseño. La sobrecarga `GetPivotAreas().Add(PivotArea)` aún compila pero está marcada como obsoleta; prefiera `AddPivotArea`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada `pivotTable.GetConditionalFormats().Add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; al volver a abrir el archivo en el ejemplo siguiente se muestran la misma regla con su tipo, operador y fórmula intacta, y `GetCellAreas()` informa las mismas regiones. Las entradas que nunca recibieron una condición se descartan al guardar el libro de trabajo, del mismo modo que Excel elimina un formato condicional que no tiene regla.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Artículos relacionados**
- [Aplicar estilo a tabla dinámica](/cells/es/cpp/apply-style-to-pivot-table/)
- [Formato de parte de una tabla dinámica](/cells/es/cpp/format-part-of-pivot-table/)
- [Mostrar o filtrar los 10 principales en tabla dinámica](/cells/es/cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}