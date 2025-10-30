---
title: Passwort, das zum Schutz des Arbeitsblatts verwendet wurde, mit JavaScript über C++ überprüfen
linktitle: Das Verifizieren des zum Schutz des Arbeitsblatts verwendeten Passworts
type: docs
weight: 370
url: /de/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: Erfahren Sie, wie Sie das zum Schutz eines Arbeitsblatts verwendete Passwort mit Aspose.Cells for JavaScript über C++ verifizieren.
---

{{% alert color="primary" %}}

Aspose.Cells APIs haben die [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection)-Klasse durch die Einführung nützlicher Eigenschaften & Methoden verbessert. Eine davon ist die [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)-Methode, mit der Sie ein Passwort als *string*-Instanz angeben und überprüfen können, ob dieses Passwort zum Schutz des [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) verwendet wurde.

{{% /alert %}}

Die [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)-Methode gibt **true** zurück, wenn das angegebene Passwort mit dem zum Schutz des Arbeitsblatts verwendeten Passwort übereinstimmt, und **false**, wenn das Passwort nicht übereinstimmt. Der folgende Code verwendet die [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-)-Methode in Verbindung mit der [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--)-Eigenschaft, um die Passwortsicherung zu erkennen und das Passwort zu überprüfen.

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
