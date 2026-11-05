---
title: Aggiungere la Formattazione Condizionale a una Tabella Pivot
linktitle: Aggiungere la Formattazione Condizionale a una Tabella Pivot
description: Aggiungere la formattazione condizionale a una tabella pivot in Aspose.Cells for JavaScript via C++ - ancorare una regola all'area dati con applyTo e un ambito PivotConditionFormatScopeType, oppure definire la destinazione con addCellArea e pivotAreas, quindi collegare regole e stili tramite formatConditions.addCondition.
keywords: Aspose.Cells for JavaScript via C++, tabella pivot, formattazione condizionale, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /it/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Gli stili descritti nella pagina principale e nella pagina sorella sono statici: un'area `PivotArea` o `CellArea` viene dipinta una sola volta e mantiene il proprio stile indipendentemente dai valori. La formattazione condizionale è la controparte basata su regole: evidenziare ogni importo superiore a 200, colorare la fascia centrale del cinquanta per cento o segnalare gli elementi con ranking più basso – e l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale di una tabella pivot vive nella raccolta `pivotTable.conditionalFormats`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** L'area di destinazione è definita oppure tramite `applyTo(row, column, scope)`, che replica il selettore di ambito dell’interfaccia utente di Excel, oppure tramite `addCellArea(cellArea)` e la raccolta `pivotAreas`, che nominano esplicitamente l’area.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte a `formatConditions` con `addCondition(type, operatorType, formula1, formula2)`, e ogni condizione possiede il proprio `style`.

{{% alert color="primary" %}}
Non chiamare `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` o `formatConditions.addArea(cellArea)` sull’oggetto `formatConditions` di un formato condizionale pivot. Queste due overload provengono dall’API di formattazione condizionale dei fogli di lavoro ordinari e non funzionano per le tabelle pivot: l’area della cella non viene mai convertita in un’area pivot, quindi la richiesta viene ignorata silenziosamente. Definisci sempre l’area sullo stesso `PivotConditionalFormat` (`applyTo`, `addCellArea` o `pivotAreas`) e aggiungi la regola con una delle overload di `addCondition`.
{{% /alert %}}

## **Applicare una regola con uno scope (modalità UI di Excel)**
Il primo metodo posiziona la regola nello stesso modo in cui lo fa l’interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate zero‑based del foglio di lavoro, e un scope `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a dove deve estendersi la regola partendo da quella cella:
- `PivotConditionFormatScopeType.Data` – tutte le celle valore prodotte dalla tabella pivot, inclusi i totali generali.
- `PivotConditionFormatScopeType.Field` – le celle valore appartenenti al campo identificato dalla cella, esclusi i totali generali. La cella deve essere una cella campo, ad esempio un’etichetta di riga; passare una cella valore genera un’eccezione.
- `PivotConditionFormatScopeType.Selection` – solo le celle valore all’intersezione selezionata dalla cella, tipicamente una singola cella valore.  
L’esempio sottostante crea una tabella pivot di vendite di frutta con l’angolo in alto a sinistra in E3, ancora un formato condizionale nella cella F4 (riga 3, colonna 5) con lo scope `Data`, e evidenzia ogni importo superiore a 200 in grassetto bianco su rosso. Con i valori Apple 220, Banana 330, Cherry 200 e il totale generale 750, la regola colora F4, F5 e F7 – l’area risolta è l’intera colonna dati F4:F7, e solo le celle il cui valore supera la regola si illuminano.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Ancorare il formato condizionale in F4 (riga 3, colonna 5) con l'ambito Data
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Regola - evidenzia importi maggiori di 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) restituisce il file come byte
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Ancorare la stessa regola all’etichetta del campo di riga E4 (riga 3, colonna 4) con lo scope `Field` risolve a F4:F6 invece – la stessa colonna dati senza la riga del totale generale – perché lo scope ora descrive il campo `Fruit` anziché l’intera area valori. Lo scope `Selection` ancorato a F4 risolve solo a F4.

## **Definire la regione manualmente**
Il secondo metodo omette il selettore di ambito e nomina esplicitamente l’area sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con addCellArea**
`addCellArea(cellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono zero‑based del foglio di lavoro, e l’area è esattamente il rettangolo indicato – senza espansione alla colonna dati e senza logica di totale generale. Usalo quando le celle di interesse costituiscono un rettangolo fisso noto del layout pivot corrente.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Individua il rettangolo F4:F6 (le celle di valore senza il totale complessivo)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Regola - corsivo su giallo chiaro per importi tra 150 e 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **Una regione pivot semantica con pivotAreas**
`pivotAreas` utilizza lo stesso modello di regione semantica impiegato dalla pagina sorella per gli stili statici. Crea un `PivotArea`, seleziona un campo o un’area con `select` o `selectField`, e aggiungilo con `pivotAreas.addPivotArea(pivotArea)`. Una regione semantica rimane collegata al proprio campo, così il formato condizionale segue il campo quando la tabella pivot viene aggiornata e il layout si sposta. L’overload `pivotAreas.add(pivotArea)` è ancora supportato ma marcato obsoleto – è preferibile `addPivotArea`.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Attacca la regola al campo dati Amount come area semantica
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Regola - testo grigio per importi inferiori a 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Dove le regole sono memorizzate e come sopravvivono a un ricaricamento**
Ogni chiamata a `conditionalFormats.add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprire il file salvato dal primo esempio in Node mostra la stessa regola con tipo, operatore e formula intatti, e `getCellAreas()` restituisce la stessa area. Su questa piattaforma le proprietà `type` e `operator` di una condizione vengono restituite come valori numerici dell’enum. Le voci che non hanno mai ricevuto una condizione vengono eliminate quando la cartella di lavoro viene salvata, nello stesso modo in cui Excel scarta una formattazione condizionale priva di regola.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Ricarica il file scritto dal primo esempio
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // Questo stampa:
    // Formati condizionali: 1
    // Formato 0: 1 2 formula1==200   (tipo 1 = CellValue, operatore 2 = MaggioreDi)
    //     righe 4-7, colonne 6-6        (F4:F7, l'area dati risolta)
    process.exit(0);
});
```

## **Articoli correlati**
- [Applicare lo stile a una Tabella Pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)
- [Formattare una parte di una Tabella Pivot](/cells/it/javascript-cpp/format-part-of-pivot-table/)
- [Top 10 visualizza o filtra nella Tabella Pivot](/cells/it/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrare le Tabelle Pivot per etichetta o valore](/cells/it/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}