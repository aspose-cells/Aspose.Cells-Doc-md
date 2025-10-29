---
title: Formater les cellules avec JavaScript via C++
description: Apprenez à formater et styliser les cellules dans Aspose.Cells for JavaScript via C++, y compris le formatage des nombres, la mise en forme de la date, les styles de police et d autres options de style de cellule. Notre guide vous aidera à créer des feuilles de calcul attractives et professionnelles.
keywords: Aspose.Cells for JavaScript via C++, formatage des cellules, stylisation, formatage des nombres, formatage de la date, style de police, options de style de cellule, feuille de calcul, créer, aspect professionnel, formater les lignes et les colonnes.
linktitle: Formater les cellules
type: docs
weight: 120
url: /fr/javascript-cpp/cells-formatting/
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells fournit les méthodes [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) et [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) de la classe [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), utilisées pour obtenir/modifier le style de formatage d'une cellule. Aspose.Cells fournit également une classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

{{% /alert %}}

## **Comment formater les cellules en utilisant les méthodes de style**

Appliquer différents types de styles de formatage sur les cellules pour définir des couleurs de fond ou de premier plan, des bordures, des polices, des alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.

### **Comment utiliser les méthodes de style**

Si les développeurs doivent appliquer différents styles de mise en forme à différentes cellules, il est préférable d'obtenir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) de la cellule en utilisant la méthode [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--), de spécifier les attributs de style et ensuite d'appliquer la mise en forme avec la méthode [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-). Un exemple est donné ci-dessous pour illustrer cette approche d'application de divers styles à une cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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
            const fileInput = document.getElementById('fileInput');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Comment utiliser l'objet de style pour formater différentes cellules**

Si les développeurs doivent appliquer le même style de mise en forme à différentes cellules, ils peuvent utiliser l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Veuillez suivre les étapes ci-dessous pour utiliser l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style):

1. Ajoutez un objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) en appelant la méthode [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)
2. Accédez à l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) récemment ajouté
3. Définissez les propriétés/attributs souhaités de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) pour appliquer les paramètres de formatage souhaités
4. Assignez l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) configuré à vos cellules souhaitées

Cette approche peut grandement améliorer l'efficacité de vos applications et économiser de la mémoire également.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
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

### **Comment utiliser les styles prédéfinis de Microsoft Excel 2007**

Si vous avez besoin d'appliquer différents styles de formatage pour Microsoft Excel 2007, appliquez les styles en utilisant l'API Aspose.Cells. Un exemple est donné ci-dessous pour illustrer cette approche d'application d'un style prédéfini sur une cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Comment formater des caractères sélectionnés dans une cellule**

La gestion des paramètres de police explique comment formater du texte dans les cellules, mais cela explique seulement comment formater tout le contenu de la cellule. Et si vous voulez formater uniquement des caractères sélectionnés ?

Aspose.Cells prend également en charge cette fonctionnalité. Ce sujet explique comment utiliser cette fonctionnalité efficacement.

### **Comment formater des caractères sélectionnés**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient la collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Chaque élément dans la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) fournit la méthode [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) qui prend les paramètres suivants pour sélectionner une plage de caractères à l'intérieur d'une cellule :

- **Index de début**, l'index du caractère à partir duquel la sélection commence.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

La méthode [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) retourne une instance de la classe [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) qui permet aux développeurs de formater les caractères de la même manière qu'une cellule, comme illustré ci-dessous dans l'exemple de code. Dans le fichier de sortie, dans la cellule A1, le mot 'Visit' sera formaté avec la police par défaut, mais 'Aspose!' sera en gras et en bleu.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
            const fileInput = document.getElementById('fileInput');

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si vous souhaitez formater une partie du texte enrichi dans une cellule, envisagez d'utiliser les méthodes [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) & [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). La méthode [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) est utilisée pour accéder aux parties du texte, puis des modifications peuvent être apportées à l'aide de la méthode [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-), tandis que la méthode **Get** retourne un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, le gras, etc. La méthode **Set** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Comment formater les lignes et les colonnes**

Parfois, les développeurs doivent appliquer le même formatage sur des lignes ou des colonnes. Appliquer le formatage sur chaque cellule prend souvent plus de temps et n'est pas une bonne solution.
Pour résoudre ce problème, Aspose.Cells offre une solution simple et rapide qui est discutée en détail dans cet article.

### **Mise en forme des lignes & colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). La collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) offre une collection [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--).

### **Comment formater une ligne**

Chaque élément de la collection [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) représente un objet [**Row**](https://reference.aspose.com/cells/javascript-cpp/row). L'objet [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) offre la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) utilisée pour définir la mise en forme de la ligne. Pour appliquer la même mise en forme à une ligne, utilisez l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Les étapes ci-dessous montrent comment l'utiliser.

1. Ajoutez un objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) à la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) en appelant sa méthode [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--).
2. Définissez les propriétés de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) pour appliquer les paramètres de mise en forme.
3. Activez les attributs pertinents pour l'objet [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).
4. Assignez l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) configuré à l'objet [**Row**](https://reference.aspose.com/cells/javascript-cpp/row).

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

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Comment formater une colonne**

La collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) offre également une collection [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--). Chaque élément dans la collection [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) représente un objet [**Column**](https://reference.aspose.com/cells/javascript-cpp/column). Semblable à un objet [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), l'objet [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) offre également la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) pour formater une colonne.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/javascript-cpp/cells-alignment-settings/)
- [Paramètres de bordure](/cells/fr/javascript-cpp/cells-border-settings/)
- [Définir les formats conditionnels des fichiers Excel et ODS.](/cells/fr/javascript-cpp/conditional-formatting/)
- [Thèmes et couleurs d'Excel](/cells/fr/javascript-cpp/excel-themes-and-colors/)
- [Paramètres de remplissage](/cells/fr/javascript-cpp/cells-fill-settings/)
- [Paramètres de police](/cells/fr/javascript-cpp/cells-font-settings/)
- [Formater les cellules de feuille de calcul dans un classeur](/cells/fr/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [Mise en œuvre du système de date 1904](/cells/fr/javascript-cpp/implement-1904-date-system/)
- [Fusionner et scinder des cellules](/cells/fr/javascript-cpp/merging-and-unmerging-cells/)
- [Paramètres de nombre](/cells/fr/javascript-cpp/cells-number-settings/)
- [Obtenir et définir le style des cellules](/cells/fr/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
