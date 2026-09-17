---
title: Aggiornare le Tabelle Pivot e le Cache Pivot in Aspose.Cells for C++
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for C++ utilizzando l'API di aggiornamento delle pivot introdotta dalla v26.7+. Questo articolo illustra RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi di codice pratici.
linktitle: Aggiornare le Tabelle Pivot
keywords: Aspose.Cells, C++, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre un'API di aggiornamento stratificata che consente di ricaricare i dati pivot a quattro diversi livelli, dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for C++ v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.
{{% /alert %}}

## Introduzione
L'aggiornamento di una tabella pivot raramente è una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati stratificata che collega i dati di origine originali ai valori renderizzati che vedi nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.
La catena di dati a quattro livelli è:
1. **Origine dati** — gli intervalli originali del foglio di lavoro, la query al database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; qui tutti i dati vengono raccolti e aggregati.
3. **Tabella Pivot** — l'oggetto vista che definisce i campi di riga, colonna, valore e filtro. Una `PivotTable` legge *esclusivamente* dal proprio `PivotCache`, mai direttamente dall'origine dati.
4. **Celle** — le `Cells` del foglio di lavoro in cui la `PivotTable` renderizza i valori calcolati e gli stili.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire dalla v26.7, `PivotCache.Refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`**, ovvero dati che risiedono in intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.
{{% /alert %}}

A causa di questa catena, esistono due percorsi di aggiornamento fondamentali in Aspose.Cells:
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` a partire dai dati già presenti nella cache, senza tornare all'origine dati.
Tutti gli scenari di questo articolo utilizzano dati di origine provenienti da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Avvio rapido
Se hai bisogno solo del codice più breve possibile per aggiornare ogni pivot nella cartella di lavoro, è sufficiente una singola chiamata:

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

Tutto il resto di questo articolo spiega quando scegliere invece un'API più specifica.

## Direttive di inclusione richieste
Tutti gli esempi in C++ di questo articolo iniziano con le seguenti direttive di inclusione degli header e di namespace, poiché i tipi relativi alle pivot si trovano nel namespace `Aspose::Cells::Pivot`:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Aggiornare tutte le Tabelle Pivot nella cartella di lavoro
Quando hai bisogno di garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro rifletta i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro, aggiornando ogni `PivotCache` dalla propria origine e quindi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento, quando le prestazioni non sono un problema.
L'esempio seguente crea una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine e quindi utilizza `RefreshAll()` per riportare tutto aggiornato con una singola chiamata.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
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

## Aggiornare tutte le Tabelle Pivot su un singolo foglio di lavoro
A volte è necessario aggiornare solo le tabelle pivot che si trovano su uno specifico foglio di lavoro, ad esempio quando le tabelle pivot presenti su altri fogli non sono correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che ha come ambito una singola istanza di `Worksheet`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Scrivi riga di intestazione Frutto / Anno / Importo
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo di origine A1:C9)
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
    // Aggiungi una tabella pivot denominata "Pivot1" posizionata nella cella di destinazione E3, con origine da A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Assegna campi: Frutto a Riga, Anno a Colonna, Importo a Dati
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modifica una proprietà di visualizzazione/layout — questa è una modifica solo di presentazione,
    // quindi NON richiede di rileggere i dati di origine tramite PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
    // dati già contenuti nella PivotCache. Poiché i dati di origine non sono cambiati,
    // non viene eseguito alcun round-trip verso l'origine — solo i valori memorizzati nella cache vengono ricalcolati
    // nelle celle del foglio di lavoro.
    pivotTable.CalculateData();
    // Salva la cartella di lavoro su disco
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Aggiornare una singola Tabella Pivot
Quando desideri un controllo capillare su una singola tabella pivot, l'API basata sulla cache ti offre due opzioni. La scelta tra esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti oppure solo le impostazioni di vista/layout della tabella pivot.

### Dati di origine modificati — Usa `PivotCache.Refresh()`
Se i dati di origine sottostanti sono cambiati, il punto di ingresso corretto è `pivotTable.GetPivotCache().Refresh()`. Questa chiamata rilegge i dati di origine nella cache e quindi ricalcola ogni `PivotTable` che dipende da quella cache.

### È cambiata solo la vista/layout — Usa `CalculateData()`
Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, oppure è stata attivata/disattivata un'impostazione di aggiornamento all'apertura), non è necessario tornare all'origine dati. La cache contiene già i dati corretti; deve essere ricalcolata solo la `PivotTable` renderizzata. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.
L'esempio seguente modifica una proprietà non legata all'origine della tabella pivot e quindi chiama `CalculateData()` per renderizzarla nuovamente dalla cache esistente.

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

Una cartella di lavoro spesso contiene molte tabelle pivot che si appoggiano tutte su un'unica cache condivisa. Per enumerarle, ad esempio prima di eseguire un aggiornamento in blocco o per diagnosticare l'impatto di una cache condivisa, usa `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di tutte le `PivotTable` che dipendono dalla cache specificata.

## Migrazione dall'obsoleto `PivotTable.RefreshData()`
Prima di Aspose.Cells for C++ v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ciascuna tabella pivot singolarmente. A partire dalla v26.7, tale metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API basate sulla cache descritte sopra.
Ci sono due motivi per cui l'approccio `RefreshData()` per singola tabella è problematico nelle cartelle di lavoro reali:
- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
Le sostituzioni consigliate sono:
L'esempio seguente illustra il nuovo pattern efficiente per cartelle di lavoro con più tabelle pivot che condividono un'unica cache.

## Quale API di aggiornamento devo usare?
La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.
| Obiettivo | API consigliata | Note |
|------|-----------------|-------|
| Aggiornare tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una sola chiamata; copre tutte le cache e le tabelle. |
| Aggiornare solo le tabelle pivot su un singolo foglio | `Worksheet.RefreshPivotTables()` | Ambito limitato a un singolo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.GetPivotCache().Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Sono cambiate solo le impostazioni di vista/layout | `pivotTable.CalculateData()` | Evita l'inutile round-trip verso l'origine. |
| Elencare tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Da usare per enumerare prima di un aggiornamento massivo. |
In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `RefreshData()` per singola tabella. Esse sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine e ti permettono di scegliere l'ambito più piccolo che soddisfa la tua esigenza di aggiornamento.

## Errori comuni
- **Dimenticare di aggiornare prima di salvare.** Una tabella pivot scrive i valori renderizzati nel foglio di lavoro solo quando la sua catena di dati viene aggiornata. Se modifichi le celle di origine, chiama `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) prima di `Workbook.Save()`, altrimenti il file salvato conterrà ancora i vecchi valori aggregati.
- **Chiamare l'obsoleto `RefreshData()` per ogni tabella.** Nella v26.7, `PivotTable.RefreshData()` è contrassegnato come obsoleto e recupera l'origine a ogni chiamata. Con più tabelle pivot che condividono una cache, ciò comporta N recuperi ridondanti dall'origine. Sostituiscilo con una singola `PivotCache.Refresh()` seguita da `CalculateData()` per ciascuna tabella.
- **Aggiornare quando è cambiato solo il layout.** Se hai modificato solo la vista di una tabella pivot (ordine delle colonne, `ConsolidationFunction`, ecc.) senza toccare i dati di origine, `PivotCache.Refresh()` è inutile e lento. Chiama `pivotTable.CalculateData()` per renderizzare dalla cache esistente.
- **Origine esterna non supportata da `PivotCache.Refresh()`.** Se l'origine della tabella pivot proviene da una connessione esterna (database, cubo OLAP, ecc.), `PivotCache.Refresh()` non è in grado di aggiornarla nella v26.7, poiché attualmente supporta solo i tipi di origine `Sheet` e `Consolidation`. Per le origini esterne, riapri la cartella di lavoro o ricostruisci la cache dall'origine.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="cpp" >}}