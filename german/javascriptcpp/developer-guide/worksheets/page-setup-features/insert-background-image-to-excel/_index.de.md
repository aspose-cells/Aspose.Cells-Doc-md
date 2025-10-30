---
title: Hintergrundbild in Excel mit JavaScript über C++ einfügen
linktitle: Hintergrundbild in Excel einfügen
type: docs
weight: 90
url: /de/javascript-cpp/insert-background-image-to-excel/
description: "Wie man Hintergrundbild in Excel mit Aspose.Cells for JavaScript über C++ einfügt."
---

{{% alert color="primary" %}} 

Sie können ein Arbeitsblatt attraktiver gestalten, indem Sie ein Bild als Hintergrundbild hinzufügen. Diese Funktion kann sehr effektiv sein, wenn Sie eine spezielle Unternehmensgrafik haben, die einen Hauch des Hintergrunds hinzufügt, ohne die Daten auf dem Blatt zu verdecken. Sie können mithilfe der Aspose.Cells-API ein Hintergrundbild für ein Blatt festlegen.

{{% /alert %}} 

## **Blatthintergrund in Microsoft Excel festlegen**

Um ein Hintergrundbild für ein Blatt in Microsoft Excel festzulegen (z. B. Microsoft Excel 2019):

1. Wählen Sie im Menü **Seitenlayout** die Option **Seiteneinrichtung** und anschließend die Option **Hintergrund**.
1. Wählen Sie ein Bild aus, um das Hintergrundbild des Blatts festzulegen.

   **Festlegen eines Blatthintergrunds**

![todo:image_alt_text](insert-background-to-excel.jpg)

## ** Blatt-Hintergrund mit Aspose.Cells for JavaScript über C++ einstellen**

Der unten stehende Code legt ein Hintergrundbild mithilfe eines Bildes aus einem Stream fest.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## Verwandte Artikel

- [Arbeiten mit Hintergründen in ODS-Dateien](/cells/de/javascript-cpp/working-with-background-in-ods-files/)
