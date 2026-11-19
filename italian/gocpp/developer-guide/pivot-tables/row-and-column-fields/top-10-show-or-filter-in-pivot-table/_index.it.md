---
title: Visualizza o filtra i primi 10 in una Tabella Pivot
description: Scopri come visualizzare solo gli elementi più alti o più bassi di un campo pivot in Aspose.Cells for Go via C++. Questo articolo copre il metodo Excel 97-2003 Top10AutoShow, la lettura delle opzioni con Top10AutoShowSettings e il filtro Top 10 di Excel 2007-365 tramite FilterTop10.
linktitle: Visualizza o filtra i primi 10
keywords: Aspose.Cells, Go via C++, tabella pivot, top 10, visualizzazione automatica, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /it/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo riga può essere difficile da leggere quando il campo ha decine di membri. Un report Top 10 mantiene solo gli elementi più alti o più bassi in classifica, che è esattamente ciò di cui hanno bisogno i report di classificazione — "top 5 prodotti per fatturato" o "bottom 3 regioni per conteggio vendite". Aspose.Cells supporta due meccanismi per questo, e corrispondono a due generazioni di Microsoft Excel.
- **Excel 97-2003 AutoShow** — il metodo `PivotField.Top10AutoShow()`. Questa è l'impostazione classica "Mostra i primi/ultimi N elementi" memorizzata direttamente sul campo pivot. Funziona in ogni versione di Excel, vecchia e nuova, perché fa parte del formato originale della tabella pivot.
- **Excel 2007-365 Top 10 Filter** — il metodo `PivotField.FilterTop10()`. Questo è il filtro Top 10 moderno presente nel menu del campo (Filtri valori, Top 10...). Viene memorizzato come oggetto `PivotFilter` collegato al campo e offre classificazione basata sul conteggio degli elementi o sulla percentuale.

## **Visualizzazione Top 10 in Excel 97-2003 (Top10AutoShow)**
Il classico AutoShow è configurato con una singola chiamata a `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isTop` — `true` mantiene gli elementi più alti in classifica (Top), `false` mantiene i più bassi (Bottom).
- `count` — quanti elementi conservare, ad esempio 10 per un report classico Top 10.
- `rankBy` — l'indice basato su zero del **campo dati** i cui valori classificano gli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
Il ranking può essere basato su un campo valore o sul campo stesso. Esistono due varianti naturali, mostrate di seguito.

### **Classifica per un campo valore**
Classifica gli elementi del campo riga in base a un normale campo valore come Somma delle vendite. L'esempio seguente crea una tabella pivot con un campo riga (`Sport`) e un campo dati (`Sales`), quindi mostra i primi 2 sport per vendite. `rankBy` è 0 perché "Somma delle vendite" è il campo dati all'indice 0.

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Classifica per il campo stesso**
Un campo può anche essere classificato da sé — passare -1 a `rankBy`. Non è necessario un campo dati aggiuntivo per questa variante; il campo deve solo trovarsi nell'area riga (o colonna). L'esempio seguente mostra gli ultimi 3 sport classificati in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dall'XML della tabella pivot perché -1 è il valore predefinito del formato, e `GetRankBy()` restituisce -1.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Lettura delle opzioni AutoShow correnti**
Il metodo `PivotField.GetTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Usalo per ispezionare come una cartella di lavoro esistente, o una tabella pivot appena configurata, presenterà i suoi elementi — inclusi i file caricati da disco.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

Le impostazioni corrispondono agli attributi AutoShow classici scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), quindi i valori letti sono quelli che ogni versione di Excel riconoscerà.

## **Nota**

{{% alert color="primary" %}}
- Dopo aver chiamato `Top10AutoShow()`, richiama nuovamente `PivotTable.CalculateData()` — le impostazioni hanno effetto nel layout renderizzato solo al successivo ricalcolo.
- Le impostazioni AutoShow funzionano con i campi riga e colonna. Un campo presente solo nell'area pagina (filtro) non può essere classificato in questo modo perché i suoi elementi non sono visualizzati nel corpo della pivot.
{{% /alert %}}

## **Excel 2007-365: Filtro Top 10 (FilterTop10)**
Le versioni moderne di Excel espongono Top 10 come filtro valore nel menu del campo (Filtri valori, Top 10...). Aspose.Cells lo modella con il metodo `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, che restituisce il `PivotFilter` creato:
- `valueFieldIndex` — l'indice basato su zero del campo dati i cui valori aggregati classificano gli elementi.
- `type` — cosa indica `itemCount`. `PivotFilterType.Count` mantiene un numero fisso di elementi (opzione Elementi della finestra di dialogo). `PivotFilterType.Percent` mantiene una percentuale degli elementi, quindi `itemCount` è la percentuale stessa — 30 mantiene il 30 % superiore. `PivotFilterType.Sum` classifica in base alla copertura di valore cumulativa.
- `isTop` — `true` per Top, `false` per Bottom.
- `itemCount` — il N in Top N; la sua unità dipende da `type`.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Le impostazioni AutoShow e `FilterTop10` sono due funzionalità separate. AutoShow scrive l'attributo classico `autoShow` impostato sul campo pivot ed è rispettato da tutte le versioni di Excel a partire da Excel 97. `FilterTop10` scrive una voce `PivotFilter` moderna, che richiede Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta in una versione più vecchia di Excel, una tabella pivot che utilizza il filtro moderno ricade nella visualizzazione di tutti gli elementi. Per documenti che devono passare attraverso strumenti legacy, preferire `Top10AutoShow`; per cartelle di lavoro moderne, preferire `FilterTop10` poiché si combina con gli altri filtri valore.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa campi pivot nella Tabella Pivot](/cells/it/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}