---
title: Get HTML5 string from Cell
type: docs
weight: 90
url: /javascript-cpp/get-html5-string-from-cell/
description: Learn how to get an HTML5 string from a cell through the Aspose.Cells for JavaScript via C++ API.
keywords: Get HTML5 string from Cell JavaScript via C++, Obtain HTML5 string from Cell JavaScript via C++, Manage HTML5 string of Cell JavaScript via C++
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of the cell using the [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) method, which accepts a boolean parameter. If you pass **false** as a parameter, it will return standard HTML, but if you pass **true**, it will return an HTML5 string.

## **Get HTML5 string from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the normal HTML and HTML5 string from cell A1 using the [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) method and prints them on the console.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Get HTML String from Cell</h1>
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
            // This example creates a new workbook, writes text to A1 and retrieves HTML strings.
            const wb = new Workbook();

            const ws = wb.worksheets.get(0);

            const cell = ws.cells.get("A1");
            cell.value = "This is some text.";

            const strNormal = cell.htmlString;
            const strHtml5 = cell.htmlString;

            console.log("Normal:\r\n" + strNormal);
            console.log();
            console.log("HTML5:\r\n" + strHtml5);

            document.getElementById('result').innerHTML =
                '<h2>Results</h2>' +
                '<p><strong>Normal:</strong></p><pre>' + escapeHtml(strNormal) + '</pre>' +
                '<p><strong>HTML5:</strong></p><pre>' + escapeHtml(strHtml5) + '</pre>' +
                '<p style="color: green;">Operation completed successfully!</p>';
        });

        function escapeHtml(text) {
            if (text === null || text === undefined) return "";
            return String(text)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }
    </script>
</html>
```

## **Console Output**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

HTML5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}