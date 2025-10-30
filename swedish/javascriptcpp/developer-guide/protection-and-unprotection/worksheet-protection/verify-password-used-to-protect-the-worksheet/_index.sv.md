---
title: Verifiera lösenordet som används för att skydda arbetsbladet med JavaScript via C++
linktitle: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 370
url: /sv/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: Lär dig hur du verifierar lösenordet som användes för att skydda ett arbetsblad med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells API har förbättrat [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection)-klassen genom att introducera några användbara egenskaper och metoder. En sådan metod är [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) som tillåter att ange ett lösenord som ett *string*-objekt och verifierar om samma lösenord har använts för att skydda [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

{{% /alert %}}

Metoden [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) returnerar **true** om det angivna lösenordet matchar lösenordet som användes för att skydda kalkbladet och **false** om det inte matchar. Följande kod använder [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) i samband med [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)-egenskapen för att upptäcka lösenordsskyddet och verifiera lösenordet.

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

            // Instantiate Workbook with file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                // Verify the password used to protect the Worksheet
                if (sheet.protection.verifyPassword("1234")) {
                    resultDiv.innerHTML = '<p style="color: green;">Specified password has matched</p>';
                } else {
                    resultDiv.innerHTML = '<p style="color: red;">Specified password has not matched</p>';
                }
            } else {
                resultDiv.innerHTML = '<p style="color: blue;">Worksheet is not password protected</p>';
            }
        });
    </script>
</html>
```
