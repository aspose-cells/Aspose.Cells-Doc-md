---
title: Formatteil einer Pivot-Tabelle
linktitle: Formatteil einer Pivot-Tabelle
description: Formatteil einer Pivot-Tabelle in Aspose.Cells for Go via C++ indem Stile auf semantische PivotArea‑Regionen oder CellArea‑Rechtecke über PivotTable.Format angewendet werden, wobei Formate in PivotTable.PivotFormats gespeichert und beim Aktualisieren der Pivot‑Tabelle erhalten bleiben.
keywords: Aspose.Cells for Go via C++, Pivot-Tabelle, formatieren, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /de/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
`PivotTable.FormatAll` wendet einen einzelnen Stil auf die gesamte Pivot-Tabelle an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Gesamtsumme‑Zeile oder bestimmten Bereichen des Berichts.  
In der Praxis muss in der Regel nur ein Teil einer Pivot-Tabelle hervorgehoben werden. Häufige Ziele sind die Beschriftungen, die zu einem Zeilenfeld gehören, die Zellwerte, die von einem Feld erzeugt werden, die Gesamtsumme‑Zeile oder ein beliebiges Rechteck, z. B. die ersten beiden Elementzeilen.  
Das Anwenden eines Stils direkt auf die Arbeitsblattzellen einer Pivot-Tabelle ist nicht äquivalent. Excel speichert Pivot‑Tabellen‑Formatierungen als semantische `PivotArea`‑Regionen statt als gewöhnliche Zell‑Stil‑Einträge. Ein Pivot‑Area‑Format bleibt an einer Region wie den Beschriftungen eines Feldes oder Datenwerten befestigt und wird neu aufgelöst, wenn die Pivot‑Tabelle neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebener Stil hingegen ist an die Zellposition gebunden und wird vom Pivot‑Modell nicht nachverfolgt.  
Aspose.Cells stellt die vollständige Überladungsfamilie von `PivotTable.Format` bereit, sodass beide Arten von Formatierung verfügbar sind:
- `Format(PivotArea, Style)` verankert einen Stil an einer semantischen Region, die mit `PivotArea.Select` oder `PivotArea.SelectField` erstellt wird.
- `Format(CellArea, Style)` verankert einen Stil an einem Arbeitsblatt‑Rechteck innerhalb der Pivot‑Tabelle.
- `Format(int row, int column, Style)` richtet sich an eine einzelne Zelle.
- `FormatAll(Style)` formatiert die gesamte Pivot‑Tabelle.

## **Format einer Pivot‑Area**
Der semantische‑Area‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erstellen Sie eine `PivotArea` mit `NewPivotArea(pivotTable)`. Das Objekt beschreibt eine semantische Region, die zu dieser konkreten Pivot‑Tabelle gehört.
2. Wählen Sie ein Feld anhand seiner nullbasierten Position auf einer bestimmten Achse mit `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType.LabelOnly` wählt ausschließlich die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType.DataOnly` wählt ausschließlich die Datenzellen des Feldes aus.
3. Wählen Sie ein Feld anhand seines Namens mit `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Wird ein Zeilenfeld per Name ausgewählt, löst die Region die Wertzellen auf, die von den Elementen dieses Feldes erzeugt werden.
4. Erstellen Sie einen `Style` mit `Workbook.CreateStyle()`, konfigurieren Sie dessen Schriftart, Vordergrundfarbe und einfarbiges Hintergrundmuster und übergeben Sie den Stil an `PivotTable.Format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.PivotFormats` hinzu.
6. Feldgebundene Formate werden angewendet, wenn die Pivot‑Daten berechnet werden. Rufen Sie daher nach dem Anwenden der Formate `PivotTable.CalculateData()` auf, damit die Stile sichtbar werden.  
Das folgende Beispiel erstellt eine kleine Pivot‑Tabelle für Fruchterlöse, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.Select` und `PivotTableSelectionType.LabelOnly`, formatiert die von demselben Zeilenfeld erzeugten Wertzellen mit `PivotArea.SelectField` und berechnet anschließend die Pivot‑Tabelle neu, sodass beide Stile angewendet werden.

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

## **Format eines Zellbereichs der Pivot‑Tabelle**
Verwenden Sie `PivotTable.Format(CellArea, Style)`, wenn der interessierende Bereich ein einfaches Arbeitsblatt‑Rechteck statt einer semantischen Pivot‑Region ist.  
Ein `CellArea` wird durch die Werte `StartRow`, `EndRow`, `StartColumn` und `EndColumn` beschrieben, die über die entsprechenden `Set_StartRow`‑ähnlichen Zugriffe gesetzt werden. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile bzw. Spalte an, die im Rechteck enthalten sind; somit umfasst der Bereich die Zellen von der Start‑ bis zur Endposition, einschließlich beider.  
Im Gegensatz zu einem feldgebundenen Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `CalculateData()` ist nicht erforderlich, damit der Stil erscheint.  
Ein `CellArea`‑Rechteck kann sowohl Beschriftungs‑ als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.  
Das folgende Beispiel formatiert das Rechteck `E4:F5` der Pivot‑Tabelle mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe, ohne eine erneute Berechnung durchzuführen.

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

## **Wie Pivot‑Bereiche und Zellbereiche zugeordnet werden**
Excel speichert Pivot‑Tabellen‑Formatierungen als `pivotArea`‑Datensätze statt als gewöhnliche Arbeitsblatt‑Zell‑Stil‑Einträge. Dasselbe Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanfrage beim Aufzeichnen in Pivot‑Areas umgewandelt wird.  
Die Beziehung zwischen dem vom Benutzer angegebenen `CellArea` und den intern gespeicherten Pivot‑Areas ist in beide Richtungen many‑to‑many:
- Ein `CellArea` kann mehrere Pivot‑Areas erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Wertzellen umfasst, wird es in separate Beschriftungs‑ und Daten‑Regeln zerlegt, weil das Pivot‑Modell Beschriftungs‑ und Daten‑Formatierungen unabhängig behandelt.
- Eine Pivot‑Area kann auf mehrere disjunkte `CellArea`‑Instanzen auflösen. Eine semantische Region wie eine Gesamtsumme‑Zeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb liefert `PivotArea.GetCellAreas()` eine Sammlung statt eines einzelnen Rechtecks.  
Jeder Formatierungsvorgang, der über `PivotTable.Format` ausgeführt wird, wird in `PivotTable.PivotFormats` protokolliert. Jeder `PivotTableFormat`‑Eintrag gibt die zugehörige `PivotArea` und den darauf angewendeten `Style` wieder. Die `PivotArea`‑Überladung fügt genau einen Eintrag pro Aufruf hinzu, während ein `CellArea`, das unterschiedliche semantische Regionen enthält, mehrere Einträge hinzufügen kann.  
Um die gespeicherten Regionen zu unterscheiden, stellt jede `PivotArea` die Flags `OnlyLabel` und `OnlyData` bereit. Das untenstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, untersucht `PivotTable.PivotFormats` und gibt die `CellArea`‑Koordinaten aus, zu denen jede gespeicherte Pivot‑Area aufgelöst wird.

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
Da die Formate als Pivot‑Areas und nicht als gewöhnliche Zell‑Stile gespeichert werden, überleben sie Berechnungen und Aktualisierungen. Wenn die Pivot‑Tabelle mit `PivotTable.RefreshData` aktualisiert, mit `CalculateData` neu berechnet oder gespeichert und erneut geladen wird, löst jede gespeicherte Pivot‑Area erneut ihre aktuelle Position auf und ihr Stil wird wieder angewendet.
{{% /alert %}}

Verwenden Sie eine mit `Select` oder `SelectField` erstellte `PivotArea`, wenn eine Hervorhebung über Aktualisierungen hinweg an ein Feld oder eine semantische Region gebunden bleiben soll, und verwenden Sie ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Pivot‑Tabellen‑Layout ausreicht. Die Einzelzellen‑Überladung `Format(int row, int column, Style)` zielt auf eine einzelne Zelle. Verwenden Sie `FormatAll`, das auf der übergeordneten Seite behandelt wird, wenn die gesamte Pivot‑Tabelle auf einmal neu gestaltet werden soll.

{{< app/cells/assistant language="go" >}}