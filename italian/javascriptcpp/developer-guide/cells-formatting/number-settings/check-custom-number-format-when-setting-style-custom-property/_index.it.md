---
title: Controlla il formato numero personalizzato quando imposti Style.Custom Property
linktitle: Controlla il formato numero personalizzato quando imposti Style.Custom Property
description: Aspose.Cells è una libreria JavaScript per lavorare con file di fogli di calcolo, che supporta il controllo dei formati numerici personalizzati durante lo stile. Questo articolo ti mostrerà come usare la libreria Aspose.Cells per verificare i formati numerici personalizzati e assicurarti che lo stile sia corretto.
keywords: Aspose.Cells, librerie JavaScript, fogli di calcolo, stile, formattazione numerica personalizzata, verifica, convalida
type: docs
weight: 170
url: /it/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se assegni un formato numerico personalizzato non valido alla proprietà [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-), allora Aspose.Cells for JavaScript via C++ non lancerà eccezioni. Ma se vuoi che Aspose.Cells controlli se il formato numerico personalizzato assegnato è valido o meno, imposta la proprietà [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) su **true**.

## **Controlla il formato numerico personalizzato quando imposti la proprietà Style.custom**

Il seguente esempio di codice assegna un formato numerico personalizzato non valido alla proprietà [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-). Poiché abbiamo già impostato la proprietà [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) su **true**, genera un'eccezione, ad esempio, formato numerico non valido. Leggi i commenti all’interno del codice per ulteriori aiuti.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
