---
title: Visualizzazione o filtro Top 10 nella tabella pivot
linktitle: Visualizzazione o filtro Top 10 nella tabella pivot
description: Scopri come mostrare in Aspose.Cells for C++ solo gli elementi con il valore più alto o più basso di un campo pivot. Questo articolo illustra il metodo Top10AutoShow di Excel 97-2003, la lettura delle opzioni con GetTop10AutoShowSettings e il filtro Top 10 di Excel 2007-365 tramite FilterTop10.
keywords: Aspose.Cells, C++, tabella pivot, Top 10, visualizzazione automatica, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /it/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può risultare difficile da leggere quando il campo contiene decine di elementi. Un report Top 10 conserva soltanto gli elementi più in alto o più in basso nella classifica, fornendo esattamente le informazioni necessarie ai report di classifica: «i 5 prodotti con maggiori ricavi» o «le 3 regioni con il minor numero di vendite». Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **Excel 97-2003 AutoShow** — il metodo `PivotField.Top10AutoShow()`. Si tratta dell'impostazione classica «Mostra i primi/ultimi N elementi», memorizzata direttamente sul campo pivot. Funziona in tutte le versioni di Excel, poiché fa parte del formato originale della tabella pivot.
- **Excel 2007-365, filtro Top 10** — il metodo `PivotField.FilterTop10()`. Si tratta del filtro moderno Top 10 basato sui valori, disponibile nella sezione «Filtri valore» del menu del campo. Viene memorizzato come oggetto `PivotFilter` associato al campo e supporta la classificazione in base al numero di elementi o alla percentuale.

## **Visualizzazione Top 10 in Excel 97-2003 (Top10AutoShow)**
L'impostazione AutoShow classica viene configurata con una singola chiamata a `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isTop` — `true` mantiene gli elementi con la classificazione più alta (Primi), `false` mantiene quelli con la classificazione più bassa (Ultimi).
- `count` — il numero di elementi da mantenere, ad esempio 10 per un report Top 10 classico.
- `rankBy` — l'indice a base zero del **campo dati** in base al quale classificare gli elementi. Passare -1 per classificare gli elementi in base ai valori del campo stesso.
La classificazione può basarsi su un campo valore oppure sul campo stesso. Sono disponibili due varianti, illustrate di seguito.

### **Classifica in base a un campo valore**
Classificare gli elementi del campo di riga in base a un campo valore, ad esempio «Somma delle vendite». L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i 2 sport con le vendite più alte. `rankBy` è 0 perché «Somma delle vendite» è il campo dati all'indice 0.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Mostra i 2 elementi principali classificati in base a "Somma delle vendite" (indice del campo dati 0)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Classifica in base al campo stesso**
Un campo può essere classificato in base ai propri valori: passare -1 come `rankBy`. Per questa variante non è necessario alcun campo dati aggiuntivo; il campo deve essere collocato nell'area delle righe o delle colonne. L'esempio seguente mostra gli ultimi 3 sport in base ai valori del campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dall'XML della tabella pivot perché -1 è il valore predefinito del formato e `GetTop10AutoShowSettings().GetRankBy()` restituisce -1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Mostra i 3 elementi inferiori classificati in base al campo stesso (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Lettura delle opzioni correnti (GetTop10AutoShowSettings)**
Il metodo `PivotField.GetTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Utilizzarlo per verificare come verranno visualizzati gli elementi di una cartella di lavoro esistente o di una tabella pivot appena configurata. Il metodo può essere utilizzato anche con cartelle di lavoro caricate da file.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

I quattro membri corrispondono agli attributi AutoShow classici scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`); i valori letti sono quindi quelli applicati da tutte le versioni di Excel.

## **Nota**

{{% alert color="primary" %}}
- I membri diretti `IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` e `GetAutoShowField` di `PivotField` sono deprecati. Utilizzare invece l'oggetto `PivotFieldTop10AutoShowSettings`: `IsAutoShow` è sostituito da `GetTop10AutoShowSettings().IsAutoShow()`, `IsAscendShow` da `GetTop10AutoShowSettings().IsTop()`, `GetAutoShowCount` da `GetTop10AutoShowSettings().GetAutoShowCount()` e `GetAutoShowField` da `GetTop10AutoShowSettings().GetRankBy()`. Il metodo `Top10AutoShow()` è il metodo supportato per modificare le impostazioni.
- `Top10AutoShow` funziona con i campi di riga e di colonna. Un campo collocato soltanto nell'area dei filtri (area dei campi pagina) non può essere classificato in questo modo, perché i suoi elementi non sono organizzati nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro Top 10 (FilterTop10)**
Le versioni moderne di Excel presentano Top 10 come filtro sui valori nel menu del campo (sezione «Filtri valore», «Top 10...»). Aspose.Cells rappresenta questa funzionalità tramite il metodo `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`, che restituisce l'oggetto `PivotFilter` creato:
- `valueFieldIndex` — l'indice a base zero del campo dati i cui valori aggregati determinano la classifica degli elementi.
- `type` — il significato di `itemCount`. `PivotFilterType::Count` mantiene un numero fisso di elementi (l'opzione «Elementi» della finestra di dialogo). `PivotFilterType::Percent` mantiene una percentuale degli elementi, quindi `itemCount` è essa stessa la percentuale: con il valore 30, mantiene il 30% degli elementi più in alto nella classifica. `PivotFilterType::Sum` effettua la classifica in base alla copertura cumulativa dei valori.
- `isTop` — `true` per Primi, `false` per Ultimi.
- `itemCount` — il valore N in «Primi N»; l'unità dipende da `type`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Filtro Top 10 — mantiene i 2 elementi superiori in base a "Somma delle vendite" (indice del campo dati 0)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // Per un filtro basato sulla percentuale, mantenere invece il 30% superiore degli elementi:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` e `FilterTop10` sono due funzionalità distinte. AutoShow scrive sul campo pivot l'attributo classico `autoShow` ed è supportato da tutte le versioni di Excel, da Excel 97 in poi. `FilterTop10` scrive una voce `PivotFilter` del formato moderno, che richiede Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, una tabella pivot che utilizza il filtro moderno visualizza tutti gli elementi. Per i documenti che devono essere salvati e riaperti senza problemi tramite strumenti di versioni precedenti, preferire `Top10AutoShow`; per le cartelle di lavoro moderne, preferire `FilterTop10`, perché si integra con gli altri filtri sui valori.
{{% /alert %}}

## **Articoli correlati**
- [Filtro delle tabelle pivot per etichetta o valore](/cells/it/cpp/filter-by-label-or-value-of-pivot-table/)
- [Aggiunta di campi di riga e colonna alla tabella pivot](/cells/it/cpp/pivot-table-add-row-and-column-fields/)
- [Raggruppamento dei campi pivot nella tabella pivot](/cells/it/cpp/group-pivot-fields-in-the-pivot-table/)
- [Aggiornamento della tabella pivot](/cells/it/cpp/refresh-pivot-table/)
- [Aggiunta di un campo pagina alla tabella pivot](/cells/it/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}