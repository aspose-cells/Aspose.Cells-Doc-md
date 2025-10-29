---
title: Ajouter du texte Word Art avec Styles intégrés en utilisant JavaScript via C++
linktitle: Ajouter un texte WordArt avec des styles intégrés
type: docs
weight: 270
url: /fr/javascript-cpp/add-word-art-text-with-built-in-styles/
description: Apprenez à ajouter du texte Word Art avec Styles intégrés en utilisant Aspose.Cells for JavaScript via C++. Créez du texte visuellement attrayant dans Excel en utilisant des styles intégrés.
---

## **Scénarios d'utilisation possibles**
Vous pouvez ajouter du texte Word Art avec Styles intégrés en utilisant Aspose.Cells for JavaScript via C++. Veuillez utiliser la méthode [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) à cette fin.

## **Ajouter un texte Word Art avec des styles intégrés**
Le code d'échantillon suivant ajoute des textes Word Art avec différents styles intégrés. Veuillez vérifier le [fichier Excel de sortie](5115470.xlsx) généré avec ce code. Voici à quoi ressemble le [fichier Excel de sortie](5115470.xlsx) dans Microsoft Excel.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add WordArt Example</title>
    </head>
    <body>
        <h1>Add WordArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PresetWordArtStyle } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // If no file selected, create a new workbook
                var workbook = new Workbook();
            } else {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add Word Art Text with Built-in Styles
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">WordArt added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
