---
title: Spécifier comment croiser la chaîne dans le PDF et l image de sortie avec JavaScript via C++
linktitle: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image
type: docs
weight: 120
url: /fr/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Apprenez à contrôler le débordement de texte dans le PDF/image de sortie en spécifiant le type de croisement en utilisant le script Aspose.Cells for Java via C++.
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais est plus large que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lors de la sauvegarde de votre fichier Excel en PDF/Image, vous pouvez contrôler ce débordement en spécifiant le type de croisement avec le [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Il a les valeurs suivantes :

- **TextCrossType.Default** : Affiche le texte comme MS Excel, dépendant de la cellule suivante. Si la cellule suivante est nulle, la chaîne débordera ou sera tronquée.

- **TextCrossType.CrossKeep** : Affiche la chaîne comme l'exportation PDF/Image de MS Excel.

- **TextCrossType.CrossOverride** : Affiche tout le texte en croisant d'autres cellules et en écrasant le texte des cellules croisées.

- **TextCrossType.StrictInCell**: Affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser une chaîne dans le PDF de sortie/une image en utilisant TextCrossType**

Le code d'exemple suivant charge le fichier Excel d'exemple et le sauvegarde au format PDF/Image en spécifiant différents [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés depuis les liens suivants :

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Code d'exemple

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
