---
title: Impostazione dell opzione tabella pivot  Per le celle vuote mostra
type: docs
weight: 40
url: /it/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Puoi impostare opzioni diverse per la tabella pivot usando Aspose.Cells for JavaScript tramite C++. Una di queste opzioni è "Per le celle vuote visualizza". Impostando questa opzione, tutte le celle vuote in una tabella pivot vengono visualizzate come una stringa specificata.

{{% /alert %}}

## **Impostazione dell'opzione della tabella pivot in Microsoft Excel**

Per trovare e impostare questa opzione in Microsoft Excel:

1. Seleziona una tabella pivot e fai clic con il pulsante destro del mouse.
1. Seleziona **Opzioni tabella pivot**.
1. Seleziona la scheda **Layout e Formato**.
1. Seleziona l'opzione **Per le celle vuote mostra** e specifica una stringa.

## **Impostare l’opzione della Tabella Pivot usando Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript tramite C++ fornisce le proprietà [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-) e [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-) per impostare l’opzione "Per le celle vuote visualizza" della tabella pivot.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Articoli correlati

- [Formattazione tabella pivot](/cells/it/javascript-cpp/formatting-pivot-table/)
