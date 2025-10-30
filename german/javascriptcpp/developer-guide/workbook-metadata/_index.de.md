---
title: Verwendung von WorkbookMetadata mit JavaScript über C++
linktitle: Metadaten der Arbeitsmappe
type: docs
weight: 320
url: /de/javascript-cpp/using-workbookmetadata/
description: Erfahren Sie, wie Sie die Metadaten einer Arbeitsmappe mit Aspose.Cells for JavaScript über C++ bearbeiten.
---

{{% alert color="primary" %}}  
Aspose.Cells ermöglicht das Laden einer leichten Version eines Arbeitsbuchs ins Speicher für die Bearbeitung seiner Metadaten. Bitte verwenden Sie die [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata)-Klasse, um das Arbeitsbuch zu laden.  
{{% /alert %}}  

Der folgende Beispielcode verwendet die [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata)-Klasse, um benutzerdefinierte Dokumenteigenschaften eines Arbeitsbuchs zu bearbeiten. Nachdem Sie das Arbeitsbuch mit der [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse geöffnet haben, können Sie die Dokumenteigenschaften lesen. Hier ist ein Beispielcode mit der [**WorkbookMetadata**](https://reference.aspose.com/cells/javascript-cpp/workbookmetadata)-Klasse.  

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
