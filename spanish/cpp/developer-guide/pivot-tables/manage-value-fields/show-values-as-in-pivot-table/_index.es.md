---
title: Mostrar valores como en tabla dinámica en Aspose.Cells for C++
linktitle: Mostrar valores como en tabla dinámica en Aspose.Cells for C++
description: Muestre los valores de los campos de datos de tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /es/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La característica **Mostrar valores como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o un rango— para que pueda realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas. Los usos típicos incluyen análisis de participación total, incluyendo porcentajes de una fila, columna o total general; informes acumulativos usando un total acumulado en un campo de periodo; análisis de variación frente a un elemento de referencia utilizando diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for C++, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. El accessor `PivotField.GetShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyas métodos `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` y `SetBaseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.ShowValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estos ajustes a un campo de datos o de valores obtenido mediante `PivotTable.GetDataFields()`.

## **Miembros de la enumeración PivotFieldDataDisplayFormat**
El campo de datos mantiene su función de agregación, como Sum o Count, mientras que Mostrar valores como transforma solo la forma en que se muestra el valor agregado.
Además de escribir directamente los valores de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Parámetro | Significado | Cuándo es requerido |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` que se aplicará. | Siempre. |
| `baseField` | Índice cero‑basado del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base en relación con el elemento actual: `PivotItemPositionType::Previous`, `::Next` o `::Custom`. | Solo para los tres formatos con elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); los demás formatos lo ignoran. |
| `baseItem` | Índice cero‑basado del elemento base. | Solo cuando `baseItemPositionType` es `Custom` (el índice del elemento elige el elemento base exacto); se ignora para `Previous` / `Next` y para cualquier formato que no sea de base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como un porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total fila * total columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como un porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como un porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | — |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` escribe los valores de `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — el método y el objeto de ajustes son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.ShowValuesAs` con `PivotFieldDataDisplayFormat::PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto de resultados completo. Este formato mide cada valor únicamente contra el total general, por lo que no necesita campo base ni elemento base — los argumentos finales (`0`, `PivotItemPositionType::Previous`, `0`) son marcadores de posición que el formato ignora, según indica la tabla de parámetros anterior.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obtener y configurar PivotField.ShowValuesSetting**
Lea la configuración actual mediante `PivotField.GetShowValuesSetting()`: el accessor devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro métodos getter describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.ShowValuesAs` — escribe los cuatro ajustes en una sola llamada, de modo que nunca necesite asignar los valores uno por uno.
El objeto `PivotShowValuesSetting` expone los cuatro valores que escribe `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` seleccionan el cálculo secundario `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` especifican el índice cero‑basado del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos a la base.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` determinan cómo se posiciona el elemento base respecto al elemento actual y aceptan `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` o `PivotItemPositionType::Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` especifican el índice cero‑basado del elemento base y se usan cuando el tipo de posición es `Custom`.
Después de llamar a `ShowValuesAs`, invoque `PivotTable.CalculateData()` nuevamente para que el cuerpo de la tabla dinámica se recalcula y se vuelva a renderizar con la configuración actualizada.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Artículos relacionados**
- [Administrar campos de valor en tabla dinámica](/cells/es/cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/cpp/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}