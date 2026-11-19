---
title: Mostrar valores como en una tabla dinámica
linktitle: Mostrar valores como en una tabla dinámica
description: Muestre los valores de los campos de datos de una tabla dinámica como porcentaje del total, diferencia respecto a un elemento base, totales acumulados, clasificaciones y más con Aspose.Cells for .Net.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /es/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica normalmente agrega cada campo de datos mediante una función de agregación como `Sum` o `Count`. La característica **Mostrar valores como** de Excel sustituye cada resultado mostrado por un cálculo secundario derivado de esa agregación; por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o una clasificación, lo que permite realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.
Entre los usos habituales se encuentran el análisis de participación en el total, incluidos los porcentajes del total de una fila, una columna o del total general; los informes acumulativos que utilizan un total acumulado en un campo de período; el análisis de variaciones frente a un elemento de referencia mediante la diferencia o la diferencia porcentual respecto a un elemento base; y la clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for .Net, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. La propiedad de solo lectura `PivotField.ShowValuesSetting` devuelve un objeto `PivotShowValuesSetting`, cuyas propiedades `ShowValuesAs`, `BaseFieldIndex` y `BaseItemIndex` permiten configurar el comportamiento; el método auxiliar `PivotField.ShowValuesAs(...)` aplica la misma configuración en una sola llamada. Aplique esta configuración a un campo de datos o de valor obtenido de `PivotTable.DataFields`.

## **Miembros de la enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como `Sum` o `Count`, mientras que Mostrar valores como transforma únicamente la forma en que se muestra el valor agregado.
Además de establecer directamente las propiedades de `PivotShowValuesSetting` (consulte la última sección), existe un método auxiliar que aplica la misma configuración en una sola llamada. Este método dispone de dos sobrecargas: una permite especificar el campo base y el elemento base por índice y la otra, por nombre:

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Parámetro | Significado | Cuándo es obligatorio |
| --- | --- | --- |
| `showValuesAsType` | Cálculo secundario `PivotShowValuesAsType` que se debe aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base) o, en la sobrecarga de cadena, el nombre del campo base. | Los ocho formatos relativos a la base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`); pase `0` (o `null` en la sobrecarga de cadena) para cualquier otro formato. |
| `baseItem` | Índice basado en cero del elemento base, con dos valores centinela: `PivotShowValuesSetting.PreviousPivotItem` (-1) selecciona el elemento anterior y `PivotShowValuesSetting.NextPivotItem` (-2), el siguiente. La sobrecarga de cadena acepta en su lugar el rótulo del elemento base y `null` cuando el formato seleccionado no necesita ningún elemento base. | Solo los tres formatos de elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) evalúan el elemento base; los cinco formatos relativos al campo (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, ambas clasificaciones) lo omiten: pase `0` o `null`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | Sin cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o los valores centinela anterior/siguiente) |
| `PercentageOf` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o los valores centinela anterior/siguiente) |
| `PercentageDifferenceFrom` | Muestra el valor como diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o los valores centinela anterior/siguiente) |
| `RunningTotalIn` | Muestra el valor como total acumulado para elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos determina la acumulación) |
| `PercentageOfRow` | Muestra el valor como porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como porcentaje del total general. | — |
| `Index` | Muestra el valor mediante la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como porcentaje del total de su fila principal (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como porcentaje del total de su columna principal (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como porcentaje del total de su elemento principal. | `baseField` (el campo principal cuyo total sirve de referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Establece la clasificación del valor, de menor (1) a mayor. | `baseField` (el campo cuyos elementos definen el ámbito de la clasificación) |
| `RankLargestToSmallest` | Establece la clasificación del valor, de mayor (1) a menor. | `baseField` (el campo cuyos elementos definen el ámbito de la clasificación) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` establece el estado de `PivotShowValuesSetting` (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`); el método y el objeto de propiedades son dos formas de configurar el mismo estado, equivalentes a los controles de selección del campo base y del elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.ShowValuesAs` con `PivotShowValuesAsType.PercentageOfTotal` para convertir cada celda de los campos de datos, incluida la celda del total general, en su participación en el total general. Por tanto, los números mostrados representan proporciones del conjunto completo de resultados. Este formato mide cada valor únicamente respecto del total general, por lo que no necesita ningún campo base ni elemento base; los argumentos finales (`0`, `0`) son valores de relleno que el formato ignora, tal como se indica en la tabla de parámetros anterior.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtener y configurar PivotField.ShowValuesSetting**
Lea la configuración actual mediante `PivotField.ShowValuesSetting`: la propiedad de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas propiedades describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.ShowValuesAs`: el método establece toda la configuración en una sola llamada, por lo que no es necesario asignar las propiedades una por una.
El objeto `PivotShowValuesSetting` expone el estado que establece `ShowValuesAs`:
- `ShowValuesAs` selecciona el cálculo secundario `PivotShowValuesAsType`.
- `BaseFieldIndex` especifica el índice basado en cero del campo base entre los campos de la tabla dinámica. Se utiliza en los formatos relativos a la base.
- `BaseItemIndex` especifica el elemento base: un índice basado en cero de un elemento específico de la tabla dinámica, o uno de los dos valores centinela: `PivotShowValuesSetting.PreviousPivotItem` (-1) para el elemento anterior y `PivotShowValuesSetting.NextPivotItem` (-2) para el siguiente. Se utiliza en los formatos de elemento base.
- `BaseFieldName` y `BaseItemCaption` son vistas de solo lectura que devuelven el nombre resuelto del campo base y el rótulo resuelto del elemento base, respectivamente; por ejemplo, después de seleccionar el valor centinela correspondiente al elemento anterior, `BaseItemCaption` devuelve `(previous)`.
Después de llamar a `ShowValuesAs`, llame de nuevo a `PivotTable.CalculateData()` para que el cuerpo de la tabla dinámica se recalcule y se regenere con la configuración actualizada.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Artículos relacionados**
- [Administrar campos de valor en una tabla dinámica](/cells/es/net/manage-value-fields/)
- [Trabajar con formatos de visualización de datos de DataField en una tabla dinámica](/cells/es/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/net/refresh-pivot-table/)
- [Aplicar estilo a una tabla dinámica](/cells/es/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}