---
title: Filtrare i Nomi definiti durante il caricamento del Workbook con JavaScript via C++
linktitle: Filtra i Nomi Definiti durante il caricamento del Workbook
type: docs
weight: 50
url: /it/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells consente di filtrare o rimuovere i nomi definiti presenti all’interno del workbook. Si usi [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) per caricare i nomi definiti e [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) per rimuoverli durante il caricamento del workbook. Si noti che, se si rimuovono i nomi definiti, le formule all’interno del workbook potrebbero non funzionare più correttamente.

## **Filtra i nomi definiti durante il caricamento del foglio di lavoro**

Il seguente esempio carica il file Excel di esempio](61767860.xlsx) che contiene una formula nella cella **C1** con i nomi definiti, cioè *SUM(MyName1, MyName2)*. Dato che usiamo [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) per rimuovere i nomi definiti durante il caricamento del workbook, la formula nella cella C1 nel [file Excel di output](61767861.xlsx) si interrompe e visualizza *#NAME?*. Si veda il seguente screenshot che mostra l’effetto del codice sul file Excel di esempio.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
