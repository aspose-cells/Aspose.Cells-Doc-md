---
title: Rendre une feuille de calcul dans un contexte graphique avec JavaScript via C++
linktitle: Rendre la feuille de calcul dans le contexte graphique
type: docs
weight: 300
url: /fr/javascript-cpp/render-worksheet-to-graphic-context/
description: Apprenez comment rendre une feuille de calcul dans un contexte graphique en utilisant Aspose.Cells for JavaScript via C++. Cela inclut le rendu vers des fichiers image, des écrans et des imprimantes.
---

{{% alert color="primary" %}}

Aspose.Cells peut maintenant rendre des feuilles de calcul en contexte graphique. Le contexte graphique peut être une image, un écran, une imprimante, etc. Veuillez utiliser l'une des deux méthodes suivantes pour rendre une feuille de calcul en contexte graphique.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

 Le code suivant illustre comment utiliser Aspose.Cells pour rendre une feuille de calcul en contexte graphique. Une fois le code exécuté, il imprimera toute la feuille, puis remplira l'espace vide restant en bleu dans le contexte graphique et enregistrera l'image sous le nom **OutputImage_out_.png**. Vous pouvez utiliser n'importe quel fichier Excel source pour essayer ce code. Veuillez également lire les commentaires à l'intérieur du code pour une meilleure compréhension.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
