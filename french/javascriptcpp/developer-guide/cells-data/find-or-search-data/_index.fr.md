---
title: Trouver ou rechercher des données
type: docs
weight: 50
url: /fr/javascript-cpp/find-or-search-data/
description: Apprenez comment trouver ou rechercher des cellules dans une feuille de calcul contenant des données spécifiées via l API Aspose.Cells for JavaScript via C++.
keywords: Trouver des données JavaScript via C++, Rechercher des données JavaScript via C++, Trouver des cellules contenant une formule JavaScript via C++, Rechercher des cellules contenant une formule JavaScript via C++, Trouver ou rechercher des données ou des formules en utilisant FindOptions JavaScript via C++, Rechercher des données ou des formules en utilisant FindOptions JavaScript via C++, Trouver ou rechercher des cellules contenant une valeur chaîne ou un nombre spécifié JavaScript via C++, Trouver ou rechercher des cellules contenant des données spécifiées
---

{{% alert color="primary" %}}  
Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiques.  
{{% /alert %}}  

## **Recherche de cellules contenant des données spécifiées**  

### **Utilisation de Microsoft Excel**  

Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiques. Si vous sélectionnez **Modifier** dans le menu **Rechercher** dans Microsoft Excel, vous verrez une boîte de dialogue où vous pouvez spécifier la valeur de recherche.  

Ici, nous recherchons la valeur "Oranges". Aspose.Cells permet également aux développeurs de trouver des cellules dans la feuille de calcul contenant des valeurs spécifiées.  

### **Utilisation du Script Aspose.Cells for Java via C++**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) qui représente toutes les cellules dans la feuille. La collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) offre plusieurs méthodes pour rechercher des cellules dans une feuille contenant des données saisies par l’utilisateur. Certaines de ces méthodes sont abordées ci-dessous en détail.  

{{% alert color="primary" %}}  
Toutes les méthodes de recherche renvoient les références des cellules contenant les données spécifiées à rechercher.  
{{% /alert %}}  

## **Recherche de cellules contenant une formule**  

Les développeurs peuvent trouver une formule spécifique dans la feuille de calcul en appelant la méthode [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Généralement, la méthode [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) accepte trois paramètres :  

-  L'objet à rechercher. Le type doit être int, double, DateTime, string, bool.  
-  La cellule précédente avec le même objet. Ce paramètre peut être défini sur null si la recherche commence du début.  
-  Options pour trouver l'objet requis.  

Les exemples ci-dessous utilisent les données de la feuille de calcul pour apprendre les méthodes de recherche.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

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

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **Recherche de données ou de formules à l'aide de FindOptions**  

Il est possible de rechercher des valeurs spécifiées en utilisant la méthode [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) avec diverses [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). Généralement, la méthode [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) accepte les paramètres suivants :  

- **Valeur de recherche**, les données ou la valeur à rechercher.  
- **Cellule précédente**, la dernière cellule qui contient la même valeur. Ce paramètre peut être défini sur null lors de la recherche depuis le début.  
- **Options de recherche**, les options de recherche.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

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

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **Recherche des cellules contenant une valeur de chaîne spécifiée ou un nombre.**  

Il est possible de rechercher des valeurs de chaîne spécifiées en appelant la même méthode [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) trouvée dans la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) avec diverses [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

Spécifiez les propriétés [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) et [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-). Le code d’exemple suivant montre comment utiliser ces propriétés pour rechercher des cellules avec divers nombres de chaînes au **début**, au **centre** ou à la **fin** de la chaîne de la cellule.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **Sujets avancés**  
- [Rechercher des cellules avec un style spécifique](/cells/fr/javascript-cpp/find-cells-with-specific-style/)  
- [Trouver si la valeur de la cellule commence par un guillemet simple](/cells/fr/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Rechercher des données en utilisant des valeurs originales](/cells/fr/javascript-cpp/search-data-using-original-values/)
