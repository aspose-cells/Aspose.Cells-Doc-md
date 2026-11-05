---
title: Agregar Formato Condicional a una Tabla Dinámica
linktitle: Agregar Formato Condicional a una Tabla Dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for Go via C++ - anclar una regla a la región de datos con ApplyTo y un alcance PivotConditionFormatScopeType, o definir el objetivo con AddCellArea y PivotAreas, luego adjuntar reglas y estilos mediante FormatConditions.AddCondition.
keywords: Aspose.Cells, tabla dinámica, formato condicional, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /es/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una sola vez y mantiene su estilo sin importar los valores. El formato condicional es la contrapartida basada en reglas: resaltar cada monto superior a 200, sombrear el cincuenta por ciento intermedio o marcar los elementos con menor rango, y el resaltado sigue a los valores cada vez que la tabla dinámica se recalcula o actualiza.  
En Aspose.Cells, el formato condicional de una tabla dinámica reside en la colección `PivotTable.ConditionalFormats`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región objetivo se define ya sea a través de `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, que refleja el selector de alcance de la interfaz de usuario de Excel, o mediante `AddCellArea(CellArea)` y la colección `PivotAreas`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Una o más condiciones se agregan a `FormatConditions` con `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, y cada condición lleva su propio `Style`.

{{% alert color="primary" %}}
No llame a `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ni a `FormatConditionCollection.AddArea(CellArea)` sobre el objeto `FormatConditions` de un formato condicional de pivote. Estas dos sobrecargas se heredan de la API de formato condicional de hoja de cálculo ordinaria y no funcionan para tablas dinámicas: el área de celdas nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Siempre defina la región en el propio `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` o `PivotAreas`) y agregue la regla con una de las sobrecargas `AddCondition`.
{{% /alert %}}

## **Aplicar una Regla con un Alcance (de la Interfaz de Excel)**
La primera forma posiciona la regla como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se identifica por sus coordenadas de hoja de cálculo basadas en cero, y un alcance `PivotConditionFormatScopeType` le indica an Aspose.Cells hasta dónde debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType.Data` – todas las celdas de valores que produce la tabla dinámica, incluidos los totales generales.  
- `PivotConditionFormatScopeType.Field` – las celdas de valores que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila de campo; pasar una celda de valor genera una excepción.  
- `PivotConditionFormatScopeType.Selection` – solo las celdas de valores en la intersección que la celda selecciona, típicamente una única celda de valor.  
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el alcance `Data`, y resalta cada monto mayor a 200 en blanco negrita sobre rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla colorea F4, F5 y F7; la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	a1, _ := cells.Get_String("A1")
	a1.PutValue_String("Fruit")
	b1, _ := cells.Get_String("B1")
	b1.PutValue_String("Year")
	c1, _ := cells.Get_String("C1")
	c1.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(2))
		amountCell.PutValue_Int(amounts[i])
	}
	// Tabla dinámica con su esquina superior izquierda en E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance de Datos
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Regla - resaltar cantidades mayores a 200
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_GreaterThan,
		"200",
		"",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsBold(true)
	white, _ := Color_FromArgb(int32(-1))
	red, _ := Color_FromArgb(int32(-65536))
	font.SetColor(white)
	style.SetForegroundColor(red)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatData.xlsx")
}
```

Anclar la misma regla en la etiqueta de fila‑campo E4 (fila 3, columna 4) con el alcance `Field` se resuelve en F4:F6 en su lugar: la misma columna de datos pero sin la fila de total general, porque el alcance ahora describe el campo `Fruit` en lugar de todo el área de valores. El alcance `Selection` anclado en F4 se resuelve únicamente en F4.

## **Definir la Región Manualmente**
La segunda forma omite el selector de alcance y nombra la región explícitamente en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con AddCellArea**
`AddCellArea(CellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado, sin expansión a la columna de datos y sin lógica de totales generales. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Year")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Amount")
	for i := range fruits {
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(0))
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(1))
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Apunta al rectángulo F4:F6 (las celdas de valor sin el total general)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Regla - cursiva en amarillo claro para montos entre 150 y 300
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_Between,
		"150",
		"300",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsItalic(true)
	lightYellow, _ := Color_FromArgb(int32(0xFFFFE0))
	style.SetForegroundColor(lightYellow)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatCellArea.xlsx")
}
```

### **Una región pivote semántica con PivotAreas**
`PivotAreas` es el mismo modelo de región semántica que la página hermana utiliza para estilos estáticos. Cree un `PivotArea`, seleccione un campo o región con `Select` o `SelectField`, y agréguelo con `PivotAreas.AddPivotArea(PivotArea)`. Una región semántica permanece adjunta a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `PivotAreas.Add(PivotArea)` aún compila pero está marcada como obsoleta; prefiera `AddPivotArea`.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Crear un nuevo libro de trabajo
	workbook, _ := NewWorkbook()
	// Obtener la primera hoja de cálculo
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Obtener la colección de celdas
	cells, _ := sheet.GetCells()
	// Arreglos de datos
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Escribir encabezados
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Escribir filas de datos
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Crear tabla dinámica
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Añadir campos a la tabla dinámica
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Adjuntar formato condicional al campo de datos Amount
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Definir el área de tabla dinámica que cubre el campo de datos Amount
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Añadir una condición: texto gris para cantidades menores a 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // segunda fórmula nula
	)
	// Crear estilo con color de fuente gris
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Aplicar estilo a la condición
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Guardar el libro de trabajo
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **Dónde se Almacenan las Reglas y Cómo Persisten tras una Recarga**
Cada llamada a `ConditionalFormats.Add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; al volver a abrir el archivo en el ejemplo siguiente se muestran la misma regla con su tipo, operador y fórmula intactos, y `GetCellAreas()` informa de las mismas regiones. Las entradas que nunca recibieron una condición se descartan al guardar el libro de trabajo, de la misma forma que Excel elimina un formato condicional sin regla.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("PivotConditionalFormatData.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	conditionalFormatCount, _ := conditionalFormats.GetCount()
	fmt.Printf("Conditional formats: %d\n", conditionalFormatCount)
	for i := int32(0); i < conditionalFormatCount; i++ {
		format, _ := conditionalFormats.Get(i)
		formatConditions, _ := format.GetFormatConditions()
		formatConditionCount, _ := formatConditions.GetCount()
		for j := int32(0); j < formatConditionCount; j++ {
			condition, _ := formatConditions.Get(j)
			conditionType, _ := condition.GetType()
			operatorType, _ := condition.GetOperator()
			formula1, _ := condition.GetFormula1()
			conditionTypeName := fmt.Sprintf("%v", conditionType)
			if int32(conditionType) == int32(FormatConditionType_CellValue) {
				conditionTypeName = "CellValue"
			}
			operatorTypeName := fmt.Sprintf("%v", operatorType)
			if int32(operatorType) == int32(OperatorType_GreaterThan) {
				operatorTypeName = "GreaterThan"
			}
			fmt.Printf("Format %d: %s %s formula1=%s\n",
				i, conditionTypeName, operatorTypeName, formula1)
		}
		areas, _ := format.GetCellAreas()
		for _, area := range areas {
			startRow, _ := area.Get_StartRow()
			endRow, _ := area.Get_EndRow()
			startColumn, _ := area.Get_StartColumn()
			endColumn, _ := area.Get_EndColumn()
			fmt.Printf("    rows %d-%d, columns %d-%d\n",
				startRow+1, endRow+1, startColumn+1, endColumn+1)
		}
	}
	// Esto imprime:
	// Conditional formats: 1
	// Format 0: CellValue GreaterThan formula1==200
	//     rows 4-7, columns 6-6        (F4:F7, la región de datos resuelta)
}
```

## **Artículos Relacionados**
- [Formato de una Parte de la Tabla Dinámica](/cells/es/go-cpp/format-part-of-pivot-table/)
- [Top 10 Mostrar o Filtrar en Tabla Dinámica](/cells/es/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}