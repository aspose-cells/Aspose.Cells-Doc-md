---
title: Bedingte Formatierung einer Pivot‑Tabelle hinzufügen
linktitle: Bedingte Formatierung einer Pivot‑Tabelle hinzufügen
description: Bedingte Formatierung zu einer Pivot‑Tabelle in Aspose.Cells for Go via C++ hinzufügen – verankern Sie eine Regel im Datenbereich mit ApplyTo und einem PivotConditionFormatScopeType‑Bereich oder definieren Sie das Ziel mit AddCellArea und PivotAreas und fügen Sie anschließend Regeln und Stile über FormatConditions.AddCondition hinzu.
keywords: Aspose.Cells, Pivot‑Tabelle, bedingte Formatierung, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /de/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Die auf der übergeordneten Seite und auf der verwandten Seite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal formatiert und behält sein Format bei, unabhängig von den Werten. Bedingte Formatierung ist das regelbasierte Gegenstück – heben Sie jeden Betrag über 200 hervor, schattieren Sie die mittleren fünfzig Prozent oder markieren Sie die am schlechtesten platzierten Elemente – und die Hervorhebung folgt den Werten, sobald die Pivot‑Tabelle neu berechnet oder aktualisiert wird.
In Aspose.Cells befindet sich die bedingte Formatierung von Pivot‑Tabellen in der Sammlung `PivotTable.ConditionalFormats`. Jeder Eintrag ist ein `PivotConditionalFormat`, der zwei Fragen unabhängig voneinander beantwortet:
- **Wo wird die Regel angewendet?** Der Zielbereich wird entweder über `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` definiert, das dem Bereichsauswahl‑Steuerelement der Excel‑Benutzeroberfläche entspricht, oder über `AddCellArea(CellArea)` und die `PivotAreas`‑Sammlung, die den Bereich explizit benennen.
- **Was prüft die Regel?** Einer oder mehrere Bedingungen werden zu `FormatConditions` hinzugefügt mit `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, und jede Bedingung enthält ihr eigenes `Style`.

{{% alert color="primary" %}}
Rufen Sie nicht `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` oder `FormatConditionCollection.AddArea(CellArea)` auf dem `FormatConditions`‑Objekt eines Pivot‑bedingten Formats auf. Diese beiden Überladungen stammen aus der regulären Arbeitsblatt‑Bedingte‑Formatierungs‑API und funktionieren nicht für Pivot‑Tabellen – der Zellbereich wird niemals in einen Pivot‑Bereich konvertiert, sodass die Anfrage stillschweigend ignoriert wird. Definieren Sie den Bereich immer direkt auf dem `PivotConditionalFormat` selbst (`ApplyTo`, `AddCellArea` oder `PivotAreas`) und fügen Sie die Regel mit einer der `AddCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Regel mit einem Bereich anwenden (wie in der Excel‑UI)**
Der erste Ansatz positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der Pivot‑Tabelle wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich gibt Aspose.Cells an, wie weit die Regel von dieser Zelle aus gelten soll:
- `PivotConditionFormatScopeType.Data` – alle Wertzellen, die die Pivot‑Tabelle erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.Field` – die Wertzellen, die zu dem Feld gehören, das die Zelle bezeichnet, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, z. B. ein Zeilen‑Feld‑Label; das Übergeben einer Wertzelle wirft eine Ausnahme.
- `PivotConditionFormatScopeType.Selection` – nur die Wertzellen an der Schnittstelle, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.
Das folgende Beispiel erstellt eine Pivot‑Tabelle für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `Data`‑Bereich und hebt jeden Betrag über 200 fett weiß auf rot hervor. Mit den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 malt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten auf.

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
	// Pivot‑Tabelle mit ihrer oberen linken Ecke bei E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Regel – hebe Beträge hervor, die größer als 200 sind
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

Verankert man dieselbe Regel beim Zeilen‑Feld‑Label E4 (Zeile 3, Spalte 4) mit dem `Field`‑Bereich, wird sie stattdessen auf F4:F6 angewendet – dieselbe Datenspalte ohne die Gesamtsummen‑Zeile –, da der Bereich nun das Feld `Fruit` statt des gesamten Wertebereichs beschreibt. Der `Selection`‑Bereich, der an F4 verankert ist, löst nur F4 auf.

## **Region manuell definieren**
Der zweite Ansatz überspringt die Bereichsauswahl und benennt den Bereich explizit auf dem `PivotConditionalFormat`.

### **Ein Arbeitsblatt‑Rechteck mit AddCellArea**
`AddCellArea(CellArea)` zeichnet das übergebene Rechteck als Ziel der Regel auf. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich ist exakt das bereitgestellte Rechteck – keine Erweiterung zur Datenspalte und keine Gesamtsummen‑Logik. Verwenden Sie es, wenn die interessierenden Zellen ein bekanntes festes Rechteck des aktuellen Pivot‑Layouts bilden.

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
	// Zielrechteck F4:F6 (die Wertzellen ohne Gesamtsumme)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Regel – kursiv auf hellgelb für Beträge zwischen 150 und 300
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

### **Ein semantischer Pivot‑Bereich mit PivotAreas**
`PivotAreas` ist dasselbe semantische‑Bereich‑Modell, das die verwandte Seite für statische Stile verwendet. Erstellen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `Select` oder `SelectField` aus und fügen Sie es mit `PivotAreas.AddPivotArea(PivotArea)` hinzu. Ein semantischer Bereich bleibt an sein Feld gekoppelt, sodass die bedingte Formatierung dem Feld folgt, wenn die Pivot‑Tabelle aktualisiert und das Layout verschoben wird. Die Überladung `PivotAreas.Add(PivotArea)` lässt sich noch kompilieren, ist jedoch als veraltet markiert – bevorzugen Sie `AddPivotArea`.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Erstelle ein neues Arbeitsbuch
	workbook, _ := NewWorkbook()
	// Hole das erste Arbeitsblatt
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Hole die Zellen‑Sammlung
	cells, _ := sheet.GetCells()
	// Daten‑Arrays
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Schreibe Überschriften
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Schreibe Datenzeilen
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Erstelle Pivot‑Tabelle
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Felder zur Pivot hinzufügen
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Bedingte Formatierung an das Betrag‑Datenfeld anhängen
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Definiere den Pivot‑Bereich, der das Betrag‑Datenfeld abdeckt
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Füge eine Bedingung hinzu: grauer Text für Beträge unter 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // null zweite Formel
	)
	// Erstelle Stil mit grauer Schriftfarbe
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Wende Stil auf die Bedingung an
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Speichere das Arbeitsbuch
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **Wo die Regeln gespeichert werden und wie sie einen Neuladevorgang überstehen**
Jeder Aufruf von `ConditionalFormats.Add()` fügt der Pivot‑Tabelle ein `PivotConditionalFormat` hinzu. Die Bedingungen, ihre Formeln und ihre Stile werden mit der Arbeitsmappe gespeichert – das erneute Öffnen der Datei im nachstehenden Beispiel zeigt die gleichen beiden Regeln mit ihren Typen, Operatoren und Formeln unverändert, und `GetCellAreas()` meldet dieselben Bereiche. Einträge, die nie eine Bedingung erhalten haben, werden beim Speichern der Arbeitsmappe verworfen, analog dazu, dass Excel ein bedingtes Format ohne Regel verwirft.

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
	// Dies gibt aus:
	// Bedingte Formate: 1
	// Format 0: CellValue GreaterThan formula1==200
	//     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
}
```

## **Verwandte Artikel**
- [Teil einer Pivot‑Tabelle formatieren](/cells/de/go-cpp/format-part-of-pivot-table/)
- [Top‑10‑Anzeige oder -Filter in Pivot‑Tabelle](/cells/de/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}