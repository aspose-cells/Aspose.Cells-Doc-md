---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for Java supporta un insieme completo di funzionalità per il filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot mediante filtri per etichetta, filtri per data, filtri per valore, filtri Top 10 e nascondendo o mostrando nuovamente singoli elementi pivot.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro Top 10, elemento pivot, nascondere elemento pivot
type: docs
weight: 10
url: /it/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi riga o colonna contenenti testo, utilizzare filtri per data quando il campo contiene solo celle con valori di data e ora oppure celle vuote, applicare filtri per valore ai numeri aggregati, utilizzare filtri Top 10 per classificare gli elementi in base a un campo valore oppure nascondere e mostrare nuovamente singoli elementi pivot mediante la proprietà `IsHidden`. Ogni strategia è disponibile tramite API dedicate nelle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma le sintesi non elaborate spesso contengono molte più informazioni di quelle necessarie per la presentazione. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori rilevanti per un report specifico. Aspose.Cells for Java replica le funzionalità di filtraggio disponibili in Microsoft Excel e le espone a livello programmatico, consentendo di automatizzare completamente la generazione dei report.
In questo articolo vengono illustrate le seguenti strategie di filtraggio:
1. **Filtro per etichetta** — filtra gli elementi di un campo riga o colonna in base alle relative etichette testuali.
2. **Filtro per data** — filtra i campi riga o colonna che contengono soltanto valori di data e ora oppure valori vuoti.
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro Top 10** — mostra solo i N elementi con i valori più alti o più bassi in base a un campo valore.
5. **Nascondere / mostrare elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento di un campo.
Ogni approccio utilizza un metodo diverso della classe `PivotField` o una proprietà della classe `PivotItem`. Dopo aver applicato un filtro, è necessario chiamare `getPivotCache().refresh()` sulla tabella pivot, in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo riga o colonna confrontando le relative didascalie testuali con un criterio di corrispondenza. È utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano un altro criterio basato sulle didascalie.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, String)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e altri. Il secondo argomento specifica la stringa dell'etichetta da confrontare.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta che consente di mantenere visibili solo gli elementi le cui didascalie iniziano con il prefisso specificato, aggiorna la tabella pivot e salva il risultato.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri temporali, quali oggi, la settimana scorsa, il mese corrente, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che operano soltanto su campi che memorizzano informazioni relative a data e ora.

{{% alert color="primary" %}}
Il filtro per data funziona soltanto quando l'area delle righe o l'area delle colonne contiene esclusivamente celle con valori di data e ora oppure valori vuoti. Se il campo di origine contiene altri tipi di dati, ad esempio numeri o testo, il filtro per data non consentirà di ottenere il risultato previsto. Prima di applicare il filtro, assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure celle vuote.
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori specifici per i filtri di data, tra cui `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro selezionato, è necessario passare uno o due valori `DateTime`; per `Between`, passare la data di inizio e quella di fine.
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area delle righe contiene un campo di data, applica un filtro per data che limita gli elementi visibili a un intervallo di date specifico, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Filtro per valore**
I filtri per valore operano sui valori aggregati calcolati da una tabella pivot nella propria area dati. A differenza dei filtri per etichetta, confrontano i totali numerici con una soglia. I casi d'uso tipici includono la visualizzazione dei soli prodotti la cui somma delle vendite supera un importo prestabilito oppure delle sole regioni per le quali il numero di transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica il campo dati da valutare, mentre gli argomenti finali forniscono i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene esclusivamente gli elementi con vendite aggregate superiori a una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Filtro Top 10**
Il filtro Top 10 è una forma specializzata di filtro per valore che conserva esclusivamente i N elementi con i valori più alti o più bassi, in base a un campo valore selezionato. È comunemente utilizzato per realizzare report di ranking, come "i 10 prodotti con il fatturato più alto" o "le 5 regioni con il numero di vendite più basso".

{{% alert color="primary" %}}
Il filtro Top 10 è efficace soltanto quando la tabella pivot contiene uno o più campi valore nell'area dati. In assenza di almeno un campo valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtraggio Top 10 tramite il metodo `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)`. Il parametro `valueFieldIndex` è l'indice del campo dati i cui valori aggregati determinano la classifica degli elementi. Il parametro `filterType` seleziona l'unità di `itemCount`: `PivotFilterType.COUNT` mantiene un numero fisso di elementi, mentre `PivotFilterType.PERCENT` mantiene una percentuale degli elementi e fa sì che `itemCount` rappresenti la percentuale stessa. Il parametro `isTop` indica se mantenere i primi elementi (true) o gli ultimi (false), mentre `itemCount` definisce quanti elementi o quale percentuale mantenere.
L'esempio seguente carica una cartella di lavoro con una tabella pivot contenente un campo valore, applica un filtro Top 10 che mantiene soltanto i 10 elementi con il valore più elevato della somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtro tramite nascondimento o ripristino della visibilità degli elementi pivot**
Oltre alle API di filtro strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Iterando la raccolta `PivotItems` di un `PivotField` e impostando la proprietà `IsHidden`, è possibile nascondere selettivamente elementi specifici senza applicare un filtro basato su formule. L'impostazione di `IsHidden = true` nasconde l'elemento dalla tabella pivot; l'impostazione di `IsHidden = false` lo rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o vale per singoli elementi, ad esempio per nascondere un numero ridotto di categorie identificate dal nome che non devono comparire in un report specifico. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico in base al nome, mostra come renderlo nuovamente visibile, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Riepilogo**
Aspose.Cells for Java offre un insieme completo di funzionalità di filtraggio delle tabelle pivot, analogo a quello disponibile in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro Top 10 gestisce i report basati sulla classifica. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un'alternativa flessibile a livello di singolo elemento. La combinazione di queste strategie — ad esempio, l'applicazione di un filtro per etichetta seguita dal nascondimento di elementi specifici — consente di creare interamente tramite codice report di tabelle pivot mirati con precisione.

## Articoli correlati
- [Inserire una tabella pivot](/cells/it/java/create-pivot-table/)
- [Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells for Java](/cells/it/java/pivot-table-add-row-and-column-fields/)
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Java](/cells/it/java/add-page-field-in-pivot-table/)
- [Gestire i campi valore di una tabella pivot in Aspose.Cells for Java](/cells/it/java/manage-value-fields/)
- [Aggiornare tabelle pivot e le relative cache in Aspose.Cells for Java](/cells/it/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}