---
title: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter des données des lignes aux colonnes ou inversement dans des fichiers Excel en utilisant Aspose.Cells for JavaScript via C++ avec trois approches différentes.
linktitle: Transpose Range
url: /fr/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, JavaScript via C++, feuille de calcul, plage transposée, faire pivoter les données, fonction TRANSPOSE, formule tableau dynamique, formule tableau, Excel TRANSPOSE, lignes en colonnes
type: docs
weight: 80
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ prend en charge la transposition (rotation) des données afin que les lignes deviennent des colonnes et que les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode `range.transpose()` en place et fonctionne avec toutes les versions d'Excel, tandis que la deuxième utilise `cell.setDynamicArrayFormula()` pour écrire une formule de tableau dynamique moderne `=TRANSPOSE(...)` qui se déverse automatiquement sur Excel 365 ou Excel 2021. La troisième approche utilise `cell.setArrayFormula()` pour écrire une formule de tableau classique Ctrl+Shift+Enter (CSE) compatible avec les versions plus anciennes d'Excel. Cet article décrit chaque approche avec des instructions étape par étape et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte qu’une ligne devienne une colonne et qu’une colonne devienne une ligne, reflétant ainsi les données par rapport à leur diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l’adresse https://support.microsoft.com/en-us/excel/functions/transpose-function. Ce concept peut être appliqué programmatiquement à une plage de cellules, ce qui est utile dans de nombreux scénarios d’entreprise et de reporting.
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s’affichent normalement horizontalement et les régions verticalement, ou inversement.
- Permuter l’orientation des axes dans les tableaux de bord ou graphiques afin qu’une série temporelle s’affiche verticalement plutôt qu’horizontalement.
- Remodeler les données importées depuis des systèmes externes pour qu’elles correspondent à la mise en page attendue par les analyses ou modèles de reporting en aval.
Pour rendre le reste de l’article concret, chaque exemple utilise le petit tableau de ventes par région et par trimestre suivant. Dans le classeur d’exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide comme coin supérieur gauche, **B1:D1** contenant les en‑têtes de région, et **A2:A5** contenant les en‑têtes de trimestre.
| Région            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
Cet article présente ensuite trois méthodes différentes pour transposer ces données en utilisant Aspose.Cells for JavaScript via C++, chacune adaptée à une version d’Excel et à un cas d’utilisation différents.

## **Approche 1 — Transposer la plage sur place (Range.transpose)**
Utilisez cette approche chaque fois que vous souhaitez transposer des données sans faire appel à la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne avec **toutes les versions d’Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l’option la plus sûre compatible entre versions. Elle est idéale lorsque vous avez uniquement besoin du résultat transposé final et que vous n’avez pas besoin de conserver la formule `TRANSPOSE` d’origine dans le classeur.

### **API utilisée**
`Range.transpose()` est une méthode d’instance de la classe `Aspose.Cells.Range`. Son appel inverse la plage sur place en échangeant ses lignes et ses colonnes, de sorte qu’une ligne devient une colonne et qu’une colonne devient une ligne. La méthode modifie directement les cellules sous‑jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` configuré au format `.xlsx` en appelant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul du classeur en utilisant `workbook.getWorksheets().get(0)`.
3. Accédez à la collection de cellules de la feuille via `worksheet.getCells()`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.createRange("A1:D5")`.
5. Appelez `source.transpose()` pour faire pivoter la plage sur place, en échangeant lignes et colonnes.
6. Enregistrez le classeur avec `workbook.save(outputFile)`.
Après la transposition, cette plage d’ancrage contient les données pivotées. La première ligne lit (vide, **Europe**, **Asia**, **North America**) et la première colonne lit (vide, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Chaque colonne originale de ventes devient une ligne dans la plage transposée.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` en tant que formule dynamique dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou version ultérieure** où les tableaux dynamiques et l’opérateur de déversement sont pris en charge.

### **API utilisée**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` est une méthode de la classe `Aspose.Cells.Cell` qui définit la formule de la cellule comme une **formule de tableau dynamique**. Excel évalue la formule une fois et déverse automatiquement le résultat dans les cellules adjacentes. Le troisième paramètre, lorsqu’il est fixé à `true`, indique à Aspose.Cells de calculer également les valeurs résultantes lors de l’écriture.

### **Étapes**
1. Chargez le classeur source en utilisant `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Récupérez la première feuille de calcul et accédez à sa collection de cellules.
3. Placez la formule de tableau dynamique dans la cellule **A6**, juste sous la plage source, en appelant `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. L’argument `new FormulaParseOptions()` utilise les paramètres par défaut de `FormulaParseOptions`, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l’évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la zone **A6:E9**, un bloc de 4 lignes sur 5 colonnes correspondant aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les versions antérieures d’Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Approche 3 — Transposer avec une formule de tableau classique (CSE)**
Utilisez cette approche lorsque vous souhaitez conserver une formule `TRANSPOSE` dans le classeur mais que le fichier Excel cible peut être ouvert dans **des versions plus anciennes d’Excel (avant 2021, incluant 2019, 2016, 2013, etc.)** où le déversement des tableaux dynamiques n’est pas pris en charge. La formule de tableau classique CSE (Ctrl+Shift+Enter) est l’alternative compatible avec les anciennes versions que toutes les versions d’Excel peuvent évaluer.

### **API utilisée**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` est une méthode de la classe `Aspose.Cells.Cell` qui attribue une **formule de tableau classique (CSE)** à la cellule d’ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule de tableau multi‑cellules afin qu’Excel évalue la formule comme une expression de tableau unique remplissant la plage déclarée.

### **Étapes**
1. Chargez le classeur source comme décrit dans les approches précédentes.
2. Récupérez la première feuille de calcul et accédez à sa collection de cellules.
3. Appelez `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` représente le nombre de lignes du tableau de destination et le troisième argument `5` le nombre de colonnes.
4. Enregistrez le classeur avec `workbook.save(outputFile)`.
La cellule **A6** est l’ancre de la formule de tableau et le tableau évalué s’étend sur 4 lignes et 5 colonnes à partir de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un unique marqueur de formule de tableau sur la plage résultante afin que les versions antérieures d’Excel l’évaluent correctement.

{{% alert color="primary" %}}
Les formules de tableau CSE sont la méthode classique d’Excel pour évaluer une expression `TRANSPOSE` et cette approche est universellement compatible avec toutes les versions d’Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Charger le classeur source avec les options de chargement xlsx
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // Accéder à la première feuille de calcul et à sa collection de cellules
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Définir la formule matricielle CSE classique sur la cellule A6.
                // La formule =TRANSPOSE(A1:D5) fait pivoter la plage source de 5 lignes sur 4 colonnes
                // en un tableau de 4 lignes sur 5 colonnes. Le deuxième argument (4) est le nombre de lignes
                // et le troisième argument (5) est le nombre de colonnes du tableau résultant.
                // Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue comme
                // une formule matricielle multi-cellule unique, compatible avec les versions anciennes d'Excel
                // (2019, 2016, 2013, etc.) qui ne prennent pas en charge le débordement des tableaux dynamiques.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Enregistrer le classeur afin que le marqueur de formule matricielle soit conservé
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version Excel | Formule source préservée ? | Plage de sortie |
|----------|--------------|---------------|---------------------------|-----------------|
| Approche 1 — Transposition sur place | `range.transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Plage d’ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Oui (déversement dynamique) | Déversé depuis l’ancre |
| Approche 3 — Formule de tableau classique (CSE) | `cell.setArrayFormula()` | Toutes les versions d'Excel | Oui (formule de tableau multi‑cellules) | Taille explicite, 4×5 |
Utilisez **l’Approche 1** lorsque vous avez besoin d’une transformation rapide, compatible entre versions, et que vous ne requérez que les valeurs transposées écrites dans le fichier. Utilisez **l’Approche 2** lorsque Excel moderne est garanti et que vous souhaitez que la formule reste dynamique et se mette à jour si la source change. Utilisez **l’Approche 3** lorsque vous avez besoin de la compatibilité la plus large avec une formule préservée sur chaque version d’Excel, y compris les versions plus anciennes qui ne supportent pas les tableaux dynamiques.

{{< app/cells/assistant language="javascript-cpp" >}}