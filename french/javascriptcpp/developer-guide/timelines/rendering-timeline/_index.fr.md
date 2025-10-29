---
title: Rendu de la chronologie
type: docs
weight: 40
url: /fr/javascript-cpp/rendering-timeline/
description: Gérer les chronologies de fichiers Excel avec Aspose.Cells for JavaScript via C++.
keywords: Rendu de la chronologie sans Office 2013, Office 2016, Office 2019 et Office 365
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for JavaScript via C++ supporte le rendu de la forme de la chronologie sans utiliser Office 2013, Office 2016, Office 2019 et Office 365. Si vous convertissez votre feuille de calcul en image ou si vous enregistrez votre classeur en formats PDF ou HTML, vous verrez que les chronologies sont rendues correctement.

## **Rendu de la chronologie**
Le code d'exemple suivant charge le [fichier Excel d'exemple](input.xlsx) contenant une chronologie existante. Obtenez l'objet forme selon le nom de la chronologie, puis la rendre en une image via la méthode Shape.ToImage(). L'image suivante est le [contenu de sortie](out.png) montrant la chronologie rendue. Comme vous pouvez le voir, la chronologie a été rendue correctement et ressemble à celle du fichier Excel d'origine.

![todo:image_alt_text](out.png)
### **Code d'exemple**
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
