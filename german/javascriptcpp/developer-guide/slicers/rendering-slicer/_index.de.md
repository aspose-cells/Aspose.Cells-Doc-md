---
title: Slicer mit JavaScript über C++ rendern
linktitle: Slicer rendern
type: docs
weight: 40
url: /de/javascript-cpp/rendering-slicer/
---  

## **Mögliche Verwendungsszenarien**  
Die Aspose.Cells for JavaScript API über C++ unterstützt das Rendern von Slicer-Formen. Wenn Sie Ihre Arbeitsmappe in ein Bild umwandeln oder im PDF- oder HTML-Format speichern, werden die Slicer korrekt dargestellt.  

## **Slicer rendern**  
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338479.xlsx), die einen bestehenden Slicer enthält. Er wandelt das Arbeitsblatt in ein Bild um, indem er den Druckbereich festlegt, der nur den Slicer abdeckt. Das resultierende Bild ist das [Ausgabebild](67338480.png), das den gerenderten Slicer zeigt. Wie Sie sehen können, wurde der Slicer richtig gerendert und sieht genauso aus wie in der Beispiel-Excel-Datei.  

![todo:image_alt_text](rendering-slicer_1)  
## **Beispielcode**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Slicer to Image</title>
    </head>
    <body>
        <h1>Render Slicer to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Set the print area because we want to render slicer only.
            ws.pageSetup.printArea = "B15:E25";

            // Specify image or print options, set one page per sheet and only area to true.
            const imgOpts = new ImageOrPrintOptions();
            imgOpts.horizontalResolution = 200;
            imgOpts.verticalResolution = 200;
            imgOpts.imageType = ImageType.Png;
            imgOpts.onePagePerSheet = true;
            imgOpts.onlyArea = true;

            // Create sheet render object and render worksheet to image.
            const sr = new SheetRender(ws, imgOpts);

            // Render to image (first page/index 0) and prepare download link
            const imageData = sr.toImage(0);
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRenderingSlicer.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Rendered Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rendering completed successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
