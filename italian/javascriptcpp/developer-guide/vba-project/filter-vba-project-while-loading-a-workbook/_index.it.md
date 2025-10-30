---
title: Filtra il progetto VBA durante il caricamento di una cartella di lavoro con JavaScript via C++
linktitle: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 140
url: /it/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: Scopri come filtrare i progetti VBA durante il caricamento dei file Excel usando Aspose.Cells for JavaScript via C++.
---

## **Filtrare il progetto VBA durante il caricamento di un file Excel in JavaScript tramite C++**

Alcuni file .xlsm/.xslb contengono un numero estremamente elevato di macro (o macro molto lunghe). Aspose.Cells for JavaScript via C++ caricherà incondizionatamente questi dati (metadata) all'apertura di tali file. Potrebbe essere necessario controllare questo [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) quando si desidera solo estrarre i nomi dei fogli per un grande numero di file, evitando così di caricare contenuti non necessari. Questo filtro viene fornito introducendo una nuova opzione, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions).

## **Codice di Esempio**

Il seguente codice di esempio carica un documento di lavoro in modo che solo il VBA venga filtrato. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
