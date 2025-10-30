---
title: Hämta kalkylbladets unika ID med JavaScript via C++
linktitle: Få arbetsbladets unika id
type: docs
weight: 190
url: /sv/javascript-cpp/get-worksheet-unique-id/
description: Denna artikel visar hur man hämtar Excel arkets unika ID med JavaScript bibliotek och C++ API programmässigt.
keywords: unikt ID excelark JavaScript via C++, unikt ID ark JavaScript via C++
---

## **Få arbetsbladets unika id**

Aspose.Cells for JavaScript via C++ ger möjlighet att få det unika ID:t för ett ark genom att använda [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--)-egenskapen. Följande kodavsnitt visar användning av [**Worksheet.uniqueId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#uniqueId--)-egenskapen för att skriva ut det unika ID:t för ett ark. Koden använder detta [provexempel](105480213.xlsx).

### Källkod

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
