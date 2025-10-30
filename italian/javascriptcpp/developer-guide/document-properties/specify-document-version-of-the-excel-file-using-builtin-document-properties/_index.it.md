---
title: Specificare la versione del documento del file Excel utilizzando proprietà di documento integrate con JavaScript via C++
linktitle: Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato
type: docs
weight: 20
url: /it/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Impara come specificare la versione del documento di un file Excel programmaticamente utilizzando le proprietà di documento integrate con JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**  

Puoi cambiare il **Numero di versione** di un file Excel facendo clic destro sul file e selezionando Proprietà > Dettagli e modificando il campo **Numero di versione**. Usa la proprietà [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) per cambiarlo programmaticamente usando le API Aspose.Cells.  

## **Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato**  

Il codice di esempio seguente crea un workbook e ne modifica le proprietà documento incorporate, inclusi Titolo, Autori e Numero di versione. Si prega di vedere il [file Excel di output](64716811.xlsx) generato dal codice e lo screenshot che mostra il numero di versione modificato tramite la proprietà [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
