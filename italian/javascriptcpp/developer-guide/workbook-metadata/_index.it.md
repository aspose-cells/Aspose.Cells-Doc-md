---
title: Usando WorkbookMetadata con JavaScript tramite C++
linktitle: Metadati del foglio di lavoro
type: docs
weight: 320
url: /it/javascript-cpp/using-workbookmetadata/
description: Impara come modificare i metadati del workbook usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  
Aspose.Cells permette di caricare una versione leggera di una cartella di lavoro in memoria per modificare le sue informazioni metadata. Si prega di usare la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata) per caricare la cartella di lavoro.  
{{% /alert %}}  

Il seguente esempio di codice usa la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata) per modificare le proprietà personalizzate di un documento. Una volta aperta la cartella di lavoro usando la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), sarai in grado di leggere le proprietà del documento. Ecco un esempio di codice usando la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Metadata Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Metadata Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MetadataOptions, MetadataType, WorkbookMetadata } = AsposeCells;

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
            const uint8 = new Uint8Array(arrayBuffer);

            // Create metadata options for document properties
            const options = new MetadataOptions(MetadataType.Document_Properties);

            // Open Workbook metadata from the uploaded file
            const meta = new WorkbookMetadata(uint8, options);

            // Set some properties
            meta.customDocumentProperties.add("test", "test");

            // Save the metadata info and get resulting workbook bytes
            const outputData = meta.save(SaveFormat.Xlsx);

            // Provide download link for the modified file
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Sample2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            // Open the workbook from the modified bytes
            const w = new Workbook(outputData);

            // Read document property
            const propValue = w.customDocumentProperties.get("test");
            console.log(propValue);

            document.getElementById('result').innerHTML = `<p style="color: green;">Metadata updated successfully! Document property "test" = ${propValue}</p>`;
        });
    </script>
</html>
```
