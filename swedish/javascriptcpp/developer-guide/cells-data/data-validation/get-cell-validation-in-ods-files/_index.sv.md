---
title: Få cellvalidering i ODS filer
type: docs
weight: 180
url: /sv/javascript-cpp/get-cell-validation-in-ods-files/
description: Lär dig hur du hämtar cellvalidering i ODS filer via API t Aspose.Cells for JavaScript via C++.
keywords: Hämta cellvalidering JavaScript via C++, Hämta cellvalidering JavaScript via C++
---

## **Hämta cellvalidering i ODS-filer**  

Med Aspose.Cells for JavaScript via C++ kan du hämta valideringen som tillämpats på en cell i ODS-filer. För detta tillhandahåller API:t egenskapen `[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)` i klassen `[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/)`.  

Följande kodexempel visar användningen av egenskapen [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) genom att ladda filen [source ODS](101089354.ods) och läsa valideringen av cellen A9.  

### **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
