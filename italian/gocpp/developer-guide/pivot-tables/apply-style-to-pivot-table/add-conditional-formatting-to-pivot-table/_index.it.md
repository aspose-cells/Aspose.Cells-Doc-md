---
title: Aggiungere la formattazione condizionale a una Tabella Pivot
linktitle: Aggiungere la formattazione condizionale a una Tabella Pivot
description: Aggiungi la formattazione condizionale a una tabella pivot in Aspose.Cells for Go via C++ - ancorare una regola all'area dati con ApplyTo e un ambito PivotConditionFormatScopeType, oppure definire l'obiettivo con AddCellArea e PivotAreas, quindi collegare regole e stili tramite FormatConditions.AddCondition.
keywords: Aspose.Cells, tabella pivot, formattazione condizionale, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /it/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Gli stili descritti nella pagina padre e nella pagina sorella sono statici – un'area `PivotArea` o `CellArea` viene colorata una sola volta e mantiene il proprio stile indipendentemente dai valori. La formattazione condizionale è la controparte basata su regole – evidenziare ogni importo superiore a 200, ombreggiare il cinquanta percento intermedio o segnalare gli elementi con classifica più bassa – e l’evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale della tabella pivot vive nella collezione `PivotTable.ConditionalFormats`. Ogni voce è un `PivotConditionalFormat` che risponde indipendentemente a due domande:
- **Dove si applica la regola?** La regione di destinazione è definita oppure tramite `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, che riproduce il selettore di ambito dell'interfaccia utente di Excel, oppure tramite `AddCellArea(CellArea)` e la collezione `PivotAreas`, che specificano esplicitamente la regione.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte a `FormatConditions` con `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, e ogni condizione possiede il proprio `Style`.

{{% alert color="primary" %}}
Non chiamare `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` né `FormatConditionCollection.AddArea(CellArea)` sull'oggetto `FormatConditions` di un formato condizionale pivot. Queste due overload provengono dall'API di formattazione condizionale del normale foglio di lavoro e non funzionano per le tabelle pivot: l'area di celle non viene mai convertita in un'area pivot, quindi la richiesta viene ignorata silenziosamente. Definisci sempre la regione sul `PivotConditionalFormat` stesso (`ApplyTo`, `AddCellArea` o `PivotAreas`) e aggiungi la regola con una delle overload di `AddCondition`.
{{% /alert %}}

## **Applica una regola con un ambito (modo UI di Excel)**
Il primo metodo posiziona la regola nello stesso modo in cui lo fa l’interfaccia utente di Excel. Una cella della tabella pivot è indicata dalle sue coordinate del foglio di lavoro a partire da zero, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a che punto la regola deve estendersi da quella cella:
- `PivotConditionFormatScopeType.Data` – tutte le celle valore generate dalla tabella pivot, inclusi i totali generali.
- `PivotConditionFormatScopeType.Field` – le celle valore che appartengono al campo identificato dalla cella, esclusi i totali generali. La cella deve essere una cella campo, ad esempio un’etichetta di campo riga; passare una cella valore genera un’eccezione.
- `PivotConditionFormatScopeType.Selection` – solo le celle valore all’intersezione selezionata dalla cella, tipicamente una singola cella valore.
L’esempio seguente crea una tabella pivot di vendite di frutta il cui angolo in alto a sinistra è in E3, ancorando una formattazione condizionale nella cella F4 (riga 3, colonna 5) con l’ambito `Data`, e evidenzia ogni importo maggiore di 200 in grassetto bianco su sfondo rosso. Con i valori Mela 220, Banana 330, Ciliegia 200 e il totale generale 750, la regola colora F4, F5 e F7 – l’area risolta è l’intera colonna dati F4:F7, e solo le celle il cui valore soddisfa la regola si illuminano.

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
	// Tabella pivot con il suo angolo in alto a sinistra in E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Ancorare il formato condizionale a F4 (riga 3, colonna 5) con l'ambito Dati
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Regola - evidenziare gli importi maggiori di 200
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

Ancorare la stessa regola all’etichetta del campo riga E4 (riga 3, colonna 4) con l’ambito `Field` risolve in F4:F6 – la stessa colonna dati senza la riga del totale generale – perché l’ambito ora descrive il campo `Fruit` anziché l’intera area valori. L’ambito `Selection` ancorato a F4 risolve solo F4.

## **Definisci l’area manualmente**
Il secondo metodo evita il selettore di ambito e specifica l’area esplicitamente sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con AddCellArea**
`AddCellArea(CellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono quelle del foglio di lavoro a partire da zero, e l’area è esattamente il rettangolo specificato – nessuna espansione alla colonna dati e nessuna logica di totale generale. Usalo quando le celle di interesse formano un rettangolo fisso noto del layout pivot corrente.

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
	// Seleziona il rettangolo F4:F6 (le celle di valore senza il totale generale)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Regola - corsivo su giallo chiaro per importi tra 150 e 300
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

### **Una regione pivot semantica con PivotAreas**
`PivotAreas` è lo stesso modello di regione semantica utilizzato dalla pagina sorella per gli stili statici. Crea un `PivotArea`, seleziona un campo o un’area con `Select` o `SelectField`, e aggiungilo con `PivotAreas.AddPivotArea(PivotArea)`. Una regione semantica rimane collegata al suo campo, quindi la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout cambia. L’overload `PivotAreas.Add(PivotArea)` compila ancora ma è contrassegnato come obsoleto – preferisci `AddPivotArea`.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Crea una nuova cartella di lavoro
	workbook, _ := NewWorkbook()
	// Ottieni il primo foglio di lavoro
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Ottieni la collezione di celle
	cells, _ := sheet.GetCells()
	// Array di dati
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Scrivi le intestazioni
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Scrivi le righe di dati
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Crea tabella pivot
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Aggiungi campi alla pivot
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Attacca formato condizionale al campo dati Amount
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Definisci l'area pivot che copre il campo dati Amount
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Aggiungi una condizione: testo grigio per importi inferiori a 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // formula secondaria nulla
	)
	// Crea stile con colore del font grigio
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Applica lo stile alla condizione
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Salva la cartella di lavoro
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **Dove vengono memorizzate le regole e come sopravvivono a un ricaricamento**
Ogni chiamata `ConditionalFormats.Add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprire il file nell’esempio sotto mostra la stessa regola con tipo, operatore e formule intatto, e `GetCellAreas()` restituisce le stesse aree. Le voci che non hanno mai ricevuto una condizione vengono eliminate al salvataggio della cartella di lavoro, proprio come Excel scarta una formattazione condizionale priva di regola.

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
	// Questo stampa:
	// Formati condizionali: 1
	// Formato 0: CellValue GreaterThan formula1==200
	//     righe 4-7, colonne 6-6        (F4:F7, l'intervallo di dati risolto)
}
```

## **Articoli correlati**
- [Formattare parte di una Tabella Pivot](/cells/it/go-cpp/format-part-of-pivot-table/)
- [Top 10 Mostra o Filtra nella Tabella Pivot](/cells/it/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}