---
title: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad med JavaScript via C++
linktitle: Hur man upptäcker ett filformat och kontrollerar om filen är krypterad
type: docs
weight: 2700
url: /sv/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Lär dig hur man upptäcker filformat och kontrollerar om en fil är krypterad med Aspose.Cells for JavaScript via C++
---

{{% alert color="primary" %}}  
Ibland måste du upptäcka ett filformat innan du öppnar det eftersom filtillägget inte garanterar att filinnehållet är lämpligt. Filen kan vara krypterad (lösenordsskyddad fil) så den kan inte läsas direkt, eller så bör vi inte läsa den. Aspose.Cells for JavaScript via C++ ger den statiska metoden [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) och några relevanta API:er som du kan använda för att bearbeta dokument.  
{{% /alert %}}  

Följande exempelkod illustrerar hur man upptäcker ett filformat (med hjälp av filvägen) och kontrollerar dess förlängning. Du kan också avgöra om filen är krypterad.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
