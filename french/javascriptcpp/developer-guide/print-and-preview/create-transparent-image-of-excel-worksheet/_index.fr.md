---
title: Créer une image transparente de la feuille Excel avec JavaScript via C++
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /fr/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: Apprenez comment générer une image transparente d une feuille Excel en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de générer l'image de votre feuille de calcul en tant qu'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleur de remplissage. Aspose.Cells fournit la propriété [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--) pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est **fausse**, les cellules sans couleur de remplissage sont dessinées en blanc et lorsqu'elle est **true**, les cellules sans couleur de remplissage sont dessinées de manière transparente.

{{% /alert %}}

Dans l'image de la feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.

|**Sortie sans transparence : l'arrière-plan de la cellule est blanc**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Alors que dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.

|**Sortie avec transparence activée**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Le code d'exemple suivant génère une image transparente à partir d'une feuille de calcul Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Create Transparent Image Example</title>
    </head>
    <body>
        <h1>Create Transparent Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Create Transparent PNG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = wb.worksheets.get(0);

            // Apply different image or print options
            const imgOption = new ImageOrPrintOptions();
            imgOption.imageType = ImageType.Png;
            imgOption.horizontalResolution = 200;
            imgOption.verticalResolution = 200;
            imgOption.onePagePerSheet = true;

            // Apply transparency to the output image
            imgOption.transparent = true;

            // Create image after applying image or print options
            const sr = new SheetRender(sheet, imgOption);
            const outputData = await sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateTransparentImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image created successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
