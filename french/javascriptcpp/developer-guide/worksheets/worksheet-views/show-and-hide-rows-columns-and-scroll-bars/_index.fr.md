---
title: Afficher et masquer les lignes, colonnes et barres de défilement avec JavaScript via C++
linktitle: Afficher et masquer les lignes, colonnes et barres de défilement
type: docs
weight: 20
url: /fr/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Cet article montre comment afficher et cacher de manière programmatique les lignes et colonnes d une feuille Excel en utilisant JavaScript via C++. Contrôlez la visibilité des barres de défilement et cachez plusieurs lignes et colonnes efficacement.
---

{{% alert color="primary" %}}  
Aspose.Cells offre des moyens de contrôler la visibilité des lignes, des colonnes et des barres de défilement d'une feuille de calcul.  
{{% /alert %}}  

## **Afficher et masquer les lignes et les colonnes**  

Aspose.Cells for JavaScript via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet aux développeurs d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) qui représente toutes les cellules dans la feuille. La collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) offre plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille. Quelques-unes de ces méthodes sont expliquées ci-dessous.  

### **Afficher les lignes et les colonnes**  

Les développeurs peuvent afficher toute ligne ou colonne cachée en appelant respectivement les méthodes [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) et [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ces deux méthodes prennent deux paramètres :  

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.  
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unhide Row and Column Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.unhideRow(2, 13.5);
            worksheet.cells.unhideColumn(1, 8.5);

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

{{% alert color="primary" %}}  
Lorsqu'une colonne cachée est rendue visible, si vous devez la restaurer à la largeur précédemment attribuée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Masquer les lignes et les colonnes**  

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) et [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ces deux méthodes prennent en paramètre l'indice de la ligne ou de la colonne pour masquer la ligne ou colonne spécifique.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Hide Row/Column Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Hide the 3rd row (index 2) and 2nd column (index 1)
            worksheet.cells.hideRow(2);
            worksheet.cells.hideColumn(1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.  
{{% /alert %}}  

### **Masquer plusieurs lignes et colonnes**  

Les développeurs peuvent masquer plusieurs lignes ou colonnes simultanément en appelant respectivement les méthodes [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) et [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ces deux méthodes prennent en paramètres l'indice de la ligne ou de la colonne de début et le nombre de lignes ou colonnes à masquer.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4 and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
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

## **Afficher et masquer les barres de défilement**  

Les barres de défilement sont utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :  

- Barres de défilement verticales  
- Barres de défilement horizontales  

Microsoft Excel propose également des barres de défilement horizontales et verticales permettant aux utilisateurs de naviguer dans le contenu de la feuille de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.  

### **Contrôler la visibilité des barres de défilement**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) offre une large gamme de propriétés et méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez les propriétés [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) et [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) et [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) sont des propriétés booléennes, ce qui signifie qu'elles ne peuvent contenir que des valeurs **true** ou **false**.  

#### **Rendre les barres de défilement visibles**  

Rendez les barres de défilement visibles en définissant la propriété [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) ou [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) à **true**.  

#### **Masquer les barres de défilement**  

Masquez les barres de défilement en définissant la propriété [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) ou [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) à **false**.  

**Code d'exemple**  

Ci-dessous se trouve un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous le nom de output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Hide Scrollbars Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the vertical scroll bar of the Excel file
            workbook.settings.isVScrollBarVisible = false;

            // Hiding the horizontal scroll bar of the Excel file
            workbook.settings.isHScrollBarVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scrollbars hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
