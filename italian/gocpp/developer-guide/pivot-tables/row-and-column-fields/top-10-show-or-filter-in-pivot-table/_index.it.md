---
title: Visualizzazione o filtro Top 10 nella tabella pivot
linktitle: Visualizzazione o filtro Top 10 nella tabella pivot
description: Scopri come mostrare esclusivamente gli elementi che occupano i primi o gli ultimi posti nella classifica di un campo pivot in Aspose.Cells for Go via C++. Questo articolo illustra le impostazioni AutoShow di Excel 97-2003 (SetIsAutoShow e i relativi metodi), la lettura delle opzioni e il filtro Top 10 di Excel 2007-365 tramite FilterTop10.
keywords: Aspose.Cells, Go via C++, tabella pivot, primi 10, AutoShow, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /it/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può risultare difficile da leggere quando il campo contiene decine di elementi. Un report Top 10 mostra esclusivamente gli elementi ai primi o agli ultimi posti della classifica, come richiesto dai report di classifica, ad esempio «i 5 prodotti più redditizi in base al fatturato» o «le 3 regioni con il minor numero di vendite». Aspose.Cells supporta due meccanismi a questo scopo, che corrispondono a due generazioni di Microsoft Excel.
- **AutoShow di Excel 97-2003** — i quattro metodi di impostazione di `PivotField`: `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` e `SetAutoShowField`. Si tratta dell'impostazione classica «Mostra i primi/ultimi N elementi», memorizzata direttamente sul campo pivot. È supportata da tutte le versioni di Excel, perché fa parte del formato originale della tabella pivot.
- **Filtro Top 10 di Excel 2007-365** — il metodo `PivotField.FilterTop10()`. Si tratta del filtro Top 10 moderno sui valori, disponibile nel menu del campo in «Filtri valori». Viene memorizzato come oggetto `PivotFilter` associato al campo e consente di classificare gli elementi in base al numero di elementi o alla percentuale.

## **Visualizzazione dei primi 10 in Excel 97-2003 (AutoShow)**
La funzionalità AutoShow classica viene configurata mediante quattro chiamate ai metodi di impostazione di `PivotField`:
- `SetIsAutoShow(bool)` — attiva o disattiva l'impostazione AutoShow sul campo.
- `SetIsAscendShow(bool)` — `false` per mantenere i primi elementi della classifica, `true` per mantenere gli ultimi.
- `SetAutoShowCount(int32)` — il numero di elementi da mantenere, ad esempio 10 per un report classico dei primi 10.
- `SetAutoShowField(int32)` — l'indice in base zero del **campo dati** i cui valori vengono utilizzati per classificare gli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
La classifica può essere determinata da un campo di valore o dal campo stesso. Di seguito sono illustrate due varianti tipiche.

### **Classifica in base a un campo di valore**
Per classificare gli elementi del campo di riga, utilizzare un campo di valore ordinario, ad esempio la somma delle vendite. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i 2 sport con le vendite più alte. `rankBy` è 0 perché «Sum of Sales» è il campo dati all'indice 0.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Mostra i primi 2 elementi ordinati in base a "Somma delle vendite" (indice del campo dati 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Classifica in base al campo stesso**
Un campo può essere classificato in base a sé stesso: passare -1 a `SetAutoShowField`. Per questa variante non è necessario alcun campo dati aggiuntivo; il campo deve trovarsi soltanto nell'area delle righe o delle colonne. L'esempio seguente mostra i 3 sport con i valori più bassi, classificati in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dal XML della tabella pivot perché -1 è il valore predefinito del formato e `GetAutoShowField()` restituisce di nuovo -1.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Mostra i 3 elementi inferiori classificati in base al campo stesso (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Lettura delle opzioni AutoShow correnti**
I metodi di lettura `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` e `GetAutoShowField()` di `PivotField` espongono le opzioni AutoShow attualmente memorizzate sul campo. Consentono di controllare come verranno visualizzati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata. Possono essere utilizzati anche con cartelle di lavoro caricate da file.

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
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

Le quattro proprietà corrispondono agli attributi classici di AutoShow scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`); pertanto, i valori letti sono quelli che verranno applicati da ogni versione di Excel.

## **Nota**

{{% alert color="primary" %}}
- Dopo aver richiamato uno qualsiasi dei metodi di impostazione AutoShow, chiamare di nuovo `PivotTable.CalculateData()`: le impostazioni vengono applicate al layout visualizzato solo alla ricalcolazione successiva.
- Le impostazioni AutoShow funzionano con i campi di riga e di colonna. Un campo presente soltanto nell'area dei filtri non può essere classificato in questo modo, perché i suoi elementi non sono disposti nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro Top 10 (FilterTop10)**
Le versioni moderne di Excel mostrano Top 10 come filtro sui valori nel menu del campo («Filtri valori», «Top 10...»). Aspose.Cells implementa questo filtro tramite il metodo `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, che restituisce il `PivotFilter` creato:
- `valueFieldIndex` — l'indice in base zero del campo dati i cui valori aggregati vengono utilizzati per classificare gli elementi.
- `type` — determina il significato di `itemCount`. `PivotFilterType.Count` mantiene un numero fisso di elementi (l'opzione «Elementi» della finestra di dialogo). `PivotFilterType.Percent` mantiene una percentuale degli elementi, quindi `itemCount` rappresenta direttamente la percentuale: 30 mantiene il 30 per cento degli elementi con i valori più alti. `PivotFilterType.Sum` classifica in base alla copertura cumulativa dei valori.
- `isTop` — `true` per selezionare i primi elementi della classifica, `false` per selezionare gli ultimi.
- `itemCount` — il valore N in «Primi N»; l'unità dipende da `type`.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Filtro Top 10 — mantiene i 2 elementi superiori in base a "Sum of Sales" (indice 0 del campo dati)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// Per un filtro basato sulla percentuale, mantieni invece il 30 percento degli elementi:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Le impostazioni AutoShow e `FilterTop10` sono due funzionalità distinte. AutoShow scrive sul campo pivot il set classico di attributi, incluso `autoShow`, ed è supportato da tutte le versioni di Excel a partire da Excel 97. `FilterTop10` scrive una voce `PivotFilter` moderna, utilizzabile solo con Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, la tabella pivot che utilizza il filtro moderno torna a visualizzare tutti gli elementi. Per i documenti che devono essere rielaborati senza perdita di informazioni mediante strumenti di versioni precedenti, preferire i metodi di impostazione AutoShow; per le cartelle di lavoro moderne, preferire `FilterTop10`, poiché si combina con gli altri filtri sui valori.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}