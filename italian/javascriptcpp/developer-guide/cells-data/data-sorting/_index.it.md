---
title: Ordinamento dei dati
type: docs
weight: 130
url: /it/javascript-cpp/sort-data-of-excel/
description: Impara come ordinare i dati usando lo Script Aspose.Cells for Java tramite API C++.
keywords: Ordina i dati in ordine ascendente o discendente, ordina i dati in base al colore di sfondo.
---

{{% alert color="primary" %}}

L'ordinamento dei dati è una delle numerose funzionalità utili di Microsoft Excel. Permette agli utenti di ordinare i dati per facilitarne la scansione. Lo Script Aspose.Cells for Java tramite C++ consente agli sviluppatori di ordinare i dati del foglio di lavoro alfabeticamente o numericamente, funzionando allo stesso modo di Microsoft Excel per l'ordinamento dei dati.

{{% /alert %}}

## **Ordinare i dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1. Seleziona **Dati** dal menu **Ordina**. Verrà visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco - definito come un gruppo contiguo di dati in cui i dati sono visualizzati in colonne.

## **Ordinare i dati con Aspose.Cells**

Lo Script Aspose.Cells for Java tramite C++ fornisce la classe [**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter) utilizzata per ordinare i dati in ordine crescente o decrescente. La classe ha alcuni membri importanti, ad esempio proprietà come Key1 ... Key3 e Order1 ... Order3. Questi membri sono usati per definire le chiavi ordinate e specificare l'ordine di ordinamento delle chiavi.

È necessario definire le chiavi e impostare l'ordine di ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il metodo [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

Il metodo [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) accetta i seguenti parametri:

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), le celle per il foglio di lavoro sottostante.
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea), l'intervallo di celle. Definire l'area delle celle prima di applicare l'ordinamento dei dati.

Questo esempio utilizza il file di modello "Book1.xls" creato in Microsoft Excel. Dopo l'esecuzione del codice seguente, i dati vengono ordinati in modo appropriato.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Se si desidera ordinare *DaSinistraADestra*, utilizzare l'attributo [**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-).

{{% /alert %}}

### **Ordinamento dati con il colore di sfondo**

Excel offre funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzionalità è disponibile anche con lo Script Aspose.Cells for Java tramite C++ usando DataSorter, dove [**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor può essere usato in [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato nel funzione [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) vengono posizionate in cima o in fondo secondo il valore SortOrder e l'ordine delle altre celle non viene modificato.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Ordina dati nella colonna con elenco di ordinamenti personalizzati](/cells/it/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/javascript-cpp/specifying-sort-warning-while-sorting-data/)
