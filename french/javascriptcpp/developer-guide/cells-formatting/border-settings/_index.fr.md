---
title: Paramètres de bordure
linktitle: Paramètres de bordure
description: Comment utiliser la bibliothèque Aspose.Cells en JavaScript via C++ pour définir le style et la couleur de la bordure des cellules. En ajustant la largeur, le style et la couleur de la bordure, vous avez plus de contrôle sur l apparence et l aspect des cellules.
keywords: Aspose.Cells, Paramètres de bordure de cellule, JavaScript via C++, Largeur de la bordure, Style de la bordure, Couleur de la bordure
type: docs
weight: 40
url: /fr/javascript-cpp/cells-border-settings/
---

## **Ajout de bordures aux cellules**

Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures. Le type de bordure dépend de l'endroit où elle est ajoutée. Par exemple, une bordure supérieure est celle ajoutée en haut d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells for JavaScript via C++, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible que dans Microsoft Excel.

### **Ajout de bordures aux cellules**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Chaque élément dans la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells fournit la propriété [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) dans la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). La propriété [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) est utilisée pour définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) offre des propriétés pour ajouter des bordures aux cellules.

#### **Ajout de bordures à une cellule**

Les développeurs peuvent ajouter des bordures à une cellule en utilisant la collection [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Le type de bordure est passé comme un index à la collection [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--). Tous les types de bordures sont prédéfinis dans l'énumération [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).

**Énumération de bordure**

|**Types de bordures**|**Description**|
| :- | :- |
|BottomBorder|Une ligne de bordure inférieure|
|DiagonalDown|Une ligne diagonale de haut gauche à bas droite|
|DiagonalUp|Une ligne diagonale de bas gauche à haut droit|
|LeftBorder|Une ligne de bordure gauche|
|RightBorder|Une ligne de bordure droite|
|TopBorder|Une ligne de bordure supérieure|

La collection [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) stocke toutes les bordures. Chaque bordure dans la collection [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) est représentée par un objet [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) qui fournit deux propriétés, [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) et [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) pour définir respectivement la couleur et le style de la ligne d'une bordure.

Pour définir la couleur de ligne d'une bordure, sélectionnez une couleur en utilisant l'énumération Color (faisant partie de JavaScript) et assignez-la à la propriété color de l'objet Border.

Le style de ligne de la bordure est défini en sélectionnant un style de ligne dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).

**Énumération de Type de Bordure Cellulaire**

|**Styles de ligne**|**Description**|
| :- | :- |
|DashDot|Ligne pointillée fine|
|DashDotDot|Ligne pointillée fine avec point|
|Dashed|Ligne en tirets|
|Dotted|Ligne en pointillés|
|Double|Ligne double|
|Hair|Ligne fine|
|MediumDashDot|Ligne mixte pointillée|
|MediumDashDotDot|Ligne mixte pointillée-traitée|
|MediumDashed|Ligne en pointillés moyens|
|None|Aucune ligne|
|Medium|Ligne moyenne|
|SlantedDashDot|Ligne mixte pointillée inclinée moyenne|
|Thick|Ligne épaisse|
|Thin|Ligne fine|
Sélectionnez l'un des styles de ligne, puis assignez-le à la propriété [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) de l'objet [**Border**](https://reference.aspose.com/cells/javascript-cpp/border).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Vous devez définir à la fois le style de ligne et la couleur en même temps. Les deux lignes diagonales de la bordure doivent avoir le même style de ligne et la même couleur.
{{% /alert %}}

#### **Ajout de bordures à une plage de cellules**

Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, créez d'abord une plage de cellules en appelant la méthode [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Elle prend les paramètres suivants :

- Première ligne, la première ligne de la plage.
- Première colonne, represente la première colonne de la plage.
- Nombre de lignes, le nombre de lignes dans la plage.
- Nombre de colonnes, le nombre de colonnes dans la plage.

La méthode [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) renvoie un objet [**Range**](https://reference.aspose.com/cells/javascript-cpp/range), qui contient la plage de cellules spécifiée. L'objet [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) fournit une méthode [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) qui accepte les paramètres suivants pour ajouter une bordure à cette plage de cellules :

- **Type de Bordure**, le type de bordure, sélectionné dans l'énumération [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).
- **Style de Ligne**, le style de ligne de la bordure, sélectionné dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).
- **Couleur**, la couleur de la ligne, sélectionnée dans l'énumération Color.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
