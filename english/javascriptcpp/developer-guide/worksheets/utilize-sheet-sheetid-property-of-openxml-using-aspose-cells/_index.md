---
title: Utilize Sheet.SheetId property of OpenXml using Aspose.Cells for JavaScript via C++
linktitle: Utilize Sheet.SheetId property of OpenXml using Aspose.Cells
type: docs
weight: 200
url: /javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: This article demonstrates how to utilize Sheet.SheetId property of OpenXml using Excel manipulation with Aspose.Cells for JavaScript via C++ programmatically.
keywords: sheet id property of openxml JavaScript via C++, sheet id excel worksheet JavaScript via C++
---

## **Possible Usage Scenarios**

*Sheet.SheetId* property is available inside the *DocumentFormat.OpenXml.Spreadsheet* module and is part of OpenXml. You can see this property and its value inside *workbook.xml* as shown in the following screenshot. Aspose.Cells provides the equivalent property as [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilize Sheet.SheetId property of OpenXml using Aspose.Cells for JavaScript via C++**

The following sample code loads the [sample Excel file](51740716.xlsx), reads its Sheet or Tab Id, then assigns it new Tab Id and saves it as [output Excel file](51740717.xlsx). Please also see the console output of the code given below for a reference.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Console Output**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}