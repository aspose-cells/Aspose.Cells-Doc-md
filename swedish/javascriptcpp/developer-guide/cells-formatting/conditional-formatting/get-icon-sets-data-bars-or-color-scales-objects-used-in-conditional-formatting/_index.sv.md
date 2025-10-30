---
title: Hämta ikonuppsättningar, Data Bars eller färgskalobjekt som används i betingad formatering
linktitle: Hämta ikonuppsättningar, Data Bars eller färgskalobjekt som används i betingad formatering
description: Lär dig hur man använder Aspose.Cells for JavaScript via C++ för att hämta ikonuppsättningar, datastavar och färgskalobjekt i villkorsstyrd formatering från kalkylbladsfiler.
keywords: Aspose.Cells, Villkorsstyrd formatering, Ikonuppsättning, Datastav, Färgskala, Kalkylblad, JavaScript via C++
type: docs
weight: 10
url: /sv/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

Ibland behöver du hämta ikonuppsättningar som används i den betingade formateringen av en cell eller ett cellintervall och du vill skapa en bildfil baserad på den. Du kan behöva läsa databalkar eller färgskalor som används i den betingade formateringen. Aspose.Cells stöder denna funktion.

{{% /alert %}}  

Följande kodexempel visar hur man läser ikonuppsättningar som används för villkorsstyrd formatering. Med Aspose.Cells enkla API sparas ikonuppsättningens bilddata som en bild.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
