---
title: Gérer les formules des fichiers Excel avec JavaScript via C++
linktitle: Formules
type: docs
weight: 122
url: /fr/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Apprenez à gérer les formules des fichiers Excel via Aspose.Cells for JavaScript via C++. Aspose.Cells peut simplement obtenir, définir et calculer les formules des fichiers Excel.
keywords: Comment calculer des formules en JavaScript via C++, Formules et fonctions en JavaScript via C++, Gérer les fonctions intégrées JavaScript via C++, Utiliser des fonctions d’add in avec JavaScript via C++, Utiliser la formule de tableau via JavaScript via C++, Utiliser la formule R1C1 en JavaScript via C++.
---

## **Introduction**

 L’une des fonctionnalités attrayantes de Microsoft Excel est sa capacité à traiter des données avec des formules et des fonctions. Microsoft Excel fournit un ensemble de fonctions et de formules intégrées qui aident les utilisateurs à effectuer des calculs complexes rapidement. Aspose.Cells offre également un vaste ensemble de fonctions et de formules intégrées qui facilitent le calcul pour les développeurs. Aspose.Cells supporte également les fonctions add-in. De plus, Aspose.Cells supporte les formules de tableau et R1C1.

## **Comment utiliser des formules et des fonctions**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Chaque élément de la collection Cells représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Il est possible d'appliquer des formules aux cellules à l'aide des propriétés et des méthodes offertes par la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), comme discuté plus en détail ci-dessous.

- Utilisation de fonctions intégrées.
- Utilisation de fonctions supplémentaires.
- Travailler avec des formules de tableau.
- Créer une formule R1C1.

## **Comment utiliser les fonctions intégrées**

Les fonctions ou formules intégrées sont fournies sous forme de fonctions préétablies pour réduire les efforts et le temps des développeurs. Voir [une liste des fonctions intégrées](/cells/fr/javascript-cpp/supported-formula-functions/) supportées par Aspose.Cells. Les fonctions sont listées par ordre alphabétique. D’autres fonctions seront prises en charge à l’avenir.

Aspose.Cells prend en charge la plupart des formules ou fonctions proposées par Microsoft Excel. Les développeurs peuvent utiliser ces formules via l'API ou [le fichier de conception](/cells/fr/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporte un vaste ensemble de formules mathématiques, de chaîne, booléennes, date/heure, statistiques, base de données, recherche et référence.

Utilisez la propriété [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) pour ajouter une formule à une cellule. **Les formules complexes**, par exemple

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également prises en charge dans Aspose.Cells. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) de la feuille de calcul. La formule utilise une fonction intégrée **SI** fournie par Aspose.Cells.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Comment utiliser les fonctions d'extension**

Nous pouvons avoir des formules définies par l'utilisateur que nous souhaitons inclure en tant qu’add-in Excel. Lors de la définition de la fonction cell.formula, les fonctions intégrées fonctionnent bien, mais il est nécessaire de définir des fonctions ou formules personnalisées en utilisant les fonctions d’add-in.

Aspose.Cells offre des fonctionnalités pour enregistrer des fonctions d’add-in en utilisant [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Ensuite, lorsque nous définissons cell.formula = anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction AddIn.

Le fichier XLAM suivant doit être téléchargé pour enregistrer la fonction d'extension dans le code d'exemple ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Comment utiliser les formules de tableau**

Les formules de tableau sont des formules qui prennent des tableaux, au lieu de nombres individuels, en tant qu'arguments pour les fonctions qui composent la formule. Lorsqu'une formule de tableau est affichée, elle est entourée d'accolades ({}).

Certaines fonctions Microsoft Excel renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule de tableau, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

Il est possible d'appliquer une formule de tableau à une cellule en appelant la méthode [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). La méthode [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) prend les paramètres suivants:

- **Formule de tableau**, la formule de tableau.
- **Nombre de lignes**, le nombre de lignes pour remplir le résultat de la formule de tableau.
- **Nombre de colonnes**, le nombre de colonnes pour peupler le résultat de la formule de tableau.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **Comment utiliser la formule R1C1**

Ajoutez une formule de référence R1C1 à une cellule avec la propriété de la classe [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Précédents et dépendants](/cells/fr/javascript-cpp/precedents-and-dependents/)
- [Définir des liens externes dans les formules](/cells/fr/javascript-cpp/set-external-links-in-formulas/)
- [Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes](/cells/fr/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Définition de la formule pour une plage nommée](/cells/fr/javascript-cpp/setting-formula-for-named-range/)
- [Définition de formules - Avis aux utilisateurs non anglophones](/cells/fr/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Définition de formule partagée](/cells/fr/javascript-cpp/setting-shared-formula/)
- [Spécifier le nombre maximum de lignes de formule partagée](/cells/fr/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Fonctions Excel prises en charge](/cells/fr/javascript-cpp/supported-formula-functions/)
