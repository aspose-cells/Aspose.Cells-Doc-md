---
title: Mostrar valores como en Tabla Dinámica
linktitle: Mostrar valores como en Tabla Dinámica
description: Mostrar los valores del campo de datos de la tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for .NET.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /es/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La función **Mostrar valores como** de Excel sustituye cada resultado mostrado por un cálculo secundario derivado de esa agregación — por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido, o un rango — lo que permite realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes por fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variación frente a un elemento de referencia mediante diferencia o diferencia porcentual; y clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for .NET, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. La propiedad de solo lectura `PivotField.ShowValuesSetting` devuelve un objeto `PivotShowValuesSetting`, cuyas propiedades editables `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` y `BaseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.ShowValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estos ajustes a un campo de datos o de valor obtenido de `PivotTable.DataFields`.

## **Miembros de la enumeración PivotFieldDataDisplayFormat**
El campo de datos conserva su función de agregación, como Sum o Count, mientras que Mostrar valores como transforma solo la forma en que se muestra el valor agregado.  
Además de asignar directamente las propiedades de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Parámetro | Significado | Cuándo es obligatorio |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` que se aplicará. | Siempre. |
| `baseField` | Índice de base cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base respecto al elemento actual: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo para los tres formatos con elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); los demás formatos lo ignoran. |
| `baseItem` | Índice de base cero del elemento base. | Solo cuando `baseItemPositionType` es `Custom` (el índice del elemento selecciona el elemento base exacto); se ignora para `Previous` / `Next` y para cualquier formato que no sea base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Muestra el valor como diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Muestra el valor como total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total fila * total columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como porcentaje del total de su fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como porcentaje del total de su columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | — |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` escribe las propiedades de `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`); el método y el objeto de propiedad son dos formas de configurar el mismo estado, replicando los selectores de campo base y elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.ShowValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto de resultados completo. Este formato mide cada valor solo contra el total general, por lo que no necesita campo base ni elemento base; los argumentos finales (`0`, `PivotItemPositionType.Previous`, `0`) son marcadores de posición que el formato ignora, según indica la tabla de parámetros anterior.

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
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Obtener y configurar PivotField.ShowValuesSetting**
Lea la configuración actual a través de `PivotField.ShowValuesSetting`: la propiedad de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro propiedades describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.ShowValuesAs` — escribe los cuatro ajustes en una sola llamada, de modo que nunca necesite asignar las propiedades una por una.  
El objeto `PivotShowValuesSetting` expone las cuatro propiedades que `ShowValuesAs` escribe:
- `CalculationType` selecciona el cálculo secundario `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` especifica el índice de base cero del campo base dentro de los campos de la tabla dinámica. Se utiliza en los formatos relativos a la base.
- `BaseItemPositionType` determina cómo se posiciona el elemento base respecto al elemento actual y acepta `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.
- `BaseItemIndex` indica el índice de base cero del elemento base y se usa cuando `BaseItemPositionType` es `Custom`.
Después de llamar a `ShowValuesAs`, invoque `PivotTable.CalculateData()` nuevamente para que el cuerpo de la tabla dinámica se vuelva a calcular y renderizar con la configuración actualizada.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Artículos relacionados**
- [Administrar campos de valor en tabla dinámica](/cells/es/net/manage-value-fields/)
- [Trabajar con formatos de visualización de datos del DataField en tabla dinámica](/cells/es/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Actualizar tabla dinámica](/cells/es/net/refresh-pivot-table/)
- [Aplicar estilo a tabla dinámica](/cells/es/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}