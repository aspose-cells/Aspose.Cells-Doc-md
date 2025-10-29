---
title: Afficher et masquer les feuilles de calcul et les onglets avec JavaScript via C++
linktitle: Afficher et masquer des feuilles de calcul et des onglets
type: docs
weight: 10
url: /fr/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: Cet article fournit un code d exemple pour utiliser l API JavaScript ou la bibliothèque JavaScript afin d afficher et masquer de manière programmatique une feuille Excel. De plus, comment afficher et masquer les onglets du classeur Excel.
---

{{% alert color="primary" %}}
Aspose.Cells permet à l'utilisateur d'afficher et de masquer des éléments d'un classeur, y compris des feuilles de calcul et des onglets.
{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

Un fichier Excel peut avoir une ou plusieurs feuilles de calcul. Lorsque nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres données et paramètres de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Donc, **Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.

Aspose.Cells offre une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui donne accès à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre un large éventail de propriétés et de méthodes pour gérer les feuilles. Pour contrôler la visibilité d'une feuille, utilisez la propriété [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

### **Rendre une feuille de calcul visible**

Rendez une feuille visible en définissant la propriété [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) à **true**.

### **Masquer une feuille de calcul**

Masquez une feuille en définissant la propriété [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) à **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Afficher et masquer les onglets**

Si vous regardez de près le bas d'un fichier Microsoft Excel, vous verrez un certain nombre de contrôles. Ceux-ci incluent:

- Onglets de feuille.
- Boutons de défilement d'onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur un onglet pour basculer vers cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel comporte un bon nombre de feuilles de calcul, vous avez besoin de boutons pour naviguer à travers elles. Donc, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de feuille.

En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement dans les fichiers Excel.

Aspose.Cells offre une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des onglets dans un fichier Excel, les développeurs peuvent utiliser la propriété [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

### **Rendre les onglets visibles**

Rendez les onglets visibles avec la propriété [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) à **true**.

### **Masquage des onglets**

Masquez les onglets dans un fichier Excel en définissant la propriété [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) à **false**.

Voici un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous le nom de output.xls. Après l'exécution du code, vous verrez que les onglets du classeur sont masqués.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Contrôler la largeur de la barre d'onglets**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
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
