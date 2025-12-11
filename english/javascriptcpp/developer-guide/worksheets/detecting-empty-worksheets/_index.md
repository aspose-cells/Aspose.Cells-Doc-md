---
title: Detecting Empty Worksheets with JavaScript via C++
linktitle: Detecting Empty Worksheets
type: docs
weight: 410
url: /javascript-cpp/detecting-empty-worksheets/
description: This article shows you code explaining how to detect empty worksheets of Excel workbooks programmatically using the JavaScript API with the C++ library.
keywords: detect empty worksheet JavaScript via C++, find empty excel worksheet JavaScript via C++
---

## **Check for Populated Cells**

Worksheets can have one or more cells populated with values, where a value can be simple (text, numeric, date/time) or a formula, or a formula‑based value. In such a case, it is easy to detect if a given worksheet is empty or not. All we have to check is the [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) or [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) properties. If the aforementioned properties return zero or positive values, that means one or more cells have been populated; however, if any of these properties return **-1**, that indicates that none of the cells have been populated in the given worksheet.

{{% alert color="primary" %}}

The rows and columns collections have zero‑based indices; therefore, a cell at row 0 and column 0 means the first cell in the worksheet, which is **A1**.

{{% /alert %}}

## **Check for Empty Initialized Cells**

All cells that have values are automatically initialized; however, there is a possibility that a worksheet has cells with only formatting applied. In such a scenario, the [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) or [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) properties will return **-1**, indicating the absence of any populated values, but initialized cells due to cell formatting cannot be detected using this approach. In order to check if a worksheet has empty initialized cells, it is advised to use the `Enumerator.MoveNext` method on the enumerator obtained from the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection. If the `Enumerator.MoveNext` method returns **true**, that means there are one or more initialized cells in the given worksheet.

## **Check for Shapes**

It is possible that a given worksheet does not have any populated cells; however, it could contain shapes and objects such as controls, charts, images, and so on. If we need to check if a worksheet contains any shapes, we can do it by inspecting the [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--) property. Any positive value indicates the presence of shape(s) in the worksheet.

## **Programming Sample**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```