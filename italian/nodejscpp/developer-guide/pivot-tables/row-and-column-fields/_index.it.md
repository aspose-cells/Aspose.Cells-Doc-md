---
title: Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET
linktitle: Campi riga e colonna
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /it/nodejs-cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


I campi riga e i campi colonna sono gli elementi fondamentali di una tabella pivot. Un campo posizionato nell'area riga appare verticalmente sulla sinistra della tabella pivot, mentre un campo posizionato nell'area colonna appare orizzontalmente nella parte superiore. Questo articolo mostra come aggiungere campi di base a queste aree a livello di codice e come controllare i subtotali che vengono visualizzati tra i gruppi di campi utilizzando il metodo `PivotField.SetSubtotals`.

## **Aggiungere un campo all'area riga o colonna**

Il metodo `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` sposta un campo di base dai dati di origine in una delle quattro aree della tabella pivot. L'argomento `fieldType` accetta uno dei seguenti valori di `PivotFieldType`.

- `Row` — campi posizionati verticalmente sulla sinistra
- `Column` — campi posizionati orizzontalmente nella parte superiore
- `Data` — campi i cui valori vengono aggregati
- `Page` — campi utilizzati come filtri del report

Dopo aver aggiunto i campi, è possibile accedervi tramite le proprietà `PivotTable.RowFields` e `PivotTable.ColumnFields`. Ogni proprietà restituisce un `PivotFieldCollection`. Il campo all'indice 0 di `RowFields` è il campo riga più esterno, e gli indici successivi rappresentano i campi annidati al suo interno. La stessa convenzione di indicizzazione si applica a `ColumnFields`.

L'ordine di annidamento dei campi è importante. Aggiungere `Category` all'area riga per primo e poi `Item` produce una tabella pivot il cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertendo l'ordine si inverte la gerarchia.

## **Subtotali dei campi pivot**

Il metodo `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva/disattiva un singolo tipo di subtotale in modo indipendente. Passando `shown = true` si visualizza il subtotale, mentre `shown = false` lo nasconde. Poiché ogni chiamata influisce su un solo tipo, chiamare il metodo più volte con valori di `subtotalType` diversi consente di creare un sottoinsieme personalizzato di subtotali.

L'enumerazione `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.

- `Automatic` — Aspose.Cells sceglie la selezione predefinita (tipicamente `Sum` per i campi numerici)
- `None` — elimina ogni riga di subtotale
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando sono presenti due o più campi pivot nell'area riga (o nell'area colonna). Un singolo campo non ha nulla di significativo da subtotalizzare tra un gruppo e l'altro, quindi le chiamate a `SetSubtotals` non hanno alcun effetto visibile in tal caso. Questo articolo, pertanto, inserisce due campi riga (`Category` esterno, `Item` interno) in ogni esempio, in modo che il confine di subtotale tra ciascun gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**

Quando non si chiama affatto `SetSubtotals`, Aspose.Cells applica la selezione `Automatic` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sul campo riga esterno `Category`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Eliminazione di tutti i subtotali (None)**

Chiamare `SetSubtotals(PivotFieldSubtotalType.None, true)` rimuove ogni riga di subtotale dalla tabella pivot, lasciando solo le righe dei campi e il totale generale in fondo. Ciò è utile quando si desidera raggruppare i dati grezzi senza alcuna riga di riepilogo.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];

for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Scenario 3 — Sottoinsieme di subtotali personalizzato (Sum + Average)**

Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `SetSubtotals` agisce in modo indipendente su un singolo tipo, quindi chiamare il metodo due volte — una con `Sum` e una con `Average` — produce un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
## **Riepilogo**

I tre scenari precedenti condividono lo stesso set di dati e la stessa struttura di tabella pivot. L'unica differenza tra essi è la chiamata a `SetSubtotals` applicata al campo riga esterno `Category`. Ricordare la regola dei due campi: un singolo campo in un'area non ha nulla da subtotalizzare tra un gruppo e l'altro, quindi è sempre necessario inserire almeno due campi nell'area riga o colonna quando si desidera che `SetSubtotals` abbia un effetto visibile.

## **Articoli correlati**

- [Campi pagina nelle tabelle pivot](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
