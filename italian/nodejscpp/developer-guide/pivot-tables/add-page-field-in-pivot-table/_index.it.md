---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi filtro
description: Impara come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for Node.js via C++, inclusi l'aggiunta di campi filtro, il filtraggio a selezione singola e il filtraggio a selezione multipla.
keywords: Aspose.Cells, Node.js via C++, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/nodejs-cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. Puoi aggiungere un campo filtro tramite un'API di alto livello o tramite la collezione di livello inferiore `PageFields`, e puoi gestire il filtro pagina in modalità a selezione singola, azzerarlo per mostrare ogni elemento della pagina, oppure commutare il campo sulla selezione multipla in modo che gli utenti possano selezionare più elementi della pagina contemporaneamente tramite l'interfaccia a caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**

Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una pivot renderizzata in Excel, e selezionare uno degli elementi di pagina disponibili ricostruisce il corpo della pivot in modo che vengano riepilogati solo i record appartenenti a quell'elemento di pagina. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

Un campo filtro può operare in due modalità. Nella modalità predefinita **a selezione singola** è visibile un solo elemento di pagina alla volta, quindi il corpo della pivot riassume esattamente un sottoinsieme. Nella modalità **a selezione multipla** il campo espone un elenco di caselle di controllo, e il corpo della pivot riassume l'unione di ogni elemento di pagina selezionato. Lo stesso campo di origine può essere spostato avanti e indietro tra queste modalità attivando o disattivando una singola proprietà.

Aspose.Cells for Node.js via C++ espone due modi equivalenti per registrare un campo filtro. L'API di alto livello è `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, che prende il nome della colonna di origine e aggiunge il campo in una singola chiamata. L'API di livello inferiore è `PivotTable.pageFields.add(PivotField)`, che viene utilizzata quando si dispone già di un riferimento `PivotField` e si desidera aggiungere la stessa istanza di campo all'area filtro. Entrambe le API finiscono per popolare la stessa collezione `PageFields`, e il resto di questo articolo mostra come scegliere tra esse e come gestire ciascuna modalità di filtraggio.

## **Aggiungere un campo filtro**

Esistono due modi per registrare un campo pivot nell'area filtro. La chiamata di alto livello prende il nome della colonna di origine come stringa ed è il percorso più comune. La chiamata di livello inferiore accetta un'istanza `PivotField` esistente ed è comoda quando lo stesso oggetto campo deve essere riutilizzato su più aree pivot. Entrambe le chiamate inseriscono il campo in `PivotTable.pageFields`, dopodiché appare come menu a discesa della pagina nella parte superiore della pivot renderizzata.

### Aggiungere un campo filtro con addFieldToArea

L'esempio seguente crea un piccolo set di dati Frutta / Anno / Importo, posiziona una tabella pivot nella cella E3 con `Fruit` nell'area riga, `Amount` nell'area dati e `Year` nell'area filtro, aggiorna la pivot e salva la cartella di lavoro.

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

// Aggiungi campi alle rispettive aree: Frutto come Riga, Quantità come Dati, Anno come campo Pagina
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Aggiorna e calcola i dati della tabella pivot
pivotTable.refreshData();
pivotTable.calculateData();

// Salva la cartella di lavoro
workbook.save("pageFieldSample.xlsx");
```

### Aggiungere un campo filtro con pageFields.add

Quando si lavora già con un'istanza `PivotField`, è possibile passarla direttamente a `PivotTable.pageFields.add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area filtro viene sostituita con la chiamata API di livello inferiore.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Intestazioni
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Dati di esempio (9 righe)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Aggiungi tabella pivot a partire da E3 coprendo A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Riga, Amount -> Dati (Year verrà inserito nell'area Page qui sotto)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Approccio a basso livello: recupera il PivotField Year esistente dai BaseFields
// e registralo nell'area Page tramite PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Aggiorna la tabella pivot in modo che il nuovo campo di pagina venga riflesso nel workbook salvato
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtraggio a selezione singola (mostrare un elemento di pagina)**

Nella modalità predefinita a selezione singola, il campo filtro viene renderizzato come un singolo menu a discesa e l'intero `PivotField.currentPageItem` seleziona quale elemento di pagina guida il corpo della pivot. Assegnando un indice specifico si seleziona quell'unico elemento; assegnando il valore sentinella speciale `0x7FFD` (decimale 32765) si azzera il filtro in modo che ogni elemento di pagina venga riepilogato contemporaneamente. La selezione singola è la modalità predefinita; non è necessario abilitarla esplicitamente.

### Mostrare tutti gli elementi

Impostare `currentPageItem` sul valore magico `0x7FFD` equivale ad azzerare il filtro pagina: il corpo della pivot riassume ogni elemento di pagina come se non fosse applicato alcun filtro.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Popola i dati Frutto/Anno/Importo
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Crea una tabella pivot in E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Configura i campi pivot: Frutto→Riga, Importo→Dati, Anno→Pagina
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Cancella il filtro della pagina in modo che ogni elemento nel campo pagina sia visibile.
// 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi" —
// equivalente a selezionare "(Tutti)" nel menu a tendina del campo pagina di Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Mostrare un elemento specifico

Impostare `currentPageItem` su un indice reale seleziona solo quell'unico elemento di pagina. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Aggiungi dati di esempio (Frutto/Anno/Importo)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

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

## **Filtraggio a selezione multipla**

Il filtraggio a selezione multipla trasforma il menu a discesa della pagina in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi di pagina contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.isMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia a selezione multipla abbia effetto. Dopo averlo abilitato, `PivotItem.isHidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento o consentire solo elementi specifici.

Il codice seguente abilita la selezione multipla sullo stesso campo filtro Year costruito nello Scenario 1a, e quindi mostra due pattern: la Parte A rivela ogni elemento di pagina lasciando `isHidden` impostato su `false` per ogni voce, mentre la Parte B consente solo i valori di origine scelti e nasconde tutto il resto tramite un blocco `switch (pivotItems[i].getStringValue())`.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Dati di esempio: Frutta | Anno | Quantità
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Abilita la selezione multipla sul campo pagina
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Parte B — seleziona solo elementi specifici per valore di origine
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Nota:** Quando si utilizza il filtraggio a selezione multipla tramite `PivotItem.isHidden`, **almeno un `PivotItem` deve rimanere visibile** (`isHidden == false`). Se ogni elemento è nascosto, Excel si blocca all'apertura del file oppure renderizza una pivot vuota. Verifica sempre che la tua whitelist a selezione multipla includa almeno un elemento dei tuoi dati di origine.

## **Quale API e quale modalità devo usare?**

La tabella seguente riassume quando utilizzare ciascuna API e modalità, così puoi scegliere la combinazione giusta senza dover leggere ogni scenario nel dettaglio.

| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro tramite il nome della colonna di origine (caso più comune) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/d | Alto livello, una sola riga. Usalo a meno che tu non abbia bisogno di un riferimento `PivotField`. |
| Aggiungere un campo filtro quando si dispone già di un oggetto `PivotField` | `PivotTable.pageFields.add(PivotField)` | n/d | Usalo quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare su un singolo elemento di pagina (modalità predefinita) | `PivotField.currentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / azzerare il filtro pagina | `PivotField.currentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è la sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia a selezione multipla in Excel | `PivotField.isMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata a `isHidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.isHidden` | impostare per ogni elemento | Almeno un elemento deve rimanere visibile (`isHidden == false`). |

{{% alert color="primary" %}}
Ricorda sempre il vincolo di visibilità quando configuri il filtraggio a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si blocca all'apertura oppure renderizza una pivot vuota. Costruisci la tua whitelist sui tuoi dati di origine in modo che almeno un elemento rimanga visibile, e le tue cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}