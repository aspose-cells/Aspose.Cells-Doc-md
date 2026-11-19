---
title: Mostrar valores como en tabla dinámica
description: Muestra los valores de los campos de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for Node.js via C++
linktitle: Mostrar valores como
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /es/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La característica **Show Values As** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación —por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido, o un rango— para que puedas realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de fila, columna o total general; informes acumulativos mediante un total acumulado en un campo de período; análisis de variaciones frente a un elemento de referencia usando diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for Node.js via C++, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. El accesor de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `setShowValuesAs()`, `setBaseFieldIndex()` y `setBaseItemIndex()` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica la misma configuración en una única llamada. Aplica estas configuraciones a un campo de datos o de valor obtenido mediante `PivotTable.getDataFields()`.

## **Miembros de la enumeración PivotShowValuesAsType**
El campo de datos mantiene su función de agregación, como SUM o COUNT, mientras que **Show Values As** transforma solo la forma en que se muestra el valor agregado.  
Además de escribir directamente la configuración `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración. Está disponible en dos formas: una que usa el índice del campo base y del elemento base, y otra que usa el nombre:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parámetro | Significado | Cuándo es necesario |
| --- | --- | --- |
| `showValuesAsType` | El cálculo secundario `PivotShowValuesAsType` a aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base), o —en la forma por nombre— el nombre del campo base. | Los ocho formatos relativos al base a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); pasa `0` (o `null` en la forma por nombre) para cualquier otro formato. |
| `baseItem` | Índice basado en cero del elemento base, con dos valores centinela: -1 selecciona el elemento anterior y -2 el siguiente (la vinculación Node.js via C++ no exporta las constantes con nombre —pasa los valores literales). La forma por nombre toma el texto del elemento base, y `null` cuando el formato seleccionado no necesita un elemento base. | Solo los tres formatos que usan elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) evalúan el elemento base; los cinco formatos relativos al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, ambos rangos) lo ignoran —pasa `0` o `null`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | Sin cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o texto, o el centinela anterior/siguiente) |
| `PercentageOf` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o texto, o el centinela anterior/siguiente) |
| `PercentageDifferenceFrom` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o texto, o el centinela anterior/siguiente) |
| `RunningTotalIn` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como un porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como un porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como un porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo padre cuyo total es la referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | `baseField` (el campo cuyos elementos definen el ámbito de clasificación) |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | `baseField` (el campo cuyos elementos definen el ámbito de clasificación) |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe la configuración del objeto `PivotShowValuesSetting` (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, y `getBaseItemIndex()`/`setBaseItemIndex()`) — el método y el objeto de propiedad son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base del cuadro de diálogo **Show Values As** de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llama al método `PivotField.showValuesAs()` con `PivotShowValuesAsType.PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su parte del total general. Los números mostrados se interpretan entonces como proporciones del conjunto completo de resultados. Este formato mide cada valor únicamente contra el total general, por lo que no necesita campo base ni elemento base —los argumentos finales (`0`, `0`) son marcadores que el formato ignora, según indica la tabla de parámetros anterior.

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
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtener y configurar PivotField.getShowValuesSetting()**
Lee la configuración actual mediante `PivotField.getShowValuesSetting()`: el accesor de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas propiedades describen el cálculo activo de **Show Values As**. Para cambiar la configuración, llama al método `PivotField.showValuesAs()` —escribe todas las configuraciones en una única llamada, por lo que nunca necesitarás establecerlas una a una.  
El objeto `PivotShowValuesSetting` expone el estado que escribe `showValuesAs()`:
- `getShowValuesAs()` y `setShowValuesAs()` eligen el cálculo secundario `PivotShowValuesAsType`.
- `getBaseFieldIndex()` y `setBaseFieldIndex()` especifican el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Se utiliza en los formatos relativos al base.
- `getBaseItemIndex()` y `setBaseItemIndex()` especifican el elemento base: un índice basado en cero de un elemento pivot específico, o uno de los dos valores centinela — -1 para el elemento anterior, -2 para el siguiente (la vinculación no exporta las constantes con nombre). Se utiliza en los formatos relativos al elemento base.
- `getBaseFieldName()` y `getBaseItemCaption()` son vistas de solo lectura que informan el nombre del campo base resuelto y el texto del elemento base; por ejemplo, después de seleccionar el centinela de elemento anterior, `getBaseItemCaption()` devuelve `(previous)`.  
Después de llamar a `showValuesAs()`, vuelve a llamar a `PivotTable.calculateData()` para que el cuerpo de la tabla dinámica se recalcule y se vuelva a renderizar con la configuración actualizada.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Artículos relacionados**
- [Administrar campos de valor en tabla dinámica](/cells/es/nodejs-cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}