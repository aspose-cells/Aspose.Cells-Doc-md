---
title: Verifiera lösenord för krypterade filer med JavaScript via C++
linktitle: Verifiera lösenordet för krypterade filer
type: docs
weight: 10
url: /sv/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verifiera lösenordet för krypterade Excel (xlsx, xlsb, xls, xlsm) och Open Office (ODS) filer med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Om Excel (xlsx, xlsb, xls, xlsm) och Open Office (ODS)-filer är låsta med ett lösenord, stöder Aspose enkel lösenordsverifikation utan att analysera specifika filuppgifter.  
{{% /alert %}}  

## **Verifiera lösenordet för den krypterade filen**  

För att verifiera lösenordet för filen som är krypterad, tillhandahåller Aspose.Cells for JavaScript via C++ metoden [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Denna metod tar emot två parametrar, filströmmen och lösenordet som ska verifieras.  
Följande kodavsnitt demonstrerar användningen av metod [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) för att verifiera om det angivna lösenordet är giltigt eller inte.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
