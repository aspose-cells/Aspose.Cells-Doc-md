---
title: Aggiungere la formattazione condizionale a una Tabella Pivot
linktitle: Aggiungere la formattazione condizionale a una Tabella Pivot
description: Aggiungi la formattazione condizionale a una tabella pivot in Aspose.Cells for Node.js via Java - ancorare una regola all'intervallo dati con applyTo e un ambito PivotConditionFormatScopeType, oppure definire il target con addCellArea e getPivotAreas, quindi collegare regole e stili tramite getFormatConditions().addCondition.
keywords: Aspose.Cells, tabella pivot, formattazione condizionale, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /it/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Gli stili descritti nella pagina principale e nella pagina sorella sono statici – un intervallo `PivotArea` o `CellArea` viene dipinto una volta e mantiene il suo stile indipendentemente dai valori. La formattazione condizionale è il corrispondente basato su regole – evidenziare ogni importo superiore a 200, colorare la metà centrale del cinquanta percento, o segnalare gli elementi con classifica più bassa – e l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells for Node.js via Java, la formattazione condizionale delle tabelle pivot risiede nella collezione `pivotTable.getConditionalFormats()`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** La regione target è definita o tramite `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, che riproduce il selettore di ambito dell'interfaccia utente di Excel, o tramite `addCellArea(CellArea)` e la collezione `getPivotAreas()`, che nominano esplicitamente la regione.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte a `getFormatConditions()` con `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, e ogni condizione porta il proprio `getStyle()`.

{{% alert color="primary" %}}
Non chiamare `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` o `FormatConditionCollection.addArea(CellArea)` sull'oggetto `getFormatConditions()` di una formattazione condizionale pivot. Queste due overload sono ereditate dall'API di formattazione condizionale del foglio di lavoro ordinario e non funzionano per le tabelle pivot – l'area **CellArea** non viene mai convertita in un'area pivot, quindi la richiesta viene ignorata silenziosamente. Definisci sempre l'area sul `PivotConditionalFormat` stesso (`applyTo`, `addCellArea` o `getPivotAreas()`) e aggiungi la regola con una delle overload `addCondition`.
{{% /alert %}}

## **Applicare una regola con un ambito (modo Excel UI)**
Il primo metodo posiziona la regola nello stesso modo in cui lo fa l'interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate a zero‑based del foglio di lavoro, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells quanto lontano la regola deve estendersi da quella cella:
- `PivotConditionFormatScopeType.DATA` – tutte le celle valore prodotte dalla tabella pivot, incluse le totali generali.
- `PivotConditionFormatScopeType.FIELD` – le celle valore che appartengono al campo identificato dalla cella, escludendo le totali generali. La cella deve essere una cella di campo, ad esempio un'etichetta di riga; fornire una cella valore genera un'eccezione.
- `PivotConditionFormatScopeType.SELECTION` – solo le celle valore all'intersezione selezionata dalla cella, tipicamente una singola cella valore.  
L'esempio seguente crea una tabella pivot vendite di frutta il cui angolo in alto a sinistra è in E3, ancora una formattazione condizionale **sulla** cella F4 (riga 3, colonna 5) con l'ambito `DATA`, e evidenzia ogni importo superiore a 200 in bianco grassetto su rosso. Con i valori Apple 220, Banana 330, Cherry 200 e il totale generale 750, la regola colora F4, F5 e F7 – la regione risolta è l'intera colonna dei dati F4:F7, e solo le celle il cui valore soddisfa la regola vengono evidenziate.

```javascript
const AsposeCells = require("aspose.cells");
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
// Tabella pivot con l'angolo in alto a sinistra su E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Ancorare il formato condizionale su F4 (riga 3, colonna 5) con l'ambito Dati
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Regola - evidenziare gli importi superiori a 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Ancora la stessa regola sull'etichetta del campo di riga E4 (riga 3, colonna 4) con l'ambito `FIELD` risolve a F4:F6 invece – la stessa colonna dei dati senza la riga del totale generale – perché l'ambito ora descrive il campo `Fruit` anziché l'intera area dei valori. L'ambito `SELECTION` ancorato a F4 risolve solo a F4.

## **Definire la regione manualmente**

### **Un rettangolo del foglio di lavoro con addCellArea**
`addCellArea(CellArea)` registra il rettangolo fornito come target della regola. Le coordinate sono zero‑based del foglio di lavoro, e la regione è esattamente il rettangolo fornito – nessuna espansione verso la colonna dei dati e nessuna logica di totale generale. Usalo quando le celle di interesse sono un rettangolo fisso conosciuto del layout pivot corrente.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Seleziona il rettangolo F4:F6 (le celle di valore senza il totale generale)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regola - corsivo su giallo chiaro per importi tra 150 e 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Una regione pivot semantica con PivotAreas**
`getPivotAreas()` è lo stesso modello di regione semantica utilizzato dalla pagina sorella per gli stili statici. Crea un `PivotArea`, seleziona un campo o una regione con `select` o `selectField`, e aggiungilo con `getPivotAreas().addPivotArea(PivotArea)`. Una regione semantica rimane collegata al suo campo, quindi la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout cambia. L'overload `getPivotAreas().add(PivotArea)` compila ancora ma è contrassegnato come obsoleto – preferisci `addPivotArea`.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Allega la regola al campo dati Amount come una regione semantica
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regola - testo grigio per importi inferiori a 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dove sono archiviate le regole e come sopravvivono a un ricaricamento**
Ogni chiamata `add()` su `getConditionalFormats()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprire il file nell'esempio seguente mostra la stessa regola con il relativo tipo, operatori e formule intatto, e `getCellAreas()` segnala le stesse regioni. Le voci che non hanno mai ricevuto una condizione vengono scartate al salvataggio della cartella di lavoro, nello stesso modo in cui Excel elimina una formattazione condizionale senza regola.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// Questo stampa:
// Formati condizionali: 1
// Formato 0: CellValue GreaterThan formula1==200
//     righe 4-7, colonne 6-6        (F4:F7, l'area dati risolta)
```

## **Articoli correlati**
- [Applicare stile a Tabella Pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Formattare parte di una Tabella Pivot](/cells/it/nodejs-java/format-part-of-pivot-table/)
- [Top 10 mostra o filtra nella Tabella Pivot](/cells/it/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrare tabelle pivot per etichetta o valore](/cells/it/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}