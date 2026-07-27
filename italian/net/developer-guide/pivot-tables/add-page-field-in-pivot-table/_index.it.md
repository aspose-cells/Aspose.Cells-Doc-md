---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi filtro
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for .NET, inclusi l'aggiunta di campi filtro, il filtro a selezione singola e il filtro a selezione multipla.
keywords: Aspose.Cells, .NET, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello di comodo utilizzo oppure tramite la raccolta di livello inferiore `PageFields`, ed è possibile gestire il filtro pagina in modalità a selezione singola, azzerarlo per mostrare ogni elemento della pagina, oppure commutare il campo in selezione multipla in modo che gli utenti possano scegliere più elementi della pagina contemporaneamente tramite l'interfaccia a caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**

Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una pivot renderizzata in Excel, e selezionando uno degli elementi di pagina disponibili il corpo della pivot viene ricostruito in modo che vengano riepilogati solo i record appartenenti a quell'elemento di pagina. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché come `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

Un campo filtro può operare con due comportamenti. Nel comportamento predefinito di **selezione singola** è visibile un solo elemento di pagina alla volta, quindi il corpo della pivot riepiloga esattamente un sottoinsieme. Nel comportamento di **selezione multipla** il campo espone un elenco di caselle di controllo e il corpo della pivot riepiloga l'unione di ogni elemento di pagina selezionato. Lo stesso campo di origine può essere spostato avanti e indietro tra questi comportamenti attivando/disattivando una singola proprietà.

Aspose.Cells for .NET espone due modi equivalenti per registrare un campo filtro. L'API di alto livello è `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, che prende il nome della colonna di origine e aggiunge il campo in una singola chiamata. L'API di livello inferiore è `PivotTable.PageFields.Add(PivotField)`, che viene utilizzata quando si dispone già di un riferimento a `PivotField` e si desidera aggiungere la stessa istanza di campo all'area filtro. Entrambe le API finiscono per popolare la stessa raccolta `PageFields`, e il resto di questo articolo mostra come scegliere tra di esse e come gestire ciascuna modalità di filtraggio.

## **Aggiungere un campo filtro**

Esistono due modi per registrare un campo pivot nell'area filtro. La chiamata di alto livello accetta il nome della colonna di origine come stringa ed è il percorso più comune. La chiamata di livello inferiore accetta un'istanza esistente di `PivotField` ed è comoda quando lo stesso oggetto campo deve essere riutilizzato in più aree pivot. Entrambe le chiamate inseriscono il campo in `PivotTable.PageFields`, dopodiché appare come menu a discesa della pagina nella parte superiore della pivot renderizzata.

### Aggiungere un campo filtro con AddFieldToArea

L'esempio seguente crea un piccolo set di dati Frutta / Anno / Importo, posiziona una tabella pivot nella cella E3 con `Fruit` nell'area riga, `Amount` nell'area dati e `Year` nell'area filtro, aggiorna la pivot e salva la cartella di lavoro.

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

// Aggiungi campi alle loro aree: Frutto come Riga, Importo come Dati, Anno come campo Pagina
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Aggiorna e calcola i dati della tabella pivot
pivotTable.CalculateData();

// Salva la cartella di lavoro
workbook.Save("pageFieldSample.xlsx");
```

### Aggiungere un campo filtro con PageFields.Add

Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.Add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area filtro viene sostituita con la chiamata API di livello inferiore.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — La tabella pivot e il campo pagina vengono costruiti esattamente come in
//   Scenario 1a (dati Frutto/Anno/Importo, pivot in E3, Frutto→Riga,
//   Importo→Dati). Sotto otteniamo il PivotField Anno dalla
//   raccolta BaseFields e lo passiamo a PageFields.Add — l'
//   alternativa di basso livello a AddFieldToArea. Il risultato è
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

// Aggiungi tabella pivot in E3 coprendo A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Frutto -> Riga, Importo -> Dati (Anno andrà a Pagina sotto)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Approccio di basso livello: prendi il PivotField Anno esistente da BaseFields
// e registralo nell'area Pagina tramite PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Aggiorna così che il nuovo campo pagina venga riflesso nella cartella di lavoro salvata
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Filtraggio a selezione singola (visualizzazione di un elemento di pagina)**

Nel comportamento predefinito di selezione singola, il campo filtro viene renderizzato come un singolo menu a discesa e l'intero `PivotField.CurrentPageItem` seleziona quale elemento di pagina guida il corpo della pivot. Assegnando un indice specifico si seleziona quell'unico elemento; assegnando il valore sentinella speciale `0x7FFD` (decimale 32765) il filtro viene azzerato in modo che ogni elemento di pagina venga riepilogato contemporaneamente. La selezione singola è il valore predefinito; non è necessario abilitarla esplicitamente.

### Visualizzare tutti gli elementi

Impostare `CurrentPageItem` sul valore magico `0x7FFD` equivale ad azzerare il filtro pagina: il corpo della pivot riepiloga ogni elemento di pagina come se non fosse applicato alcun filtro.

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

        // Crea una tabella pivot in E3
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

### Visualizzare un elemento specifico

Impostare `CurrentPageItem` su un indice reale seleziona solo quell'unico elemento di pagina. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crea cartella di lavoro
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

// Operazioni specifiche del campo pagina
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = secondo elemento nell'ordine ordinato (ad es. "2021")

// Aggiorna e calcola la tabella pivot
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Filtraggio a selezione multipla**

Il filtraggio a selezione multipla trasforma il menu a discesa della pagina in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi di pagina contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia di selezione multipla abbia effetto. Dopo che è stata abilitata, `PivotItem.IsHidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento o inserire in una whitelist solo elementi specifici.

Il codice seguente abilita la selezione multipla sullo stesso campo filtro Year costruito nello Scenario 1a, quindi mostra due schemi: la Parte A rivela ogni elemento di pagina lasciando `IsHidden` impostato su `false` per ogni voce, mentre la Parte B inserisce in whitelist solo i valori di origine scelti e nasconde tutto il resto tramite un blocco `switch (pivotItems[i].GetStringValue())`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — La tabella pivot e il campo pagina sono costruiti esattamente come in
//   Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit→Row,
//   Amount→Data, Year→Page tramite AddFieldToArea).
//   Di seguito applichiamo il filtro a selezione multipla sul campo pagina.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Dati di esempio: Fruit | Year | Amount
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
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
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

// Parte B — seleziona solo elementi specifici per valore sorgente
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

> **Nota:** Quando si utilizza il filtraggio a selezione multipla tramite `PivotItem.IsHidden`, **almeno un `PivotItem` deve rimanere visibile** (`IsHidden == false`). Se ogni elemento è nascosto, Excel si arresta in modo anomalo all'apertura del file oppure rende una pivot vuota. Verificare sempre che la whitelist di selezione multipla includa almeno un elemento dei dati di origine.

## **Quale API e quale modalità dovrei usare?**

La tabella seguente riassume quando utilizzare ciascuna API e modalità, in modo da poter scegliere la giusta combinazione senza leggere ogni scenario nel dettaglio.

| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro tramite il nome della colonna di origine (caso più comune) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/d | Alto livello, una sola riga. Utilizzare questa opzione a meno che non serva un riferimento a `PivotField`. |
| Aggiungere un campo filtro quando si dispone già di un oggetto `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/d | Utilizzare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare un singolo elemento di pagina (modalità predefinita) | `PivotField.CurrentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / azzerare il filtro pagina | `PivotField.CurrentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è la sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia di selezione multipla in Excel | `PivotField.IsMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata a `IsHidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.IsHidden` | impostare per ogni elemento | Almeno un elemento deve rimanere visibile (`IsHidden == false`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtraggio a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si arresta in modo anomalo all'apertura oppure rende una pivot vuota. Costruire la whitelist in base ai dati di origine in modo che almeno un elemento rimanga visibile, e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
