---
title: Filtraggio delle Tabelle Pivot per Etichetta o Valore
linktitle: Filtraggio delle Tabelle Pivot per Etichetta o Valore
description: Aspose.Cells for Java supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati delle tabelle pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando elementi pivot.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondi elemento pivot
type: docs
weight: 10
url: /it/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle di tipo data-ora o vuote, applicare filtri per valore rispetto ai numeri aggregati, utilizzare i filtri primi 10 per classificare in base a un campo di valore, oppure nascondere e mostrare manualmente singoli elementi pivot utilizzando la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma le sintesi grezze spesso contengono molte più informazioni di quelle che è necessario presentare. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, colonne o valori che contano per un report specifico. Aspose.Cells for Java rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole a livello di programmazione così che la generazione dei report possa essere completamente automatizzata.
In questo articolo vengono illustrate le seguenti strategie di filtraggio:
1. **Filtro per Etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per Data** — filtra i campi di riga o colonna che contengono solo valori di data-ora (o vuoti).
3. **Filtro per Valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro Primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo di valore.
5. **Nascondi / Mostra Elementi Pivot** — controlla manualmente la visibilità di ogni singolo elemento in un campo.
Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `refreshData()` e `calculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per Etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le loro didascalie di testo con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una lettera specifica, contengono una determinata parola o soddisfano qualche altro criterio basato sulla didascalia.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.filterByLabel(PivotFilterType, String)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, e così via. Il secondo argomento fornisce la stringa dell'etichetta utilizzata per il confronto.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie iniziano con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Carica la cartella di lavoro esistente contenente una tabella pivot
Workbook workbook = new Workbook(fileName);
// Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Accedi alla tabella pivot tramite indice
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Recupera il primo campo riga PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Applica il filtro delle etichette: mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Aggiorna e ricalcola i dati della tabella pivot affinché il filtro abbia effetto
pivotTable.refreshData();
// Salva la cartella di lavoro sul disco
workbook.save(fileName);
```

## **Filtro per Data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, la settimana scorsa, questo mese, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni di data-ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene solo celle di data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` o celle vuote prima di applicare questo filtro.
{{% /alert %}}

Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alla data come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between`, si passano la data di inizio e di fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Carica la cartella di lavoro esistente che contiene la tabella pivot
Workbook workbook = new Workbook(inputPath);
// Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Accedi alla tabella pivot per indice
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Recupera il PivotField della data dall'area delle righe
// (Il filtro per data funziona solo quando l'area di righe/colonne contiene solo celle data-ora o vuote)
PivotField dateField = pivotTable.getRowFields().get(0);
// Definisci il criterio di data per il filtro Between (Compreso tra)
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Applica il filtro per data sul campo pivot
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
pivotTable.refreshData();
// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtro per Valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella propria area dati. Invece di confrontare etichette di testo, confrontano i totali numerici rispetto a una soglia. Casi d'uso tipici includono la visualizzazione solo dei prodotti la cui somma delle vendite supera un importo obiettivo o solo delle regioni il cui conteggio delle transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato, e gli argomenti finali forniscono il valore o i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Trova l'indice del campo dati manualmente poiché PivotFieldCollection non ha IndexOf
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
pivotTable.refreshData();
workbook.save("output.xlsx");
```

## **Filtro Primi 10**
Il filtro primi 10 è una forma specializzata di filtro per valore che conserva solo i primi o gli ultimi N elementi in base a un campo di valore scelto. È comunemente utilizzato per report di classificazione come "i primi 10 prodotti per ricavo" o "le ultime 5 regioni per numero di vendite".

{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot ha uno o più campi pivot di valore nell'area dati. Senza almeno un campo di valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi, e il filtro non può essere applicato.
{{% /alert %}}

Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere gli elementi superiori (true) o inferiori (false), `valueField` fa riferimento al campo dati utilizzato per la classificazione, e `filterType` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo di valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;
// Carica la cartella di lavoro esistente che contiene la tabella pivot
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Accedi al foglio di lavoro che contiene la tabella pivot (indice 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Accedi alla tabella pivot tramite indice
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Verifica che ci sia almeno un PivotField di tipo valore nell'area dati
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Recupera il PivotField della riga di destinazione (il campo su cui vogliamo applicare i primi 10)
PivotField rowField = pivotTable.getRowFields().get(0);
// Il primo (e unico) campo dati è all'indice 0; i primi 10 si classificano in base ad esso.
int valueFieldIndex = 0;
// Applica il filtro Primi 10 sul campo riga:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (primi N; false significherebbe ultimi N)
//   - valueFieldIndex = l'indice del campo dati utilizzato per classificare gli elementi
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);
// Aggiorna i dati della tabella pivot e ricalcola in modo che il filtro abbia effetto
pivotTable.refreshData();
// Salva la cartella di lavoro
workbook.save(outputPath);
```

## **Filtro tramite Nascondere o Mostrare Elementi Pivot**
Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Iterando attraverso la collezione `PivotItems` di un `PivotField` e attivando/disattivando la proprietà `IsHidden`, è possibile eliminare selettivamente elementi specifici senza applicare un filtro basato su formule. Impostando `IsHidden = true` si nasconde l'elemento dalla tabella pivot; impostando `IsHidden = false` lo si rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per elemento, come nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come mostrarlo di nuovo, aggiorna la tabella pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;
// Carica una cartella di lavoro esistente contenente una tabella pivot
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Accedi al primo foglio di lavoro che contiene la tabella pivot
Worksheet sheet = workbook.getWorksheets().get(0);
// Accedi alla tabella pivot tramite indice (la prima tabella pivot nel foglio)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Ottieni il PivotField di destinazione (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Itera attraverso la collezione PivotItems del PivotField selezionato
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }
    // Dimostra come mostrare nuovamente: ri-mostra un elemento pivot precedentemente nascosto
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}
// Aggiorna e ricalcola la tabella pivot affinché le modifiche abbiano effetto
pivotTable.refreshData();
// Salva la cartella di lavoro - gli elementi nascosti rimangono nei dati sottostanti
// ma sono esclusi dall'output della tabella pivot visualizzata
workbook.save("output_pivot_filtered.xlsx");
```

## **Riepilogo**
Aspose.Cells for Java fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle presenti in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinare queste strategie — ad esempio, applicare un filtro per etichetta e poi nascondere elementi specifici — consente di creare report di tabelle pivot precisamente mirati interamente da codice.

## Articoli Correlati
- [Inserire una Tabella Pivot](/cells/it/java/pivot-tables/)
- [Aggiungere Campi Riga e Colonna della Tabella Pivot in Aspose.Cells for Java](/cells/it/java/pivot-table-add-row-and-column-fields/)
- [Aggiungere Campi Filtro a una Tabella Pivot in Aspose.Cells for Java](/cells/it/java/add-page-field-in-pivot-table/)
- [Gestire i Campi Valore della Tabella Pivot in Aspose.Cells for Java](/cells/it/java/manage-value-fields/)
- [Aggiornare le Tabelle Pivot e le Cache Pivot in Aspose.Cells for Java](/cells/it/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}