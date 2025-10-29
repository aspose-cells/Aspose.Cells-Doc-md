---
title: Spécifier un ensemble individuel ou privé de polices pour le rendu du classeur avec JavaScript via C++
linktitle: Spécifier un ensemble individuel ou privé de polices pour le rendu de classeur
type: docs
weight: 40
url: /fr/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Apprenez comment spécifier des ensembles individuels ou privés de polices pour le rendu d’un classeur en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

En général, vous spécifiez le répertoire ou la liste de polices pour tous les classeurs, mais parfois, vous devez spécifier un ensemble individuel ou privé de polices pour vos classeurs. Aspose.Cells for JavaScript via C++ fournit la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) qui peut être utilisée pour spécifier l’ensemble individuel ou privé de polices pour votre classeur.  

## **Spécifier un ensemble de polices individuelles ou privées pour le rendu du classeur**  

Le code exemple suivant charge le [fichier Excel d'exemple](67338268.xlsx) avec son ensemble individuel ou privé de polices qui sont spécifiées à l'aide de la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs). Veuillez voir la [police d'exemple](67338271.zip) utilisée dans le code ainsi que le [PDF de sortie](67338269.pdf) généré par celui-ci. La capture d'écran suivante montre à quoi ressemble le PDF de sortie si la police est trouvée avec succès.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
