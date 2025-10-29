---
title: Comment utiliser la palette de couleurs
linktitle: Comment utiliser la palette de couleurs
type: docs
weight: 80
url: /fr/javascript-cpp/excel-color-palette/
description: Code JavaScript pour ajouter des couleurs personnalisées à la palette et utiliser la palette de couleurs Excel avec Aspose.Cells for JavaScript via C++.
keywords: JavaScript pour ajouter des couleurs personnalisées à la palette, programme JavaScript de palette de couleurs Excel, comment utiliser la palette de couleurs dans un classeur, JavaScript comment utiliser la palette de couleurs dans Excel
---

## **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.

Avec Aspose.Cells for JavaScript via C++, il est possible non seulement d'utiliser les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.

## **Ajouter des couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) fournit une méthode [**changePalette(Color, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchid) à la palette avant de l'appliquer sur une police.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            const isInPaletteBefore = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteBefore);
            resultDiv.innerHTML = `<p>Is Orchid in palette before change: ${isInPaletteBefore}</p>`;

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(Color.Orchid, 55);

            const isInPaletteAfter = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteAfter);
            resultDiv.innerHTML += `<p>Is Orchid in palette after change: ${isInPaletteAfter}</p>`;

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).

{{% /alert %}}
