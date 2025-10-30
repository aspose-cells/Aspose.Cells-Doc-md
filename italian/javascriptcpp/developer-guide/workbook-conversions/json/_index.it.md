---
title: Json con JavaScript tramite C++
linktitle: Json
type: docs
weight: 300
url: /it/javascript-cpp/convert-workbook-to-json/
description: Impara come convertire Excel Workbook in JSON usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Aspose.Cells supporta la conversione di un workbook in file Json (JavaScript Object Notation).
{{% /alert %}}

## **Converti Workbook Excel in JSON**

L’API Aspose.Cells supporta la conversione dei fogli di calcolo in formato JSON. Per esportare il workbook in JSON, passa [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) come secondo parametro del metodo [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). Puoi anche usare la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) per specificare ulteriori impostazioni per l’esportazione del foglio di lavoro in JSON.

Il seguente esempio di codice dimostra come esportare il foglio attivo in JSON usando il membro di enumerazione [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json). Consulta il codice per convertire il [file sorgente](book1.xlsx) nel [file Json di output](book1.Json) generato dal codice come riferimento.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Convertire CSV in JSON](/cells/it/javascript-cpp/convert-csv-to-json/)
- [Converti-Excel-in-JSON](/cells/it/javascript-cpp/convert-excel-to-json/)
- [Convertire JSON in CSV](/cells/it/javascript-cpp/convert-json-to-csv/)
- [Converti-JSON-in-Excel](/cells/it/javascript-cpp/convert-json-to-excel/)
