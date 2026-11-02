---
title: Mostrar valores como en tabla dinámica
linktitle: Mostrar valores como en tabla dinámica
description: Muestre los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /es/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La función **Mostrar valores como** de Excel sustituye cada resultado mostrado por un cálculo secundario derivado de esa agregación —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o un rango— para que pueda realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de fila, columna o total general; informes acumulativos mediante un total acumulado en un campo de período; análisis de variación frente a un elemento de referencia usando diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Node.js via C++, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. El accesor de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos configurables `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` y `setBaseItemIndex()` establecen el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estos ajustes a un campo de datos o de valores obtenido mediante `PivotTable.getDataFields()`.

## **Miembros de enumeración PivotFieldDataDisplayFormat**
El campo de datos conserva su función de agregación, como SUM o COUNT, mientras que **Mostrar valores como** transforma solo la forma en que se muestra el valor agregado.  
Además de escribir directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTableIndex = pivotTables.add("A1:C7", 0, 4);
const pivotTable = pivotTables.get(pivotTableIndex);
pivotTable.getRowFields().add("Region");
pivotTable.getDataFields().add("Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| Parámetro | Significado | Cuándo es requerido |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` a aplicar. | Siempre. |
| `baseField` | Índice base‑cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base respecto al elemento actual: `PivotItemPositionType.PREVIOUS`, `.NEXT` o `.CUSTOM`. | Solo para los tres formatos con elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); los demás formatos lo ignoran. |
| `baseItem` | Índice base‑cero del elemento base. | Sólo cuando `baseItemPositionType` es `CUSTOM` (el índice del elemento selecciona el elemento base exacto); ignorado para `PREVIOUS` / `NEXT` y por cualquier formato que no sea de base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `NORMAL` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como el porcentaje de diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como un porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como un porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como un porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | — |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe los ajustes de `PivotShowValuesSetting` (`getCalculationType()`/`setCalculationType()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, `getBaseItemPositionType()`/`setBaseItemPositionType()`, y `getBaseItemIndex()`/`setBaseItemIndex()`) — el método y el objeto de propiedades son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base del cuadro de diálogo **Mostrar valores como** de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs()` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por tanto, se leen como proporciones del conjunto completo de resultados. Este formato mide cada valor solo frente al total general, por lo que no necesita campo base ni elemento base —los argumentos finales (`0`, `PivotItemPositionType.PREVIOUS`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
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
Lea la configuración actual mediante `PivotField.getShowValuesSetting()`: el accesor de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro propiedades describen el cálculo activo de **Mostrar valores como**. Para cambiar la configuración, llame al método `PivotField.showValuesAs()` —escribe los cuatro ajustes en una sola llamada, por lo que nunca necesita asignar las propiedades una a una.  
El objeto `PivotShowValuesSetting` expone los cuatro ajustes que `showValuesAs()` escribe:
- `getCalculationType()` y `setCalculationType()` seleccionan el cálculo secundario `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` y `setBaseFieldIndex()` especifican el índice base‑cero del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos a la base.
- `getBaseItemPositionType()` y `setBaseItemPositionType()` determinan cómo se posiciona el elemento base respecto al elemento actual y aceptan `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` y `setBaseItemIndex()` especifican el índice base‑cero del elemento base y se usan cuando `getBaseItemPositionType()` es `CUSTOM`.  
Después de llamar a `showValuesAs()`, invoque `PivotTable.calculateData()` nuevamente para que el cuerpo de la tabla dinámica se recalcule y vuelva a renderizarse con la configuración actualizada.

```javascript
const AsposeCells = require("aspose.cells.node");
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
    AsposeCells.Pivot.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.Pivot.PivotItemPositionType.Previous,
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
- [Administrar campos de valor en tabla dinámica](/cells/es/nodejs-cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}