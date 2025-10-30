---
title: Räkna antalet celler i arbetsbladet med JavaScript via C++
linktitle: Räkna antalet celler i kalkylbladet
type: docs
weight: 110
url: /sv/javascript-cpp/count-number-of-cells-in-the-worksheet/
description: Lär dig hur du programmatiskt räknar antalet celler i ett Excel arbetsblad med Aspose.Cells for JavaScript via C++.
keywords: räknar antalet celler i Excel arbetsblad JavaScript via C++, excel arbetsblad cell JavaScript via C++
---

Du kan räkna antalet celler i kalkylbladet genom att använda [**Cells.count**](https://reference.aspose.com/cells/javascript-cpp/cells/#count--) eller [**Cells.countLarge**](https://reference.aspose.com/cells/javascript-cpp/cells/#countLarge--) egenskaper som visas i kodexemplet nedan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cells Count Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get number of cells (regular Count)
            const numberOfCells = worksheet.cells.count;

            // If very large, use CountLarge
            const numberOfCellsLarge = worksheet.cells.countLarge;

            console.log("Number of Cells: " + numberOfCells);
            console.log("Number of Cells (CountLarge): " + numberOfCellsLarge);

            resultDiv.innerHTML = '<p style="color: green;">Number of Cells: ' + numberOfCells + '</p>'
                + '<p style="color: green;">Number of Cells (CountLarge): ' + numberOfCellsLarge + '</p>';
        });
    </script>
</html>
```
