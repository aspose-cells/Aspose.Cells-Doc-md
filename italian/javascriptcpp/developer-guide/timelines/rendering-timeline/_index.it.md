---
title: Rappresentazione della Timeline
type: docs
weight: 40
url: /it/javascript-cpp/rendering-timeline/
description: Gestisci le timeline dei file Excel con Aspose.Cells for JavaScript tramite C++.
keywords: Rappresentazione della timeline senza office 2013, office 2016, office 2019 e office 365
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for JavaScript tramite C++ supporta il rendering della forma della timeline senza utilizzare Office 2013, Office 2016, Office 2019 e Office 365. Se converti il foglio di lavoro in immagine o salvi il file in formato PDF o HTML, vedrai che le timeline vengono renderizzate correttamente.

## **Rappresentazione della Timeline**
Il seguente esempio di codice carica il [file Excel di esempio](input.xlsx) che contiene una timeline esistente. Ottieni l'oggetto forma in base al nome della timeline, quindi rendilo sotto forma di immagine tramite il metodo Shape.ToImage(). La seguente immagine è l'[immagine di output](out.png) che mostra la timeline renderizzata. Come puoi vedere, la timeline è stata renderizzata correttamente e appare uguale a quella nel file Excel di esempio.

![todo:image_alt_text](out.png)
### **Codice di Esempio**
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
