---
title: Raggruppa i campi pivot nella tabella pivot con Golang via C++
linktitle: Raggruppa i campi pivot nella tabella pivot con Golang via C++
description: Scopri come raggruppare i campi pivot di riga e di colonna di una tabella pivot in periodi di data, come mesi e trimestri, e in intervalli numerici, utilizzando PivotField.Group e PivotFieldGroupOptions all'interno di Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, tabella pivot, campo pivot, raggruppamento dei campi pivot, Raggruppamento, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, raggruppamento per data, intervallo numerico, Go
type: docs
weight: 80
url: /it/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento dei campi pivot è utile quando un campo di riga o di colonna di una tabella pivot contiene numerosi elementi distinti, ad esempio un campo di data con centinaia di date o un campo numerico con molti valori dispersi. Il raggruppamento collassa questi elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. In questo modo, una tabella pivot di grandi dimensioni diventa più compatta e facile da analizzare. Aspose.Cells fornisce questa funzionalità tramite il metodo `PivotField.Group()` (raggruppamento automatico in base al tipo di dati) e `PivotField.Group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento per date aggrega le singole date in periodi più ampi, come giorni, mesi, trimestri e anni, e costruisce una gerarchia temporale (ad esempio, Anni, Trimestri, Mesi). Le tendenze nel tempo diventano visibili a colpo d'occhio e ogni livello temporale diventa un campo pivot distinto nell'area di riga o di colonna della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area ROW o COLUMN di una tabella pivot. Un campo di dati (valore) non può essere raggruppato direttamente. Per raggruppare un campo di questo tipo, è necessario aggiungerlo preventivamente all'area di riga o di colonna della tabella pivot.

## **Raggruppa automaticamente i campi pivot**
L'overload senza parametri di `PivotField.Group()` esamina il tipo di dati del campo ed esegue il raggruppamento automatico. Un campo contenente solo date (e celle vuote) viene raggruppato per mesi. Un campo contenente solo numeri (e celle vuote) viene raggruppato in intervalli numerici utilizzando un intervallo automatico.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **Raggruppa i campi pivot con opzioni personalizzate**
La classe `PivotFieldGroupOptions` consente di configurare il raggruppamento in modo personalizzato. Per i campi di data, impostare `StartDate`, `EndDate` e `GroupTypes`; le date vengono passate come valori `time.Time` di Go. Per i campi numerici, impostare `StartNumber`, `EndNumber` e `Interval`. L'impostazione `newPivotField` determina se il raggruppamento crea nuovi campi pivot oltre a quello originale (consultare la sezione Nota alla fine di questo articolo).

### **Raggruppa un campo di data per mesi e trimestri**
L'esempio seguente raggruppa per mesi e trimestri, tra una data di inizio e una data di fine, il campo di riga contenente date della tabella pivot di esempio. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. L'immagine mostra l'effetto: il campo di riga contenente date è ora raggruppato per trimestri e mesi.
Si noti che l'ordine dei valori in `GroupTypes` viene ignorato. Qualunque sia l'ordine in cui sono elencati i tipi di raggruppamento, i campi raggruppati vengono sempre visualizzati dal periodo più ampio al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio, i mesi sono elencati prima dei trimestri in `GroupTypes`, ma i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppa un campo numerico in intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo di dati (valore). Poiché solo i campi di riga o di colonna possono essere raggruppati, il codice chiama prima `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` per spostare `FieldTwo` nell'area di riga, aggiorna la tabella pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 utilizzando `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **Nota**

{{% alert color="primary" %}}
- Gli overload del metodo `PivotField.GroupBy()` sono deprecati e sono stati rimossi dall'API. `PivotField.Group()` e `PivotField.Group(PivotFieldGroupOptions)` sono i metodi sostitutivi.
- In Microsoft Excel, il raggruppamento di un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre il raggruppamento di un campo di data crea NUOVI campi pivot (uno per ogni livello di raggruppamento, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `PivotField.Group()` seguono lo stesso comportamento di Excel.
- La proprietà `PivotFieldGroupOptions.Interval` si applica esclusivamente al raggruppamento numerico e a quello delle date per giorni (ad esempio, al raggruppamento di date in periodi di 7 giorni); viene invece ignorata quando le date vengono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Mostra o filtra i 10 principali elementi in una tabella pivot](/cells/it/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Mostra i valori come in una tabella pivot](/cells/it/go-cpp/show-values-as-in-pivot-table/)
- [Formatta una parte della tabella pivot](/cells/it/go-cpp/format-part-of-pivot-table/)
- [Aggiungi la formattazione condizionale a una tabella pivot](/cells/it/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}