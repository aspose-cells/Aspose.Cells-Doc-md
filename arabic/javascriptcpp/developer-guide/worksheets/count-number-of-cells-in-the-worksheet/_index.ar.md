---
title: عد خلايا الورقة باستخدام جافا سكريبت عبر C++
linktitle: عدد خلايا ورقة العمل
type: docs
weight: 110
url: /ar/javascript-cpp/count-number-of-cells-in-the-worksheet/
description: تعلم كيفية عد خلايا ورقة إكسل برمجيًا باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: عد خلايا ورقة إكسل باستخدام جافا سكريبت عبر C++، خلايا ورقة إكسل جافا سكريبت عبر C++
---

يمكنك إحصاء عدد الخلايا في الورقة باستخدام الخصائص [**Cells.count**](https://reference.aspose.com/cells/javascript-cpp/cells/#count--) أو [**Cells.countLarge**](https://reference.aspose.com/cells/javascript-cpp/cells/#countLarge--) كما هو موضح في مثال الكود أدناه.

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
