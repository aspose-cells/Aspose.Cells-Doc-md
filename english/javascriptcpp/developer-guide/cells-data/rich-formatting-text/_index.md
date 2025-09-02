---
title: Access and Update the Portions of Rich Text of Cell
linktitle: Rich Formatting Text
type: docs
weight: 40
url: /javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Learn how to Access and Update the Portions of Rich Text of Cell through the Aspose.Cells for JavaScript via C++ API.
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ allows you to access and update the portions of the rich text of the cell. For this purpose, you can use [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) and [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) properties. These properties will return and accept the array of [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) objects which you can use to access and update various properties of font like font name, font color, boldness, etc.

{{% /alert %}}

## **Access and Update the Portions of Rich Text of Cell**

The following code demonstrates the usage of [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) and [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) property using the [source excel file](5112369.xlsx) which you can download from the provided link. The source excel file has a rich text in the cell A1. It has 3 portions and each portion has a different font. The following code snippet accesses these portions and updates the first portion with a new font name. Finally, it saves the workbook as [output excel file](5112366.xlsx). When you will open it, you will find the font of the first portion of the text has changed to **"Arial"**.

### JavaScript code to access and update the portions of Rich Text of Cell

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Console output generated by the sample code



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}