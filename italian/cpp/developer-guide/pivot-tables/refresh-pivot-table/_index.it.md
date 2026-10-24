---
title: Aggiornare Tabelle Pivot e cache pivot in Aspose.Cells for C++
linktitle: Aggiornare Tabelle Pivot e cache pivot
description: Scopri come aggiornare le Tabelle Pivot in Aspose.Cells for C++ utilizzando l'API di aggiornamento delle Tabelle Pivot v26.7+. Questo articolo illustra RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi di codice pratici.
keywords: Aspose.Cells, C++, Tabella Pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce un'API di aggiornamento a livelli che consente di ricaricare i dati delle Tabelle Pivot a quattro diversi ambiti, dall'intera cartella di lavoro fino a una singola Tabella Pivot. A partire da **Aspose.Cells for C++ v26.7**, il metodo tradizionale `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito dalle API più efficienti e basate sulla cache descritte in questo articolo.
{{% /alert %}}

## Introduction
L'aggiornamento di una Tabella Pivot raramente consiste in una singola operazione. All'interno, Aspose.Cells mantiene una catena di dati a livelli che collega i dati di origine originali ai valori visualizzati nel foglio di lavoro. La comprensione di questa catena è essenziale per scegliere l'API di aggiornamento corretta per ogni situazione.
La catena di dati a quattro livelli è la seguente:
1. **Sorgente dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni Tabella Pivot è costruita su un `PivotCache`; qui tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto di visualizzazione che definisce i campi di riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal proprio `PivotCache`, mai direttamente dalla sorgente dati.
4. **Cells** — le `Cells` del foglio di lavoro nel quale il `PivotTable` rende i valori calcolati e applica gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire da v26.7, `PivotCache.Refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati contenuti in intervalli di fogli di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
Poiché esiste questa catena, in Aspose.Cells sono disponibili due percorsi fondamentali di aggiornamento:
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` a partire dai dati già memorizzati nella cache, senza dover tornare alla sorgente dati.
Tutti gli scenari di questo articolo utilizzano dati di origine contenuti nelle celle dei fogli di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.
{{% /alert %}}

## Quick Start
Se serve solo il codice più breve possibile per aggiornare tutte le Tabelle Pivot della cartella di lavoro, è sufficiente una singola chiamata:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Il resto di questo articolo spiega quando scegliere un'API con un ambito più ristretto.

## Required Include Directives
Tutti gli esempi C++ di questo articolo iniziano con le seguenti direttive di inclusione dell'header e di namespace, poiché i tipi pivot risiedono nel namespace `Aspose::Cells::Pivot`:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
Quando è necessario assicurarsi che ogni cache pivot e ogni Tabella Pivot della cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per gli aggiornamenti generali dell'intero documento quando le prestazioni non costituiscono un problema.
L'esempio seguente costruisce una cartella di lavoro con un intervallo di origine Fruit/Year/Amount, crea una Tabella Pivot, modifica alcuni valori di origine e quindi usa `RefreshAll()` per aggiornare tutto con una singola chiamata.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh All Pivot Tables on a Single Worksheet
Talvolta è necessario aggiornare solo le Tabelle Pivot presenti in un foglio di lavoro specifico, ad esempio quando quelle in altri fogli di lavoro sono note come non correlate e non devono essere modificate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, il cui ambito è limitato a una singola istanza di `Worksheet`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh a Single Pivot Table
Quando si desidera un controllo dettagliato su una singola Tabella Pivot, l'API basata sulla cache offre due opzioni. La scelta dipende da ciò che è effettivamente cambiato: i dati di origine sottostanti oppure solo le impostazioni di visualizzazione o layout della Tabella Pivot stessa.

### Source Data Changed — Use `PivotCache.Refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.GetPivotCache().Refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da essa.

### Only View/Layout Changed — Use `CalculateData()`
Se i dati di origine *non* sono cambiati, ma sono state modificate solo le impostazioni di visualizzazione o layout della Tabella Pivot (ad esempio, un campo è stato spostato in un'area diversa o un'impostazione di aggiornamento all'apertura è stata attivata o disattivata), non è necessario tornare alla sorgente dati. La cache contiene già i dati corretti; occorre solo ricalcolare la `PivotTable` visualizzata. In questo caso, `pivotTable.CalculateData()` è la scelta corretta.
L'esempio seguente modifica una proprietà della Tabella Pivot non correlata alla sorgente e quindi chiama `CalculateData()` per rigenerarne la visualizzazione dalla cache esistente.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
    // Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Una cartella di lavoro contiene spesso molte Tabelle Pivot tutte basate su una singola cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento massivo o per diagnosticare l'impatto di una cache condivisa, usare `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache indicata.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Prima di Aspose.Cells for C++ v26.7, il modo standard per aggiornare una Tabella Pivot era chiamare `PivotTable.RefreshData()` su ogni singola Tabella Pivot. A partire da v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito dalle API basate sulla cache descritte sopra.
Esistono due motivi per cui l'approccio `RefreshData()` per singola tabella è problematico nelle cartelle di lavoro reali:
- Ricarica i dati dalla origine *ogni volta* che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente dimostra il nuovo schema efficiente per cartelle di lavoro con più Tabelle Pivot che condividono una singola cache.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Which Refresh API Should I Use?
La tabella seguente riepiloga le API di aggiornamento disponibili e le circostanze in cui scegliere ciascuna.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una singola chiamata; include tutte le cache e le Tabelle Pivot. |
| Aggiornare solo le Tabelle Pivot in un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un foglio di lavoro. |
| I dati di origine di una cache sono cambiati | `pivotTable.GetPivotCache().Refresh()` | Aggiorna TUTTE le Tabelle Pivot associate a quella cache condivisa. |
| Sono cambiate solo le impostazioni di visualizzazione o layout | `pivotTable.CalculateData()` | Evita il ritorno non necessario alla sorgente. |
| Elencare tutte le Tabelle Pivot associate a una cache condivisa | `pivotCache.GetPivotTables()` | Utilizzare per enumerarle prima di un aggiornamento massivo. |
In pratica, si preferiscono le API basate sulla cache rispetto all'obsoleto `RefreshData()` per singola tabella. Queste API riconoscono le cache condivise, evitano recuperi ridondanti della sorgente e consentono di scegliere l'ambito più ristretto che soddisfa la necessità di aggiornamento.

## Common Pitfalls
- **Dimenticare di aggiornare prima di salvare.** Una Tabella Pivot scrive i propri valori visualizzati nel foglio di lavoro solo quando la relativa catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) prima di `Workbook.Save()`, altrimenti il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per ogni tabella.** In v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera nuovamente la sorgente a ogni chiamata. Con più Tabelle Pivot che condividono una cache, ciò comporta N recuperi ridondanti della sorgente. Sostituiscilo con una singola `PivotCache.Refresh()` seguita da `CalculateData()` per ogni tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai modificato solo la visualizzazione di una Tabella Pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza intervenire sui dati di origine, `PivotCache.Refresh()` è inutile e lenta. Chiama `pivotTable.CalculateData()` per rigenerare la visualizzazione dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.Refresh()`.** Se la sorgente della Tabella Pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non può eseguire l'aggiornamento in v26.7; attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dalla sorgente.

{{< app/cells/assistant language="cpp" >}}