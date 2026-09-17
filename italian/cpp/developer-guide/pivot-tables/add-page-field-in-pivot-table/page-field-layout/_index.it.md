---
title: Modificare il Layout dei Campi Pagina nella Tabella Pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for C++, inclusa l'impostazione dell'ordine di visualizzazione, del conteggio di avvolgimento e dell'ordine dei campi dei campi pagina nella parte superiore della tabella pivot.
linktitle: Modificare il Layout dei Campi Pagina nella Tabella Pivot
keywords: Aspose.Cells, libreria C++, foglio di calcolo, tabella pivot, campo pagina, ordine campi pagina, conteggio campi pagina per riga, spostare campo pagina
type: docs
weight: 191
url: /it/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Questo articolo è un proseguimento dell'argomento **Aggiungere un Campo Pagina nella Tabella Pivot**. Illustra come controllare il layout dell'area dei campi pagina — la striscia di controlli filtro nella parte superiore di una tabella pivot — incluso l'ordine di visualizzazione, il conteggio di avvolgimento e il riordino dei campi.
{{% /alert %}}

## **Introduzione**
Una tabella pivot in Microsoft Excel espone una dedicata **area dei campi pagina** che si trova sopra il corpo riga/colonna/dati della tabella. Quest'area viene visualizzata come una striscia di controlli filtro a discesa (uno per campo pagina) ed è ciò che gli utenti finali cliccano per suddividere la pivot per criteri come anno o regione. Aspose.Cells for C++ modella quest'area attraverso la raccolta `PivotTable.PageFields` ed espone tre proprietà che controllano come la striscia viene disposta visivamente:
- `PivotTable.PageFieldOrder` (un valore di `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti oppure *sotto* di essi.
- `PivotTable.PageFieldWrapCount` imposta quanti campi pagina vengono posizionati per riga o colonna prima di andare a capo.
- `PivotTable.PageFields.Move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordinamento.
Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un dataset condiviso, in modo da poter confrontare i layout risultanti fianco a fianco.

## **Dati di Origine**
| Frutta | Anno | Regione | Importo |
|--------|------|---------|---------|
| Mela   | 2022 | Nord    | 150     |
| Mela   | 2023 | Nord    | 180     |
| Banana | 2022 | Sud     | 120     |
| Banana | 2023 | Sud     | 140     |
| Ciliegia | 2022 | Est   | 200     |
| Ciliegia | 2023 | Est   | 220     |
| Uva    | 2022 | Ovest   | 90      |
| Uva    | 2023 | Ovest   | 110     |
Tutte le otto righe sono popolate in ogni esempio di codice, nello stesso ordine, quindi i dati di origine non differiscono mai tra gli scenari — solo le proprietà di layout dei campi pagina cambiano.

## **Esempio 1: Over Then Down**
Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) per apparire **fianco a fianco in una singola riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse delle pagine (l'ordine delle chiamate `AddFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati, e quindi impostiamo `PageFieldOrder` su `PrintOrderType.OverThenDown` con `PageFieldWrapCount = 2`. Con `OverThenDown` e un conteggio di avvolgimento di 2, i due campi pagina sono disposti orizzontalmente fianco a fianco in una singola riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();
    // Intestazioni (riga 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");
    // Riga 1: Mela, 2022, Nord, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);
    // Riga 2: Mela, 2023, Nord, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);
    // Riga 3: Banana, 2022, Sud, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);
    // Riga 4: Banana, 2023, Sud, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);
    // Riga 5: Ciliegia, 2022, Est, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);
    // Riga 6: Ciliegia, 2023, Est, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);
    // Riga 7: Uva, 2022, Ovest, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);
    // Riga 8: Uva, 2023, Ovest, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);
    // Aggiungi foglio PivotTableReport
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();
    // Crea tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    // Aggiungi campi
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Frutta
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Anno
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Regione
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Importo
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);
    // Configura il layout dell'area dei campi pagina: posiziona i campi pagina prima in orizzontale, va a capo ogni 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);
    // Aggiorna e calcola
    pivotTable.CalculateData();
    // Salva
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Esempio 2: Down Then Over**
In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse delle pagine (con `Year` per primo), e `Amount` (Sum) come campo dati — esattamente come nell'Esempio 1. Quindi impostiamo `PageFieldOrder` su `PrintOrderType.DownThenOver` e `PageFieldWrapCount` su `2`. Con `DownThenOver` e un conteggio di avvolgimento di 2, i due campi pagina sono impilati verticalmente — `Year` in alto, `Region` direttamente sotto — formando una singola colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza uno, in contrasto con l'Esempio 1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");
    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }
    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };
    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };
    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }
    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);
    pivotTable.CalculateData();
    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Esempio 3: Spostare un Campo Pagina**
Nel terzo scenario manteniamo questo dataset e l'allocazione dei campi, impostiamo un layout neutro (`OverThenDown` con conteggio di avvolgimento `2`), e quindi dimostriamo l'operazione `PageFields.Move`. La chiamata `Move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) alla posizione 1, e il campo pagina che era alla posizione 1 (`Region`) si sposta alla posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di avvolgimento e di ordinamento non cambia, quindi la striscia è ancora visualizzata orizzontalmente fianco a fianco — solo l'ordine dei due menu a discesa è stato scambiato.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");
    Cells dataCells = dataSheet.GetCells();
    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");
    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);
    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);
    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);
    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);
    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);
    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);
    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);
    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);
    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");
    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);
    pivotTable.GetPageFields().Move(0, 1);
    pivotTable.CalculateData();
    wb.Save(u"pageFieldLayout_move.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articoli Correlati**
- [Aggiungere un Campo Pagina nella Tabella Pivot](/cells/it/cpp/add-page-field-in-pivot-table/) — la pagina principale che illustra come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi Riga e Colonna nella Tabella Pivot](/cells/it/cpp/row-and-column-fields/) — tratta l'allocazione dei campi agli assi di riga e colonna, completando il lavoro sull'asse delle pagine mostrato qui.
- [Gestire i Campi Valore nella Tabella Pivot](/cells/it/cpp/manage-value-fields/) — descrive come configurare l'area dati (valore), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Aggiornare la Tabella Pivot](/cells/it/cpp/refresh-pivot-table/) — spiega `RefreshData` e `CalculateData`, che sono necessari dopo il riordino dei campi pagina.
- [Applicare uno Stile alla Tabella Pivot](/cells/it/cpp/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot visualizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="" >}}