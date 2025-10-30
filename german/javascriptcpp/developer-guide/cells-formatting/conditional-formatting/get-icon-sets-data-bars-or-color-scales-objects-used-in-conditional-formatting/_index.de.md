---
title: Rufen Sie Icons Sets, Datenleisten oder Farbskalen Objekte, die in der bedingten Formatierung verwendet werden, ab
linktitle: Rufen Sie Icons Sets, Datenleisten oder Farbskalen Objekte, die in der bedingten Formatierung verwendet werden, ab
description: Lernen Sie, wie man Aspose.Cells for JavaScript über C++ verwendet, um Symbolsets, Datenbalken und Farbskalen Objekte aus bedingter Formatierung von Tabellenkalkulationsdateien abzurufen.
keywords: Aspose.Cells, Bedingte Formatierung, Symbolset, Datenbalken, Farbskala, Tabellenkalkulation, JavaScript über C++
type: docs
weight: 10
url: /de/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

Manchmal müssen Icons Sets abgerufen werden, die für die bedingte Formatierung einer Zelle oder eines Zellbereichs verwendet werden, und Sie möchten auf ihrer Grundlage eine Bilddatei erstellen. Möglicherweise müssen Sie die Datenleisten oder Farbskalen, die in der bedingten Formatierung verwendet werden, lesen. Aspose.Cells unterstützt diese Funktion.

{{% /alert %}}  

Das folgende Codebeispiel zeigt, wie man Icon-Sets liest, die für die bedingte Formatierung verwendet werden. Mit der einfachen API von Aspose.Cells wird die Bilddaten des Icon-Sets als Bild gespeichert.

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
