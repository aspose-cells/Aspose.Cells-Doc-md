---
title: Zeitachse rendern
type: docs
weight: 40
url: /de/javascript-cpp/rendering-timeline/
description: Verwalten Sie Zeitachsen von Excel Dateien mit Aspose.Cells for JavaScript via C++.
keywords: Zeitachse rendern ohne Office 2013, Office 2016, Office 2019 und Office 365
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells for JavaScript via C++ unterstützt die Darstellung der Zeitleistenform ohne Office 2013, Office 2016, Office 2019 und Office 365. Wenn Sie Ihr Arbeitsblatt in ein Bild umwandeln oder Ihre Arbeitsmappe in Formate wie PDF oder HTML speichern, werden die Zeitachsen ordnungsgemäß gerendert.

## **Zeitachse rendern**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](input.xlsx), die eine vorhandene Zeitleiste enthält. Erhalten Sie das Shape-Objekt entsprechend dem Namen der Zeitleiste und rendern Sie es dann mittels Shape.ToImage() in ein Bild. Das folgende Bild ist das [Ausgabebild](out.png), das die gerenderte Zeitleiste zeigt. Wie Sie sehen können, wurde die Zeitleiste richtig gerendert und sieht aus wie in der Beispiel-Excel-Datei.

![todo:image_alt_text](out.png)
### **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
