---
title: Modificare il Layout dei Campi Pagina in una Tabella Pivot
linktitle: Modificare il Layout dei Campi Pagina in una Tabella Pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for C++, incluse le impostazioni dell'ordine di visualizzazione, del conteggio di disposizione e dell'ordine dei campi pagina nella parte superiore della tabella pivot.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, tabella pivot, campo pagina, ordine dei campi pagina, conteggio di disposizione dei campi pagina, spostare il campo pagina
type: docs
weight: 191
url: /it/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Questo articolo è un proseguimento dell'argomento **Aggiungere un Campo Pagina in una Tabella Pivot**. Dimostra come controllare il layout dell'area dei campi pagina, ovvero la striscia di controlli filtro nella parte superiore di una tabella pivot, inclusi l'ordine di visualizzazione, il conteggio di disposizione e il riordino dei campi.

{{% /alert %}}

## **Introduzione**

Una tabella pivot in Microsoft Excel espone una dedicata **area dei campi pagina** che si trova sopra il corpo di righe/colonne/dati della tabella. Quest'area viene visualizzata come una striscia di controlli filtro a discesa (uno per ciascun campo pagina) ed è ciò che gli utenti finali cliccano per suddividere la pivot in base a criteri come anno o regione. Aspose.Cells for C++ modella quest'area tramite la raccolta `PivotTable.PageFields` ed espone tre proprietà che controllano la disposizione visiva della striscia:

- `PivotTable.PageFieldOrder` (un valore `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti oppure *sotto* di essi.
- `PivotTable.PageFieldWrapCount` imposta quanti campi pagina vengono disposti per riga o colonna prima di andare a capo.
- `PivotTable.PageFields.Move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordinamento.

Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un dataset condiviso, in modo da poter confrontare i layout risultanti fianco a fianco.

## **Dati di Origine**

Tutti i tre esempi seguenti caricano queste otto righe di dati di vendita in un foglio di lavoro denominato `PivotData`. I dati contengono due candidati per il campo pagina (`Year`, `Region`), un candidato per il campo riga (`Fruit`) e una misura (`Amount`), il che rende significativa la striscia dei campi pagina da analizzare.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Tutte le otto righe vengono popolate in ogni esempio di codice, nello stesso ordine, quindi i dati di origine non differiscono mai tra gli scenari, cambiano solo le proprietà di layout dei campi pagina.

## **Esempio 1: Prima in Larghezza, poi in Altezza**

Nella prima scenario configuriamo i due campi pagina (`Year`, `Region`) in modo che appaiano **fianco a fianco in un'unica riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse della pagina (l'ordine delle chiamate ad `AddFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati, e quindi impostiamo `PageFieldOrder` su `PrintOrderType.OverThenDown` con `PageFieldWrapCount = 2`. Con `OverThenDown` e un conteggio di disposizione pari a 2, i due campi pagina vengono disposti orizzontalmente fianco a fianco in un'unica riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

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

    // Riga 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Riga 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Riga 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Riga 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Riga 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Riga 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Riga 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Riga 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // Aggiungi il foglio PivotTableReport
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Crea una tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Aggiungi i campi
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Configura il layout dell'area dei campi pagina: posiziona i campi pagina in orizzontale, a capo ogni 2
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

## **Esempio 2: Prima in Altezza, poi in Larghezza**

In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse della pagina (con `Year` per primo), e `Amount` (Sum) come campo dati, esattamente come nell'Esempio 1. Quindi impostiamo `PageFieldOrder` su `PrintOrderType.DownThenOver` e `PageFieldWrapCount` su `2`. Con `DownThenOver` e un conteggio di disposizione pari a 2, i due campi pagina vengono impilati verticalmente, `Year` in alto, `Region` direttamente sotto, formando un'unica colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza uno, in contrasto con l'Esempio 1.

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

Nella terzo scenario manteniamo lo stesso dataset e l'allocazione dei campi, impostiamo un layout neutro (`OverThenDown` con conteggio di disposizione `2`), e quindi dimostriamo l'operazione `PageFields.Move`. La chiamata `Move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) nella posizione 1, e il campo pagina che era nella posizione 1 (`Region`) si sposta nella posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di disposizione e l'ordine rimangono invariati, quindi la striscia viene ancora visualizzata orizzontalmente fianco a fianco, è stato scambiato solo l'ordine dei due menu a discesa.

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

- [Aggiungere un Campo Pagina in una Tabella Pivot](/cells/it/cpp/add-page-field-in-pivot-table/) — la pagina principale che introduce come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi Riga e Colonna in una Tabella Pivot](/cells/it/cpp/row-and-column-fields/) — tratta l'allocazione dei campi sugli assi di riga e colonna, completando il lavoro sull'asse della pagina mostrato qui.
- [Gestire i Campi Valore in una Tabella Pivot](/cells/it/cpp/manage-value-fields/) — descrive come configurare l'area dei dati (valore), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Aggiornare una Tabella Pivot](/cells/it/cpp/refresh-pivot-table/) — spiega `RefreshData` e `CalculateData`, che sono richiesti dopo aver riordinato i campi pagina.
- [Applicare uno Stile a una Tabella Pivot](/cells/it/cpp/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot visualizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="" >}}