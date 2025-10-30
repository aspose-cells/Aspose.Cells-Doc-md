---
title: Aggiungere celle alla finestra di monitoraggio delle formule di Microsoft Excel con JavaScript tramite C++
linktitle: Aggiungi celle alla finestra di monitoraggio delle formule di Microsoft Excel
description: Come usare la libreria Aspose.Cells per aggiungere celle alla finestra di monitoraggio delle formule in Excel usando JavaScript tramite C++. Caricando un file Excel esistente o creandone uno nuovo, possiamo manipolare le celle al suo interno e impostare le formule. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, Finestra di monitoraggio delle formule, Celle, Aggiunta, JavaScript tramite C++
type: docs
weight: 60
url: /it/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possibili Scenari di Utilizzo**

La finestra di watch di Microsoft Excel è uno strumento utile per osservare i valori delle celle e le relative formule comodamente in una finestra. Puoi aprire la *Finestra di Watch* usando Microsoft Excel cliccando su *Formulas > Watch* *Window*. Ha il pulsante *Add Watch* che può essere usato per aggiungere le celle da ispezionare. In modo simile, puoi usare il metodo [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) per aggiungere celle alla *Watch Window* usando l'API di Aspose.Cells.

## **Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel**

Il seguente esempio di codice imposta le formule delle celle C1 ed E1 e le aggiunge entrambe alla finestra di watch. Successivamente, salva il workbook come [file Excel di output](67338481.xlsx). Se apri il file Excel di output e visualizzi la *Finestra di Watch*, vedrai entrambe le celle come mostrato in questa schermata.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
