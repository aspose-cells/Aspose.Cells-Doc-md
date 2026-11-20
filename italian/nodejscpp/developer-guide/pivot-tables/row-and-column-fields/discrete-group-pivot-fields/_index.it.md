---
title: Raggruppamento discreto degli elementi del campo pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi del campo pivot in gruppi personalizzati con nome, come frutta e verdura, usando DiscreteGroupItem e PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppare elementi pivot, gruppi personalizzati, PivotField.Group, Node.js, tabella pivot di Excel
type: docs
weight: 90
url: /it/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scenari di utilizzo possibili**
- Il raggruppamento automatico raccoglie gli elementi per tipo di dato, ad esempio le date in mesi e trimestri o i numeri in intervalli. Il raggruppamento discreto risolve il problema opposto, raccogliendo elementi specifici e non correlati in gruppi personalizzati con nome, ad esempio prodotti in frutta e verdura, negozi in regioni o conti in zone. Aspose.Cells for Node.js via C++ fornisce il raggruppamento discreto tramite la classe `DiscreteGroupItem` e la proprietà `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` è un nome di gruppo più gli elementi che vi appartengono. Gli elementi possono essere identificati in due modi, per nome (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) o per le loro posizioni basate su indice zero nei dati di origine (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Entrambe le forme producono lo stesso risultato.
- Il raggruppamento discreto viene applicato a un campo nell'area righe o colonne della tabella pivot passando le opzioni a `pivotField.group(pivotFieldGroupOptions)`.

## **Raggruppa gli elementi del campo pivot per nome dell'elemento**
L'esempio seguente crea un piccolo elenco di vendite (prodotto, data e importo), genera una tabella pivot con `product` nell'area righe, `date` nell'area colonne e `amount` nell'area dati, quindi definisce due gruppi personalizzati per nome dell'elemento, frutta (grape, cherry) e verdura (carrot, potato). Il risultato mostra un layout a due livelli nelle righe, con il nome del gruppo come livello esterno e gli elementi originali nidificati al di sotto, in modo che le tendenze possano essere lette per ciascun gruppo personalizzato e per ogni elemento.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Dopo `calculateData()` l'area righe della tabella pivot mostra frutta (grape 50, cherry 80) e verdura (carrot 60, potato 70) con il totale generale 260, e le etichette delle colonne mantengono le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppa gli elementi del campo pivot per indice dell'elemento**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` identifica gli elementi per indice. Gli indici sono posizioni basate su indice zero degli elementi nell'ordine in cui compaiono nei dati di origine, non in ordine alfabetico. Nell'esempio di dati sopra, grape è l'elemento 0, carrot è l'elemento 1, potato è l'elemento 2 e cherry è l'elemento 3, quindi frutta è `{ 0, 3 }` e verdura è `{ 1, 2 }`. Il risultato è identico all'esempio basato sul nome.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi che non sono assegnati a nessun gruppo personalizzato non vengono persi. Rimangono nella tabella pivot allo stesso livello dei gruppi personalizzati, ciascuno come voce singola. Nell'esempio sopra, definendo solo il gruppo frutta, carota e patata rimangono nell'area righe come voci autonome accanto al gruppo frutta.
- La proprietà `PivotFieldGroupOptions.newPivotField` controlla il layout del raggruppamento discreto. Il valore predefinito è true, il che aggiunge il campo raggruppato come nuovo campo esterno accanto a quello originale, producendo il layout a due livelli mostrato sopra (`rowFields` cresce a 2). Impostandola a false il campo originale viene sostituito, e l'area righe mostra un unico livello contenente solo i nomi dei gruppi con i loro valori aggregati, frutta 130 (50 + 80) e verdura 130 (60 + 70).
- I costruttori basati sul nome e sull'indice di `DiscreteGroupItem` possono essere mescolati nello stesso array `PivotFieldGroupOptions.discreteGroupItems`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/it/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi riga e colonna nella tabella pivot](/it/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtraggio delle tabelle pivot per etichetta o valore](/it/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Applica stile alla tabella pivot](/it/nodejs-cpp/apply-style-to-pivot-table/)
- [Aggiorna tabella pivot](/it/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}