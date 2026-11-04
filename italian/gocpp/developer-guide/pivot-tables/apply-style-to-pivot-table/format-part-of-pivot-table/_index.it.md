---
title: Formattare una parte di una Tabella Pivot
description: Formatta una parte di una tabella pivot in Aspose.Cells for Go via C++ applicando stili a regioni semantiche PivotArea o rettangoli CellArea tramite PivotTable.Format, con i formati archiviati in PivotTable.PivotFormats e conservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Go via C++, tabella pivot, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /it/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scenari di utilizzo possibili**
`PivotTable.FormatAll` applica un singolo stile all'intera tabella pivot ed è trattato nella pagina padre. Non distingue tra etichette, valori, totali o particolari regioni del report.
In pratica, solo una parte della tabella pivot solitamente necessita di evidenziarsi. Gli obiettivi comuni includono le etichette appartenenti a un campo di riga, le celle di valore generate da un campo, la riga del totale generale, o un rettangolo arbitrario come le prime due righe di elementi.
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione delle tabelle pivot come regioni semantiche `PivotArea` anziché come normali record di stile delle celle. Un formato di area pivot rimane associato a una regione, ad esempio le etichette o i valori di dati di un campo, e viene rielaborato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente in una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.
Aspose.Cells espone l'intera famiglia di overload `PivotTable.Format` in modo che entrambi i tipi di formattazione siano disponibili:
- `Format(PivotArea, Style)` associa uno stile a una regione semantica costruita con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(CellArea, Style)` associa uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `Format(int row, int column, Style)` mira a una singola cella.
- `FormatAll(Style)` formatta l'intera tabella pivot.

## **Formattare un'Area Pivot**
Il flusso di lavoro basato su aree semantiche è l'approccio consigliato quando un'evidenziazione deve seguire un campo o una regione del report.
1. Creare un `PivotArea` con `NewPivotArea(pivotTable)`. L'oggetto descrive una regione semantica che appartiene a quella specifica tabella pivot.
1. Selezionare un campo per la sua posizione basata su zero su un determinato asse con `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LabelOnly` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DataOnly` seleziona solo le celle dati del campo.
1. Selezionare un campo per nome con `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve alle celle di valore generate dagli elementi di quel campo.
1. Creare uno `Style` con `Workbook.CreateStyle()`, configurare il suo carattere, colore di primo piano e pattern di sfondo solido, e passare lo stile a `PivotTable.Format(area, style)`.
1. Ogni chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.PivotFormats`.
1. I formati ancorati al campo vengono applicati quando i dati pivot sono calcolati. Pertanto, chiamare `PivotTable.CalculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.
L'esempio seguente crea una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.Select` e `PivotTableSelectionType.LabelOnly`, formatta le celle di valore prodotte dallo stesso campo di riga con `PivotArea.SelectField`, e quindi ricalcola la tabella pivot in modo che entrambi gli stili vengano applicati.

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

## **Formattare un'Area Cell della Tabella Pivot**
Utilizzare `PivotTable.Format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione pivot semantica.
Un `CellArea` è descritto dai valori `StartRow`, `EndRow`, `StartColumn` e `EndColumn`, impostati tramite gli accessor `Set_StartRow` corrispondenti. I valori sono coordinate del foglio di lavoro basate su zero, e le coordinate finali identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area comprende le celle dalla posizione iniziale fino a quella finale inclusive.
Diversamente da un formato ancorato a un campo, un formato `CellArea` viene applicato alle celle immediatamente. Non è necessaria un'altra chiamata a `CalculateData()` perché lo stile appaia.
Un rettangolo `CellArea` può contenere sia celle di etichetta sia celle di valore insieme. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile italic, di colore azzurro chiaro, e salva la cartella di lavoro senza ulteriori ricalcoli.

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

## **Come le Aree Pivot e le Aree Cell si mappano**
Excel memorizza la formattazione delle tabelle pivot come record `pivotArea` anziché come normali record di stile delle celle del foglio di lavoro. Lo stesso modello è usato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot al momento della registrazione.
La relazione tra il `CellArea` fornito dall'utente e le aree pivot memorizzate internamente è molti-a-molti in entrambe le direzioni.
- Un `CellArea` può produrre diverse aree pivot. Se il rettangolo comprende sia celle di etichetta sia celle di valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta la formattazione delle etichette e dei dati in modo indipendente.
- Un'area pivot può risolversi in diverse istanze `CellArea` disgiunte. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. È per questo che `PivotArea.GetCellAreas()` restituisce una collezione invece di un singolo rettangolo.
Ogni operazione di formattazione eseguita tramite `PivotTable.Format` è registrata in `PivotTable.PivotFormats`. Ogni voce `PivotTableFormat` espone il `PivotArea` associato e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre un `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.
Per distinguere le regioni memorizzate, ogni `PivotArea` espone i flag `OnlyLabel` e `OnlyData`. L'esempio seguente formatta un singolo rettangolo che copre sia etichette che valori, ispeziona `PivotTable.PivotFormats` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

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
Poiché i formati sono memorizzati come aree pivot anziché come normali stili delle celle, sopravvivono al ricalcolo e all'aggiornamento. Quando la tabella pivot viene aggiornata con `PivotTable.RefreshData`, ricalcolata con `CalculateData`, o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e il suo stile viene riapplicato.
{{% /alert %}}

Utilizzare un `PivotArea` costruito con `Select` o `SelectField` quando un'evidenziazione deve rimanere collegata a un campo o a una regione semantica attraverso gli aggiornamenti, e utilizzare un `CellArea` quando è sufficiente formattare un rettangolo fisso nel layout corrente della tabella pivot. L'overload a singola cella `Format(int row, int column, Style)` mira a una cella individuale. Utilizzare `FormatAll`, trattato nella pagina padre, quando l'intera tabella pivot deve essere riformattata in un'unica operazione.

{{< app/cells/assistant language="go" >}}