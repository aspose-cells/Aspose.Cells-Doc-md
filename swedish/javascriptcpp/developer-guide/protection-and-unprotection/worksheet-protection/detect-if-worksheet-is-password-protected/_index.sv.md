---
title: Upptäck om Arbetssnitt är lösenordsskyddat med JavaScript via C++
linktitle: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 360
url: /sv/javascript-cpp/detect-if-worksheet-is-password-protected/
description: Lär dig hur du upptäcker om ett arbetsblad är lösenordsskyddat med Aspose.Cells for JavaScript via C++. 
keywords: Upptäck arbetsbladets lösenordsskydd JavaScript via C++, Kontrollera om arbetsblad är lösenordsskyddat JavaScript via C++, Aspose.Cells for JavaScript via C++
---

{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböcker och arbetsblad separat. Till exempel kan ett kalkylblad innehålla ett eller flera arbetsblad som är lösenordsskyddade, men själva kalkylbladet kan vara skyddat eller inte skyddat. Aspose.Cells API:er ger möjligheten att upptäcka om ett givet arbetsblad är lösenordsskyddat eller inte. Denna artikel visar användningen av Aspose.Cells for JavaScript via C++ API för att uppnå detta.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ har exponerat egenskapen [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) för att upptäcka om ett arbetsblad är lösenordsskyddat eller inte. Den booleska egenskapen [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) returnerar **true** om [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) är lösenordsskyddat och **false** om inte.

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
