---
title: Formato de parte de una Tabla Dinámica
description: Formato de parte de una tabla dinámica en Aspose.Cells for Go via C++ mediante la aplicación de estilos a regiones semánticas PivotArea o rectángulos CellArea a través de PivotTable.Format, con los formatos almacenados en PivotTable.PivotFormats y preservados cuando se actualiza la tabla dinámica.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Go via C++, tabla dinámica, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /es/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
`PivotTable.FormatAll` aplica un único estilo a toda la tabla dinámica y se describe en la página principal. No distingue entre etiquetas, valores, totales o regiones particulares del informe.
En la práctica, solo una parte de la tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valor producidas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de elementos.
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de registros de estilo de celda ordinarios. Un formato de área de tabla dinámica permanece asociado a una región, como las etiquetas o los valores de datos de un campo, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Por otro lado, un estilo escrito directamente en una celda pertenece a esa posición de celda y no es rastreado por el modelo de tabla dinámica.
Aspose.Cells expone la familia completa de sobrecargas de `PivotTable.Format` para que estén disponibles ambos tipos de formato:
- `Format(PivotArea, Style)` ancla un estilo a una región semántica que se construye con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(CellArea, Style)` ancla un estilo a un rectángulo de la hoja de cálculo dentro de la tabla dinámica.
- `Format(int row, int column, Style)` apunta a una única celda.
- `FormatAll(Style)` formatea toda la tabla dinámica.

## **Formatear un Área de Tabla Dinámica**
El flujo de trabajo basado en áreas semánticas es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Cree un `PivotArea` con `NewPivotArea(pivotTable)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
1. Seleccione un campo por su posición basada en cero en un eje dado con `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LabelOnly` selecciona solo las etiquetas del campo.
   - `PivotTableSelectionType.DataOnly` selecciona solo las celdas de datos del campo.
1. Seleccione un campo por nombre con `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve a las celdas de valor producidas por los elementos de ese campo.
1. Cree un `Style` con `Workbook.CreateStyle()`, configure su fuente, color de primer plano y patrón de fondo sólido, y pase el estilo a `PivotTable.Format(area, style)`.
1. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.PivotFormats`.
1. Los formatos anclados al campo se aplican cuando se calculan los datos de la tabla dinámica. Por lo tanto, llame a `PivotTable.CalculateData()` después de aplicar los formatos para que los estilos se vuelvan visibles.
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilo a las etiquetas de fila `Fruit` con `PivotArea.Select` y `PivotTableSelectionType.LabelOnly`, aplica estilo a las celdas de valor producidas por ese mismo campo de fila con `PivotArea.SelectField`, y luego recalcula la tabla dinámica para que ambos estilos se apliquen.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	// Fruit sales data
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	a1Cell, _ := cells.Get_String("A1")
	a1Cell.PutValue_String("Fruit")
	b1Cell, _ := cells.Get_String("B1")
	b1Cell.PutValue_String("Year")
	c1Cell, _ := cells.Get_String("C1")
	c1Cell.PutValue_String("Amount")
	for i := 0; i < len(fruits); i++ {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), 0)
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), 1)
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), 2)
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivot table with its top-left corner at E3 (row 2, column 4)
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Bold yellow fill on the row field's label cells
	labelStyle, _ := workbook.CreateStyle()
	labelFont, _ := labelStyle.GetFont()
	labelFont.SetIsBold(true)
	yellow, _ := Color_Yellow()
	labelStyle.SetForegroundColor(yellow)
	labelStyle.SetPattern(BackgroundType_Solid)
	labelArea, _ := NewPivotArea(pivotTable)
	labelArea.Select(PivotFieldType_Row, 0, PivotTableSelectionType_LabelOnly)
	pivotTable.Format_PivotArea_Style(labelArea, labelStyle)
	// Light green fill on the value cells the row field produces
	valueStyle, _ := workbook.CreateStyle()
	lightGreen, _ := Color_LightGreen()
	valueStyle.SetForegroundColor(lightGreen)
	valueStyle.SetPattern(BackgroundType_Solid)
	valueArea, _ := NewPivotArea(pivotTable)
	valueArea.SelectField_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.Format_PivotArea_Style(valueArea, valueStyle)
	// Field-anchored formats are painted when the data is calculated
	pivotTable.CalculateData()
	// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
	workbook.Save_String("FormatPivotArea.xlsx")
}
```

## **Formatear un Área de Celdas de la Tabla Dinámica**
Utilice `PivotTable.Format(CellArea, Style)` cuando la región de interés sea un simple rectángulo de hoja de cálculo en lugar de una región semántica de tabla dinámica.
Un `CellArea` se describe mediante sus valores `StartRow`, `EndRow`, `StartColumn` y `EndColumn`, establecidos a través de los accesores correspondientes estilo `Set_StartRow`. Los valores son coordenadas de hoja de cálculo basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, de modo que el área cubre las celdas desde la posición inicial hasta la posición final inclusive.
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas inmediatamente. No se necesita otra llamada a `CalculateData()` para que el estilo aparezca.
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor juntas. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva, azul claro y guarda el libro de trabajo sin necesidad de recalcular.

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
	years := []int{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int{100, 150, 120, 180, 90, 110}
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
		cell.PutValue_Int(int32(years[i]))
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(int32(amounts[i]))
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Highlight the first two fruit rows (the rectangle E4:F5)
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// E4:F5 is italic on light blue immediately, no recalculation needed
	workbook.Save_String("FormatPivotCellArea.xlsx")
}
```

## **Cómo se Mapean las Áreas de Tabla Dinámica y las Áreas de Celdas**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros de estilo de celda ordinarios. Aspose.Cells utiliza el mismo modelo, por lo que una solicitud de formato se traduce en áreas de tabla dinámica cuando se registra.
La relación entre el `CellArea` proporcionado por el usuario y las áreas de tabla dinámica almacenadas internamente es de muchos a muchos en ambas direcciones.
- Un `CellArea` puede generar varias áreas de tabla dinámica. Si el rectángulo abarca tanto celdas de etiqueta como celdas de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo de tabla dinámica trata el formato de etiquetas y el formato de datos de forma independiente.
- Una área de tabla dinámica puede resolverse en varias instancias `CellArea` disjuntas. Una región semántica como una fila de total general, o un campo cuyos elementos no son contiguos, puede cubrir varios rectángulos. Por eso `PivotArea.GetCellAreas()` devuelve una colección en lugar de un solo rectángulo.
Cada operación de formato realizada a través de `PivotTable.Format` se registra en `PivotTable.PivotFormats`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede añadir múltiples entradas.
Para distinguir las regiones almacenadas, cada `PivotArea` expone las banderas `OnlyLabel` y `OnlyData`. El ejemplo a continuación formatea un solo rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.PivotFormats` y muestra las coordenadas `CellArea` a las que cada área de tabla dinámica almacenada se resuelve.

```go
import (
	"fmt"
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
		cell, _ = cells.Get_Int_Int(int32(i+1), 0)
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 1)
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 2)
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	// ONE rectangle in...
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// ...TWO semantic pivot areas out: the label part and the data part are stored separately
	pivotFormats, _ := pivotTable.GetPivotFormats()
	formatCount, _ := pivotFormats.GetCount()
	fmt.Printf("Stored formats: %d\n", formatCount)
	for i := int32(0); i < int32(formatCount); i++ {
		pivotFormat, _ := pivotFormats.Get(i)
		storedArea, _ := pivotFormat.GetPivotArea()
		onlyLabel, _ := storedArea.GetOnlyLabel()
		onlyData, _ := storedArea.GetOnlyData()
		onlyLabelText := "False"
		if onlyLabel {
			onlyLabelText = "True"
		}
		onlyDataText := "False"
		if onlyData {
			onlyDataText = "True"
		}
		fmt.Printf("Format %d: OnlyLabel=%s, OnlyData=%s\n", i, onlyLabelText, onlyDataText)
		resolvedAreas, _ := storedArea.GetCellAreas()
		for _, resolved := range resolvedAreas {
			startRow, _ := resolved.Get_StartRow()
			endRow, _ := resolved.Get_EndRow()
			startColumn, _ := resolved.Get_StartColumn()
			endColumn, _ := resolved.Get_EndColumn()
			fmt.Printf(
				"    rows %d-%d, columns %d-%d\n",
				startRow+1,
				endRow+1,
				startColumn+1,
				endColumn+1,
			)
		}
	}
	// This prints:
	// Stored formats: 2
	// Format 0: OnlyLabel=True, OnlyData=False
	//     rows 4-5, columns 5-5        (E4:E5, the label part)
	// Format 1: OnlyLabel=False, OnlyData=True
	//     rows 4-5, columns 6-6        (F4:F5, the data part)
	workbook.Save_String("FormatPivotAreasMap.xlsx")
}
```

{{% alert color="primary" %}}
Debido a que los formatos se almacenan como áreas de tabla dinámica en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y a la actualización. Cuando la tabla dinámica se actualiza con `PivotTable.RefreshData`, se recalcula con `CalculateData` o se guarda y se vuelve a cargar, cada área de tabla dinámica almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` creado con `Select` o `SelectField` cuando un resaltado debe permanecer unido a un campo o a una región semántica a través de actualizaciones, y utilice un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `Format(int row, int column, Style)` apunta a una celda individual. Use `FormatAll`, descrito en la página principal, cuando toda la tabla dinámica deba volver a formatearse de una vez.

{{< app/cells/assistant language="go" >}}