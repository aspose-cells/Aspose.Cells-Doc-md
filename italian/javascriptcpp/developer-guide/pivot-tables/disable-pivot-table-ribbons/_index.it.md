---
title: Disabilita le barre delle tabelle pivot
type: docs
weight: 90
url: /it/javascript-cpp/disable-pivot-table-ribbons/
description: Come disabilitare le schede della tabella pivot con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, libreria JavaScript di Excel tramite C++, disattivare le schede della tabella pivot usando Aspose.Cells for JavaScript via C++ Excel Library.
---

{{% alert color="primary" %}}

I report basati su tabelle pivot sono utili ma soggetti a errori se gli utenti target non hanno una conoscenza dettagliata di Excel per configurare questi report. In queste circostanze, le organizzazioni vorranno limitare la possibilità degli utenti di modificare un report basato su tabella pivot. Funzionalità comuni come l'aggiunta di filtri, slicer, campi, o il cambio dell'ordine degli elementi nel report sono generalmente sconsigliate per ogni utente. D'altra parte, questi utenti dovrebbero poter aggiornare il report e usare filtri o slicer esistenti. Aspose.Cells for JavaScript via C++ ha fornito questa possibilità agli sviluppatori per limitare le modifiche degli utenti durante la creazione di questi report. A tal fine, Excel fornisce una funzione per disattivare la barra della scheda della tabella pivot, funzione che è supportata anche da Aspose.Cells for JavaScript via C++, cioè gli sviluppatori possono disabilitare la barra che contiene i controlli per modificare questi report.

{{% /alert %}}

## **Come disabilitare la scheda della tabella pivot usando Aspose.Cells for JavaScript via C++**

Il seguente codice dimostra questa funzionalità accedendo a una tabella pivot da un foglio e impostando [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) su **false**. Il file di esempio della tabella pivot può essere scaricato da questo [link](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
