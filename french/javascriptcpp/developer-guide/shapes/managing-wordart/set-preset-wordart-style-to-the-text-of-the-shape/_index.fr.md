---
title: Définir un style WordArt prédéfini au texte de la forme avec JavaScript via C++
linktitle: Définir un style de WordArt prédéfini pour le texte de la forme
type: docs
weight: 280
url: /fr/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Apprenez à définir un style WordArt prédéfini au texte d une forme en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir un style WordArt prédéfini au texte de la forme en utilisant Aspose.Cells for JavaScript via C++. Veuillez utiliser [FontSetting.wordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/javascript-cpp/fontsetting/#wordArtStyle-presetwordartstyle-) ou [FontSettingCollection.wordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/javascript-cpp/fontsettingcollection/#wordArtStyle-presetwordartstyle-) à cet effet.

## **Définir un style de WordArt prédéfini pour le texte de la forme**
Le code d'exemple suivant crée une zone de texte avec du texte puis définit le style WordArt prédéfini de son texte en utilisant la méthode [FontSetting.wordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/javascript-cpp/fontsetting/#wordArtStyle-presetwordartstyle-). Voici à quoi ressemble le [fichier Excel de sortie](5115445.xlsx) dans Microsoft Excel.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Preset WordArt Style</title>
    </head>
    <body>
        <h1>Set Preset WordArt Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            // Create a new workbook (original JavaScript code created a new Workbook without reading a file)
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a textbox with some text
            const textbox = worksheet.shapes.addTextBox(0, 0, 0, 0, 100, 700);
            textbox.text = "Aspose File Format APIs";
            textbox.font.size = 44;

            // Sets preset WordArt style to the text of the shape.
            const fntSetting = textbox.richFormattings[0];
            fntSetting.wordArtStyle = AsposeCells.PresetWordArtStyle.WordArtStyle3;

            // Save the workbook in xlsx format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetPresetWordArtStyle.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with WordArt';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```
