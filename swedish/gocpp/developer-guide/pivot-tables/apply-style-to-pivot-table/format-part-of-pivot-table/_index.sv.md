---
title: Formatera del av en pivottabell
linktitle: Formatera del av en pivottabell
description: Formatera en del av en pivottabell i Aspose.Cells for Go via C++ genom att tillämpa stilar på semantiska PivotArea‑regioner eller CellArea‑rektanglar via PivotTable.Format, med format lagrade i PivotTable.PivotFormats och bevarade när pivottabellen uppdateras
keywords: Aspose.Cells for Go via C++, pivottabell, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /sv/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.FormatAll` tillämpar ett enda format på hela pivottabellen och behandlas på föräldrasidan. Det skiljer inte mellan rubriker, värden, totaler eller specifika områden i rapporten.  
I praktiken behövs ofta bara en del av en pivottabell framhävas. Vanliga mål är rubriker som hör till ett radfält, värdeceller som produceras av ett fält, totalraden eller en godtycklig rektangel som de två första radposterna.  
Att tillämpa ett format direkt på cellerna i ett kalkylblad i en pivottabell är inte ekvivalent. Excel lagrar pivottabellens formatering som semantiska `PivotArea`‑regioner snarare än som vanliga cellformat‑poster. Ett `PivotArea`‑format är knutet till ett område såsom ett fälts rubriker eller datavärden och återupptas när pivottabellen beräknas om, uppdateras eller expanderas. Ett format som skrivs direkt till en cell tillhör den specifika cellpositionen och spåras inte av pivottabellmodellen.  
Aspose.Cells exponerar hela familjen av `PivotTable.Format`‑överladdningar så att båda formateringstyperna är tillgängliga:
- `Format(PivotArea, Style)` anknyter ett format till ett semantiskt område som byggs med `PivotArea.Select` eller `PivotArea.SelectField`.
- `Format(CellArea, Style)` anknyter ett format till en arbetsbladsrektangel inne i pivottabellen.
- `Format(int row, int column, Style)` riktar in sig på en enskild cell.
- `FormatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Det semantiska arbetsflödet för området är den rekommenderade metoden när en markering ska följa ett fält eller ett område i rapporten.  
1. Skapa en `PivotArea` med `NewPivotArea(pivotTable)`. Objektet beskriver ett semantiskt område som tillhör den specifika pivottabellen.  
1. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` väljer både fältets rubriker och data.  
   - `PivotTableSelectionType.LabelOnly` väljer endast fältets rubriker.  
   - `PivotTableSelectionType.DataOnly` väljer endast fältets dataceller.  
1. Välj ett fält efter namn med `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. När ett radfält väljs efter namn löser området upp till de värdeceller som produceras av fältets poster.  
1. Skapa ett `Style` med `Workbook.CreateStyle()`, konfigurera dess teckensnitt, förgrundsfärg och solid bakgrundsmönster, och skicka stilen till `PivotTable.Format(area, style)`.  
1. Varje anrop av `PivotArea`‑överladdningen lägger till ett `PivotTableFormat`‑objekt i `PivotTable.PivotFormats`.  
1. Fält‑anknutna format målas när pivottabellens data beräknas. Anropa därför `PivotTable.CalculateData()` efter att formaten har tillämpats så att stilarna blir synliga.  
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radens rubriker med `PivotArea.Select` och `PivotTableSelectionType.LabelOnly`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.SelectField` och beräknar sedan pivottabellen på nytt så att båda formaten appliceras.

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

## **Formatera ett Cell‑område i pivottabellen**
Använd `PivotTable.Format(CellArea, Style)` när området av intresse är en vanlig arbetsbladsrektangel snarare än ett semantiskt pivot‑område.  
Ett `CellArea` beskrivs av värdena `StartRow`, `EndRow`, `StartColumn` och `EndColumn`, som sätts via motsvarande `Set_StartRow`‑liknande åtkomstmetoder. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista raden och kolumnen som ingår i rektangeln, så att området omfattar cellerna från startpositionen till slutpositionen inklusivt.  
Till skillnad från ett fält‑anknutet format tillämpas ett `CellArea`‑format omedelbart på cellerna. Ett extra anrop av `CalculateData()` behövs inte för att formatet ska visas.  
Ett `CellArea`‑rektangel kan innehålla både rubrikceller och värdeceller. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.  
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan ytterligare omräkning.

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

## **Hur Pivot‑områden och Cell‑områden mappar**
Excel lagrar pivottabellens formatering som `pivotArea`‑poster snarare än som vanliga cell‑format‑poster i arbetsbladet. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivottabellsområden när den registreras.  
Relationen mellan det `CellArea` som användaren levererar och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan producera flera pivot‑områden. Om rektangeln spänner över både rubrikceller och värdeceller, dekomponeras den i separata rubrik‑ och dataregler, eftersom pivottabellmodellen behandlar rubrik‑ och dataformat oberoende av varandra.  
- Ett pivot‑område kan lösa upp i flera separata `CellArea`‑instanser. Ett semantiskt område såsom en totalrad, eller ett fält vars poster inte är sammanhängande, kan omfatta flera rektanglar. Detta är anledningen till att `PivotArea.GetCellAreas()` returnerar en samling istället för en enda rektangel.  
Varje formatoperation som utförs via `PivotTable.Format` registreras i `PivotTable.PivotFormats`. Varje `PivotTableFormat`‑post exponerar det associerade `PivotArea` och den `Style` som applicerats på det. `PivotArea`‑överladdningen lägger exakt till en post per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera poster.  
För att skilja på de lagrade regionerna exponerar varje `PivotArea` flaggorna `OnlyLabel` och `OnlyData`. Exemplet nedan formaterar en enda rektangel som omfattar både rubriker och värden, inspekterar `PivotTable.PivotFormats` och skriver ut de `CellArea`‑koordinater som varje lagrat pivot‑område löser upp till.

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
Eftersom formaten lagras som pivot‑områden istället för vanliga cellformat överlever de omräkningar och uppdateringar. När pivottabellen uppdateras med `PivotTable.RefreshData`, omberäknas med `CalculateData`, eller sparas och läses in igen, återupptas varje lagrat pivot‑område till sin nuvarande position och dess stil appliceras på nytt.
{{% /alert %}}

Använd ett `PivotArea` byggt med `Select` eller `SelectField` när en markering ska förbli knuten till ett fält eller ett semantiskt område över flera uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i den aktuella pivottabellslayouten är tillräcklig. Den enskilda cell‑överladdningen `Format(int row, int column, Style)` riktar in sig på en individuell cell. Använd `FormatAll`, som behandlas på föräldrasidan, när hela pivottabellen ska omstylingas på en gång.

{{< app/cells/assistant language="go" >}}