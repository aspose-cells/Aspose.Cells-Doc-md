---
title: Aggiungere campi di riga e colonna a una tabella pivot in Aspose.Cells for Node.js via C++
linktitle: Aggiungere campi di riga e colonna a una tabella pivot
description: Scopri come aggiungere campi di base alle aree delle righe e delle colonne di una tabella pivot e controllare i subtotali dei campi pivot utilizzando PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, tabella pivot, campo di riga, campo di colonna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aggiunta di un campo all'area delle righe o delle colonne**
Il metodo `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` sposta un campo di base dai dati di origine in una delle quattro aree della tabella pivot. L'argomento `fieldType` accetta uno dei seguenti valori `PivotFieldType`.
- `Row` — campi disposti verticalmente a sinistra
- `Column` — campi disposti orizzontalmente nella parte superiore
- `Data` — campi i cui valori vengono aggregati
- `Page` — campi utilizzati come filtri del rapporto
L'ordine di annidamento dei campi è importante. Se si aggiunge prima `Category` all'area delle righe e poi `Item`, si ottiene una tabella pivot il cui raggruppamento esterno è `Category` e quello interno è `Item`. L'ordine inverso inverte la gerarchia.

## **Sottototali dei campi della tabella pivot**
Il metodo `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controlla quali righe di subtotale vengono visualizzate per un campo della tabella pivot. Ogni chiamata attiva o disattiva indipendentemente un singolo tipo di subtotale. Il valore `shown = true` visualizza il subtotale, mentre `shown = false` lo nasconde. Poiché ogni chiamata interessa un solo tipo, la chiamata del metodo più volte con diversi valori `subtotalType` consente di definire un sottoinsieme personalizzato di subtotali.
L'enumerazione `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.
- `Automatic` — Aspose.Cells sceglie l'opzione predefinita (in genere `Sum` per i campi numerici)
- `None` — sopprime tutte le righe di subtotale
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
I subtotali vengono visualizzati solo quando nell'area delle righe (o delle colonne) sono presenti due o più campi della tabella pivot. Un singolo campo non fornisce elementi significativi rispetto ai quali calcolare un subtotale; pertanto, in questo caso, le chiamate a `setSubtotals` non producono effetti visibili. Questo articolo inserisce quindi, in ogni esempio, due campi di riga (`Category` come campo esterno e `Item` come campo interno), in modo da rendere visibile il confine dei subtotali tra ciascun gruppo `Category`.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**
Quando `setSubtotals` non viene chiamato, Aspose.Cells applica l'opzione `Automatic` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `setSubtotals(PivotFieldSubtotalType.Automatic, true)` sul campo di riga esterno `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Soppressione di tutti i subtotali (None)**
La chiamata `setSubtotals(PivotFieldSubtotalType.None, true)` rimuove tutte le righe di subtotale dalla tabella pivot, lasciando soltanto le righe dei campi e il totale generale in basso. Questa impostazione è utile quando si desidera visualizzare i dati raggruppati in forma grezza, senza righe di riepilogo.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scenario 3 — Sottototali personalizzati (Sum + Average)**
Non è necessario limitarsi a un singolo tipo di subtotale. Ogni chiamata a `setSubtotals` opera indipendentemente su un tipo; pertanto, chiamando il metodo due volte, una con `Sum` e una con `Average`, si ottiene un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Riepilogo**

I tre scenari differiscono in un unico aspetto: le chiamate a `setSubtotals`. Tutto il resto — il set di dati, i campi e le aree a cui vengono assegnati — è identico, il che rende i layout direttamente confrontabili.
- **Posizionamento dei campi.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` sposta una colonna di origine in una regione. All'interno di una stessa regione, l’ordine delle chiamate determina l’ordine di visualizzazione, pertanto la prima chiamata corrisponde al gruppo esterno più esteso. Per calcolare le subtotali servono due o più campi nella stessa regione: con un unico campo non esiste alcun elemento tra i gruppi su cui calcolare le subtotali.
- **Scenario 1 — subtotali automatiche.** Non chiamare `setSubtotals` lascia la scelta a Excel, che applica la propria subtotals predefinita ai campi numerici. Chiamare `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.Automatic` registra esplicitamente tale scelta, invece di lasciarla implicita.
- **Scenario 2 — nessuna subtotale.** `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.None` disattiva la subtotale predefinita, per cui il pivot mantiene le righe del campo e la totale generale, ma omette le righe di subtotale che Excel altrimenti inserirebbe tra di esse.
- **Scenario 3 — un sottoinsieme selezionato.** Ogni chiamata abilita o disabilita esattamente un tipo di subtotale, e le chiamate si accumulano piuttosto che sovrascidersi reciprocamente. Di conseguenza, chiamarlo una volta con `AsposeCells.PivotFieldSubtotalType.Sum` e una volta con `AsposeCells.PivotFieldSubtotalType.Average` lascia entrambi abilitati, e il pivot genera una subtotale Sum, una subtotale Average e la totale generale.

{{% alert color="primary" %}}
Nulla riguardo le subtotali è specifico per la regione riga. Le stesse chiamate a `setSubtotals` su un campo estratto da `PivotTable.ColumnFields` producono gli stessi tre layout sull’asse delle colonne, poiché l’impostazione appartiene al campo pivot e non all’asse su cui è posizionato.
{{% /alert %}}
## **Articoli correlati**
- [Campi di pagina nelle tabelle pivot](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/refresh-pivot-table/)
- [Applicazione degli stili alle tabelle pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}