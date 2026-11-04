---
title: Formattare parte di una Tabella Pivot
description: Formattare parte di una tabella pivot in Aspose.Cells for Node.js via C++ applicando stili a regioni semantiche PivotArea o rettangoli CellArea tramite PivotTable.format, con i formati memorizzati in PivotTable.getPivotFormats() e conservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Node.js via C++, tabella pivot, formattazione, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /it/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
`PivotTable.formatAll` applica uno stile unico all'intera tabella pivot ed è trattato nella pagina principale. Non distingue tra etichette, valori, totali o regioni particolari del report.
In pratica, di solito solo una parte di una tabella pivot necessita di evidenziarsi. Gli obiettivi comuni includono le etichette appartenenti a un campo di riga, le celle di valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elemento.
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile cella. Un formato `PivotArea` rimane collegato a una regione, ad esempio le etichette di un campo o i valori dei dati, e viene rielaborato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione e non è tracciato dal modello pivot.
Aspose.Cells espone l'intera famiglia di overload `PivotTable.format` in modo che entrambi i tipi di formattazione siano disponibili:
- `format(PivotArea, Style)` collega uno stile a una regione semantica costruita con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` collega uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `format(number row, number column, Style)` mira a una singola cella.
- `formatAll(Style)` formatta l'intera tabella pivot.

## **Formattare un'area Pivot**
Il flusso di lavoro basato su area semantica è l'approccio consigliato quando un'evidenziazione deve seguire un campo o una regione del report.
1. Crea un `PivotArea` con `new PivotArea(pivotTable)`. L'oggetto descrive una regione semantica che appartiene a quella specifica tabella pivot.
2. Seleziona un campo in base alla sua posizione a indice zero su un determinato asse utilizzando `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LabelOnly` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DataOnly` seleziona solo le celle dati del campo.
3. Seleziona un campo per nome con `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve nelle celle di valore generate dagli elementi di quel campo.
4. Crea uno `Style` con `workbook.createStyle()`, configura il suo carattere, colore di primo piano e pattern di sfondo solido, e passa lo stile a `pivotTable.format(area, style)`.
5. Ogni chiamata alla sovraccarico `PivotArea` aggiunge una voce `PivotTableFormat` a `pivotTable.getPivotFormats()`.
6. I formati ancorati a un campo vengono applicati quando i dati della tabella pivot vengono calcolati. Pertanto, chiama `pivotTable.calculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.
Il seguente esempio crea una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.select` e `PivotTableSelectionType.LabelOnly`, formatta le celle di valore generate dallo stesso campo di riga con `PivotArea.selectField` e quindi ricalcola la tabella pivot affinché entrambi gli stili vengano applicati.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formattare un'area Cell della Tabella Pivot**
Usa `PivotTable.format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione pivot semantica.
Un `CellArea` è descritto dalle proprietà `startRow`, `startColumn`, `endRow` e `endColumn`. I valori sono coordinate a indice zero del foglio di lavoro e le coordinate finali identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area copre le celle dalla posizione iniziale fino alla posizione finale, inclusa.
Diversamente da un formato ancorato a un campo, un formato `CellArea` viene applicato alle celle immediatamente. Non è necessario un ulteriore richiamo a `pivotTable.calculateData()` perché lo stile compaia.
Un rettangolo `CellArea` può contenere contemporaneamente celle di etichetta e celle di valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.
Il seguente esempio formatta il rettangolo `E4:F5` della tabella pivot con uno stile italico di colore azzurro chiaro e salva la cartella di lavoro senza ulteriori ricalcoli.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Come le aree Pivot e le aree Cell si mappano**
Excel memorizza la formattazione della tabella pivot come record `pivotArea` anziché come normali record di stile cella del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot quando viene registrata.
La relazione tra il `CellArea` fornito dall'utente e le aree pivot archiviate internamente è molti-a-molti in entrambe le direzioni.
- Un `CellArea` può produrre diverse aree pivot. Se il rettangolo comprende sia celle di etichetta sia celle di valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta indipendentemente la formattazione delle etichette e dei dati.
- Un'area pivot può risolversi in diverse istanze `CellArea` disgiunte. Una regione semantica, come una riga di totale generale, oppure un campo i cui elementi non sono contigui, può coprire più rettangoli. È per questo che `PivotArea.getCellAreas()` restituisce una collezione anziché un unico rettangolo.
Ogni operazione di formattazione eseguita tramite `pivotTable.format()` è registrata in `pivotTable.getPivotFormats()`. Ogni voce `PivotTableFormat` espone il `PivotArea` associato e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre un `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.
Per distinguere le regioni memorizzate, ogni `PivotArea` espone le flag `getOnlyLabel()` e `getOnlyData()`. L'esempio qui sotto formatta un unico rettangolo che copre sia etichette sia valori, ispeziona `pivotTable.getPivotFormats()` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

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
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Poiché i formati sono memorizzati come aree pivot anziché come semplici stili cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot viene aggiornata con `pivotTable.refreshData()`, ricalcolata con `pivotTable.calculateData()`, o salvata e ricaricata, ogni area pivot memorizzata si rielabora nella posizione corrente della sua regione e il suo stile viene riapplicato.
{{% /alert %}}

Utilizza un `PivotArea` costruito con `select` o `selectField` quando un'evidenziazione deve rimanere collegata a un campo o a una regione semantica attraverso gli aggiornamenti, e usa un `CellArea` quando è sufficiente formattare un rettangolo fisso nel layout corrente della tabella pivot. L'overload a cella singola `format(number row, number column, Style)` mira a una cella individuale. Usa `formatAll`, descritto nella pagina principale, quando l'intera tabella pivot deve essere riformattata in un'unica operazione.

## **Articoli correlati**
- [Applicare lo stile alla tabella pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla tabella pivot](/cells/it/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore nella tabella pivot](/cells/it/nodejs-cpp/manage-value-fields/)
- [Aggiornare la tabella pivot](/cells/it/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}