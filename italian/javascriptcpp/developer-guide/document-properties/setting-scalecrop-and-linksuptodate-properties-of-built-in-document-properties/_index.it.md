---
title: Impostare le proprietà ScaleCrop e LinksUpToDate delle proprietà di documento incorporate con JavaScript tramite C++
linktitle: Imposta le proprietà ScaleCrop e LinksUpToDate delle proprietà del documento built in
type: docs
weight: 320
url: /it/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Impara come impostare le proprietà ScaleCrop e LinksUpToDate delle proprietà di documento incorporate usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) e [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) sono due proprietà estese di documento incorporate definite nel formato OpenXml. Lo scopo di queste proprietà sono i seguenti.

## **1) ScaleCrop**
Questo elemento indica la modalità di visualizzazione dell'anteprima del documento. Imposta questo elemento su **TRUE** per abilitare il ridimensionamento dell'anteprima del documento per la visualizzazione. Imposta questo elemento su **FALSE** per abilitare il ritaglio dell'anteprima del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.

## **2) LinksUpToDate**
Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su **TRUE** per indicare che i collegamenti ipertestuali sono aggiornati. Imposta questo elemento su **FALSE** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.

## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato**
Il seguente esempio di codice imposta le proprietà di documento estese integrate [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) e [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) del libro di lavoro. Si prega di verificare il [file Excel di output](5115500.xlsx) generato con questo codice, cambiarne l'estensione in .zip, estrarre il contenuto e visualizzare app.xml come mostrato nello screenshot sopra.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
