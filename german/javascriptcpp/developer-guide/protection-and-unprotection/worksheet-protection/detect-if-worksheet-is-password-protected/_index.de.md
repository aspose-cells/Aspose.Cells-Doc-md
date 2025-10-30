---
title: Erkennen, ob ein Arbeitsblatt passwortgeschützt ist mit JavaScript über C++
linktitle: Erkennen, ob Arbeitsblatt passwortgeschützt ist
type: docs
weight: 360
url: /de/javascript-cpp/detect-if-worksheet-is-password-protected/
description: So erkennen Sie, ob ein Arbeitsblatt mit Aspose.Cells for JavaScript über C++ passwortgeschützt ist. 
keywords: Arbeitsblatt Passwortschutz erkennen JavaScript über C++, prüfen, ob ein Arbeitsblatt passwortgeschützt ist JavaScript über C++, Aspose.Cells for JavaScript über C++
---

{{% alert color="primary" %}}

Es ist möglich, Arbeitsmappen und Arbeitsblätter separat zu schützen. Zum Beispiel kann eine Tabelle ein oder mehrere passwortgeschützte Arbeitsblätter enthalten, während die Tabelle selbst geschützt oder ungeschützt sein kann. Die Aspose.Cells APIs bieten die Möglichkeiten, zu erkennen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. Dieser Artikel zeigt die Verwendung der Aspose.Cells for JavaScript über C++ API, um dasselbe zu erreichen.

{{% /alert %}}

Aspose.Cells for JavaScript über C++ hat die Eigenschaft [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) eingeführt, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht. Der boolesche Eigenschaftswert [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) gibt **wahr** zurück, wenn [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) passwortgeschützt ist, und **falsch**, wenn nicht.

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
