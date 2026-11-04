---
title: Formattare parte di una Tabella Pivot
description: Formattare parte di una tabella pivot in Aspose.Cells for JavaScript via C++ applicando stili alle regioni semantiche PivotArea o ai rettangoli CellArea tramite PivotTable.Format, con i formati memorizzati in PivotTable.PivotFormats e conservati quando la tabella pivot viene aggiornata.
linktitle: Formattare parte di una Tabella Pivot
keywords: Aspose.Cells for JavaScript via C++, tabella pivot, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /it/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
`PivotTable.FormatAll` applica un unico stile all'intera tabella pivot ed è descritto nella pagina padre. Non distingue tra etichette, valori, totali o regioni specifiche del report.  
Nella pratica, di solito è necessario evidenziare solo una parte della tabella pivot. Gli obiettivi comuni includono le etichette appartenenti a un campo di riga, le celle valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile delle celle. Un formato di area pivot rimane associato a una regione, ad esempio le etichette o i valori di un campo, e viene risolto nuovamente quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l'intera famiglia di overload `PivotTable.Format` in modo che entrambi i tipi di formattazione siano disponibili:  
- `Format(PivotArea, Style)` associa uno stile a una regione semantica creata con `PivotArea.Select` o `PivotArea.SelectField`.  
- `Format(CellArea, Style)` associa uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.  
- `Format(int row, int column, Style)` mira a una singola cella.  
- `FormatAll(Style)` formatta l'intera tabella pivot.

## **Formattare un'area pivot**
Il flusso di lavoro basato su aree semantiche è l'approccio consigliato quando un evidenziatore deve seguire un campo o una regione del report.  
1. Creare un `PivotArea` con `new PivotArea(pivotTable)`. L'oggetto descrive una regione semantica che appartiene a quella specifica tabella pivot.  
1. Selezionare un campo tramite la sua posizione zero‑based su un asse specificato con `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DataAndLabel` seleziona sia le etichette sia i dati del campo.  
   - `PivotTableSelectionType.LabelOnly` seleziona solo le etichette del campo.  
   - `PivotTableSelectionType.DataOnly` seleziona solo le celle dati del campo.  
1. Selezionare un campo per nome con `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve nelle celle valore prodotte dagli elementi di quel campo.  
1. Creare uno `Style` con `Workbook.CreateStyle()`, configurarne il carattere, il colore di primo piano e il modello di sfondo solido, quindi passare lo stile a `PivotTable.Format(area, style)`.  
1. Cada chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.PivotFormats`.  
1. I formati ancorati al campo vengono applicati quando i dati pivot vengono calcolati. Pertanto, chiamare `PivotTable.CalculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L'esempio seguente costruisce una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.Select` e `PivotTableSelectionType.LabelOnly`, formatta le celle valore prodotte dallo stesso campo di riga con `PivotArea.SelectField`, quindi ricalcola la tabella pivot in modo che entrambi gli stili vengano applicati.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Formattare un'area di celle della tabella pivot**
Utilizzare `PivotTable.Format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione pivot semantica.  
Un `CellArea` è descritto dai campi `startRow`, `startColumn`, `endRow` e `endColumn`. I valori sono coordinate zero‑based del foglio di lavoro, e le coordinate finali identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area comprende tutte le celle dalla posizione iniziale a quella finale, inclusa.  
Diversamente da un formato ancorato a un campo, un formato `CellArea` viene applicato alle celle immediatamente. Non è necessario un'ulteriore chiamata a `CalculateData()` perché lo stile appaia.  
Un rettangolo `CellArea` può contenere sia celle etichetta sia celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile corsivo e di colore blu chiaro, quindi salva la cartella di lavoro senza ulteriori ricalcoli.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Come le aree pivot e le aree di celle vengono mappate**
Excel memorizza la formattazione della tabella pivot come record `pivotArea` anziché come normali record di stile delle celle del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot al momento della registrazione.  
La relazione tra il `CellArea` fornito dall'utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.  
- Un `CellArea` può generare diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene scomposto in regole separate per etichette e dati, perché il modello pivot tratta indipendentemente la formattazione delle etichette e dei dati.  
- Un'area pivot può risolversi in più istanze `CellArea` disgiunte. Una regione semantica come una riga del totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.GetCellAreas()` restituisce una collezione anziché un singolo rettangolo.  
Ogni operazione di formattazione eseguita tramite `PivotTable.Format` viene registrata in `PivotTable.PivotFormats`. Ogni voce `PivotTableFormat` espone il relativo `PivotArea` e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre un `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone i flag `OnlyLabel` e `OnlyData`. L'esempio seguente formatta un unico rettangolo che copre sia etichette sia valori, ispeziona `PivotTable.PivotFormats` e stampa le coordinate `CellArea` a cui ogni area pivot memorizzata si risolve.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Poiché i formati sono memorizzati come aree pivot anziché come normali stili di cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot viene aggiornata con `PivotTable.RefreshData`, ricalcolata con `CalculateData`, o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e lo stile viene riapplicato.
{{% /alert %}}

Utilizzare un `PivotArea` costruito con `Select` o `SelectField` quando un evidenziatore deve rimanere collegato a un campo o a una regione semantica attraverso gli aggiornamenti, e utilizzare un `CellArea` quando è sufficiente formattare un rettangolo fisso nel layout corrente della tabella pivot. L'overload `Format(int row, int column, Style)` per una singola cella mira a una cella individuale. Usare `FormatAll`, descritto nella pagina padre, quando l'intera tabella pivot deve essere riformattata in un'unica operazione.

## **Articoli correlati**
- [Applicare stile alla Tabella Pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla Tabella Pivot](/cells/it/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore nella Tabella Pivot](/cells/it/javascript-cpp/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}