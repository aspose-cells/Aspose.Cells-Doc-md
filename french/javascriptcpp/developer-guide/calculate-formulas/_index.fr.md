---
title: Calculer des formules avec JavaScript via C++
linktitle: Calcul des formules
description: Cet article explique comment utiliser la bibliothèque Aspose.Cells pour calculer des formules dans Microsoft Excel en utilisant JavaScript via C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la formule et obtenir le résultat. Enfin, nous sauvegardons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, formules, calculs, Calcul direct de formule, Calculer des formules à répétition, Ajouter des formules en JavaScript via C++
type: docs
weight: 125
url: /fr/javascript-cpp/calculate-formulas/
---

## **Ajout de formules et calcul de résultats**

Aspose.Cells dispose d’un moteur de calcul de formules intégré. Il peut non seulement recalculer les formules importées à partir de modèles de conception, mais également supporter le calcul des résultats des formules ajoutées en temps réel.

Aspose.Cells supporte la plupart des formules ou fonctions qui font partie de Microsoft Excel (lire [une liste des fonctions supportées par le moteur de calcul](/cells/fr/javascript-cpp/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou avec les feuilles de calcul du concepteur. Aspose.Cells supporte un large ensemble de formules mathématiques, de chaînes, booléennes, de dates/horaires, statistiques, de bases de données, de recherche et de références.

Utilisez la propriété [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) ou les méthodes [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) pour ajouter une formule à une cellule. Lors de l’application d’une formule, commencez toujours la chaîne par un signe égal (=), comme lors de la création d’une formule dans Microsoft Excel, et utilisez une virgule (,) pour délimiter les paramètres des fonctions.

Pour calculer les résultats des formules, l'utilisateur peut appeler la méthode [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui traite toutes les formules intégrées dans un fichier Excel. Ou, l'utilisateur peut appeler la méthode [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) qui traite toutes les formules d'une feuille. Ou, l'utilisateur peut aussi appeler la méthode [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) qui traite la formule d'une seule cellule :

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **Important à savoir pour les formules**

{{% alert color="primary" %}}

La propriété **Formula** et les méthodes **formula(...)** de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) fonctionnent différemment des méthodes **calculate** des classes [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) et [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). La propriété **Formula** et les méthodes **formula(...)** ajoutent simplement la formule à une cellule sans calculer le résultat en temps réel. Pour obtenir le résultat des formules, veuillez appeler les méthodes **calculate**.

{{% /alert %}}

## **Calcul direct de formule**

Aspose.Cells possède un moteur de calcul de formules intégré. En plus de calculer les formules importées à partir d'un fichier, Aspose.Cells peut calculer les résultats des formules directement.

Parfois, vous souhaitez calculer directement les résultats des formules sans les ajouter dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille, et tout ce que vous avez à faire est de trouver le résultat de ces valeurs en utilisant une formule Microsoft Excel sans ajouter la formule dans une feuille.

Vous pouvez utiliser les API du moteur de calcul de formules d'Aspose.Cells pour [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) à [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) pour obtenir les résultats de telles formules sans les ajouter dans la feuille :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

Le code ci-dessus produit la sortie suivante :
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Comment calculer des formules de manière répétée**

Lorsqu'il y a beaucoup de formules dans le classeur, et que l'utilisateur doit les calculer à plusieurs reprises en modifiant uniquement une petite partie d'entre elles, il peut être utile pour la performance d'activer la chaîne de calcul des formules : [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Important à savoir**

{{% alert color="primary" %}}

Par défaut, la chaîne de calcul est désactivée. Car la création de la chaîne nécessite également du temps supplémentaire, la première fois que vous calculez les formules ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) peut consommer plus de temps CPU et de mémoire par rapport au calcul sans chaîne. Si l'utilisateur n'a pas besoin de recalculer les formules à plusieurs reprises, le comportement par défaut (calculer directement la formule sans créer une chaîne de calcul) devrait être la meilleure option.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel](/cells/fr/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcul de la fonction SIERREUR en utilisant Aspose.Cells](/cells/fr/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule de tableau de données](/cells/fr/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions MINIFS et MAXIFS d'Excel 2016](/cells/fr/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Réduire le temps de calcul de la méthode Cell.calculate](/cells/fr/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Détection des références circulaires](/cells/fr/javascript-cpp/detecting-circular-reference/)
- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompre ou annuler le calcul de formule du classeur](/cells/fr/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Définir le mode de calcul de formule du classeur](/cells/fr/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilisation de la fonction FormulaText dans Aspose.Cells](/cells/fr/javascript-cpp/using-formulatext-function-in-aspose-cells/)
