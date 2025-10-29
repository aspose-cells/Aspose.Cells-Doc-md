---
title: Précédents et dépendants avec JavaScript via C++
linktitle: Prédécesseurs et dépendants
type: docs
weight: 230
url: /fr/javascript-cpp/precedents-and-dependents/
description: Apprenez à tracer les cellules précedentes et dépendantes dans les feuilles de calcul en utilisant Aspose.Cells for JavaScript via C++. Comprenez comment identifier les cellules liées dans les feuilles de calcul financières complexes.
---

{{% alert color="primary" %}} 

Les feuilles de calcul financières complexes, en particulier celles développées en collaboration, peuvent cacher les erreurs les plus gênantes. Vérifier la précision des formules et trouver la source d'une erreur peut être difficile lorsque la formule utilise des cellules précédentes et des cellules dépendantes.

{{% /alert %}} 
## **Introduction**
- **Cellules précédentes** sont des cellules auxquelles une formule d'une autre cellule fait référence. Par exemple, si la cellule D10 contient la formule =B5, la cellule B5 est une cellule précédente de la cellule D10.
- **Cellules dépendantes** contiennent des formules qui référencent d'autres cellules. Par exemple, si la cellule D10 contient la formule =B5, la cellule D10 dépend de la cellule B5.

Pour rendre la feuille de calcul facile à lire, vous voudrez peut-être clairement indiquer quelles cellules d'une feuille de calcul sont utilisées dans une formule. De même, vous voudrez peut-être extraire les cellules dépendantes d'autres cellules.

Aspose.Cells vous permet de tracer les cellules et de savoir lesquelles sont liées.
## **Tracer les cellules précédentes et dépendantes : Microsoft Excel**
Les formules peuvent changer en fonction des modifications apportées par un client. Par exemple, si la cellule C1 dépend de C3 et C4 contenant une formule, et que C1 est modifiée (la formule étant remplacée), C3 et C4, ou d'autres cellules, doivent changer pour équilibrer la feuille de calcul en fonction des règles métier.

De même, supposons que C1 contient la formule "=(B1*22)/(M2*N32)". Je veux trouver les cellules dont C1 dépend, c'est-à-dire les cellules précédentes B1, M2 et N32.

Il se peut que vous deviez retracer la dépendance d'une cellule particulière à d'autres cellules. Si des règles métier sont intégrées dans des formules, nous aimerions connaître la dépendance et exécuter certaines règles en fonction de celle-ci. De même, si la valeur d'une cellule particulière est modifiée, quelles cellules dans la feuille de calcul sont impactées par ce changement ?

Microsoft Excel permet aux utilisateurs de tracer les cellules précédentes et dépendantes.

1. Sur la **Barre d'outils Affichage**, sélectionnez **Audit des formules**. La boîte de dialogue Audit des formules s'affichera.
1. Tracer les cellules précédentes :
   1. Sélectionnez la cellule contenant la formule pour laquelle vous souhaitez trouver les cellules précédentes.
   1. Pour afficher une flèche de traçage vers chaque cellule qui fournit directement des données à la cellule active, cliquez sur **Tracer les cellules précédentes** sur la **Barre d'outils Audit de formules**.
1. Tracer les formules qui référencent une cellule particulière (dépendantes)
   1. Sélectionnez la cellule pour laquelle vous souhaitez identifier les cellules dépendantes.
   1. Pour afficher une flèche de traçage vers chaque cellule dépendante de la cellule active, cliquez sur **Tracer les dépendants** dans la barre d'outils d'audit de formule.
## **Tracer les cellules précédentes et dépendantes : Aspose.Cells**
### **Tracer les cellules précédentes**
Aspose.Cells facilite l'obtention de cellules précédentes. Il peut non seulement récupérer les cellules fournissant des données aux précédents de formule simples, mais aussi trouver les cellules fournissant des données aux précédents de formule complexes avec des plages nommées.

Dans l'exemple ci-dessous, un fichier excel modèle, Book1.xls, est utilisé. La feuille de calcul contient des données et des formules sur la première feuille de calcul.

Aspose.Cells fournit la méthode [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) de la classe [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), utilisée pour tracer les cellules précédentes. Elle retourne une collection de zones référencées. Comme montré ci-dessus, dans Book1.xls, la cellule B7 contient une formule "=SUM(A1:A3)". Donc, les cellules A1:A3 sont les cellules précédentes de la cellule B7. L'exemple suivant illustre cette fonctionnalité en utilisant le fichier modèle Book1.xls.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **Tracé des dépendances**
Aspose.Cells vous permet d'obtenir les cellules dépendantes dans les feuilles de calcul. Aspose.Cells peut non seulement récupérer les cellules qui fournissent des données concernant une formule simple mais aussi trouver celles qui fournissent des données aux dépendants de formules complexes avec des plages nommées.

Aspose.Cells fournit la méthode [Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) de la classe [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), utilisée pour tracer les cellules dépendantes. Par exemple, dans Book1.xlsx, il y a des formules : "=A1+20" et "=A1+30" dans les cellules B2 et C2 respectivement. L'exemple suivant montre comment tracer les dépendants de la cellule A1 en utilisant le fichier modèle Book1.xlsx.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **Tracer les cellules précédentes et dépendantes selon la chaîne de calcul**
Les API ci-dessus de traçage des précédents et dépendants sont conformes à l'expression de formule elle-même. Elles offrent simplement un moyen pratique pour les utilisateurs de suivre les interdépendances pour quelques formules. Si le classeur contient un grand nombre de formules et que l'utilisateur doit tracer les précédents et dépendants pour chaque cellule, ces méthodes donneront de mauvaises performances. Pour ce genre de situation, l'utilisateur devrait envisager d'utiliser [Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) et [Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-) qui suivent les dépendances selon la chaîne de calcul. Pour les utiliser, il faut d'abord activer la chaîne de calcul via [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--). Ensuite, effectuer un calcul complet du classeur via [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--). Après cela, vous pouvez tracer les précédents ou dépendants pour toutes ces cellules.

Pour certaines formules, les précédents résultants peuvent différer pour 'precedents' et 'precedentsInCalculation', et les dépendants peuvent différer pour 'dependents' et 'dependentsInCalculation'. Par exemple, si la formule de la cellule A1 est "=IF(TRUE,B2,C3)", 'precedents' renverra B2 et C3 comme précédents de A1. En conséquence, B2 et C3 ont tous deux pour dépendant A1 lors de la vérification via 'dependents'. Cependant, pour le calcul de cette formule, il est évident que seul B2 peut influencer le résultat calculé. Donc, 'precedentsInCalculation' ne renverra pas C3 pour A1, et 'dependentsInCalculation' ne montrera pas A1 pour C3. Parfois, les utilisateurs ont juste besoin de tracer les interdépendances qui affectent réellement le résultat du calcul des formules en fonction des données actuelles du classeur, ils doivent donc utiliser 'dependentsInCalculation'/'precedentsInCalculation' au lieu de 'dependents'/'precedents'.

L'exemple suivant montre comment suivre les antécédents et dépendants selon la chaîne de calcul pour les cellules :


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

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
