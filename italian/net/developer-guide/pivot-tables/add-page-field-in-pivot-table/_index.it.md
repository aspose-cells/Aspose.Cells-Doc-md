---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells for .NET
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for .NET, inclusa l'aggiunta di campi filtro, il filtro a selezione singola e il filtro a selezione multipla.
keywords: Aspose.Cells, .NET, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Aggiungere campi filtro
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello comoda o tramite la raccolta di basso livello `PageFields`, ed è possibile gestire il filtro in modalità selezione singola, azzerarlo per mostrare ogni elemento del filtro, oppure commutare il campo sulla selezione multipla in modo che gli utenti possano selezionare più elementi del filtro contemporaneamente tramite l'interfaccia con caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**
Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della tabella pivot. L'utente finale lo vede come un menu a discesa nella parte superiore di una tabella pivot renderizzata in Excel e la selezione di uno degli elementi del filtro disponibili ricostruisce il corpo della tabella pivot in modo che vengano riepilogati solo i record appartenenti a quell'elemento del filtro. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché come `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Aggiungere un campo filtro**

### Aggiungere un campo filtro con AddFieldToArea
L'esempio seguente crea un piccolo dataset Frutto / Anno / Importo, posiziona una tabella pivot nella cella E3 con `Fruit` nell'area delle righe, `Amount` nell'area dei dati e `Year` nell'area del filtro, aggiorna la tabella pivot e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Crea una nuova cartella di lavoro
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
// Imposta la riga di intestazione
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Popola 9 righe di dati di esempio: Frutto, Anno, Importo
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}
// Aggiungi una tabella pivot ancorata alla cella E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Aggiungi campi alle rispettive aree: Frutto come Riga, Importo come Dati, Anno come campo Pagina
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Aggiorna e calcola i dati della tabella pivot
pivotTable.CalculateData();
// Salva la cartella di lavoro
workbook.Save("pageFieldSample.xlsx");
```

### Aggiungere un campo filtro con PageFields.Add
Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.Add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area del filtro viene sostituita con la chiamata API di basso livello.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — La tabella pivot e il campo pagina vengono costruiti esattamente come nello
//   Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit→Riga,
//   Amount→Dati). Qui sotto otteniamo il PivotField Year dalla
//   collezione BaseFields e lo passiamo a PageFields.Add — l'
//   alternativa di basso livello ad AddFieldToArea. Il risultato è
//   funzionalmente identico allo Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Intestazioni
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");
// Dati di esempio (9 righe)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);
// Aggiunge la tabella pivot in E3 coprendo A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// Fruit -> Riga, Amount -> Dati (Year andrà in Pagina qui sotto)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Approccio di basso livello: prendiamo il PivotField Year esistente dai BaseFields
// e lo registriamo nell'area Page tramite PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);
// Aggiorna affinché il nuovo campo pagina venga riflesso nella cartella di lavoro salvata
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtro a selezione singola (Mostrare un singolo elemento del filtro)**
Nel comportamento predefinito a selezione singola, il campo filtro viene renderizzato come un singolo menu a discesa e l'intero `PivotField.CurrentPageItem` seleziona quale elemento del filtro guida il corpo della tabella pivot. L'assegnazione di un indice specifico seleziona quell'unico elemento; l'assegnazione del valore sentinella speciale `0x7FFD` (decimale 32765) azzera il filtro in modo che ogni elemento del filtro venga riepilogato contemporaneamente. La selezione singola è l'impostazione predefinita; non è necessario abilitarla esplicitamente.

### Mostrare tutti gli elementi
Impostare `CurrentPageItem` sul valore magico `0x7FFD` equivale ad azzerare il filtro: il corpo della tabella pivot riepiloga ogni elemento del filtro come se non fosse applicato alcun filtro.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
class Program
{
    static void Main()
    {
        // Crea una nuova cartella di lavoro
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        // Popola i dati Frutto/Anno/Importo
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");
        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };
        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }
        // Crea tabella pivot in E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];
        // Configura i campi pivot: Frutto→Riga, Importo→Dati, Anno→Pagina
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
        pivotTable.CalculateData();
        // Cancella il filtro della pagina in modo che ogni elemento nel campo pagina sia visibile.
        // 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi" —
        // equivalente a selezionare "(Tutto)" nel menu a discesa del campo pagina di Excel.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;
        workbook.Save("output.xlsx");
    }
}
```

### Mostrare un elemento specifico
Impostare `CurrentPageItem` su un indice reale seleziona solo quell'elemento del filtro. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Crea workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;
// Aggiungi dati di esempio (Frutto/Anno/Importo)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");
cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");
cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");
cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");
// Aggiungi tabella pivot in E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];
// Aggiungi campi: Frutto→Riga, Importo→Dati, Anno→Pagina
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Operazioni specifiche del campo Pagina
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = secondo elemento nell'ordine ordinato (es. "2021")
// Aggiorna e calcola la tabella pivot
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtro a selezione multipla**
Il filtro a selezione multipla trasforma il menu a discesa del filtro in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi del filtro contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia di selezione multipla abbia effetto. Dopo che è stata abilitata, `PivotItem.IsHidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento oppure inserire in una whitelist solo elementi specifici.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — La tabella pivot e il campo pagina sono costruiti esattamente come nello
//   Scenario 1a (dati Frutto/Anno/Importo, pivot in E3, Frutto→Riga,
//   Importo→Dati, Anno→Pagina tramite AddFieldToArea).
//   Di seguito applichiamo il filtro a selezione multipla sul campo pagina.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Dati di esempio: Frutto | Anno | Importo
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");
string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}
Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// — Abilita la selezione multipla sul campo pagina
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;
// Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}
// Parte B — seleziona solo elementi specifici per valore di origine
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

> **Nota:** Quando si utilizza il filtro a selezione multipla tramite `PivotItem.IsHidden`, **almeno un `PivotItem` deve rimanere visibile** (`IsHidden == false`). Se ogni elemento è nascosto, Excel si arresta in modo anomalo all'apertura del file oppure renderizza una tabella pivot vuota. Verificare sempre che la whitelist di selezione multipla includa almeno un elemento dei dati di origine.

## **Quale API e quale modalità dovrei usare?**
La tabella seguente riassume quando utilizzare ciascuna API e modalità, in modo da poter scegliere la combinazione giusta senza leggere ogni scenario nel dettaglio.
| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro per nome della colonna di origine (caso più comune) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/d | Alto livello, una sola riga. Utilizzare questa opzione a meno che non sia necessario un riferimento a `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/d | Utilizzare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare un singolo elemento del filtro (modalità predefinita) | `PivotField.CurrentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / azzerare il filtro | `PivotField.CurrentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è la sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia di selezione multipla in Excel | `PivotField.IsMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata a `IsHidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.IsHidden` | impostare per ogni elemento | Almeno un elemento deve rimanere visibile (`IsHidden == false`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtro a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si arresta in modo anomalo all'apertura oppure renderizza una tabella pivot vuota. Costruire la whitelist in base ai dati di origine in modo che almeno un elemento rimanga visibile e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}

## **Articoli correlati**
- [Aggiornamento delle tabelle pivot in Aspose.Cells for .NET](/cells/it/net/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}