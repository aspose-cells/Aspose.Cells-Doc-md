---
title: Mostrar valores como en tabla dinámica
linktitle: Mostrar valores como en tabla dinámica
description: Muestra los valores de los campos de datos de una tabla dinámica como porcentaje del total, diferencia respecto a un elemento base, totales acumulados, clasificaciones y más con Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /es/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `SUM` o `COUNT`. La función **Mostrar valores como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación — por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o una clasificación — de modo que puedas realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, incluidos porcentajes de fila, columna o total general; informes acumulativos usando un total en curso en un campo de período; análisis de variación contra un elemento de referencia usando diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Node.js via Java, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. El método de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `setShowValuesAs()`, `setBaseFieldIndex()` y `setBaseItemIndex()` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica la misma configuración en una sola llamada. Aplica estas configuraciones a un campo de datos o de valor obtenido mediante `PivotTable.getDataFields()`.

## **Miembros de la enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como SUM o COUNT, mientras que **Mostrar valores como** transforma únicamente la forma en que se muestra el valor agregado.  
Además de usar directamente los setters de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración. Existe en dos formas: una que aborda el campo base y el elemento base por índice, y otra por nombre:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Parámetro | Significado | Cuándo es necesario |
| --- | --- | --- |
| `showValuesAsType` | El cálculo secundario `PivotShowValuesAsType` a aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base), o — en la forma por nombre — el nombre del campo base. | Los ocho formatos relativos al base que aparecen a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_SMALLEST_TO_SMALLEST`); pasar `0` (o `null` en la forma por nombre) para cualquier otro formato. |
| `baseItem` | Índice basado en cero del elemento base, con dos valores centinela: -1 selecciona el elemento anterior y -2 el siguiente (el paquete raíz no exporta las constantes de `PivotShowValuesSetting`; pasar los valores literales). La forma por nombre utiliza la leyenda del elemento base y `null` cuando el formato seleccionado no necesita elemento base. | Solo los tres formatos basados en elemento (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) evalúan el elemento base; los cinco formatos relativos al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, ambos rangos) lo ignoran — pasar `0` o `null`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `NORMAL` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o leyenda, o el centinela anterior/siguiente) |
| `PERCENTAGE_OF` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o leyenda, o el centinela anterior/siguiente) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o leyenda, o el centinela anterior/siguiente) |
| `RUNNING_TOTAL_IN` | Muestra el valor como total acumulado para elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como porcentaje del total de fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como porcentaje del total de columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula de índice de Excel ((valor × total general) / (total de fila × total de columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como porcentaje de su total padre. | `baseField` (el campo padre cuyo total es la referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | `baseField` (el campo cuyos elementos definen el alcance de la clasificación) |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | `baseField` (el campo cuyos elementos definen el alcance de la clasificación) |

{{% alert color="primary" %}}
`showValuesAs(...)` escribe el estado de `PivotShowValuesSetting` mediante `setShowValuesAs()`, `setBaseFieldIndex()` y `setBaseItemIndex()` — el método y el objeto de propiedad son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base del cuadro de diálogo **Mostrar valores como** de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llama al método `PivotField.showValuesAs()` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su parte del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto completo de resultados. Este formato mide cada valor únicamente contra el total general, por lo que no necesita campo base ni elemento base — los argumentos finales (`0`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtener y configurar PivotField.getShowValuesSetting()**
Lee la configuración actual mediante `PivotField.getShowValuesSetting()`: el método de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas configuraciones describen el cálculo activo de **Mostrar valores como**. Para cambiar la configuración, llama al método `PivotField.showValuesAs()` — escribe todas las configuraciones en una sola llamada, de modo que nunca necesites establecerlas una a una.  
El objeto `PivotShowValuesSetting` expone el estado que escribe `showValuesAs()`:
- `getShowValuesAs()` / `setShowValuesAs()` selecciona el cálculo secundario `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` especifica el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Es utilizado por los formatos relativos al campo base.
- `getBaseItemIndex()` / `setBaseItemIndex()` especifica el elemento base: un índice basado en cero de un elemento pivot específico, o uno de los dos valores centinela — -1 para el elemento anterior, -2 para el siguiente (el paquete raíz no exporta las constantes con nombre). Es usado por los formatos basados en elemento.
- `getBaseFieldName()` y `getBaseItemCaption()` son vistas de solo lectura que informan el nombre del campo base resuelto y la leyenda del elemento base; por ejemplo, después de seleccionar el centinela de elemento anterior, `getBaseItemCaption()` devuelve `(previous)`.
Después de llamar a `showValuesAs()`, vuelve a llamar a `PivotTable.calculateData()` para que el cuerpo de la tabla dinámica se recalcule y se vuelva a renderizar con la configuración actualizada.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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
- [Administrar campos de valor en tabla dinámica](/cells/es/nodejs-java/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/nodejs-java/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}