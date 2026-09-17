---
title: Modificare il Layout dei Campi Pagina nella Tabella Pivot
description: Impara come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for .NET, inclusi l'impostazione dell'ordine di visualizzazione, del conteggio di avvolgimento e dell'ordine dei campi dei campi pagina nella parte superiore della tabella pivot.
linktitle: Modificare il Layout dei Campi Pagina nella Tabella Pivot
keywords: Aspose.Cells, libreria .NET, foglio elettronico, tabella pivot, campo pagina, ordine campi pagina, conteggio avvolgimento campi pagina, spostare campo pagina
type: docs
weight: 191
url: /it/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Questo articolo è una continuazione dell'argomento **Aggiungere un Campo Pagina nella Tabella Pivot**. Dimostra come controllare il layout dell'area dei campi pagina — la striscia di controlli filtro nella parte superiore di una tabella pivot — incluso l'ordine di visualizzazione, il conteggio di avvolgimento e il riordino dei campi.
{{% /alert %}}

## **Introduzione**
Una tabella pivot in Microsoft Excel espone un'**area dei campi pagina** dedicata che si trova sopra il corpo riga/colonna/dati della tabella. Questa area viene visualizzata come una striscia di controlli filtro a discesa (uno per campo pagina) e rappresenta ciò su cui gli utenti finali fanno clic per suddividere la pivot in base a criteri come anno o regione. Aspose.Cells modella questa area tramite la raccolta `PivotTable.PageFields` ed espone tre proprietà che controllano il modo in cui la striscia viene disposta visivamente:
- `PivotTable.PageFieldOrder` (un valore di `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti o *sotto* di essi.
- `PivotTable.PageFieldWrapCount` imposta quanti campi pagina vengono posizionati per riga o colonna prima dell'avvolgimento.
- `PivotTable.PageFields.Move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordine.
Questo articolo illustra tre esempi di codice che mostrano ciascuna di queste operazioni su un set di dati condiviso, in modo da poter confrontare i layout risultanti affiancati.

## **Dati di Origine**
| Frutto | Anno | Regione | Importo |
|--------|------|---------|---------|
| Mela   | 2022 | Nord    | 150     |
| Mela   | 2023 | Nord    | 180     |
| Banana | 2022 | Sud     | 120     |
| Banana | 2023 | Sud     | 140     |
| Ciliegia | 2022 | Est   | 200     |
| Ciliegia | 2023 | Est   | 220     |
| Uva    | 2022 | Ovest   | 90      |
| Uva    | 2023 | Ovest   | 110     |
Tutte e otto le righe sono popolate in ogni esempio di codice, nello stesso ordine, quindi i dati di origine non differiscono mai tra gli scenari — solo le proprietà del layout dei campi pagina cambiano.

## **Esempio 1: Over Then Down**
Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) per apparire **affiancati in una singola riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse della pagina (l'ordine delle chiamate `AddFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati, e quindi impostiamo `PageFieldOrder` su `PrintOrderType.OverThenDown` con `PageFieldWrapCount = 2`. Con `OverThenDown` e un conteggio di avvolgimento di 2, i due campi pagina sono disposti orizzontalmente affiancati in una singola riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;
int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;
// Intestazioni (riga 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");
// Riga 1: Apple, 2022, Nord, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);
// Riga 2: Apple, 2023, Nord, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);
// Riga 3: Banana, 2022, Sud, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);
// Riga 4: Banana, 2023, Sud, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);
// Riga 5: Ciliegia, 2022, Est, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);
// Riga 6: Ciliegia, 2023, Est, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);
// Riga 7: Uva, 2022, Ovest, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);
// Riga 8: Uva, 2023, Ovest, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);
// Aggiungi foglio PivotTableReport
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;
// Crea tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];
// Aggiungi campi
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Frutta
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Anno
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Regione
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Importo
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;
// Configura il layout dell'area dei campi pagina: posiziona i campi pagina prima in orizzontale, va a capo dopo ogni 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;
// Aggiorna e calcola
pivotTable.CalculateData();
// Salva
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Esempio 2: Down Then Over**
In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse della pagina (con `Year` per primo), e `Amount` (Sum) come campo dati — esattamente come nell'Esempio 1. Quindi impostiamo `PageFieldOrder` su `PrintOrderType.DownThenOver` e `PageFieldWrapCount` su `2`. Con `DownThenOver` e un conteggio di avvolgimento di 2, i due campi pagina sono impilati verticalmente — `Year` in alto, `Region` direttamente sotto — formando una singola colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza uno, in contrasto con l'Esempio 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];
var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}
var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};
for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}
int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);
pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;
pivotTable.CalculateData();
workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Esempio 3: Spostare un Campo Pagina**
Nel terzo scenario manteniamo questo set di dati e l'allocazione dei campi, impostiamo un layout neutro (`OverThenDown` con conteggio di avvolgimento `2`), e quindi dimostriamo l'operazione `PageFields.Move`. La chiamata `Move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) alla posizione 1, e il campo pagina che era alla posizione 1 (`Region`) si sposta alla posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di avvolgimento e ordine rimane invariata, quindi la striscia è ancora visualizzata orizzontalmente affiancata — solo l'ordine dei due menu a discesa è stato scambiato.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");
dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);
dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);
dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);
dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);
dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);
dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);
dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);
dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);
int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];
int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;
pivotTable.PageFields.Move(0, 1);
pivotTable.CalculateData();
workbook.Save("pageFieldLayout_move.xlsx");
```

## **Articoli Correlati**
- [Aggiungere un Campo Pagina nella Tabella Pivot](/cells/it/net/add-page-field-in-pivot-table/) — la pagina padre che introduce come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi Riga e Colonna nella Tabella Pivot](/cells/it/net/pivot-table-add-row-and-column-fields/) — tratta l'allocazione dei campi agli assi di riga e colonna, completando il lavoro sull'asse della pagina mostrato qui.
- [Gestire i Campi Valore nella Tabella Pivot](/cells/it/net/manage-value-fields/) — descrive come configurare l'area dati (valore), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Aggiornare la Tabella Pivot](/cells/it/net/refresh-pivot-table/) — spiega `RefreshData` e `CalculateData`, che sono richiesti dopo il riordino dei campi pagina.
- [Applicare uno Stile alla Tabella Pivot](/cells/it/net/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot visualizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="csharp" >}}