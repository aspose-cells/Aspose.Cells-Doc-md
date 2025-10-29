---
title: Mettre en œuvre une taille de papier personnalisée pour la mise en page de la feuille lors du rendu avec JavaScript via C++
linktitle: Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu
type: docs
weight: 70
url: /fr/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Cet article explique comment utiliser l API JavaScript via C++ pour définir une taille de papier personnalisée pour vos feuilles souhaitées lors de l exportation d un fichier Excel en format PDF de manière programmatique.
keywords: définir une taille de papier personnalisée lors du rendu d Excel en PDF via C++ en JavaScript
---

## **Scénarios d'utilisation possibles**  

Il n’existe pas d’option directe pour créer des tailles de papier personnalisées dans MS Excel, cependant, vous pouvez définir une taille de papier personnalisée pour vos feuilles désirées lors du rendu d’un fichier Excel en PDF. Ce document explique comment définir une taille de papier personnalisée d’une feuille en utilisant les API Aspose.Cells.  

## **Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu**  

Aspose.Cells permet de mettre en œuvre la taille de papier souhaitée pour la feuille de calcul. Vous pouvez utiliser la méthode [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-) de la classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) pour spécifier une taille de page personnalisée. Le code d'exemple suivant illustre comment spécifier une taille de papier personnalisée pour la première feuille de calcul du classeur. Veuillez également consulter le [PDF de sortie](45056028.pdf) généré avec le code ci-dessous pour référence.  

## **Capture d'écran**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
