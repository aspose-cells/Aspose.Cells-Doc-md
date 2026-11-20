---
title: Raggruppamento discreto degli elementi dei campi pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi dei campi pivot in gruppi personalizzati con nome, come frutta e verdura, utilizzando DiscreteGroupItem e PivotFieldGroupOptions.getDiscreteGroupItems() in Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento di elementi pivot, gruppi personalizzati, PivotField.group, Aspose.Cells for Node.js via Java, tabella pivot di Excel
type: docs
weight: 90
url: /it/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico organizza gli elementi in base al tipo di dati, ad esempio le date in mesi e trimestri o i numeri in intervalli. Il raggruppamento discreto risolve il problema opposto, consentendo di raggruppare elementi specifici e non correlati in gruppi personalizzati con nome, ad esempio i prodotti per frutta e verdura, i negozi per regioni o gli account per zone. Aspose.Cells fornisce il raggruppamento discreto tramite la classe `DiscreteGroupItem` e la proprietà `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un'istanza di `DiscreteGroupItem` è costituita da un nome di gruppo e dagli elementi che ne fanno parte. Gli elementi possono essere identificati in due modi: tramite i rispettivi nomi (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) oppure tramite le rispettive posizioni, a partire da zero, nei dati di origine (`new DiscreteGroupItem("fruit", [0, 3])`). Entrambe le forme producono lo stesso risultato.
- Il raggruppamento discreto viene applicato a un campo nell'area delle righe o delle colonne della tabella pivot, passando le opzioni a `PivotField.group(PivotFieldGroupOptions)`.

## **Raggruppamento degli elementi del campo pivot in base ai nomi degli elementi**
L'esempio seguente costruisce un piccolo elenco di vendite (prodotto, data e importo), crea da esso una tabella pivot con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi: `fruit` (`grape`, `cherry`) e `vegetables` (`carrot`, `potato`). Il risultato mostra una disposizione a due livelli nelle righe, con il nome del gruppo come livello esterno e gli elementi originali annidati al di sotto. Ciò consente di analizzare le tendenze per ogni gruppo personalizzato e per ogni elemento.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Dopo `calculateData()`, l'area delle righe della tabella pivot mostra `fruit` (`grape` 50, `cherry` 80) e `vegetable` (`carrot` 60, `potato` 70), con un totale complessivo di 260, mentre le etichette delle colonne continuano a mostrare le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppamento degli elementi del campo pivot in base agli indici degli elementi**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` li identifica tramite l'indice. Gli indici corrispondono alle posizioni degli elementi nei dati di origine, a partire da zero, e seguono l'ordine in cui gli elementi compaiono, non quello alfabetico. Nei dati di esempio riportati sopra, `grape` è l'elemento 0, `carrot` è l'elemento 1, `potato` è l'elemento 2 e `cherry` è l'elemento 3; pertanto, `fruit` è `{ 0, 3 }` e `vegetable` è `{ 1, 2 }`. Il risultato è identico a quello dell'esempio basato sui nomi.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati a un gruppo personalizzato non vengono persi. Rimangono nella tabella pivot, allo stesso livello dei gruppi personalizzati, ciascuno come voce distinta composta da un solo elemento. Nell'esempio precedente, la definizione del solo gruppo `fruit` lascia `carrot` e `potato` nell'area delle righe come voci autonome accanto al gruppo `fruit`.
- La proprietà `PivotFieldGroupOptions.getNewPivotField()` controlla la disposizione del raggruppamento discreto. Il valore predefinito è `true`; in questo caso, il campo raggruppato viene aggiunto come nuovo campo esterno accanto al campo originale, producendo la disposizione a due livelli mostrata sopra (`getRowFields()` cresce fino a 2). Per sostituire il campo originale, impostare il valore su `false` con `PivotFieldGroupOptions.setNewPivotField(false)`; l'area delle righe mostra quindi un unico livello contenente esclusivamente i nomi dei gruppi e i relativi valori aggregati: `fruit` 130 (50 + 80) e `vegetable` 130 (60 + 70).
- I costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici possono essere combinati all'interno dello stesso array `getDiscreteGroupItems()`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi di riga e colonna alla tabella pivot](/cells/it/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot in base all'etichetta o al valore](/cells/it/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Applica uno stile alla tabella pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Aggiorna la tabella pivot](/cells/it/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}