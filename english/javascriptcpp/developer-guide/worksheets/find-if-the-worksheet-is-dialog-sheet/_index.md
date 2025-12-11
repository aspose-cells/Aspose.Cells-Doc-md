---
title: Find if the Worksheet is Dialog Sheet with JavaScript via C++
linktitle: Find if the Worksheet is Dialog Sheet
type: docs
weight: 90
url: /javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: This article provides instructions and sample code for determining programmatically whether an Excel worksheet is a Dialog Sheet using Aspose.Cells for JavaScript via C++.
keywords: find excel worksheet dialog type JavaScript via C++, worksheet dialog JavaScript via C++
---

## **Possible Usage Scenarios**

A Dialog Sheet is an older sheet format that contains a dialog box. Such a sheet could be inserted by an older version of Microsoft Excel, e.g., 2003, as shown in this screenshot. It can also be inserted with VBA in newer versions, e.g., Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find if the sheet is a dialog sheet or some other type of sheet with [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) property provided by Aspose.Cells for JavaScript via C++. If it returns enumeration value [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), then it means you are dealing with a dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the [sample Excel file](64716820.xlsx) that contains a dialog sheet. It checks the [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) property, compares it with [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), and then prints the message. Please see the console output of the sample code given below for more help.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is a dialog sheet and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Console Output**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}