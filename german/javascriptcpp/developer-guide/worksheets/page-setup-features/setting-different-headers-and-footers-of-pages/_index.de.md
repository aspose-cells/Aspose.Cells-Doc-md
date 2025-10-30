---
title: Verschiedene Kopf und Fußzeilen für unterschiedliche Seiten mit JavaScript über C++ einstellen
linktitle: Setzen von verschiedenen Kopf und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Dieser Artikel bietet Beispielcode, der zeigt, wie man die Kopf und Fußzeilen des Excel Arbeitsblatt Page Setups programmatisch mit Aspose.Cells for JavaScript über C++ festlegt. Kopf und Fußzeilen für erste, ungerade und gerade Seiten einstellen.
keywords: Kopf und Fußzeile im Excel auf der ersten Seite mit JavaScript über C++ einstellen, Kopf und Fußzeile ungerader Seiten mit JavaScript über C++ einstellen, Kopf und Fußzeile gerader Seiten mit JavaScript über C++ einstellen
---

{{% alert color="primary" %}}

MS Excel unterstützt das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten seit Excel 2007.
 Aspose.Cells for JavaScript über C++ unterstützt dieselbe Funktion.

{{% /alert %}}

## **Setzen verschiedener Kopf- und Fußzeilen in MS Excel**

**![Setzen verschiedener Kopf- und Fußzeilen](difpage.png)**

1. Klicken Sie auf **Seitenlayout > Drucktitel > Kopf-/Fußzeile**.
1. Überprüfen Sie **Unterschiedliche ungerade und gerade Seiten** oder **Unterschiedliche erste Seite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## ** Verschiedene Kopf- und Fußzeilen mit Aspose.Cells for JavaScript über C++ einstellen**

Aspose.Cells verhält sich genauso wie Excel.
Setzt die Flags [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) und [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
