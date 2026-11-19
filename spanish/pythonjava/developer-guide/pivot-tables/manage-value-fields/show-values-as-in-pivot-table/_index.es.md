---
title: Mostrar Valores Como en una Tabla Dinámica
linktitle: Mostrar Valores Como en una Tabla Dinámica
description: Muestra los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /es/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La característica **Show Values As** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación — por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido, o un rango — para que pueda realizar análisis comparativo sin fórmulas auxiliares o columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, incluyendo porcentajes de una fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variación contra un elemento de referencia usando diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Python via Java, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. El método de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `setShowValuesAs(...)`, `setBaseFieldIndex(...)` y `setBaseItemIndex(...)` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica la misma configuración en una única llamada. Aplique estas configuraciones a un campo de datos o de valor obtenido de `PivotTable.getDataFields()`.

## **Miembros de la Enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como `SUM` o `COUNT`, mientras que Show Values As transforma sólo cómo se muestra el valor agregado.  
Además de usar directamente los setters de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una llamada aplica la misma configuración. Viene en dos formas — una que dirige el campo base y el elemento base por índice, y otra por nombre:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Parámetro | Significado | Cuándo es requerido |
| --- | --- | --- |
| `show_values_as_type` | El cálculo secundario `PivotShowValuesAsType` a aplicar. | Siempre. |
| `base_field` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base), o — en la forma por nombre — el nombre del campo base. | Los ocho formatos relativos al base a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_SMALLEST_TO_LARGEST`); pase `0` (o `None` en la forma por nombre) para cualquier otro formato. |
| `base_item` | Índice basado en cero del elemento base, con dos centinelas: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) selecciona el elemento anterior y `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) el siguiente. La forma por nombre toma la leyenda del elemento base en su lugar, y `None` cuando el formato seleccionado no necesita elemento base. | Sólo los tres formatos de elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) evalúan el elemento base; los cinco formatos relativos al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, ambos rangos) lo ignoran — pase `0` o `None`. |

| Tipo de Cálculo | Comportamiento | Parámetros del Elemento Base |
| --- | --- | --- |
| `NORMAL` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `base_field` + `base_item` (un índice o leyenda, o el centinela anterior/siguiente) |
| `PERCENTAGE_OF` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `base_field` + `base_item` (un índice o leyenda, o el centinela anterior/siguiente) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `base_field` + `base_item` (un índice o leyenda, o el centinela anterior/siguiente) |
| `RUNNING_TOTAL_IN` | Muestra el valor como un total acumulado para elementos sucesivos de un campo base. | `base_field` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como un porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como un porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como un porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como un porcentaje de su total padre. | `base_field` (el campo padre cuyo total es la referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `base_field` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Ordena el valor de menor (1) a mayor. | `base_field` (el campo cuyos elementos definen el alcance de la clasificación) |
| `RANK_LARGEST_TO_SMALLEST` | Ordena el valor de mayor (1) a menor. | `base_field` (el campo cuyos elementos definen el alcance de la clasificación) |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe los valores de `PivotShowValuesSetting` a través de `setShowValuesAs`, `setBaseFieldIndex` y `setBaseItemIndex` — el método y el objeto de configuración son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base en el cuadro de diálogo Mostrar Valores Como de Excel.
{{% /alert %}}

## **Mostrar Valores como Porcentaje del Total**
Llame al método `PivotField.showValuesAs` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados se leen así como proporciones del conjunto de resultados completo. Este formato mide cada valor solo contra el total general, por lo que no necesita campo base ni elemento base — los argumentos finales (`0`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **Obtener y Configurar PivotField.getShowValuesSetting()**
Lea la configuración actual mediante `PivotField.getShowValuesSetting()`: el método de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas propiedades describen el cálculo activo de Mostrar Valores Como. Para cambiar la configuración, llame al método `PivotField.showValuesAs` — escribe todas las configuraciones en una sola llamada, por lo que nunca necesita establecer las propiedades una a una.  
El objeto `PivotShowValuesSetting` expone el estado que `showValuesAs` escribe:
- `getShowValuesAs()` devuelve el cálculo secundario `PivotShowValuesAsType`, mientras que `setShowValuesAs(...)` lo modifica.
- `getBaseFieldIndex()` y `setBaseFieldIndex(...)` especifican el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Se utiliza en los formatos relativos al campo base.
- `getBaseItemIndex()` y `setBaseItemIndex(...)` especifican el elemento base: un índice basado en cero de un elemento pivot específico, o uno de los dos centinelas — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) para el elemento anterior, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) para el siguiente. Se utiliza en los formatos de elemento base.
- `getBaseFieldName()` y `getBaseItemCaption()` son vistas de solo lectura que informan el nombre del campo base resuelto y la leyenda del elemento base; por ejemplo, después de seleccionar el centinela de elemento anterior, `getBaseItemCaption()` devuelve `(previous)`.
- Después de llamar a `showValuesAs`, llame nuevamente a `PivotTable.calculateData()` para que el cuerpo de la tabla dinámica se vuelva a calcular y renderizar con la configuración actualizada.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **Artículos Relacionados**
- [Gestionar Campos de Valor en Tabla Dinámica](/cells/es/python-java/manage-value-fields/)
- [Actualizar Tabla Dinámica](/cells/es/python-java/refresh-pivot-table/)
- [Aplicar Estilo a Tabla Dinámica](/cells/es/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}