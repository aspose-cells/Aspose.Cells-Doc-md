---
title: Mostrar valores como en tabla dinámica
linktitle: Mostrar valores como en tabla dinámica
description: Mostrar valores de campos de datos de tabla dinámica como porcentaje del total, diferencia de un elemento base, totales acumulados, rangos y más con Aspose.Cells for Go via C++.
keywords: Aspose.Cells for Go via C++, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /es/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La característica **Mostrar valores como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación—por ejemplo, un porcentaje del total general, un total acumulado, una diferencia con un elemento base elegido o un rango—para que pueda realizar análisis comparativo sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, incluidos porcentajes de una fila, columna o total general; informes acumulativos usando un total acumulado en un campo de período; análisis de variación contra un elemento de referencia usando diferencia o diferencia porcentual de un elemento base; y ranking de valores de menor a mayor o de mayor a menor.  
En Aspose.Cells for Go via C++, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. El accesor `PivotField.GetShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` y `SetBaseItemIndex` configuran el comportamiento; el método de conveniencia `PivotField.ShowValuesAs(...)` aplica las mismas cuatro configuraciones en una sola llamada. Aplique estas configuraciones a un campo de datos o valor obtenido mediante `PivotTable.GetDataFields()`.

## **Miembros de enumeración PivotFieldDataDisplayFormat**
El campo de datos mantiene su función de agregación, como Sum o Count, mientras que Mostrar valores como transforma solo la forma en que se muestra el valor agregado.  
Además de escribir los valores `PivotShowValuesSetting` directamente (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Parámetro | Significado | Cuando es requerido |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` a aplicar. | Siempre. |
| `baseField` | Índice base cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base respecto al elemento actual: `PivotItemPositionType.Previous`, `.Next` o `.Custom`. | Solo para los tres formatos con elemento base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); los demás formatos lo ignoran. |
| `baseItem` | Índice base cero del elemento base. | Solo cuando `baseItemPositionType` es `Custom` (el índice del elemento elige el elemento base exacto); ignorado para `Previous` / `Next` y por cualquier formato que no sea de elemento base — pase `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `Normal` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DifferenceFrom` | Muestra el valor como diferencia del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageOf` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `PercentageDifferenceFrom` | Muestra el valor como la diferencia porcentual del valor de un elemento base en un campo base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` solo con `Custom`) |
| `RunningTotalIn` | Muestra el valor como total acumulado para elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PercentageOfRow` | Muestra el valor como porcentaje del total de la fila. | — |
| `PercentageOfColumn` | Muestra el valor como porcentaje del total de la columna. | — |
| `PercentageOfTotal` | Muestra el valor como porcentaje del total general. | — |
| `Index` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total de fila * total de columna)). | — |
| `PercentageOfParentRowTotal` | Muestra el valor como porcentaje del total de la fila padre (para campos de fila anidados). | — |
| `PercentageOfParentColumnTotal` | Muestra el valor como porcentaje del total de la columna padre (para campos de columna anidados). | — |
| `PercentageOfParentTotal` | Muestra el valor como porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PercentageOfRunningTotalIn` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RankSmallestToLargest` | Clasifica el valor de menor (1) a mayor. | — |
| `RankLargestToSmallest` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` escribe los valores de `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — el método y el objeto de configuración son dos formas de establecer el mismo estado, reflejando los selectores de campo base y elemento base en el cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.ShowValuesAs` con `PivotFieldDataDisplayFormat.PercentageOfTotal` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados se leen entonces como proporciones del conjunto de resultados completo. Este formato mide cada valor solo contra el total general, por lo que no necesita campo base ni elemento base; los argumentos finales (`0`, `PivotItemPositionType.Previous`, `0`) son marcadores de posición que el formato ignora, como indica la tabla de parámetros anterior.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **Obtener y configurar PivotField.ShowValuesSetting**
Lea la configuración actual mediante `PivotField.GetShowValuesSetting()`: el accesor devuelve el objeto `PivotShowValuesSetting` del campo, cuyos cuatro métodos getter describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.ShowValuesAs` — escribe los cuatro ajustes en una sola llamada, por lo que nunca necesita establecer los valores uno por uno.  
El objeto `PivotShowValuesSetting` expone los cuatro valores que escribe `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` seleccionan el cálculo secundario `PivotFieldDataDisplayFormat`.  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` especifican el índice base cero del campo base dentro de los campos de la tabla dinámica. Se usa en los formatos relativos a la base.  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` determinan cómo se posiciona el elemento base respecto al elemento actual y aceptan `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` o `PivotItemPositionType.Custom`.  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` especifican el índice base cero del elemento base y se usa cuando el tipo de posición es `Custom`.  
Después de llamar a `ShowValuesAs`, invoque `PivotTable.CalculateData()` nuevamente para que el cuerpo de la tabla dinámica se recalcule y se vuelva a renderizar con la configuración actualizada.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **Artículos relacionados**
- [Agrupar campos de pivote en la tabla dinámica](/cells/es/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Top 10 Mostrar o filtrar en tabla dinámica](/cells/es/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Actualización de Segmentador](/cells/es/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}