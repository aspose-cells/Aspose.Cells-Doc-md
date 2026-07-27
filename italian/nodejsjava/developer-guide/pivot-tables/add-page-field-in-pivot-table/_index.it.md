---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi filtro
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for Node.js via Java, inclusi aggiunta di campi filtro, filtro a selezione singola e filtro a selezione multipla.
keywords: Aspose.Cells, Node.js via Java, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello oppure tramite la raccolta di livello inferiore `PageFields`, e gestire il filtro pagina in modalità selezione singola, cancellarlo per mostrare ogni elemento della pagina oppure commutare il campo sulla selezione multipla in modo che gli utenti possano selezionare più elementi della pagina contemporaneamente tramite l'interfaccia con caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**

Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della tabella pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una tabella pivot visualizzata in Excel, e selezionare uno degli elementi della pagina disponibili ricostruisce il corpo della tabella pivot in modo che vengano riepilogati solo i record appartenenti a quell'elemento della pagina. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché come `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

Un campo filtro può operare in due modalità. Nella modalità predefinita **selezione singola** è visibile un solo elemento della pagina alla volta, quindi il corpo della tabella pivot riepiloga esattamente un sottoinsieme. Nella modalità **selezione multipla** il campo espone un elenco con caselle di controllo e il corpo della tabella pivot riepiloga l'unione di tutti gli elementi della pagina selezionati. Lo stesso campo di origine può essere spostato avanti e indietro tra queste modalità attivando/disattivando una singola proprietà.

Aspose.Cells for Node.js via Java espone due modi equivalenti per registrare un campo filtro. L'API di alto livello è `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, che accetta il nome della colonna di origine e aggiunge il campo in una singola chiamata. L'API di livello inferiore è `pivotTable.getPageFields().add(PivotField)`, che viene utilizzata quando si ha già un riferimento a un `PivotField` e si desidera aggiungere la stessa istanza del campo all'area filtro. Entrambe le API finiscono per popolare la stessa raccolta `PageFields`, e il resto di questo articolo mostra come scegliere tra esse e come gestire ciascuna modalità di filtraggio.

## **Aggiunta di un campo filtro**

Esistono due modi per registrare un campo pivot nell'area filtro. La chiamata di alto livello accetta il nome della colonna di origine come stringa ed è il percorso più comune. La chiamata di livello inferiore accetta un'istanza esistente di `PivotField` ed è utile quando lo stesso oggetto campo deve essere riutilizzato in più aree pivot. Entrambe le chiamate inseriscono il campo in `pivotTable.getPageFields()`, dopodiché appare come menu a discesa della pagina nella parte superiore della tabella pivot visualizzata.

### Aggiunta di un campo filtro con addFieldToArea

L'esempio seguente crea un piccolo set di dati Frutto / Anno / Importo, posiziona una tabella pivot alla cella E3 con `Fruit` nell'area riga, `Amount` nell'area dati e `Year` nell'area filtro, aggiorna la tabella pivot e salva la cartella di lavoro.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Imposta la riga di intestazione
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Popola 9 righe di dati di esempio: Frutto, Anno, Quantità
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Aggiungi una tabella pivot ancorata alla cella E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Aggiungi campi alle loro aree: Frutto come Riga, Quantità come Dati, Anno come campo Pagina
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Aggiorna e calcola i dati della tabella pivot
pivotTable.refreshData();
pivotTable.calculateData();

// Salva la cartella di lavoro
workbook.save("pageFieldSample.xlsx");
```

### Aggiunta di un campo filtro con getPageFields().add

Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `pivotTable.getPageFields().add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area filtro viene sostituita con la chiamata API di livello inferiore.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Intestazioni
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Dati di esempio (9 righe)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Aggiunge la tabella pivot in E3 coprendo A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Riga, Amount -> Dati (Year verrà inserito nell'area Pagina qui sotto)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Approccio di basso livello: recupera il PivotField Year esistente da BaseFields
// e lo registra nell'area Pagina tramite PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Aggiorna in modo che il nuovo campo pagina venga riflesso nella cartella di lavoro salvata
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtro a selezione singola (mostra un singolo elemento della pagina)**

Nella modalità predefinita di selezione singola, il campo filtro viene visualizzato come un singolo menu a discesa e l'intero `PivotField.CurrentPageItem` seleziona quale elemento della pagina guida il corpo della tabella pivot. L'assegnazione di un indice specifico seleziona quell'unico elemento; l'assegnazione del valore sentinella speciale `0x7FFD` (decimale 32765) cancella il filtro così che ogni elemento della pagina venga riepilogato contemporaneamente. La selezione singola è l'impostazione predefinita; non è necessario abilitarla esplicitamente.

### Mostra tutti gli elementi

Impostare `CurrentPageItem` sul valore magico `0x7FFD` equivale a cancellare il filtro pagina; il corpo della tabella pivot riepiloga ogni elemento della pagina come se non fosse applicato alcun filtro.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Popola i dati Frutto/Anno/Quantità
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Crea una tabella pivot in E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Configura i campi pivot: Frutto→Riga, Quantità→Dati, Anno→Pagina
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Cancella il filtro della pagina in modo che ogni elemento nel campo pagina sia visibile.
// 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi" —
// equivalente a selezionare "(Tutto)" nel menu a discesa del campo pagina di Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Mostra un elemento specifico

Impostare `CurrentPageItem` su un indice reale seleziona solo quell'elemento della pagina. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Aggiungi dati di esempio (Frutto/Anno/Importo)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// Aggiungi tabella pivot in E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Aggiungi campi: Frutto→Riga, Importo→Dati, Anno→Pagina
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Operazioni specifiche del campo pagina
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = secondo elemento nell'ordine ordinato (es. "2021")

// Aggiorna e calcola la tabella pivot
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtro a selezione multipla**

Il filtro a selezione multipla trasforma il menu a discesa della pagina in un elenco con caselle di controllo e consente all'utente finale di selezionare più elementi della pagina contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia di selezione multipla abbia effetto. Dopo che è abilitata, `PivotItem.IsHidden` controlla quali elementi appaiono nell'elenco con caselle di controllo, quindi è possibile mostrare ogni elemento oppure consentire solo elementi specifici.

Il codice seguente abilita la selezione multipla sullo stesso campo filtro Year costruito nello Scenario 1a, e poi mostra due schemi, la Parte A rivela ogni elemento della pagina lasciando `IsHidden` impostato su `false` per ogni voce, mentre la Parte B consente solo i valori di origine scelti e nasconde tutto il resto tramite un blocco `switch (pivotItems[i].getStringValue())`.

```javascript
const AsposeCells = require("aspose.cells");

// — La tabella pivot e il campo pagina sono costruiti esattamente come in
//   Scenario 1a (dati Frutto/Anno/Importo, pivot in E3, Frutto→Riga,
//   Importo→Dati, Anno→Pagina tramite AddFieldToArea).
//   Qui sotto applichiamo il filtro a selezione multipla sul campo pagina.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Dati di esempio: Frutto | Anno | Importo
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Abilita la selezione multipla sul campo pagina
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Parte B — seleziona solo elementi specifici tramite il valore di origine
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Nota:** Quando si utilizza il filtro a selezione multipla tramite `PivotItem.IsHidden`, **almeno un `PivotItem` deve rimanere visibile** (`IsHidden == false`). Se ogni elemento è nascosto, Excel si blocca all'apertura del file oppure visualizza una tabella pivot vuota. Verificare sempre che la lista di elementi consentiti per la selezione multipla includa almeno un elemento dei dati di origine.

## **Quale API e quale modalità devo usare?**

La tabella seguente riassume quando utilizzare ciascuna API e modalità, in modo da poter scegliere la giusta combinazione senza leggere ogni scenario nel dettaglio.

| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro tramite il nome della colonna di origine (caso più comune) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/d | Alto livello, una sola riga. Utilizzare questa opzione a meno che non sia necessario un riferimento a `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `pivotTable.getPageFields().add(PivotField)` | n/d | Da usare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare su un singolo elemento della pagina (modalità predefinita) | `PivotField.CurrentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostra tutti gli elementi / cancella il filtro pagina | `PivotField.CurrentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è la sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia di selezione multipla in Excel | `PivotField.IsMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata a `IsHidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.IsHidden` | impostare per ciascun elemento | Almeno un elemento deve rimanere visibile (`IsHidden == false`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtro a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si blocca all'apertura oppure visualizza una tabella pivot vuota. Costruire la lista di elementi consentiti basandosi sui dati di origine in modo che almeno un elemento rimanga visibile, e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}