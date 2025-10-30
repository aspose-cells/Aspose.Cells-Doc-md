---
title: Arbeitsblatt IDs mit JavaScript über C++ abrufen
linktitle: Arbeitsblatt eindeutige ID abrufen
type: docs
weight: 190
url: /de/javascript-cpp/get-worksheet-unique-id/
description: Dieser Artikel zeigt, wie man die eindeutige ID eines Excel Arbeitsblatts mittels JavaScript Bibliothek und C++ API programmatisch erhält.
keywords: Eindeutige ID für Excel Arbeitsblätter in JavaScript via C++, eindeutige ID für Arbeitsblatt in JavaScript via C++
---

## **Arbeitsblatt eindeutige ID abrufen**

Aspose.Cells for JavaScript über C++ bietet die Möglichkeit, die eindeutige ID eines Arbeitsblatts mit der [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--)-Eigenschaft zu erhalten. Das folgende Codebeispiel zeigt die Verwendung der [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--)-Eigenschaft, um die eindeutige ID eines Arbeitsblatts auszugeben. Das folgende Codebeispiel benutzt diese [Beispiel-Excel-Datei](105480213.xlsx).

### Quellcode

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Worksheet Unique Id Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Unique Id
            const uniqueId = worksheet.uniqueId;
            console.log("Unique Id: " + uniqueId);

            document.getElementById('result').innerHTML = '<p style="color: green;">Unique Id: ' + uniqueId + '</p>';
        });
    </script>
</html>
```
