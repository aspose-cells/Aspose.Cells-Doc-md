---
title: Modifica del layout dei campi pagina nella tabella pivot
linktitle: Modifica del layout dei campi pagina nella tabella pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for .NET, inclusa l'impostazione dell'ordine di visualizzazione, del numero di wrap e dell'ordine dei campi pagina nella parte superiore della tabella pivot.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, tabella pivot, campo pagina, ordine dei campi pagina, numero di wrap dei campi pagina, spostare un campo pagina
type: docs
weight: 191
url: /it/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Questo articolo è una continuazione dell'argomento **Aggiungere un campo pagina nella tabella pivot**. Dimostra come controllare il layout dell'area dei campi pagina, ovvero la striscia di controlli filtro nella parte superiore di una tabella pivot, inclusi l'ordine di visualizzazione, il numero di wrap e il riordino dei campi.

{{% /alert %}}

## **Introduzione**

Una tabella pivot in Microsoft Excel espone una **area dei campi pagina** dedicata che si trova sopra il corpo delle righe/colonne/dati della tabella. Quest'area viene visualizzata come una striscia di controlli filtro a discesa (uno per campo pagina) ed è ciò che gli utenti finali cliccano per filtrare la tabella pivot in base a criteri come l'anno o la regione. Aspose.Cells modella quest'area tramite la raccolta `PivotTable.PageFields` ed espone tre proprietà che controllano come la striscia viene disposta visivamente:

- `PivotTable.PageFieldOrder` (un valore `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti o *sotto* di essi.
- `PivotTable.PageFieldWrapCount` imposta quanti campi pagina vengono posizionati per riga o colonna prima di andare a capo.
- `PivotTable.PageFields.Move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordinamento.

Questo articolo illustra tre esempi di codice che mostrano ciascuna di queste operazioni su un set di dati condiviso, così da poter confrontare i layout risultanti fianco a fianco.

## **Dati di origine**

Tutti e tre gli esempi seguenti caricano queste otto righe di dati di vendita in un foglio di lavoro denominato `PivotData`. I dati contengono due candidati come campi pagina (`Year`, `Region`), un candidato come campo riga (`Fruit`) e una misura (`Amount`), il che rende significativa la striscia dei campi pagina da esaminare.

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

Tutte le otto righe vengono popolate in ogni esempio di codice, nello stesso ordine, così i dati di origine non differiscono mai tra gli scenari, cambiano solo le proprietà di layout dei campi pagina.

## **Esempio 1: Sopra poi giù**

Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) in modo che appaiano **fianco a fianco in una singola riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` come primo e `Region` come secondo sull'asse delle pagine (l'ordine delle chiamate ad `AddFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Somma) come campo dati, e quindi impostiamo `PageFieldOrder` su `PrintOrderType.OverThenDown` con `PageFieldWrapCount = 2`. Con `OverThenDown` e un wrap count di 2, i due campi pagina vengono disposti orizzontalmente fianco a fianco in una singola riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

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

// Riga 1: Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Riga 2: Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Riga 3: Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Riga 4: Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Riga 5: Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Riga 6: Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Riga 7: Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Riga 8: Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// Aggiungi il foglio PivotTableReport
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Crea la tabella pivot con origine PivotData!A1:D9 posizionata in A1 su PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Aggiungi i campi
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Fruit
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Year
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Region
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Amount
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Configura il layout dell'area dei campi pagina: disponi i campi pagina prima in orizzontale, vai a capo dopo ogni 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Aggiorna e calcola
pivotTable.CalculateData();

// Salva
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Esempio 2: Giù poi sopra**

In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse delle pagine (con `Year` per primo), e `Amount` (Somma) come campo dati, esattamente come nell'Esempio 1. Quindi impostiamo `PageFieldOrder` su `PrintOrderType.DownThenOver` e `PageFieldWrapCount` su `2`. Con `DownThenOver` e un wrap count di 2, i due campi pagina vengono impilati verticalmente — `Year` in alto, `Region` direttamente sotto — formando una singola colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza una, in contrasto con l'Esempio 1.

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

## **Esempio 3: Spostare un campo pagina**

Nel terzo scenario manteniamo questo set di dati e l'allocazione dei campi, impostiamo un layout neutro (`OverThenDown` con wrap count `2`) e quindi dimostriamo l'operazione `PageFields.Move`. La chiamata a `Move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) alla posizione 1, e il campo pagina che era alla posizione 1 (`Region`) si sposta alla posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. Il wrap e la modalità di ordinamento rimangono invariati, quindi la striscia viene ancora visualizzata orizzontalmente fianco a fianco — solo l'ordine dei due menu a discesa è stato scambiato.

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

## **Articoli correlati**

- [Aggiungere un campo pagina nella tabella pivot](/cells/it/net/add-page-field-in-pivot-table/) — la pagina principale che illustra come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi riga e colonna nella tabella pivot](/cells/it/net/pivot-table-add-row-and-column-fields/) — illustra l'allocazione dei campi agli assi di riga e colonna, completando il lavoro sull'asse delle pagine mostrato qui.
- [Gestire i campi valore nella tabella pivot](/cells/it/net/manage-value-fields/) — descrive come configurare l'area dati (valori), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Aggiornare la tabella pivot](/cells/it/net/refresh-pivot-table/) — spiega `RefreshData` e `CalculateData`, che sono richiesti dopo il riordino dei campi pagina.
- [Applicare uno stile alla tabella pivot](/cells/it/net/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot renderizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="csharp" >}}