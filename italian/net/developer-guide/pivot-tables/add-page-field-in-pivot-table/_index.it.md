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
// Create a new workbook
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
// Set up the header row
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
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
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Refresh and calculate the pivot table data
pivotTable.CalculateData();
// Save the workbook
workbook.Save("pageFieldSample.xlsx");
```

### Aggiungere un campo filtro con PageFields.Add
Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.Add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area del filtro viene sostituita con la chiamata API di basso livello.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add — the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Headers
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");
// Sample data (9 rows)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);
// Refresh so the new page field is reflected in the saved workbook
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
        // Create a new workbook
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        // Populate Fruit/Year/Amount data
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
        // Create pivot table at E3
        var pivotTables = sheet.PivotTables;
        PivotTable pivotTable = pivotTables.Add("=A1:C7", 2, 4);
        // Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
        pivotTable.CalculateData();
        // Clear the page filter so every item in the page field is visible.
        // 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
        // equivalent to selecting "(All)" in Excel's page-field dropdown.
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
// Create workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;
// Add sample data (Fruit/Year/Amount)
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
// Add pivot table at E3
var pivotTables = sheet.PivotTables;
var pivotTable = pivotTables.Add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Page-field-specific operations
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtro a selezione multipla**
Il filtro a selezione multipla trasforma il menu a discesa del filtro in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi del filtro contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia di selezione multipla abbia effetto. Dopo che è stata abilitata, `PivotItem.IsHidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento oppure inserire in una whitelist solo elementi specifici.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Sample data: Fruit | Year | Amount
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
PivotTable pivotTable = pivots.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// — Enable multi-select on the page field
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;
// Part A — select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}
// Part B — select only specific items by source value
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