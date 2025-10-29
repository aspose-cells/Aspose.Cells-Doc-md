---
title: Comment et où utiliser les énumérateurs avec JavaScript via C++
linktitle: Itérer les données
type: docs
weight: 55
url: /fr/javascript-cpp/how-and-where-to-use-enumerators/
description: Apprenez à utiliser les énumérateurs via Aspose.Cells for JavaScript en C++.
keywords: Comment utiliser les énumérateurs JavaScript via C++, Énumérateur de cellules JavaScript via C++, Énumérateur de lignes JavaScript via C++, Énumérateur de colonnes JavaScript via C++
---

{{% alert color="primary" %}}  

Un énumérateur est un objet qui offre la capacité de parcourir un conteneur ou une collection. Les énumérateurs peuvent être utilisés pour lire les données dans la collection, mais ils ne peuvent pas être utilisés pour modifier la collection sous-jacente, alors que Array est une interface qui définit une méthode `enumerator` qui renvoie une interface `IEnumerator`, ce qui permet un accès en lecture seule à une collection.  

Les API Aspose.Cells fournissent une multitude d'énumérateurs, cependant, cet article traite principalement des trois types énumérés ci-dessous.  

1. Énumérateur de cellules  
1. Énumérateur de lignes  
1. Énumérateur de colonnes  

{{% /alert %}}  

## **Comment utiliser des énumérateurs**  

### **Énumérateur de cellules**  

Il existe diverses façons d'accéder à l'énumérateur de cellules, et l'on peut utiliser l'une de ces méthodes en fonction des besoins de l'application. Voici les méthodes qui renvoient l'énumérateur de cellules.  

1. [**Cells.enumerator**](https://reference.aspose.com/cells/javascript-cpp/cells/#enumerator--)  
1. [**Row.enumerator**](https://reference.aspose.com/cells/javascript-cpp/row/#enumerator--)  
1. [**Range.enumerator**](https://reference.aspose.com/cells/javascript-cpp/range/#enumerator--)  

Toutes les méthodes mentionnées ci-dessus renvoient l'énumérateur qui permet de parcourir la collection de cellules qui ont été initialisées.  

{{% alert color="primary" %}}  

En parcourant les cellules, la collection ne doit pas être modifiée (des opérations qui entraîneront l'instanciation d'une nouvelle cellule ou la suppression d'une cellule existante). Sinon, l'énumérateur risque de ne pas pouvoir parcourir toutes les cellules correctement (certains éléments peuvent être parcourus de manière répétitive ou sautés).  

{{% /alert %}}  

L'exemple de code suivant démontre la mise en œuvre de l'interface `IEnumerator` pour une collection de cellules.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Values</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const resultLines = [];

            // Iterate over all cells in the worksheet
            const cellsEnumerator = worksheet.cells.getEnumerator();
            for (const cell of cellsEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over the first row's cells
            const firstRowEnumerator = worksheet.cells.rows.get(0).getEnumerator();
            for (const cell of firstRowEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over a specific range A1:B10
            const rangeEnumerator = worksheet.cells.createRange("A1:B10").getEnumerator();
            for (const cell of rangeEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            document.getElementById('result').innerHTML = `<pre>${resultLines.join('\n')}</pre>`;
        });
    </script>
</html>
```  

### **Itérateur de lignes**  

L'énumérateur de lignes peut être accessible lors de l'utilisation de la méthode [**RowCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/rowcollection/#enumerator--). L'exemple de code suivant démontre la mise en œuvre de l'interface `IEnumerator` pour [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - List Row Indexes</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get RowCollection and iterate using index
            const rows = workbook.worksheets.get(0).cells.rows;
            const rowCount = rows.count;

            // Traverse rows in the collection and display indexes
            let output = '<p>Row indexes:</p><ul>';
            for (let i = 0; i < rowCount; i++) {
                const row = rows.get(i);
                output += `<li>${row.index}</li>`;
                console.log(row.index);
            }
            output += '</ul>';
            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```  

### **Itérateur de colonnes**  

L'énumérateur de colonnes peut être accessible lors de l'utilisation de la méthode [**ColumnCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/columncollection). L'exemple de code suivant démontre la mise en œuvre de l'interface `IEnumerator` pour [**ColumnCollection**](https://reference.aspose.com/cells/javascript-cpp/columncollection).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Columns Indexes Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get columns collection from first worksheet
            const columns = workbook.worksheets.get(0).cells.columns;
            // Traverse columns using index
            const count = columns.count;
            let html = '<p>Columns indexes:</p><ul>';
            for (let i = 0; i < count; i++) {
                const col = columns.get(i);
                html += `<li>${col.index}</li>`;
                console.log(col.index);
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

## **Où utiliser les énumérateurs**  

Pour discuter des avantages de l'utilisation des énumérateurs, prenons un exemple en temps réel.  

**Scénario**  

Une exigence d’application est de parcourir toutes les cellules dans une [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) donnée pour lire leurs valeurs. Il pourrait y avoir plusieurs façons de réaliser cet objectif. Quelques-unes sont démontrées ci-dessous.  

### **Utilisation de la plage d'affichage**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Max Display Range Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Get the MaxDisplayRange
            const displayRange = cells.maxDisplayRange;

            // Loop over all cells in the MaxDisplayRange
            let outputLines = [];
            for (let row = displayRange.firstRow; row < displayRange.rowCount; row++) {
                for (let col = displayRange.firstColumn; col < displayRange.columnCount; col++) {
                    // Read the Cell value (stringValue property)
                    const cell = displayRange.get(row, col);
                    outputLines.push(cell.stringValue);
                    console.log(cell.stringValue);
                }
            }

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```  

### **Utilisation de MaxDataRow & MaxDataColumn**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; max-height: 400px; overflow: auto; border: 1px solid #ddd; padding: 10px; }
            .cell-value { padding: 2px 0; border-bottom: 1px dashed #eee; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Read Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;

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

        function escapeHtml(text) {
            if (text === null || text === undefined) return '';
            return String(text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p class="error">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells2 = workbook.worksheets.get(0).cells;
            const maxDataRow = cells2.maxDataRow;
            const maxDataColumn = cells2.maxDataColumn;

            const outputLines = [];
            // Loop over all cells
            for (let row = 0; row <= maxDataRow; row++) {
                for (let col = 0; col <= maxDataColumn; col++) {
                    // Read the Cell value
                    const currentCell = cells2.checkCell(row, col);
                    if (currentCell) {
                        const cellText = currentCell.stringValue;
                        outputLines.push('<div class="cell-value">' + escapeHtml(cellText) + '</div>');
                        console.log(cellText);
                    }
                }
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p>No cell values found.</p>';
            } else {
                resultDiv.innerHTML = outputLines.join('');
            }
        });
    </script>
</html>
```  

Comme vous pouvez le constater, les deux approches ci-dessus utilisent plus ou moins une logique similaire, c'est-à-dire parcourir toutes les cellules de la collection pour lire les valeurs des cellules. Cela pourrait poser problème pour un certain nombre de raisons, comme discuté ci-dessous.  

1. Des API telles que [**maxRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxRow--), [**maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--), [**maxColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxColumn--), [**maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) et [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) nécessitent du temps supplémentaire pour recueillir les statistiques correspondantes. Si la matrice de données (lignes x colonnes) est grande, l’utilisation de ces API pourrait entraîner une pénalité de performance.  
1. Dans la plupart des cas, toutes les cellules dans une plage donnée ne sont pas instanciées. Dans de telles situations, vérifier chaque cellule dans la matrice n'est pas aussi efficace que de vérifier uniquement les cellules initialisées.  
1. Accéder à une cellule dans une boucle en tant que Cells row, column entraînera l'instanciation de tous les objets de cellules dans une plage, ce qui pourrait finalement entraîner une OutOfMemoryException.  

## **Conclusion**  

Sur la base des faits mentionnés ci-dessus, voici les scénarios possibles où les énumérateurs doivent être utilisés.  

1. Un accès en lecture seule de la collection de cellules est requis, c'est-à-dire; la nécessité est uniquement d'inspecter les cellules.  
1. Un grand nombre de cellules doit être parcouru.  
1. Seules les cellules/rangées/colonnes initialisées doivent être parcourues.
