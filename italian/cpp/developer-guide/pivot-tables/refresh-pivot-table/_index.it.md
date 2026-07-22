---
title: Aggiornamento delle tabelle pivot in Aspose.Cells for C++
linktitle: Aggiornamento delle tabelle pivot
description: Scopri come aggiornare le tabelle pivot in Aspose.Cells for C++ utilizzando l'API di aggiornamento delle pivot v26.7+. Questo articolo tratta RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData e GetPivotTables con esempi pratici di codice.
keywords: Aspose.Cells, C++, tabella pivot, aggiornamento, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /it/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un'API di aggiornamento stratificata che consente di ricaricare i dati delle pivot in quattro ambiti diversi — dall'intera cartella di lavoro fino a una singola tabella pivot. A partire da **Aspose.Cells for C++ v26.7**, il metodo legacy `PivotTable.RefreshData()` è contrassegnato come obsoleto e deve essere sostituito con le API più efficienti e consapevoli della cache descritte in questo articolo.

{{% /alert %}}

## Introduzione

L'aggiornamento di una tabella pivot è raramente una singola operazione. Dietro le quinte, Aspose.Cells mantiene una catena di dati stratificata che collega i dati originali di origine ai valori renderizzati che vedi nel foglio di lavoro. Comprendere questa catena è la chiave per scegliere l'API di aggiornamento giusta per ogni situazione.

La catena di dati a quattro livelli è:

1. **Origine dati** — gli intervalli originali del foglio di lavoro, la query del database o l'intervallo di consolidamento in cui risiedono i valori grezzi.
2. **PivotCache** — l'istantanea in memoria dei dati di origine. Ogni tabella pivot è costruita sopra un `PivotCache`; qui tutti i dati vengono raccolti e aggregati.
3. **PivotTable** — l'oggetto vista che definisce i campi riga, colonna, valore e filtro. Una `PivotTable` legge *solo* dal suo `PivotCache`, mai direttamente dall'origine dati.
4. **Cells** — le `Cells` del foglio di lavoro in cui la `PivotTable` rende i valori calcolati e gli stili.

Un concetto particolarmente importante è la **cache condivisa**. Quando più tabelle pivot in una cartella di lavoro fanno riferimento allo stesso intervallo di origine, condividono *una* singola istanza di `PivotCache`. Un singolo `PivotCache` può essere referenziato da molte tabelle pivot, e l'aggiornamento di quella cache aggiorna immediatamente ogni `PivotTable` dipendente.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) indica da dove provengono i dati della cache. A partire da v26.7, `PivotCache.Refresh()` supporta solo i tipi di origine **`Sheet`** e **`Consolidation`** — cioè dati che risiedono negli intervalli del foglio di lavoro. Le origini esterne (database, connessioni esterne, ecc.) non sono ancora aggiornabili tramite l'API della cache.

{{% /alert %}}

A causa di questa catena, ci sono due percorsi di aggiornamento fondamentali in Aspose.Cells:

- **`PivotCache.Refresh()`** — ricarica origine → cache E ricalcola tutte le `PivotTable` dipendenti in una singola operazione.
- **`PivotTable.CalculateData()`** — ricalcola la visualizzazione di una singola `PivotTable` dai dati già memorizzati nella cache, senza tornare all'origine dati.

Tutti gli scenari di questo articolo utilizzano dati di origine da celle del foglio di lavoro, quindi il tipo di origine è `Sheet` e le operazioni di aggiornamento si comportano come descritto.

## Direttive Include Richieste

Tutti gli esempi C++ di questo articolo iniziano con le seguenti direttive di inclusione dell'intestazione e di namespace perché i tipi pivot si trovano nel namespace `Aspose::Cells::Pivot`:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Aggiorna Tutte le Tabelle Pivot nella Cartella di Lavoro

Quando hai bisogno di garantire che ogni cache pivot e ogni tabella pivot nella cartella di lavoro riflettano i dati di origine più recenti, l'API più semplice e completa è `Workbook.RefreshAll()`. Una singola chiamata attraversa l'intera cartella di lavoro — aggiornando ogni `PivotCache` dalla sua origine e poi ricalcolando ogni `PivotTable` dipendente. Questo è l'approccio consigliato per aggiornamenti generali e completi del documento dove le prestazioni non sono un problema.

L'esempio seguente costruisce una cartella di lavoro con un intervallo di origine Frutto/Anno/Importo, crea una tabella pivot, modifica alcuni valori di origine, e poi utilizza `RefreshAll()` per portare tutto aggiornato in una singola chiamata.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Aggiorna Tutte le Tabelle Pivot su un Singolo Foglio di Lavoro

A volte hai solo bisogno di aggiornare le tabelle pivot che si trovano su uno specifico foglio di lavoro — ad esempio, quando le tabelle pivot su altri fogli di lavoro sono note per essere non correlate e non devono essere toccate. Per questo caso, Aspose.Cells fornisce `Worksheet.RefreshPivotTables()`, che è limitato a una singola istanza di `Worksheet`.

Questo è più selettivo rispetto a `Workbook.RefreshAll()`: vengono aggiornate solo le tabelle pivot sul foglio di lavoro di destinazione, lasciando intatte le tabelle pivot su altri fogli di lavoro.

L'esempio seguente popola gli stessi dati di origine Frutto/Anno/Importo, aggiunge una tabella pivot sul primo foglio di lavoro, modifica alcuni valori di origine, e poi aggiorna solo le tabelle pivot su quel foglio di lavoro.

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

## Aggiorna una Singola Tabella Pivot

Quando desideri un controllo granulare su una singola tabella pivot, l'API basata sulla cache ti offre due opzioni. La scelta tra esse dipende da cosa è effettivamente cambiato: i dati di origine sottostanti, o solo le impostazioni di vista/layout della tabella pivot stessa.

### Dati di Origine Modificati — Usa `PivotCache.Refresh()`

Se i dati di origine sottostanti sono cambiati, il giusto punto di ingresso è `pivotTable.GetPivotCache().Refresh()`. Questa chiamata rilegge i dati di origine nella cache e poi ricalcola ogni `PivotTable` che dipende da quella cache.

{{% alert color="primary" %}}

Poiché le tabelle pivot condividono una singola istanza di `PivotCache`, la chiamata di `PivotCache.Refresh()` ricalcola **tutte** le tabelle pivot costruite su quella stessa cache — non solo quella a cui fai riferimento. Se due tabelle pivot condividono lo stesso intervallo di origine, l'aggiornamento di una cache aggiorna entrambe.

{{% /alert %}}

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine per dimostrare questo comportamento di cache condivisa, modifica alcuni valori di origine, e poi aggiorna tramite un riferimento di cache.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Riga di intestazione: Frutto / Anno / Importo
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Righe di dati
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Aggiungi la prima tabella pivot "Pivot1" ancorata alla cella E3, intervallo di origine A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Assegna i campi per Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Aggiungi una SECONDA tabella pivot "Pivot2" ancorata a E15 utilizzando lo STESSO intervallo di origine A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Assegna gli stessi campi per Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modifica diversi valori delle celle Importo nei dati di origine per simulare un cambio di dati
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Aggiorna la PivotCache condivisa aggiornando i dati della tabella pivot
    pivotTable1.RefreshData();

    // Salva la cartella di lavoro
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Solo Vista/Layout Modificato — Usa `CalculateData()`

Se i dati di origine *non* sono cambiati ma sono state modificate solo le impostazioni di vista o layout della tabella pivot (ad esempio, un campo è stato spostato in un'area diversa, o un'impostazione di aggiornamento all'apertura è stata attivata/disattivata), non c'è bisogno di tornare all'origine dati. La cache contiene già i dati corretti; deve essere ricalcolata solo la `PivotTable` renderizzata. In questo caso, `pivotTable.CalculateData()` è la scelta giusta.

Questo evita l'inutile recupero dall'origine ed è significativamente più veloce quando molte tabelle pivot condividono la stessa cache.

L'esempio seguente modifica una proprietà non di origine della tabella pivot e poi chiama `CalculateData()` per renderizzarla di nuovo dalla cache esistente.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Scrivi la riga di intestazione Frutto / Anno / Importo
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Scrivi 8 righe di dati (righe 2-9, adattandosi all'intervallo sorgente A1:C9)
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

    // Assegna i campi: Frutto a Riga, Anno a Colonna, Importo a Dati
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modifica una proprietà di visualizzazione/layout — questo è un cambio solo di presentazione,
    // quindi NON richiede la rilettura dei dati sorgente tramite PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() ridisegna la visualizzazione di QUESTA tabella pivot (dati + stile) dai
    // dati già contenuti nella PivotCache. Poiché i dati sorgente non sono cambiati,
    // non viene eseguito alcun ritorno alla sorgente — solo i valori memorizzati nella cache vengono ricalcolati
    // nelle celle del foglio di lavoro.
    pivotTable.CalculateData();

    // Salva la cartella di lavoro su disco
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Ottieni Tutte le Tabelle Pivot che Condividono lo Stesso PivotCache

Una cartella di lavoro spesso contiene molte tabelle pivot che si trovano tutte sopra una cache condivisa. Per enumerarle — ad esempio, prima di eseguire un aggiornamento in batch, o per diagnosticare l'impatto della cache condivisa — usa `PivotCache.GetPivotTables()`. Questo metodo restituisce la raccolta di ogni `PivotTable` che dipende dalla cache data.

Questo è anche il modo più diretto per confermare che due tabelle pivot effettivamente condividono la stessa istanza di `PivotCache`: puoi confrontare i riferimenti di cache, o semplicemente iterare la raccolta restituita da `GetPivotTables()` e osservare quali tabelle pivot appaiono in essa.

L'esempio seguente crea due tabelle pivot sullo stesso intervallo di origine, verifica che condividano la stessa istanza di cache, e poi enumera le tabelle pivot della cache.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // In Aspose.Cells, le tabelle pivot create dalla stessa origine dati
    // condividono automaticamente la stessa PivotCache
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // Ottieni tutte le tabelle pivot nel foglio di lavoro (che condividono la cache)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Migrazione dall'Obsoleto `PivotTable.RefreshData()`

Prima di Aspose.Cells for C++ v26.7, il modo standard per aggiornare una tabella pivot era chiamare `PivotTable.RefreshData()` su ogni tabella pivot individualmente. A partire da v26.7, quel metodo è contrassegnato come **obsoleto** e deve essere sostituito con le API consapevoli della cache descritte sopra.

Ci sono due motivi per cui l'approccio `RefreshData()` per tabella è problematico nelle cartelle di lavoro reali:

- Recupera i dati dall'origine *ogni* volta che viene chiamato, anche quando l'origine non è cambiata.
- Ogni chiamata aggiorna l'intera cache condivisa. Quando molte tabelle pivot condividono una cache, chiamare ripetutamente `RefreshData()` per ogni tabella pivot causa il recupero ripetuto della stessa cache, il che è molto lento.

Le sostituzioni consigliate sono:

- **Aggiorna TUTTE le tabelle pivot nella cartella di lavoro** → usa `workbook.RefreshAll();`
- **Aggiorna ALCUNE di esse** → usa `pivotTable.GetPivotCache().Refresh();` per una cache. Poiché la cache è condivisa, questa singola chiamata aggiorna ogni tabella pivot costruita sopra quella cache. Altre tabelle pivot che si trovano su una cache già aggiornata possono essere tranquillamente saltate.
- **Solo la vista/layout della pivot è cambiato** → usa `pivotTable.CalculateData();` per renderizzare di nuovo dalla cache esistente senza alcun ritorno all'origine.

L'esempio seguente dimostra il nuovo pattern efficiente per le cartelle di lavoro con più tabelle pivot che condividono una singola cache.

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

    pivotTable1.RefreshData();

    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Quale API di Aggiornamento Dovrei Usare?

La tabella seguente riassume le API di aggiornamento disponibili e quando scegliere ciascuna di esse.

| Obiettivo | API Consigliata | Note |
|------|-----------------|-------|
| Aggiorna tutto nella cartella di lavoro | `Workbook.RefreshAll()` | Una chiamata; copre tutte le cache e tabelle. |
| Aggiorna solo le tabelle pivot su un singolo foglio | `Worksheet.RefreshPivotTables()` | Limitato a un singolo foglio di lavoro. |
| Dati di origine modificati per una cache | `pivotTable.GetPivotCache().Refresh()` | Aggiorna TUTTE le tabelle pivot su quella cache condivisa. |
| Solo le impostazioni di vista/layout sono cambiate | `pivotTable.CalculateData()` | Salta l'inutile round-trip verso l'origine. |
| Elenca tutte le tabelle pivot su una cache condivisa | `pivotCache.GetPivotTables()` | Usa per enumerare prima dell'aggiornamento in blocco. |

In pratica, preferisci le API basate sulla cache rispetto all'obsoleto `RefreshData()` per tabella. Sono consapevoli delle cache condivise, evitano recuperi ridondanti dall'origine, e ti permettono di scegliere l'ambito più piccolo che soddisfa il tuo requisito di aggiornamento.

{{< app/cells/assistant language="cpp" >}}