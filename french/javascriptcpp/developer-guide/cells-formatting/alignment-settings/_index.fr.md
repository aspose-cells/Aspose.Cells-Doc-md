---
title: Paramètres d alignement
linktitle: Paramètres d alignement
description: Dans la bibliothèque Aspose.Cells, vous pouvez utiliser les paramètres d alignement des cellules pour ajuster la disposition et l affichage du texte en JavaScript via C++. Ce document fournit des étapes détaillées et un code exemple pour utiliser Aspose.Cells pour les paramètres d alignement des cellules.
keywords: Aspose.Cells, alignement des cellules, alignement horizontal, alignement vertical, retour à la ligne du texte JavaScript via C++
type: docs
weight: 20
url: /fr/javascript-cpp/cells-alignment-settings/
---

## **Configuration des paramètres d'alignement**

### **Paramètres d'alignement dans Microsoft Excel**

Toute personne ayant utilisé Microsoft Excel pour formater des cellules sera familière avec les paramètres d'alignement dans Microsoft Excel.

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- Alignement du texte (horizontal et vertical)
- Retrait.
- Orientation.
- Contrôle du texte.
- Direction du texte.

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.

### **Paramètres d'alignement dans Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Chaque élément de cette collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells fournit les méthodes [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) et [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) pour la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) qui permettent de récupérer et de définir le formatage d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) offre des propriétés utiles pour configurer les réglages d'alignement.

Sélectionnez n'importe quel type d'alignement du texte en utilisant l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype). Les types d'alignement de texte prédéfinis dans l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype) sont :

|**Types d'alignement de texte**|**Description**|
| :- | :- |
|Bottom|Représente un alignement de texte en bas|
|Center|Représente un alignement de texte au centre|
|CenterAcross|Représente un alignement de texte centré sur plusieurs cellules|
|Distributed|Représente un alignement de texte distribué|
|Fill|Représente un alignement de texte en remplissage|
|General|Représente un alignement de texte général|
|Justify|Représente un alignement de texte justifié|
|Left|Représente un alignement de texte à gauche|
|Right|Représente un alignement de texte à droite|
|Top|Représente un alignement de texte en haut|
|JustifiedLow|Aligne le texte avec une longueur de kashida ajustée pour le texte arabe.|
|ThaiDistributed|Distribue le texte thaïlandais en particulier, car chaque caractère est traité comme un mot.|

{{% alert color="primary" %}}

Vous pouvez également appliquer le réglage de distribution justifiée à l'aide de la méthode [**Style.isJustifyDistributed(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isJustifyDistributed-boolean-).

{{% /alert %}}

#### **Alignement horizontal**

Utilisez la méthode [**horizontalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#horizontalAlignment-textalignmenttype-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) pour aligner le texte horizontalement.

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
            const fileInput = document.getElementById('fileInput');

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Visit Aspose!");

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
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



#### **Alignement vertical**

De même que pour l'alignement horizontal, utilisez la méthode [**verticalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#verticalAlignment-textalignmenttype-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) pour aligner le texte verticalement.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Clearing all the worksheets
            workbook.worksheets.clear();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal/vertical alignment of the text in the "A1" cell via style
            const style = cell.style;
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


#### **Indentation**

Il est possible de définir le niveau d'indentation du texte dans une cellule avec la méthode [**indentLevel**](https://reference.aspose.com/cells/javascript-cpp/style/#indentLevel-number-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Set Cell Indent Level Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            cell.value = "Visit Aspose!";

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;

            // Setting the indentation level of the text (inside the cell) to 2
            style.indentLevel = 2;

            cell.style = style;

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
    </body>
</html>
```



#### **Orientation**

Définissez l'orientation (rotation) du texte dans une cellule avec la méthode [**rotationAngle**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Modify Cell</h1>
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
            // This example creates a new workbook, updates A1, sets rotation, and saves the file.
            const fileInput = document.getElementById('fileInput');

            // Instantiate a new Workbook (blank)
            const workbook = new Workbook();

            // Obtain reference to the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Setting the rotation of the text (inside the cell) to 25
            style.rotationAngle = 25;

            // Assign the modified style back to the cell
            cell.style = style;

            // Save the Excel file in Excel 97-2003 format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Contrôle du texte**

La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.

##### **Retour à la ligne du texte**

Le retour à la ligne du texte dans une cellule facilite sa lecture : la hauteur de la cellule s'ajuste pour contenir tout le texte, au lieu de le couper ou de déborder dans les cellules adjacentes. Activez ou désactivez le retour à la ligne avec la méthode [**isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = workbook.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 36;

            // Add Text to the First Cell
            const cellRef = cells.checkCell(0, 0);
            cellRef.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = cellRef.style;
            style.isTextWrapped = true;
            cellRef.style = style;

            // Save Excel File
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Rétrécissement pour s'adapter**

Une option pour le retour à la ligne dans un champ est de réduire la taille du texte pour qu'il s'adapte aux dimensions de la cellule. Cela se fait en réglant la méthode [**shrinkToFit(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#shrinkToFit-boolean-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) sur **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Cell Style Example</title>
    </head>
    <body>
        <h1>Set Cell Style Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.shrinkToFit = true;

            // Applying the style back to the cell
            cell.style = style;

            // Saving the Excel file in Excel97To2003 format
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


##### **Fusion de cellules**

Comme Microsoft Excel, Aspose.Cells supporte la fusion de plusieurs cellules en une seule. Aspose.Cells offre deux approches pour cette tâche. L'une consiste à appeler la méthode [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). La méthode [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) prend les paramètres suivants pour fusionner les cellules :

- Première rangée : la première rangée à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de rangées : le nombre de rangées à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Cells and Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook.
            const wbk = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Save the Workbook.
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


L'autre méthode consiste à d'abord appeler la méthode [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) pour créer une plage de cellules à fusionner. La méthode [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) prend le même ensemble de paramètres que celle de la méthode [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) évoquée ci-dessus et retourne un objet [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). L'objet [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) offre également une méthode [**merge**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) qui fusionne la plage spécifiée dans l'objet [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).

##### **Direction du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété [**textDirection**](https://reference.aspose.com/cells/javascript-cpp/style/#textDirection-textdirectiontype-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération [**TextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/textdirectiontype).

|**Types de direction du texte**|**Description**|
| :- | :- |
|Context|L'ordre de lecture en accord avec la langue du premier caractère saisi|
|LeftToRight|Ordre de lecture de gauche à droite|
|RightToLeft|Ordre de lecture de droite à gauche|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify A1 and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextDirectionType } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "I am using the latest version of Aspose.Cells to test this functionality.";

            // Gets style in the "A1" cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.textDirection = TextDirectionType.LeftToRight;

            // Apply the style back to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Sujets avancés**
- [Modifier l'alignement des cellules et conserver la mise en forme existante](/cells/fr/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/javascript-cpp/line-breaks-and-text-wrapping/)
