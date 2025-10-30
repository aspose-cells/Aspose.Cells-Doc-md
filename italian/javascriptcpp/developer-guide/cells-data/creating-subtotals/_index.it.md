---
title: Creazione dei subtotali
type: docs
weight: 800
url: /it/javascript-cpp/creating-subtotals/
description: Scopri come creare subtotali per qualsiasi valore ripetuto in un foglio di calcolo utilizzando l API Aspose.Cells for JavaScript attraverso C++.
keywords: Applica subtotali, Imposta subtotali, Aggiungi subtotali, Crea subtotali, Come aggiungere subtotali a un foglio di lavoro 
---

{{% alert color="primary" %}}

Puoi creare automaticamente subtotali per qualsiasi valore ripetuto in un foglio di calcolo. Aspose.Cells for JavaScript attraverso C++ fornisce funzionalità API che ti aiutano ad aggiungere subtotali ai fogli di calcolo programmaticamente.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiungere subtotali in Microsoft Excel:

1. Crea una semplice lista di dati nel primo foglio di lavoro del documento (come mostrato nella figura qui sotto) e salva il file come Book1.xls.
1. Seleziona una qualsiasi cella all'interno della tua lista.
1. Dal menu **Dati**, seleziona **Subtotali**. Verrà visualizzata la finestra di dialogo Subtotali. Definisci quale funzione utilizzare e dove inserire i subtotali.

## **Utilizzando l'API Aspose.Cells for JavaScript attraverso C++**

Aspose.Cells for JavaScript attraverso C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che permette l'accesso a ogni foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe fornisce un'ampia gamma di proprietà e metodi per gestire fogli di lavoro e altri oggetti. Ogni foglio di lavoro consiste in una collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Per aggiungere subtotali a un foglio di lavoro, usa il metodo [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) della classe [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Fornisci i valori dei parametri al metodo per specificare come il subtotale deve essere calcolato e posizionato.

Nei seguenti esempi, abbiamo aggiunto subtotali al primo foglio di lavoro del [file modello](book1.xlsx) utilizzando l'API Aspose.Cells for JavaScript attraverso C++. Quando il codice viene eseguito, viene creato un foglio di lavoro con subtotali.

Gli snippet di codice che seguono mostrano come aggiungere subtotali a un foglio di lavoro con Aspose.Cells for JavaScript attraverso C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
