---
title: Ottenere la fonte dati della connessione esterna della tabella pivot
type: docs
weight: 150
url: /it/javascript-cpp/get-external-connection-data-source-of-pivot-table/
description: Come ottenere la sorgente dati di connessione esterna di una tabella pivot con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript Excel, libreria JavaScript di Excel, ottenere la sorgente dati di connessione esterna di una tabella pivot usando Aspose.Cells for JavaScript via C++ Excel Library.
---

## **Come ottenere la fonte dati della connessione esterna della tabella pivot**

Aspose.Cells for JavaScript via C++ offre la capacità di ottenere la sorgente dati di connessione esterna della tabella pivot. Per questo, l'API fornisce la proprietà [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) della classe [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/). La proprietà [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) restituisce l'oggetto [**ExternalConnection**](https://reference.aspose.com/cells/javascript-cpp/externalconnection/). Il seguente esempio di codice dimostra l'uso della proprietà [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) per ottenere la sorgente dati di connessione esterna della tabella pivot.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Pivot Table External Connection Example</title>
    </head>
    <body>
        <h1>Pivot Table External Connection Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get the pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // Get external connection data source
            const externalConnection = pivotTable.externalConnectionDataSource;

            const name = externalConnection.name;
            const type = externalConnection.type;

            console.log("External Connection Data Source");
            console.log("Name: " + name);
            console.log("Type: " + type);

            resultDiv.innerHTML = `<p style="color: green;">External Connection Data Source</p>
                                   <p>Name: ${name}</p>
                                   <p>Type: ${type}</p>`;
        });
    </script>
</html>
```

Il file di origine utilizzato nel frammento di codice è allegato a scopo di riferimento.

[File di origine](104398862.xlsx)
