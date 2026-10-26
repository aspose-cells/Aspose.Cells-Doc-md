---
title: Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi riga e colonna a una tabella pivot
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, tabella pivot, campo riga, campo colonna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
Il metodo `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` sposta un campo di base dai dati di origine in una delle quattro aree della pivot. L'argomento `fieldType` accetta uno dei seguenti valori di `PivotFieldType`.
- `ROW` — campi disposti verticalmente a sinistra
- `COLUMN` — campi disposti orizzontalmente in alto
- `DATA` — campi i cui valori vengono aggregati
- `PAGE` — campi utilizzati come filtri del report
L'ordine di nidificazione dei campi è importante. Aggiungendo `Category` all'area riga per primo e poi `Item` si ottiene una pivot il cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertendo l'ordine si inverte la gerarchia.

## **Pivot Field Subtotals**
Il metodo `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva o disattiva un singolo tipo di subtotale in modo indipendente. Passando `shown = true` si visualizza il subtotale, mentre `shown = false` lo nasconde. Poiché ogni chiamata riguarda un solo tipo, invocare il metodo più volte con valori diversi di `subtotalType` consente di costruire un sottoinsieme personalizzato di subtotali.
L'enum `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.
- `AUTOMATIC` — Aspose.Cells sceglie la selezione predefinita (in genere `SUM` per i campi numerici)
- `NONE` — elimina ogni riga di subtotale
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando sono presenti due o più campi pivot nell'area riga (o nell'area colonna). Un singolo campo non ha nulla di significativo da subtotalizzare tra un gruppo e l'altro, quindi in quel caso le chiamate a `setSubtotals` non hanno alcun effetto visibile. Questo articolo pertanto inserisce due campi riga (`Category` esterno, `Item` interno) in ogni esempio, così che il confine di subtotale tra ciascun gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
Quando non si invoca affatto `setSubtotals`, Aspose.Cells applica la selezione `AUTOMATIC` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sul campo riga esterno `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Suppressing All Subtotals (None)**
Chiamando `setSubtotals(PivotFieldSubtotalType.NONE, true)` si rimuovono tutte le righe di subtotale dalla pivot, lasciando solo le righe dei campi e il totale generale in fondo. Questo è utile quando si desiderano i dati raggruppati grezzi senza alcuna riga di riepilogo.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `setSubtotals` agisce in modo indipendente su un solo tipo, quindi invocare il metodo due volte — una volta con `SUM` e una volta con `AVERAGE` — produce un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Recap**
I tre scenari differiscono in un unico aspetto: le chiamate a `setSubtotals`. Il resto — il set di dati, i campi e le aree a cui vengono assegnati — è identico, ed è proprio questo a rendere i layout direttamente confrontabili.
- **Posizionamento dei campi.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` sposta una colonna di origine in una regione. All'interno di una stessa regione, l’ordine delle chiamate corrisponde all’ordine di visualizzazione, perciò la prima chiamata diventa il gruppo più esterno. Le subtotal richiedono due o più campi nella stessa regione: con un singolo campo non esiste nulla tra i gruppi su cui calcolare la subtotals.
- **Scenario 1 — subtotal automatiche.** L’omissione di `setSubtotals` lascia la scelta a Excel, che applica la sua subtotals predefinita ai campi numerici. La chiamata a `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.AUTOMATIC` registra esplicitamente tale scelta invece di lasciarla implicita.
- **Scenario 2 — nessuna subtotals.** `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.NONE` disattiva la subtotals predefinita, per cui il pivot mantiene le righe dei campi e la grand total, ma elimina le righe di subtotals che Excel avrebbe altrimenti inserito tra di esse.
- **Scenario 3 — un sottoinsieme scelto.** Ogni chiamata abilita o disabilita esattamente un tipo di subtotals, e le chiamate si accumulano piuttosto che sovrascindersi reciprocamente. Chiamarlo una volta con `AsposeCells.PivotFieldSubtotalType.SUM` e una volta con `AsposeCells.PivotFieldSubtotalType.AVERAGE` lascia quindi entrambi abilitati, e il pivot genera una subtotals di tipo Somma, una subtotals di tipo Media e una grand total.

{{% alert color="primary" %}}
Nulla riguardo alle subtotals è specifico della regione di riga. Le stesse chiamate a `setSubtotals` su un campo preso da `PivotTable.ColumnFields` producono gli stessi tre layout sull’asse delle colonne, perché l’impostazione appartiene al campo pivot e non all’asse su cui è posizionato.
{{% /alert %}}

## **Related Articles**
- [Campi pagina nelle tabelle pivot](/cells/it/nodejs-java/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells per Node.js via Java](/cells/it/nodejs-java/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}