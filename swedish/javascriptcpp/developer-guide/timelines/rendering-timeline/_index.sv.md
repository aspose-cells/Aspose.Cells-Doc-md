---
title: Rendering tidslinje
type: docs
weight: 40
url: /sv/javascript-cpp/rendering-timeline/
description: Hantera tidslinjer för Excel filer med Aspose.Cells for JavaScript via C++.
keywords: Rendering tidslinje utan office 2013, office 2016, office 2019 och office 365
---

## **Möjliga användningsscenario**
Aspose.Cells for JavaScript via C++ stöder rendering av tidslinjeform utan att använda Office 2013, Office 2016, Office 2019 och Office 365. Om du konverterar ditt kalkylblad till en bild eller sparar arbetsboken i PDF- eller HTML-format, kommer du att se att tidslinjer renderas korrekt.

## **Rendering Tidslinje**
Följande exempelkod laddar [exempelfil](input.xlsx) som innehåller en befintlig tidslinje. Hämta formobjektet enligt tidslinjens namn och rendera det sedan till en bild via Shape.ToImage()-metoden. Följande bild är [utdatabilden](out.png) som visar den renderade tidslinjen. Som du ser har tidslinjen renderats korrekt och ser likadan ut som i exempel-Excel-filen.

![todo:image_alt_text](out.png)
### **Exempelkod**
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
