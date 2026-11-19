---
title: Mostrar valores como en una tabla dinámica con Aspose.Cells for C++
linktitle: Mostrar valores como en una tabla dinámica con Aspose.Cells for C++
description: Muestre los valores de los campos de datos de una tabla dinámica expresados como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, clasificaciones y más con Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /es/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega los datos de cada campo mediante una función de agregación, como `Sum` o `Count`. La característica **Mostrar valores como** de Excel sustituye cada resultado mostrado por un cálculo secundario derivado de esa agregación; por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base seleccionado o una clasificación, lo que permite realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.
Entre los usos habituales se encuentran el análisis de participación en el total, incluidos los porcentajes de una fila, una columna o del total general; los informes acumulativos que utilizan un total acumulado en un campo de período; el análisis de variaciones frente a un elemento de referencia mediante la diferencia o la diferencia porcentual respecto a un elemento base; y la clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for C++, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. El método `PivotField.GetShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `SetShowValuesAs`, `SetBaseFieldIndex` y `SetBaseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.ShowValuesAs(...)` aplica la misma configuración en una sola llamada. Aplique estos ajustes a un campo de datos o de valor obtenido de `PivotTable.GetDataFields()`.

## **Miembros de la enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como `Sum` o `Count`, mientras que Mostrar valores como transforma únicamente la forma en que se muestra el valor agregado.
Además de configurar directamente los valores de `PivotShowValuesSetting` (consulte la última sección), existe un método de conveniencia que aplica la misma configuración en una sola llamada. Este método tiene dos variantes: una permite especificar el campo base y el elemento base por índice y la otra, por nombre:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Parámetro | Significado | Cuándo es obligatorio |
| --- | --- | --- |
| `showValuesAsType` | El cálculo secundario `PivotShowValuesAsType` que se debe aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base) o, en la variante por nombre, el nombre del campo base. | Los ocho formatos relativos a la base que se indican a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); para cualquier otro formato, pase `0` (o un `U16String` vacío en la variante por nombre). |
| `baseItem` | Índice basado en cero del elemento base, con dos valores centinela: `-1` selecciona el elemento anterior y `-2` el siguiente (la API de C++ no define constantes con nombre para los valores centinela; pase los valores literales). La variante por nombre utiliza el rótulo del elemento base y un `U16String` vacío cuando el formato seleccionado no necesita ningún elemento base. | Solo los tres formatos relativos al elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) tienen en cuenta el elemento base; los cinco formatos relativos al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, ambas clasificaciones) lo omiten; pase `0` o un `U16String` vacío. |

| Tipo de cálculo | Comportamiento | Parámetros de base |
| --- | --- | --- |
| `Normal` | Ningún cálculo secundario; el valor agregado se muestra tal cual (valor predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o el valor centinela del elemento anterior o siguiente) |
| `PercentageOf` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o el valor centinela del elemento anterior o siguiente) |
| `PercentageDifferenceFrom` | Muestra el valor como una diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o el valor centinela del elemento anterior o siguiente) |
| `RunningTotalIn` | Muestra el valor como total acumulado para elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos determina la acumulación) |
| `PercentageOfRow` | Muestra el valor como porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como porcentaje del total general. | — |
| `Index` | Muestra el valor mediante la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como porcentaje del total de su fila principal (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como porcentaje del total de su columna principal (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como porcentaje del total de su campo principal. | `baseField` (el campo principal cuyo total es la referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Asigna al valor una clasificación que va de menor (1) a mayor. | `baseField` (el campo cuyos elementos definen el alcance de la clasificación) |
| `RankLargestToSmallest` | Asigna al valor una clasificación que va de mayor (1) a menor. | `baseField` (el campo cuyos elementos definen el alcance de la clasificación) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` escribe los valores de `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex` y `BaseItemIndex`); el método y el objeto de configuración son dos formas de establecer el mismo estado, en correspondencia con los selectores de campo base y elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Para convertir cada celda del campo de datos, incluido el total general, en su porcentaje del total general, invoque el método `PivotField.ShowValuesAs` con `PivotShowValuesAsType::PercentageOfTotal`. Los números mostrados representan, por tanto, proporciones del conjunto completo de resultados. Este formato calcula cada valor únicamente respecto del total general, por lo que no necesita un campo base ni un elemento base; los argumentos finales (`0`, `0`) son valores de relleno que el formato ignora, tal como se indica en la tabla de parámetros anterior.

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
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obtener y configurar PivotField.ShowValuesSetting**
Para consultar la configuración actual, utilice `PivotField.GetShowValuesSetting()`: este método devuelve el objeto `PivotShowValuesSetting` del campo, cuyos métodos de lectura indican el cálculo activo de Mostrar valores como. Para cambiar la configuración, invoque el método `PivotField.ShowValuesAs`: este escribe todos los ajustes en una sola llamada, por lo que nunca es necesario establecerlos uno por uno.
El objeto `PivotShowValuesSetting` expone el estado que configura `ShowValuesAs`:
- `GetShowValuesAs()` / `SetShowValuesAs()` seleccionan el cálculo secundario `PivotShowValuesAsType`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` especifican el índice basado en cero del campo base entre los campos de la tabla dinámica. Se utiliza en los formatos relativos a la base.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` especifican el elemento base: un índice basado en cero de un elemento específico de la tabla dinámica o uno de los dos valores centinela: `-1` para el elemento anterior y `-2` para el siguiente (la API de C++ no define constantes con nombre para los valores centinela). Se utiliza en los formatos relativos al elemento base.
- `GetBaseFieldName()` y `GetBaseItemCaption()` son vistas de solo lectura que devuelven el nombre resuelto del campo base y el rótulo del elemento base; por ejemplo, después de seleccionar el valor centinela del elemento anterior, `GetBaseItemCaption()` devuelve `(previous)`.
Después de invocar `ShowValuesAs`, invoque de nuevo `PivotTable.CalculateData()` para que el cuerpo de la tabla dinámica se recalcule y se vuelva a mostrar con la configuración actualizada.

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
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Artículos relacionados**
- [Administrar campos de valor en una tabla dinámica](/cells/es/cpp/manage-value-fields/)
- [Actualizar una tabla dinámica](/cells/es/cpp/refresh-pivot-table/)
- [Aplicar estilo a una tabla dinámica](/cells/es/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}