---
title: Diminuer le temps de calcul de la méthode Cell.Calculate avec JavaScript via C++
linktitle: Réduire le temps de calcul de la méthode Cell.Calculate
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour réduire le temps de calcul des méthodes de calcul de cellule dans Excel en utilisant JavaScript via C++.
keywords: Aspose.Cells, Excel, méthodes de calcul de cellule, optimisation, performance, réduction du temps de calcul, JavaScript via C++
type: docs
weight: 100
url: /fr/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler la méthode [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) une seule fois, puis d'obtenir les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne souhaitent pas calculer le classeur en entier. Ils veulent simplement calculer une seule cellule. Aspose.Cells fournit la propriété [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--), que vous pouvez définir sur **false** pour diminuer significativement le temps de calcul des cellules individuelles. Lorsque la propriété récursive est définie sur **true**, toutes les dépendances des cellules sont recalculées à chaque appel. Toutefois, lorsque la propriété est **false**, les cellules dépendantes sont calculées une seule fois et ne sont pas recalculées lors des appels suivants.

## **Diminuer le temps de calcul de la méthode Cell.calculate()**

Le code d'exemple suivant illustre l'utilisation de la propriété [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--). Veuillez exécuter ce code avec le [fichier excel d'exemple](5113710.xlsx) fourni et vérifier sa sortie dans la console. Vous constaterez que la fixation de la propriété récursive sur **false** a considérablement réduit le temps de calcul. Lisez également les commentaires pour mieux comprendre cette propriété.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Calculate Formulas Example</title>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Test calculation time after setting recursive true
            workbook.calculateFormula(); // initiate calculation

            // Test calculation time after setting recursive false (specify ignoreError as false)
            workbook.calculateFormula(false);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.calculated.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Calculated Excel File';

            resultEl.innerHTML = '<p style="color: green;">Calculation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Calculation Time Recursive Test</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Calculation Test (Recursive true/false)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const runs = [true, false];
            let outputHtml = '';
            for (let r = 0; r < runs.length; r++) {
                const rec = runs[r];

                // Set the calculation option, set recursive true or false as per parameter
                const opts = new CalculationOptions();
                opts.recursive = rec;

                // Start stopwatch
                const start = performance.now();

                // Calculate cell A1 one million times
                for (let i = 0; i < 1000000; i++) {
                    ws.cells.get("A1").calculate(opts);
                }

                // Stop the watch
                const end = performance.now();

                // Calculate elapsed time in seconds
                const estimatedTime = (end - start) / 1000;

                // Record the elapsed time
                const message = `Recursive ${rec}: ${estimatedTime} seconds`;
                console.log(message);
                outputHtml += `<p>${message}</p>`;
            }

            resultDiv.innerHTML = `<div style="color: green;">${outputHtml}</div>`;
        });
    </script>
</html>
```

## **Sortie console**

Voici la sortie dans la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5113710.xlsx) sur notre machine. Veuillez noter que votre sortie pourrait différer, mais le temps écoulé après avoir réglé la propriété récursive sur **false** sera toujours inférieur à celui lorsqu'elle est sur **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}
