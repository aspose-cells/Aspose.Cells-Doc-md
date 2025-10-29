---
title: Définir les formats conditionnels des fichiers Excel et ODS
linktitle: Formats conditionnels
type: docs
weight: 60
url: /fr/javascript-cpp/conditional-formatting/
description: Comment appliquer des formats conditionnels aux fichiers Excel et ODS en JavaScript via C++.
keywords: appliquer des formats conditionnels JavaScript via C++
---

## **Introduction**

Le formatage conditionnel est une fonctionnalité avancée qui permet d'appliquer des formats à une cellule ou une plage de cellules, et que ce format change en fonction de la valeur de la cellule ou d'une formule. Par exemple, une cellule n'apparaîtra en gras que lorsque sa valeur est supérieure à 500. Lorsque la condition est remplie, le format spécifié est appliqué à la cellule. Si la valeur ne correspond pas à la condition, le format par défaut de la cellule est utilisé. Dans Microsoft Excel, sélectionnez **Format**, puis **Mise en forme conditionnelle** pour ouvrir la boîte de dialogue Mise en forme conditionnelle.

Aspose.Cells prend en charge l'application de la mise en forme conditionnelle aux cellules à l'exécution. Cet article explique comment procéder. Il explique également comment calculer la couleur utilisée par Excel pour la mise en forme conditionnelle de l'échelle de couleurs.

## **Application de la mise en forme conditionnelle**

Aspose.Cells prend en charge la mise en forme conditionnelle de plusieurs manières :

- Utilisation de la feuille de calcul du concepteur
- Utilisation de la méthode de copie.
- Création de la mise en forme conditionnelle à l'exécution.

### **Utilisation de la feuille de calcul du concepteur**

Les développeurs peuvent créer une feuille de calcul du concepteur contenant une mise en forme conditionnelle dans Microsoft Excel, puis ouvrir cette feuille de calcul avec Aspose.Cells. Aspose.Cells charge et enregistre la feuille de calcul du concepteur en conservant tous les paramètres de mise en forme conditionnelle.

### **Utilisation de la méthode de copie**

Aspose.Cells permet aux développeurs de copier les paramètres de mise en forme conditionnelle d'une cellule à une autre dans la feuille de calcul en appelant la méthode [**Range.copy()**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon
            const imageData = icon.imageData;

            // Create a blob and provide download link for the image
            const blob = new Blob([imageData], { type: "image/jpeg" });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```


## **Application de la mise en forme conditionnelle à l'exécution**

Aspose.Cells vous permet d'ajouter et de supprimer la mise en forme conditionnelle à l'exécution. Les exemples de code ci-dessous montrent comment définir la mise en forme conditionnelle :

1. Instancier un classeur.
1. Ajouter une mise en forme conditionnelle vide.
1. Définir la plage à laquelle la mise en forme doit s'appliquer.
1. Définir les conditions de formatage.
1. Enregistrez le fichier.

Après cet exemple, voici un certain nombre d'autres exemples plus petits qui montrent comment appliquer les paramètres de la police, les paramètres des bordures et les motifs.

Microsoft Excel 2007 a ajouté une mise en forme conditionnelle plus avancée que Aspose.Cells supporte également. Les exemples ici illustrent comment utiliser une mise en forme simple, tandis que les exemples Excel 2007 montrent comment appliquer une mise en forme conditionnelle plus avancée.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
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
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.count;
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            let ca = AsposeCells.CellArea.createCellArea(0, 0, 0, 0);
            fcs.addArea(ca);

            ca = AsposeCells.CellArea.createCellArea(1, 1, 1, 1);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "=A2", "100");

            // Adds condition.
            const conditionIndex2 = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");

            // Sets the background color.
            const fc = fcs.get(conditionIndex);
            fc.style.backgroundColor = AsposeCells.Color.Red;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Définir la police**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get the image data from the icon
            const imageData = icon.imageData;

            // Create a Blob and provide a download link for the image
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```



{{% alert color="primary" %}}

Vous ne pouvez changer que le style de police, la couleur du texte, le style de soulignement et le style de barré.

{{% /alert %}}

### **Définir la bordure**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FormatConditionType, OperatorType, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, adds conditional formatting and offers the result for download.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(FormatConditionType.CellValue, OperatorType.Between, "50", "100");

            // Sets the borders' line style to dashed and colors
            const fc = fcs.get(conditionIndex);
            fc.style.borders.get(BorderType.LeftBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.RightBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.TopBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Dashed;

            fc.style.borders.get(BorderType.LeftBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.RightBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.TopBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.BottomBorder).color = new Color(255, 255, 0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Vous ne pouvez utiliser que des styles de ligne fins pour la bordure extérieure. Les lignes diagonales ne sont pas autorisées.

{{% /alert %}}

### **Définir le motif**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Add Conditional Formatting Example</h1>
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
            const file = fileInput.files && fileInput.files.length ? fileInput.files[0] : null;

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
            const fc = fcs.get(conditionIndex);

            // Apply style using property assignments (getter/setter conversion)
            fc.style.pattern = AsposeCells.BackgroundType.ReverseDiagonalStripe;
            fc.style.foregroundColor = new AsposeCells.Color(255, 255, 0);
            fc.style.backgroundColor = new AsposeCells.Color(0, 255, 255);

            // Save workbook to browser downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added. Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



## **Sujets avancés**  
- [Ajout de mises en forme conditionnelles à 2 couleurs et à 3 couleurs](/cells/fr/javascript-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Appliquer une mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/javascript-cpp/apply-conditional-formatting-in-worksheets/)  
- [Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle](/cells/fr/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Générer des images de barres de données pour la mise en forme conditionnelle](/cells/fr/javascript-cpp/generate-conditional-formatting-databars-images/)  
- [Obtenir des ensembles d'icônes, des barres de données ou des objets de couleurs utilisés dans la mise en forme conditionnelle](/cells/fr/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
