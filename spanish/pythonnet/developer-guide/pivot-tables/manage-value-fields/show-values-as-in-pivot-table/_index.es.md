---
title: Mostrar Valores Como en Tabla Dinámica
linktitle: Mostrar Valores Como en Tabla Dinámica
description: Mostrar los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rankings y más con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /es/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La característica **Mostrar Valores Como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación; por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o una clasificación, lo que permite realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de una fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variación frente a un elemento de referencia mediante diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Python via .NET, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. La propiedad de solo lectura `PivotField.show_values_setting` devuelve un objeto `PivotShowValuesSetting`, cuyas propiedades escribibles `show_values_as`, `base_field_index` y `base_item_index` configuran el comportamiento; el método de conveniencia `PivotField.show_values_as(...)` aplica la misma configuración en una sola llamada. Aplique estas configuraciones a un campo de datos o de valor obtenido de `PivotTable.data_fields`.

## **Miembros de la Enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como `SUM` o `COUNT`, mientras que Mostrar Valores Como transforma solo la forma en que se muestra el valor agregado.  
Además de escribir directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración. Existe en dos formas: una que dirige el campo base y el elemento base por índice y otra por nombre:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Parámetro | Significado | Cuándo se Requiere |
| --- | --- | --- |
| `show_values_as_type` | El cálculo secundario `PivotShowValuesAsType` a aplicar. | Siempre. |
| `base_field` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base), o — en la forma por nombre — el nombre del campo base. | Los ocho formatos basados en el elemento base que aparecen a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); use `0` (o `None` en la forma por nombre) para cualquier otro formato. |
| `base_item` | Índice basado en cero del elemento base, con dos sentinelas: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) selecciona el elemento anterior y `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) el siguiente. La forma por nombre toma el texto del elemento base, o `None` cuando el formato seleccionado no necesita elemento base. | Solo los tres formatos de elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) evalúan el elemento base; los cinco formatos relativos al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, ambas clasificaciones) lo ignoran — use `0` o `None`. |

| Tipo de Cálculo | Comportamiento | Parámetros del Elemento Base |
| --- | --- | --- |
| `NORMAL` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `base_field` + `base_item` (índice o nombre, o el sentinela anterior/siguiente) |
| `PERCENTAGE_OF` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `base_field` + `base_item` (índice o nombre, o el sentinela anterior/siguiente) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `base_field` + `base_item` (índice o nombre, o el sentinela anterior/siguiente) |
| `RUNNING_TOTAL_IN` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `base_field` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como un porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total fila * total columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como un porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como un porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como un porcentaje de su total padre. | `base_field` (el campo padre cuyo total sirve de referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `base_field` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | `base_field` (el campo cuyos elementos definen el alcance de la clasificación) |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | `base_field` (el campo cuyos elementos definen el alcance de la clasificación) |

{{% alert color="primary" %}}
`show_values_as(...)` escribe las propiedades del objeto `PivotShowValuesSetting` (`show_values_as`, `base_field_index`, `base_item_index`); el método y el objeto de propiedades son dos formas de configurar el mismo estado, replicando los selectores de campo base y elemento base del cuadro de diálogo Mostrar Valores Como de Excel.
{{% /alert %}}

## **Mostrar Valores Como Porcentaje del Total**
Llame al método `PivotField.show_values_as` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto completo de resultados. Este formato mide cada valor solo contra el total general, por lo que no necesita campo base ni elemento base; los argumentos finales (`0`, `0`) son marcadores que el formato ignora, según indica la tabla de parámetros anterior.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Obtener y Configurar PivotField.show_values_setting**
Lea la configuración actual mediante `PivotField.show_values_setting`: la propiedad de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas propiedades describen el cálculo activo de Mostrar Valores Como. Para cambiar la configuración, llame al método `PivotField.show_values_as`; escribe todas las configuraciones en una sola llamada, de modo que nunca necesite asignar las propiedades una a una.  
El objeto `PivotShowValuesSetting` expone el estado que escribe `show_values_as`:
- `show_values_as` selecciona el cálculo secundario `PivotShowValuesAsType`.  
- `base_field_index` especifica el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos al elemento base.  
- `base_item_index` especifica el elemento base: un índice basado en cero de un elemento pivot concreto, o uno de los dos sentinelas — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) para el elemento anterior, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) para el siguiente. Se usa en los formatos de elemento base.  
- `base_field_name` y `base_item_caption` son vistas de solo lectura que informan el nombre del campo base y el texto del elemento base resueltos; por ejemplo, después de seleccionar el sentinela de elemento anterior, `base_item_caption` muestra `(previous)`.  
Después de llamar a `show_values_as`, invoque `PivotTable.calculate_data()` nuevamente para que el cuerpo de la tabla dinámica se vuelva a calcular y renderizar con la configuración actualizada.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Artículos Relacionados**
- [Administrar Campos de Valor en Tabla Dinámica](/cells/es/python-net/manage-value-fields/)
- [Actualizar Tabla Dinámica](/cells/es/python-net/refresh-pivot-table/)
- [Aplicar Estilo a Tabla Dinámica](/cells/es/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}