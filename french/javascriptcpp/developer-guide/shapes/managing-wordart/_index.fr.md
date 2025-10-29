---
title: Ajouter une marque d eau WordArt à la feuille de calcul avec JavaScript via C++
linktitle: Gestion de WordArt
type: docs
weight: 180
url: /fr/javascript-cpp/add-wordart-watermark-to-worksheet/
description: Apprenez comment ajouter WordArt en tant que filigrane de fond à une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Utilisez WordArt pour ajouter des effets de texte spéciaux aux feuilles de calcul. Par exemple, étirez un titre sur le dessus du fichier, décorez du texte et faites en sorte que le texte s'adapte à une forme prédéfinie, ou appliquez du texte à une feuille Excel en tant que filigrane en arrière-plan. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans les feuilles de calcul pour ajouter une décoration.

{{% /alert %}} 

L'exemple suivant montre comment ajouter une forme WordArt pour définir un filigrane en arrière-plan pour une feuille de calcul.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Ajouter un texte Word Art avec des styles intégrés](/cells/fr/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [Verrouillage du filigrane WordArt](/cells/fr/javascript-cpp/locking-wordart-watermark/)
- [Définir un style de WordArt prédéfini pour le texte de la forme](/cells/fr/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
