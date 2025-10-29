---
title: Rendu de segment avec JavaScript via C++
linktitle: Rendu de la trancheuse
type: docs
weight: 40
url: /fr/javascript-cpp/rendering-slicer/
---  

## **Scénarios d'utilisation possibles**  
Aspose.Cells for JavaScript via C++ supporte le rendu des formes de segment. Si vous convertissez votre feuille de calcul en image ou enregistrez votre classeur au format PDF ou HTML, vous verrez que les segments sont rendus correctement.  

## **Rendu du tronçonneur**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338479.xlsx) contenant un segment existant. Il convertit la feuille de calcul en une image en définissant la zone d'impression qui ne couvre que le segment. L'image résultante est [l'image de sortie](67338480.png) montrant le segment rendu. Comme vous pouvez le voir, le segment a été rendu correctement et ressemble à celui du fichier Excel d'exemple.  

![todo:image_alt_text](rendering-slicer_1)  
## **Code d'exemple**  
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
