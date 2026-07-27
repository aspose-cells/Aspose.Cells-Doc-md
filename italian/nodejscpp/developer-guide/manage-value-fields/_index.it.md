---
title: Campi valore in Aspose.Cells for Node.js via C++
linktitle: Campi valore
description: Scopri come aggiungere campi base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e posizionare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js, C++, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /it/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

I campi valore sono il cuore di ogni tabella pivot, gli aggregati numerici che riepilogano i dati di origine. In Aspose.Cells for Node.js via C++, l'area dati di una tabella pivot viene popolata aggiungendovi campi base tramite `PivotTable.addFieldToArea`, e ogni campo posizionato in quell'area può avere la propria funzione di riepilogo. Quando esistono due o più campi dati, Aspose.Cells espone un campo aggregato speciale, `PivotTable.ValuesField`, che può essere posizionato sull'asse Riga o Colonna come campo base, offrendoti un controllo più preciso su come i campi valore vengono visualizzati nel layout.

## Aggiungere un campo all'area dati

Aggiungere un campo base all'area dati (valore) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.addFieldToArea(PivotFieldType, string)`, un overload che accetta la costante `PivotFieldType.Data` e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone tramite la raccolta `PivotTable.DataFields`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene riepilogata con `ConsolidationFunction.Sum`, mentre una colonna non numerica viene impostata di default su `Count`.

## Modifica della funzione di riepilogo

Ogni campo posizionato nell'area dati viene internamente incapsulato come istanza di `PivotField` e la sua proprietà `Function` restituisce un valore dall'enum `ConsolidationFunction`. Lo stesso setter `Function` consente di passare tra gli aggregati disponibili, tra cui `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`.

{{% alert color="primary" %}}
Modificare `Function` influisce solo sull'aggregato, la colonna di origine non cambia.
{{% /alert %}}

Puoi quindi lasciare un campo dati come `Sum` mentre aggiungi un secondo campo dati che fa riferimento alla stessa colonna di origine ma utilizza `Count` o `Average`, tutto in un'unica tabella pivot.

## Posizionare i campi valore sull'asse Riga o Colonna

Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un campo virtuale aggiuntivo denominato `PivotTable.ValuesField`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. Puoi trascinarlo nell'area Riga o Colonna come campo pivot base, utile per disporre più misure fianco a fianco.

{{% alert color="primary" %}}
`PivotTable.ValuesField` non funziona se non c'è alcun campo valore o se ne esiste solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna capacità descritta sopra sulla stessa struttura pivot.

## Scenario 1 — Trascinare un campo base nell'area valore

Questo scenario mostra come inserire un singolo campo base (`Amount`) nell'area dati di una tabella pivot esistente. La struttura pivot condivisa posiziona `Category` e `Item` sull'asse Riga e `Year` sull'asse Colonna. Dopo l'operazione, `Amount` appare nell'area dati e viene calcolato come `Sum` di `Amount` per impostazione predefinita.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Intestazioni in A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Righe di dati A2:D9 utilizzando cicli annidati con diramazione su j
for (let i = 1; i <= 8; i++) {
  for (let j = 0; j < 4; j++) {
    switch (j) {
      case 0:
        worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
        break;
      case 1:
        if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
        else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
        else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
        else worksheet.getCells().get(i, j).putValue("Daikon");
        break;
      case 2:
        worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
        break;
      case 3:
        if (i == 1) worksheet.getCells().get(i, j).putValue(100);
        else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
        else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
        else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
        else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
        else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
        else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
        else worksheet.getCells().get(i, j).putValue(45);
        break;
    }
  }
}

// Aggiungi tabella pivot in F3 con nome PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Layout pivot: Categoria e Articolo su Riga, Anno su Colonna, Importo come campo dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Scenario 2 — Modifica della funzione di riepilogo

Questo scenario parte dalla stessa struttura pivot dello Scenario 1 ma aggiunge il campo `Amount` all'area dati due volte. Entrambi i campi dati fanno riferimento alla stessa colonna di origine, tuttavia il secondo campo viene sovrascritto utilizzando il setter `PivotField.Function` in modo che diventi `Count` invece del valore predefinito `Sum`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
    for (let j = 0; j <= 3; j++)
    {
        if (j == 0)
        {
            worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
        }
        else if (j == 1)
        {
            let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
            worksheet.getCells().get(i, j).putValue(items[i - 1]);
        }
        else if (j == 2)
        {
            let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
            worksheet.getCells().get(i, j).putValue(years[i - 1]);
        }
        else
        {
            let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
            worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
        }
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## Scenario 3 — Posizionare i campi valore sull'asse Riga o Colonna

Con due campi dati in posizione, `PivotTable.ValuesField` diventa utilizzabile. Questo scenario trascina quel campo virtuale aggregato nell'area Colonna in modo che ogni misura nell'area dati appaia come un proprio blocco di colonne accanto a `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Insieme, questi tre scenari coprono ogni aspetto della manipolazione dei campi valore in Aspose.Cells for Node.js via C++, da un singolo campo dati con il valore predefinito `Sum` fino a una tabella pivot multi-misura in cui il campo virtuale `ValuesField` controlla il layout sull'asse Riga o Colonna.

## Articoli correlati

- [Campi Riga e Colonna della tabella pivot in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/row-and-column-fields/)
- [Campi pagina nelle tabelle pivot](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}