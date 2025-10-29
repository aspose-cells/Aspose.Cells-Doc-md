---
title: Paramètres de remplissage
linktitle: Paramètres de remplissage
description: Découvrez comment personnaliser les réglages de remplissage, l arrière plan et le style des cellules à l aide de la bibliothèque Aspose.Cells pour JavaScript via C++.
keywords: Aspose.Cells, Cellules, Paramètres de remplissage, Arrière plan, Style, JavaScript via C++
type: docs
weight: 50
url: /fr/javascript-cpp/cells-fill-settings/
---

## **Couleurs et motifs d'arrière-plan**

Microsoft Excel peut définir les couleurs avant-plan (contour) et arrière-plan (remplissage) des cellules et les motifs d'arrière-plan.

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans ce sujet, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.

### **Définition de couleurs et motifs d'arrière-plan**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) possède la propriété [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) utilisée pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) offre des propriétés pour définir les couleurs de premier plan et d'arrière-plan des cellules. Aspose.Cells fournit une énumération [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) qui contient un ensemble de types de motifs d'arrière-plan prédéfinis, listés ci-dessous.

|**Motifs d'arrière-plan**|**Description**|
| :- | :- |
|DiagonalCrosshatch|Représente le motif de quadrillage en diagonale|
|DiagonalStripe|Représente un motif de rayures diagonales|
|Gray6|Représente un motif de gris à 6,25%|
|Gray12|Représente un motif de gris à 12,5%|
|Gray25|Représente un motif de gris à 25%|
|Gray50|Représente un motif de gris à 50%|
|Gray75|Représente un motif de gris à 75%|
|HorizontalStripe|Représente un motif de rayures horizontales|
|None|Représente pas d'arrière-plan|
|ReverseDiagonalStripe|Représente un motif de rayures inversées diagonales|
|Solid|Représente un motif solide|
|ThickDiagonalCrosshatch|Représente un motif de quadrillage diagonal épais|
|ThinDiagonalCrosshatch|Représente un motif de quadrillage diagonal fin|
|ThinDiagonalStripe|Représente un motif de rayures diagonales fines|
|ThinHorizontalCrosshatch|Représente un motif de quadrillage horizontal fin|
|ThinHorizontalStripe|Représente un motif de rayures horizontales fines|
|ThinReverseDiagonalStripe|Représente un motif de rayures inversées diagonales fines|
|ThinVerticalStripe|Représente un motif de rayures verticales fines|
|VerticalStripe|Représente un motif de rayures verticales|

Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configurée pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan de rayures verticales.|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **Important à savoir**

{{% alert color="primary" %}}

- Pour définir la couleur de premier plan ou d'arrière-plan d'une cellule, utilisez les propriétés [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) ou [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Les deux ne prendront effet que si la propriété [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) est configurée.
- La propriété [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) définit la couleur d'ombrage de la cellule. La propriété [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) spécifie le type de motif d'arrière-plan utilisé pour la couleur de premier plan ou d'arrière-plan. Aspose.Cells fournit une énumération, [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), qui contient un ensemble de types de motifs d'arrière-plan prédéfinis.
- Si vous sélectionnez la valeur *BackgroundType.None* dans l'énumération [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), la couleur de premier plan n'est pas appliquée. De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez les valeurs *BackgroundType.None* ou *BackgroundType.Solid*.
- Lors de la récupération de la couleur d'ombrage/remplissage d'une cellule, si [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) est *BackgroundType.None*, [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) renverra *Color.Empty*.

{{% /alert %}}

### **Application d'effets de remplissage dégradé**

Pour appliquer vos effets de remplissage en dégradé souhaités à la cellule, utilisez la propriété [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) en conséquence.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.

Avec Aspose.Cells, il est possible non seulement d'utiliser les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.

### **Ajout de couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) fournit une méthode [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :

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
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

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
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).

{{% /alert %}}
