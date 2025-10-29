---
title: Tableaux et plages avec JavaScript via C++
linktitle: Tableaux et Plages
type: docs
weight: 50
url: /fr/javascript-cpp/tables-and-ranges/
---

## **Introduction**  

Parfois, vous créez un tableau dans Microsoft Excel et ne voulez pas continuer à travailler avec la fonctionnalité de tableau qu'il propose. À la place, vous voulez quelque chose qui ressemble à un tableau. Pour conserver les données dans un tableau sans perdre la mise en forme, convertissez le tableau en une plage de données ordinaire.  
Aspose.Cells prend en charge cette fonctionnalité de Microsoft Excel pour les tableaux et les objets liste.  

## **Utilisation de Microsoft Excel**  

Utilisez la fonctionnalité **Convertir en plage** pour convertir rapidement un tableau en une plage sans perdre le formatage. Dans Microsoft Excel 2007/2010 :  

1. Cliquez n'importe où dans le tableau pour vous assurer que la cellule active se trouve dans une colonne de tableau.  
1. Dans l'onglet **Création**, dans le groupe **Outils**, cliquez sur **Convertir en plage**.  

## **Utilisation d'Aspose.Cells**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Table to Range</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and convert the first table/list object to a normal range
            const worksheet = workbook.worksheets.get(0);
            const listObject = worksheet.listObjects.get(0);
            listObject.convertToRange();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Les fonctionnalités du tableau ne sont plus disponibles après sa conversion en plage. Par exemple, les en-têtes de ligne n'incluent plus les flèches de tri et de filtre, et les références structurées (références utilisant des noms de table) utilisées dans les formules se transforment en références de cellule classiques.  

{{% /alert %}}  

## **Convertir un tableau en plage avec des options**  

Aspose.Cells propose des options supplémentaires lors de la conversion d'une table en plage via la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) fournit la propriété [**lastRow**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/#lastRow--) qui vous permet de définir le dernier index de la ligne de table. La mise en forme du tableau sera conservée jusqu'à l'index de ligne spécifié et le reste de la mise en forme sera supprimé.  

Le code d'exemple ci-dessous démontre l'utilisation de la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Table to Range Example</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TableToRangeOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create TableToRangeOptions and set lastRow property
            const options = new TableToRangeOptions();
            options.lastRow = 5;

            // Convert the first table/list object (from the first worksheet) to normal range
            workbook.worksheets.get(0).listObjects.get(0).convertToRange(options);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
