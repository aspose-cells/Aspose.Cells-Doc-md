---
title: Laden Sie ein Webbild aus einer URL in ein Excel Arbeitsblatt mit JavaScript via C++
linktitle: Ein Webbild von einer URL in ein Excel Arbeitsblatt laden
type: docs
weight: 30
url: /de/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: So konvertieren Sie ein Bild von einer URL in ein echtes Excel Bild mit Aspose.Cells for JavaScript via C++.
keywords: Excel zeigt Bild von URL, Excel URL zu Bild, Bild in Excel aus URL anzeigen, Excel Bild aus URL einfügen, URL in Bild in Excel konvertieren, Excel Bild aus URL, Bild aus URL in Excel laden, JavaScript, Excel
---

## Laden eines Bildes von einer URL in ein Excel-Arbeitsblatt

Aspose.Cells for JavaScript via C++ bietet eine einfache Möglichkeit, Bilder aus URLs in Excel-Arbeitsblätter zu laden. Dieser Artikel erklärt das Herunterladen der Bilddaten in einen Stream und deren Einfügen in das Arbeitsblatt mit der Aspose.Cells API. Mit dieser Methode werden die Bilder Bestandteil der Excel-Datei und werden nicht bei jedem Öffnen des Arbeitsblatts heruntergeladen.

## Beispielcode

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Es kann Fälle geben, in denen Sie immer das aktualisierte Bild von einer URL möchten. Um dies zu erreichen, können Sie den Anweisungen im Artikel [Beim Webadresse verknüpftes Bild einfügen](/cells/de/javascript-cpp/insert-a-linked-picture-from-web-address/) folgen. Mit dieser Methode wird das Bild jedes Mal, wenn das Arbeitsblatt geöffnet wird, von der URL geladen.
{{% /alert %}}
