---
title: Detect if Worksheet is Password Protected with JavaScript via C++
linktitle: Detect if Worksheet is Password Protected
type: docs
weight: 360
url: /javascript-cpp/detect-if-worksheet-is-password-protected/
description: Learn how to detect if a worksheet is password protected using Aspose.Cells for JavaScript via C++. 
keywords: Detect Worksheet Password Protection JavaScript via C++, Check if Worksheet is Password Protected JavaScript via C++, Aspose.Cells for JavaScript via C++
---

{{% alert color="primary" %}}

It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password‑protected; however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect if a given worksheet is password‑protected or not. This article demonstrates the usage of Aspose.Cells for JavaScript via C++ API to achieve the same.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ has exposed the [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) property to detect if a worksheet is password‑protected or not. Boolean type [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) property returns **true** if the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) is password‑protected and **false** if not.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```