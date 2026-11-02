---
title: Mostrar valores como en tabla dinámica
linktitle: Mostrar valores como en tabla dinámica
description: Muestra los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, clasificaciones y más con Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /es/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La función **Mostrar valores como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación — por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido, o una clasificación — lo que permite realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de una fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variaciones frente a un elemento de referencia mediante diferencia o diferencia porcentual; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Node.js via Java, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. El método de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`. Sus métodos `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` y `setBaseItemIndex()` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estos ajustes a un campo de datos o de valor obtenido mediante `PivotTable.getDataFields()`.

## **Miembros de la enumeración PivotFieldDataDisplayFormat**
El campo de datos conserva su función de agregación, como SUM o COUNT, mientras que Mostrar valores como transforma solo la forma en que se muestra el valor agregado.  
Además de escribir directamente los ajustes `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Parámetro | Significado | Cuándo es necesario |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` a aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base en relación al elemento actual: `PivotItemPositionType.PREVIOUS`, `.NEXT` o `.CUSTOM`. | Solo para los tres formatos con elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); los demás formatos lo ignoran. |
| `baseItem` | Índice basado en cero del elemento base. | Solo cuando `baseItemPositionType` es `CUSTOM` (el índice del elemento elige el elemento base exacto); se ignora para `PREVIOUS` / `NEXT` y en cualquier formato que no sea de elemento base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros de elemento base |
| --- | --- | --- |
| `NORMAL` | Sin cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Muestra el valor como un total acumulado para elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como un porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como un porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como un porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | — |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe los ajustes de `PivotShowValuesSetting` (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` y `setBaseItemIndex()`) — el método y el objeto de configuración son dos formas de establecer el mismo estado, replicando los selectores de campo base y elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs()` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su proporción del total general. Los números mostrados se interpretan así como proporciones del conjunto completo de resultados. Este formato mide cada valor sólo contra el total general, por lo que no necesita un campo base ni un elemento base — los argumentos finales (`0`, `PivotItemPositionType.PREVIOUS`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

```javascript
const AsposeCells = require("aspose.cells");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtener y configurar PivotField.getShowValuesSetting()**
Lea la configuración actual mediante `PivotField.getShowValuesSetting()`: el método de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyos cuatro ajustes describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.showValuesAs()` — escribe los cuatro ajustes en una sola llamada, por lo que nunca necesita asignarlos uno a uno.  
El objeto `PivotShowValuesSetting` expone los cuatro ajustes que escribe `showValuesAs()`:
- `getCalculationType()` / `setCalculationType()` selecciona el cálculo secundario `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` especifica el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos a la base.
- `getBaseItemPositionType()` / `setBaseItemPositionType()` determina cómo se posiciona el elemento base respecto al elemento actual y acepta `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex()` especifica el índice basado en cero del elemento base y se usa cuando `getBaseItemPositionType()` es `CUSTOM`.
Después de llamar a `showValuesAs()`, invoque nuevamente `PivotTable.calculateData()` para que el cuerpo de la tabla dinámica se recalcule y vuelva a renderizarse con la configuración actualizada.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Artículos relacionados**
- [Administrar campos de valor en tabla dinámica](/cells/es/nodejs-java/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/nodejs-java/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}