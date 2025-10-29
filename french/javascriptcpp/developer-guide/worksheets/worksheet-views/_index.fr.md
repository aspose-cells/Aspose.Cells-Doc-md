---
title: Vues de la feuille de calcul avec JavaScript via C++
linktitle: Vues de la feuille de calcul
type: docs
weight: 40
url: /fr/javascript-cpp/worksheet-views/
description: Cet article décrira comment utiliser JavaScript et l API JavaScript pour interagir avec l aperçu des sauts de page d un classeur Excel et des feuilles de calcul. Travailler avec les volets scindés, les volets figés et le facteur de zoom également.
---

## **Aperçu des sauts de page**

Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue de modification qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre quelles données iront sur chaque page pour que vous puissiez ajuster la zone d'impression et les sauts de page. En utilisant Aspose.Cells for JavaScript via C++, les développeurs peuvent activer la vue normale ou le mode aperçu des sauts de page.

### **Contrôle des modes d'affichage**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'affichage normal ou d'aperçu de saut de page, utilisez la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Activation de la vue normale**

Définissez une feuille de calcul en affichage normal en définissant la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sur **false**.

#### **Activation de l'aperçu des sauts de page**

Définissez n'importe quelle feuille de calcul en aperçu de saut de page en définissant la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sur **true**. Ce faisant, la feuille de calcul passe de l'affichage normal à l'aperçu de saut de page.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) pour activer le mode d'aperçu de saut de page pour la première feuille de calcul d'un fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). La vue est basculée en aperçu de saut de page pour la première feuille de calcul en définissant la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) sur **true**. Le fichier modifié est enregistré sous le nom output.xls.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Facteur de zoom**

### **Utilisation de Microsoft Excel**

Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

### **Aspose.Cells & Facteur de zoom**

Aspose.Cells permet aux développeurs de définir le facteur de zoom de la feuille de calcul.
Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la propriété [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Le facteur de zoom est défini en attribuant une valeur numérique (entier) à la propriété [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--).

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) pour définir le facteur de zoom de la première feuille du fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Le facteur de zoom de la première feuille de calcul est défini à 75 et le fichier modifié est enregistré sous le nom de output.xls.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Figer les volets**

### **Utilisation de Microsoft Excel**

Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.

### **Aspose.Cells & Les Volets Figés**

Aspose.Cells permet aux développeurs d'appliquer des volets figés sur des feuilles de calcul à l'exécution.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer des volets gelés, appelez la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) de la classe Worksheet. La méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) prend les paramètres suivants :

- **Ligne**, l'index de la ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de la colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche.

Le fichier book1.xls est ouvert en appelant le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) lors de son instanciation et quelques lignes et colonnes sont figées dans la première feuille de calcul. Le fichier modifié est enregistré sous le nom de output.xls.

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4e ligne et la 3e colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Diviser les volets**

Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.

### **Application et Suppression des Volets Divisés**

#### **Division des Volets**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour implémenter des vues divisées, utilisez la méthode [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) de la classe [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--). Pour supprimer les volets divisés, utilisez la méthode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Après l'exécution du code ci-dessus, le fichier généré aura une vue fractionnée.

#### **Suppression de volets**

Supprimer les volets fractionnés en utilisant la méthode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Masquer l'affichage des valeurs nulles dans la feuille de calcul](/cells/fr/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur d'onglet de feuille de calcul](/cells/fr/javascript-cpp/set-worksheet-tab-color/)
- [Afficher et masquer les quadrillages, les en-têtes de lignes et de colonnes](/cells/fr/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Afficher et masquer les lignes, les colonnes et les barres de défilement](/cells/fr/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Afficher et masquer les feuilles de calcul et les onglets](/cells/fr/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [Afficher les formules au lieu des valeurs dans une feuille de calcul](/cells/fr/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/javascript-cpp/use-error-checking-options/)
