---
title: Mostrar Valores Como en Tabla Dinámica
linktitle: Mostrar Valores Como en Tabla Dinámica
description: Mostrar valores de campo de datos de tabla dinámica como un porcentaje del total, una diferencia de un elemento base, totales acumulados, rangos y más con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /es/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La función **Mostrar Valores Como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o un rango— para que pueda realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes por fila, columna o total general; informes acumulativos mediante un total acumulado en un campo de período; análisis de variación contra un elemento de referencia utilizando diferencia o diferencia porcentual; y clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for Python via .NET, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. La propiedad de solo lectura `PivotField.show_values_setting` devuelve un objeto `PivotShowValuesSetting`, cuyas propiedades editables `calculation_type`, `base_field_index`, `base_item_position_type` y `base_item_index` configuran el comportamiento; el método de conveniencia `PivotField.show_values_as(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estos ajustes a un campo de datos o de valores obtenido de `PivotTable.data_fields`.

## **Miembros de la Enumeración PivotFieldDataDisplayFormat**
El campo de datos mantiene su función de agregación, como `SUM` o `COUNT`, mientras que Mostrar Valores Como transforma solo la forma en que se muestra el valor agregado.  
Además de escribir directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una llamada aplica la misma configuración:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Parámetro | Significado | Cuándo es Requerido |
| --- | --- | --- |
| `display_format` | El cálculo secundario `PivotFieldDataDisplayFormat` a aplicar. | Siempre. |
| `base_field` | Índice base‑cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); los demás formatos lo ignoran. |
| `base_item_position_type` | Cómo se elige el elemento base respecto al elemento actual: `PivotItemPositionType.PREVIOUS`, `.NEXT` o `.CUSTOM`. | Solo para los tres formatos con elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); los demás formatos lo ignoran. |
| `base_item` | Índice base‑cero del elemento base. | Solo cuando `base_item_position_type` es `CUSTOM` (el índice del elemento elige el elemento base exacto); se ignora para `PREVIOUS` / `NEXT` y para todos los formatos que no son de elemento base — pase `0`. |

| Tipo de Cálculo | Comportamiento | Parámetros del Ítem Base |
| --- | --- | --- |
| `NORMAL` | No hay cálculo secundario; el valor agregado se muestra tal cual (valor predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como diferencia respecto al valor de un elemento base en un campo base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como diferencia porcentual respecto al valor de un elemento base en un campo base. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Muestra el valor como total acumulado para elementos sucesivos de un campo base. | `base_field` (el campo cuyo orden de ítems impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como porcentaje del total de la fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como porcentaje del total de la columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `base_field` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | — |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`show_values_as(...)` escribe las propiedades de `PivotShowValuesSetting` (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`); el método y el objeto de propiedades son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base del cuadro de diálogo Mostrar Valores Como de Excel.
{{% /alert %}}

## **Mostrar Valores como Porcentaje del Total**
Llame al método `PivotField.show_values_as` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto de resultados completo. Este formato mide cada valor únicamente contra el total general, por lo que no necesita campo base ni elemento base — los argumentos finales (`0`, `PivotItemPositionType.PREVIOUS`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
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
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **Obtener y Configurar PivotField.show_values_setting**
Lea la configuración actual mediante `PivotField.show_values_setting`: la propiedad de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro propiedades describen el cálculo activo de Mostrar Valores Como. Para cambiar la configuración, llame al método `PivotField.show_values_as`; escribe los cuatro ajustes en una sola llamada, por lo que nunca necesita asignar las propiedades una por una.  
El objeto `PivotShowValuesSetting` expone las cuatro propiedades que `show_values_as` escribe:
- `calculation_type` selecciona el cálculo secundario `PivotFieldDataDisplayFormat`.
- `base_field_index` especifica el índice base‑cero del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos a la base.
- `base_item_position_type` determina cómo se posiciona el elemento base respecto al elemento actual y acepta `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `base_item_index` especifica el índice base‑cero del elemento base y se usa cuando `base_item_position_type` es `CUSTOM`.
Después de llamar a `show_values_as`, invoque `PivotTable.calculate_data()` nuevamente para que el cuerpo de la tabla dinámica se recalcule y se vuelva a renderizar con la configuración actualizada.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **Artículos Relacionados**
- [Administrar Campos de Valor en Tabla Dinámica](/cells/es/python-net/manage-value-fields/)
- [Actualizar Tabla Dinámica](/cells/es/python-net/refresh-pivot-table/)
- [Aplicar Estilo a Tabla Dinámica](/cells/es/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}