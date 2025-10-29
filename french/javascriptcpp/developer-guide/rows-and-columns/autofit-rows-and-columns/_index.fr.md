---
title: Ajuster automatiquement la hauteur des lignes et la largeur des colonnes avec JavaScript via C++
linktitle: Ajuster automatiquement les lignes et les colonnes
type: docs
weight: 20
url: /fr/javascript-cpp/autofit-rows-and-columns/
description: Cet article montre comment ajuster automatiquement la hauteur des lignes, la largeur des colonnes, les lignes de cellules fusionnées et une ligne dans une plage de cellules en utilisant Aspose.Cells for JavaScript via C++.
keywords: Ajustement automatique des lignes JavaScript via C++, ajustement automatique des colonnes JavaScript via C++, ajustement automatique d une ligne dans une plage de cellules JavaScript via C++, ajustement automatique des lignes de cellules fusionnées JavaScript via C++
---

{{% alert color="primary" %}}  
Microsoft Excel permet aux utilisateurs de redimensionner automatiquement la largeur et la hauteur des cellules en fonction de leur contenu. Cette fonctionnalité est également disponible via Aspose.Cells for JavaScript via C++, afin que les développeurs puissent ajuster automatiquement les dimensions d'une cellule à l'exécution.  
{{% /alert %}}  

## **Ajustement automatique**  

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) permettant d’accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article présente l’utilisation de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) pour ajuster automatiquement la taille des lignes ou des colonnes.  

### **Ajuster automatiquement la ligne - Simple**  

L'approche la plus simple pour ajuster automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La méthode [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-) prend un indice de ligne (de la ligne à redimensionner) en paramètre.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Comment ajuster automatiquement une ligne dans une plage de cellules**  

Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'automatiser le réglage de la hauteur d'une ligne en fonction du contenu dans une plage de cellules de cette ligne, en appelant une version surchargée de la méthode [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-). Elle accepte les paramètres suivants :  

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.  
- **Index de la première colonne**, l'index de la première colonne de la ligne.  
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.  

La méthode [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-) vérifie le contenu de toutes les colonnes de la ligne puis ajuste automatiquement la hauteur de la ligne.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Comment ajuster automatiquement une colonne dans une plage de cellules**  

Une colonne est composée de plusieurs lignes. Il est possible d’ajuster automatiquement une colonne en fonction du contenu d’une plage de cellules dans cette colonne en appelant une version surchargée de la méthode [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) qui prend les paramètres suivants :  

- **Index de la colonne**, l'index de la colonne à ajuster automatiquement.  
- **Index de la première ligne**, l'index de la première ligne de la colonne.  
- **Index de la dernière ligne**, l'index de la dernière ligne de la colonne.  

La méthode [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) vérifie le contenu de toutes les lignes de la colonne puis ajuste automatiquement la largeur de la colonne.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Comment ajuster automatiquement les lignes pour les cellules fusionnées**  

Avec Aspose.Cells, il est possible d’ajuster automatiquement les lignes même pour les cellules fusionnées en utilisant l’API [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) fournit la propriété [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) qui peut être utilisée pour ajuster automatiquement les lignes des cellules fusionnées. [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) accepte un énumérable [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype) avec les membres suivants.  

- None : Ignorer les cellules fusionnées.  
- FirstLine : N'agrandit la hauteur que de la première ligne.  
- LastLine : N'agrandit la hauteur que de la dernière ligne.  
- EachLine : N'agrandit la hauteur de chaque ligne.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Vous pouvez également essayer d’utiliser les versions surchargées des méthodes [**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) acceptant une plage de lignes/colonnes et une instance de [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) pour ajuster automatiquement les lignes/colonnes sélectionnées selon votre [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) souhaité.  

Les signatures des méthodes susmentionnées sont les suivantes :  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Important à savoir**  

{{% alert color="primary" %}}  
Si une cellule est fusionnée, alors les méthodes d'auto-ajustement ne s’appliqueront pas, ce qui est le même comportement que dans Microsoft Excel. Vous pouvez contourner cela en utilisant l’API autofilter. De plus, si le texte d’une cellule est enroulé, la méthode [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) ne sera pas non plus appliquée. Une autre chose à savoir est que les méthodes *autoFit* prennent beaucoup de temps. Par conséquent, vous devriez appeler ces méthodes aussi rarement que possible pour assurer l’efficacité de votre application.  
{{% /alert %}}  

## **Sujets avancés**  
- [Ajustement automatique des lignes pour les cellules fusionnées](/cells/fr/javascript-cpp/autofit-rows-for-merged-cells/)
