---
title: Aggiungere la formattazione condizionale a una tabella pivot
linktitle: Aggiungere la formattazione condizionale a una tabella pivot
description: Aggiungere la formattazione condizionale a una tabella pivot in Aspose.Cells for Node.js via C++ - ancorare una regola alla regione dati con applyTo e un ambito PivotConditionFormatScopeType, oppure definire la destinazione con addCellArea e pivotAreas, quindi associare regole e stili tramite formatConditions.addCondition.
keywords: Aspose.Cells for Node.js via C++, tabella pivot, formattazione condizionale, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /it/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Gli stili descritti nella pagina padre e nella pagina sorella sono statici – un'area `PivotArea` o `CellArea` viene dipinta una volta e mantiene il suo stile indipendentemente dai valori. La formattazione condizionale è l'equivalente basato su regole – evidenzia ogni importo superiore a 200, ombreggia il cinquanta percento centrale o segnala gli elementi con classifica più bassa – e l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale delle tabelle pivot vive nella raccolta `pivotTable.getConditionalFormats()`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** La regione target è definita o tramite `applyTo(row, column, scope)`, che rispecchia il selettore di ambito dell'interfaccia utente di Excel, oppure tramite `addCellArea(cellArea)` e la raccolta `pivotConditionalFormat.getPivotAreas()`, che denominano esplicitamente la regione.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte a `formatConditions`, ottenute tramite `pivotConditionalFormat.getFormatConditions()`, con `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, e ogni condizione porta il proprio stile tramite `getStyle()`.

{{% alert color="primary" %}}
Non chiamare `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` o `formatConditions.addArea(cellArea)` sull'oggetto `formatConditions` di una formattazione condizionale pivot. Queste due sovraccariche provengono dall'API di formattazione condizionale del foglio di lavoro ordinario e non funzionano per le tabelle pivot: l'area di celle non viene mai convertita in un'area pivot, quindi la richiesta viene silenziosamente ignorata. Definisci sempre la regione sull'oggetto `pivotConditionalFormat` stesso (`applyTo`, `addCellArea` o `getPivotAreas()`) e aggiungi la regola con una delle sovraccariche `addCondition`.
{{% /alert %}}

## **Applicare una regola con ambito (come nella UI di Excel)**
Il primo metodo posiziona la regola come fa l'interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate del foglio di lavoro basate su zero, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a che punto la regola deve estendersi da quella cella:
- `PivotConditionFormatScopeType.DATA` – tutte le celle di valore generate dalla tabella pivot, inclusi i totali complessivi.
- `PivotConditionFormatScopeType.FIELD` – le celle di valore che appartengono al campo identificato dalla cella, escludendo i totali complessivi. La cella deve essere una cella di campo, ad esempio un'etichetta di campo di riga; fornire una cella di valore genera un'eccezione.
- `PivotConditionFormatScopeType.SELECTION` – solo le celle di valore all'intersezione selezionata dalla cella, tipicamente una singola cella di valore.
L'esempio seguente crea una tabella pivot di vendite di frutta con l'angolo in alto a sinistra in E3, ancorando una formattazione condizionale nella cella F4 (riga 3, colonna 5) con ambito `DATA`, e evidenzia ogni importo superiore a 200 in bianco in grassetto su rosso. Con i valori Apple 220, Banana 330, Cherry 200 e il totale complessivo 750, la regola colora F4, F5 e F7 – la regione risolta è l'intera colonna di dati F4:F7, e solo le celle il cui valore supera la regola si illuminano.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Tabella pivot con l'angolo in alto a sinistra in E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Ancora il formato condizionale in F4 (riga 3, colonna 5) con l'ambito Dati
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Regola - evidenzia gli importi superiori a 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Ancorando la stessa regola sull'etichetta del campo di riga E4 (riga 3, colonna 4) con l'ambito `FIELD` la risoluzione è F4:F6 – la stessa colonna di dati senza la riga del totale complessivo – perché l'ambito ora descrive il campo `Fruit` anziché l'intera area dei valori. L'ambito `SELECTION` ancorato a F4 si risolve solo su F4.

## **Definire la regione manualmente**
Il secondo metodo salta il selettore di ambito e denomina la regione esplicitamente sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con addCellArea**
`addCellArea(cellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono coordinate del foglio di lavoro basate su zero, e la regione è esattamente il rettangolo fornito – nessuna espansione verso la colonna dei dati e nessuna logica di totale complessivo. Usalo quando le celle di interesse sono un rettangolo fisso noto del layout pivot corrente.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Seleziona il rettangolo F4:F6 (le celle di valore senza il totale generale)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Regola - corsivo su giallo chiaro per importi compresi tra 150 e 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Una regione pivot semantica con getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` è lo stesso modello di regione semantica che la pagina sorella utilizza per gli stili statici. Crea un `PivotArea`, seleziona un campo o una regione con `select` o `selectField`, e aggiungila con `pivotAreas.addPivotArea(pivotArea)`. Una regione semantica rimane collegata al suo campo, quindi la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout cambia. La sovraccarica `pivotAreas.add(pivotArea)` compila ancora ma è contrassegnata come obsoleta – preferire `addPivotArea`.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Allega la regola al campo dati Amount come regione semantica
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regola - testo grigio per importi inferiori a 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dove vengono archiviate le regole e come sopravvivono a un ricaricamento**
Ogni chiamata a `conditionalFormats.add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i relativi stili vengono salvati con la cartella di lavoro – riaprendo il file nell'esempio seguente si vedono la stessa regola con il suo tipo, operatore e formula intatti, e `getCellAreas()` restituisce le stesse regioni. Le voci che non hanno mai ricevuto una condizione vengono eliminate quando la cartella di lavoro viene salvata, proprio come Excel scarta una formattazione condizionale priva di regola.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// Questo stampa:
// Formati condizionali: 1
// Formato 0: CellValue MaggioreDi formula1==200
//     righe 4-7, colonne 6-6        (F4:F7, l'area dati risolta)
```

## **Articoli correlati**
- [Applicare stile alla tabella pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)
- [Formattare parte della tabella pivot](/cells/it/nodejs-cpp/format-part-of-pivot-table/)
- [Top 10 visualizza o filtra nella tabella pivot](/cells/it/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrare tabelle pivot per etichetta o valore](/cells/it/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}