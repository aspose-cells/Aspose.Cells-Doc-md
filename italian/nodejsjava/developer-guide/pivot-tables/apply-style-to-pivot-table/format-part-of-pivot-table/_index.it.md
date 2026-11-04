---
title: Formattare una parte di una tabella pivot
description: Formatta una parte di una tabella pivot in Aspose.Cells for Node.js via Java applicando stili a regioni semantiche PivotArea o a rettangoli CellArea tramite PivotTable.format, con i formati memorizzati in PivotTable.getPivotFormats() e preservati quando la tabella pivot viene aggiornata
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Node.js via Java, tabella pivot, formato, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /it/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
`PivotTable.formatAll` applica un unico stile all'intera tabella pivot ed è descritto nella pagina principale. Non distingue tra etichette, valori, totali o regioni specifiche del report.  
In pratica, di solito è necessario evidenziare solo una parte della tabella pivot. Gli obiettivi più comuni includono le etichette appartenenti a un campo di riga, le celle valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile cella. Un formato di area pivot rimane associato a una regione, ad esempio le etichette di un campo o i valori dei dati, e viene rielaborato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l'intera famiglia di overload `PivotTable.format` in modo che siano disponibili entrambi i tipi di formattazione:
- `format(PivotArea, Style)` collega uno stile a una regione semantica creata con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` collega uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `format(int row, int column, Style)` mira a una singola cella.
- `formatAll(Style)` formatta l'intera tabella pivot.

## **Formattare un'area Pivot**
Il flusso di lavoro basato su area semantica è l'approccio consigliato quando un'evidenziazione deve seguire un campo o una regione del report.
1. Creare un `PivotArea` con `new PivotArea(pivotTable)`. L'oggetto descrive una regione semantica appartenente a quella specifica tabella pivot.
1. Selezionare un campo in base alla sua posizione basata su zero su un asse specifico con `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LABEL_ONLY` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DATA_ONLY` seleziona solo le celle dati del campo.
1. Selezionare un campo per nome con `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve alle celle valore generate dagli elementi di quel campo.
1. Creare uno `Style` con `Workbook.createStyle()`, configurarne il carattere, il colore di primo piano e il motivo di sfondo solido, e passare lo stile a `PivotTable.format(area, style)`.
1. Ogni chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.getPivotFormats()`.
1. I formati ancorati al campo vengono applicati quando i dati pivot sono calcolati. Pertanto, chiamare `PivotTable.calculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L'esempio seguente costruisce una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.select` e `PivotTableSelectionType.LABEL_ONLY`, formatta le celle valore prodotte dallo stesso campo di riga con `PivotArea.selectField`, quindi ricalcola la tabella pivot in modo che entrambi gli stili vengano applicati.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formattare un'area Cell della tabella pivot**
Utilizzare `PivotTable.format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione semantica pivot.  
Un `CellArea` è descritto dai campi pubblici `StartRow`, `StartColumn`, `EndRow` e `EndColumn`. I valori sono coordinate del foglio di lavoro basate su zero, e le coordinate finali identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area copre le celle dalla posizione iniziale a quella finale inclusa.  
A differenza di un formato ancorato a un campo, un formato `CellArea` viene applicato immediatamente alle celle. Non è necessaria un'ulteriore chiamata a `calculateData()` perché lo stile appaia.  
Un rettangolo `CellArea` può contenere sia celle etichetta sia celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile corsivo di colore azzurro chiaro e salva la cartella di lavoro senza ulteriori ricalcoli.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Come le aree Pivot e le aree Cell vengono mappate**
Excel memorizza la formattazione delle tabelle pivot come record `pivotArea` anziché come normali record di stile cella del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot al momento della registrazione.  
La relazione tra il `CellArea` fornito dall'utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.
- Un `CellArea` può generare diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta l formattazione delle etichette e dei dati in modo indipendente.
- Un'area pivot può risolversi in più istanze `CellArea` disgiunte. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.getCellAreas()` restituisce una collezione anziché un singolo rettangolo.  
Ogni operazione di formattazione eseguita tramite `PivotTable.format` è registrata in `PivotTable.getPivotFormats()`. Ogni voce `PivotTableFormat` espone il relativo `PivotArea` e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre un `CellArea` che contiene regioni semantiche differenti può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone i flag `getOnlyLabel()` e `getOnlyData()`. L'esempio seguente formatta un unico rettangolo che copre sia etichette sia valori, ispeziona `PivotTable.getPivotFormats()` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

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
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
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
Poiché i formati sono memorizzati come aree pivot anziché come normali stili cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot viene aggiornata con `PivotTable.refreshData()`, ricalcolata con `calculateData()`, o salvata e ricaricata, ogni area pivot memorizzata si rielabora nella posizione corrente della sua regione e lo stile viene riapplicato.
{{% /alert %}}

Utilizzare un `PivotArea` costruito con `select` o `selectField` quando un'evidenziazione deve rimanere collegata a un campo o a una regione semantica attraverso gli aggiornamenti, e utilizzare un `CellArea` quando è sufficiente formattare un rettangolo fisso nella disposizione corrente della tabella pivot. L'overload `format(int row, int column, Style)` per una singola cella mira a una cella individuale. Utilizzare `formatAll`, descritto nella pagina principale, quando l'intera tabella pivot deve essere ridipinta in una sola operazione.

## **Articoli correlati**
- [Applicare stile alla tabella pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla tabella pivot](/cells/it/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore nella tabella pivot](/cells/it/nodejs-java/manage-value-fields/)
- [Aggiornare la tabella pivot](/cells/it/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}