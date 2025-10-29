---
title: Générer des images de mise en forme conditionnelle DataBars
linktitle: Générer des images de mise en forme conditionnelle DataBars
description: Aspose.Cells est une bibliothèque JavaScript pour travailler avec des fichiers de feuille de calcul. Elle prend en charge la génération de barres de données conditionnellement formatées et d images, permettant aux utilisateurs de personnaliser l affichage de la feuille en fonction de la valeur des cellules. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour générer des barres de données et des images conditionnellement formatées.
keywords: Aspose.Cells, Formatage Conditionnel, Barres de Données, Images, Feuilles de Calcul, JavaScript via C++
type: docs
weight: 40
url: /fr/javascript-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de barres de données de formatage conditionnel. Vous pouvez utiliser la méthode Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) pour générer ces images. Cet article montre comment générer une image de barre de données à l'aide d'Aspose.Cells.

{{% /alert %}}

Le code exemple suivant génère l’image de la barre de données de la cellule C1. Il accède d’abord à l’objet de condition de mise en forme de la cellule, puis depuis cet objet, il accède à l’objet [**DataBar**](https://reference.aspose.com/cells/javascript-cpp/databar) et utilise sa méthode [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) pour générer l’image de la cellule. Enfin, il enregistre l’image sur le disque.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Generate DataBar Image</title>
    </head>
    <body>
        <h1>Generate DataBar Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Creating a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell which contains conditional formatting databar
            const cell = worksheet.cells.get("C1");

            // Create and get the conditional formatting of the worksheet
            const idx = worksheet.conditionalFormattings.add();
            const fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
            fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

            // Access the conditional formatting databar
            const dbar = fcc.get(0).dataBar;

            // Create image or print options
            const opts = new AsposeCells.ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Png;

            // Get the image bytes of the databar
            const imgBytes = dbar.toImage(cell, opts);

            // Create a blob and provide download link
            const blob = new Blob([imgBytes], { type: "image/png" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateDatabarImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated DataBar Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to save the PNG file.</p>';
        });
    </script>
</html>
```
