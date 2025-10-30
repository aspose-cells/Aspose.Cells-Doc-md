---
title: Specificare la lingua del file Excel utilizzando proprietà di documento integrate con JavaScript via C++
linktitle: Specificare la lingua del file Excel utilizzando le proprietà del documento integrato
type: docs
weight: 30
url: /it/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Possibili Scenari di Utilizzo**

Puoi cambiare la lingua di un file Excel cliccando con il tasto destro sul file e selezionando Proprietà > Dettagli e modificando il campo Lingua. Usa la proprietà [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) per cambiarla programmaticamente usando Aspose.Cells for JavaScript attraverso API C++.

## **Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate**

Il codice di esempio seguente crea un workbook e ne modifica la proprietà documento incorporata chiamata lingua. Si prega di vedere il [file Excel di output](64716891.xlsx) generato dal codice e lo screenshot che mostra il campo Lingua modificato tramite la proprietà [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
