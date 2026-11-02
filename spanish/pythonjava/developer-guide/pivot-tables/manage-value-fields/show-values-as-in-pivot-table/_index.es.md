---
title: Mostrar valores como en tabla dinámica
linktitle: Mostrar valores como en tabla dinámica
description: Muestra los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python a través de Java
type: docs
weight: 145
url: /es/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La característica **Show Values As** de Excel sustituye cada resultado mostrado por un cálculo secundario derivado de ese agregado —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o un rango— para que pueda realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes por fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variación respecto a un elemento de referencia mediante diferencia o diferencia porcentual; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Python via Java, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. El método de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos modificables `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` y `setBaseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estas configuraciones a un campo de datos o de valor obtenido de `PivotTable.getDataFields()`.

## **Miembros de la enumeración PivotFieldDataDisplayFormat**
El campo de datos conserva su función de agregación, como Suma o Conteo, mientras que Show Values As transforma únicamente la forma en que se muestra el valor agregado.  
Además de establecer directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Parámetro | Significado | Cuándo es necesario |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` a aplicar. | Siempre. |
| `baseField` | Índice base cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base en relación con el elemento actual: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo para los tres formatos con elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); los demás formatos lo ignoran. |
| `baseItem` | Índice base cero del elemento base. | Solo cuando `baseItemPositionType` es `Custom` (el índice del elemento elige el elemento base exacto); ignorado para `Previous` / `Next` y por cualquier formato que no sea de elemento base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | Sin cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como un porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total fila * total columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como un porcentaje del total de la fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como un porcentaje del total de la columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | — |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe los valores de `PivotShowValuesSetting` mediante `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` y `setBaseItemIndex`; el método y el objeto de configuración son dos formas de establecer el mismo estado, replicando los selectores de campo base y elemento base del cuadro de diálogo Show Values As de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto completo de resultados. Este formato mide cada valor únicamente contra el total general, por lo que no necesita campo base ni elemento base — los argumentos finales (`0`, `PivotItemPositionType.Previous`, `0`) son marcadores de posición que el formato ignora, según indica la tabla de parámetros anterior.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Obtener y configurar PivotField.getShowValuesSetting()**
Lea la configuración actual mediante `PivotField.getShowValuesSetting()`: el método de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro propiedades describen el cálculo activo de Show Values As. Para cambiar la configuración, llame al método `PivotField.showValuesAs` — escribe los cuatro ajustes en una sola llamada, de modo que nunca necesite asignar las propiedades una a una.  
El objeto `PivotShowValuesSetting` expone las cuatro propiedades que `showValuesAs` escribe:
- `getCalculationType()` devuelve el cálculo secundario `PivotFieldDataDisplayFormat`, mientras que `setCalculationType(...)` lo modifica.
- `getBaseFieldIndex()` y `setBaseFieldIndex(...)` especifican el índice base cero del campo base dentro de los campos de la tabla dinámica. Se utiliza en los formatos relativos a la base.
- `getBaseItemPositionType()` y `setBaseItemPositionType(...)` determinan cómo se posiciona el elemento base respecto al elemento actual y aceptan `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` y `setBaseItemIndex(...)` especifican el índice base cero del elemento base y se usan cuando `BaseItemPositionType` es `Custom`.
Después de llamar a `showValuesAs`, invoque `PivotTable.calculateData()` nuevamente para que el cuerpo de la tabla dinámica se recalcule y vuelva a renderizarse con la configuración actualizada.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Artículos relacionados**
- [Administrar campos de valores en tabla dinámica](/cells/es/python-java/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/python-java/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}