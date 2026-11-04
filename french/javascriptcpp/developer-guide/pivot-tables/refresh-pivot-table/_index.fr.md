---
title: Actualiser les Tableaux Croisés Dynamiques et les caches de pivot dans Aspose.Cells for JavaScript via C++
description: Découvrez comment actualiser les Tableaux Croisés Dynamiques dans Aspose.Cells for JavaScript via C++ à l’aide de l’API d’actualisation des pivots v26.7+. Cet article présente workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData et pivotCache.getPivotTables avec des exemples de code pratiques.
linktitle: Actualiser les Tableaux Croisés Dynamiques
keywords: Aspose.Cells, JavaScript via C++, Tableau Croisé Dynamique, actualisation, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /fr/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit une API d’actualisation à plusieurs niveaux qui permet de recharger les données des tableaux croisés dynamiques à quatre portées différentes — du classeur complet jusqu’à un Tableau Croisé Dynamique unique. À partir de **Aspose.Cells for JavaScript via C++ v26.7**, la méthode héritée `pivotTable.refreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces qui tiennent compte du cache, décrites dans cet article.
{{% /alert %}}

## Introduction
L’actualisation d’un Tableau Croisé Dynamique relève rarement d’une seule opération. En arrière-plan, Aspose.Cells maintient une chaîne de données hiérarchisée qui relie les données source d’origine aux valeurs affichées dans la feuille de calcul. Comprendre cette chaîne est essentiel pour choisir l’API d’actualisation adaptée à chaque situation.
La chaîne de données à quatre niveaux est la suivante :
1. **Source de données** — les plages de la feuille de calcul d’origine, la requête de base de données ou la plage de consolidation où résident les valeurs brutes.
2. **`PivotCache`** — l’instantané en mémoire des données source. Chaque Tableau Croisé Dynamique est construit sur un `PivotCache` ; c’est là que toutes les données sont regroupées et agrégées.
3. **`PivotTable`** — l’objet de visualisation qui définit les champs de ligne, de colonne, de valeur et de filtre. Un `PivotTable` lit *uniquement* depuis son `PivotCache`, jamais directement depuis la source de données.
4. **`Cells`** — les cellules de la feuille de calcul renvoyées par `getCells()`, dans lesquelles le `PivotTable` rend ses valeurs calculées et ses styles.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (énumération `PivotTableSourceType`) indique d’où proviennent les données du cache. À partir de v26.7, `pivotCache.refresh()` ne prend en charge que les types de source **`SHEET`** et **`CONSOLIDATION`** — autrement dit, les données qui résident dans des plages de feuilles de calcul. Les sources externes (bases de données, connexions externes, etc.) ne peuvent pas encore être actualisées via l’API de cache.
En raison de cette chaîne, il existe deux chemins d’actualisation fondamentaux dans Aspose.Cells :
- **`pivotTable.calculateData()`** — recalcule l’affichage d’un `PivotTable` à partir de données déjà mises en cache, sans aller-retour vers la source de données.
Tous les scénarios de cet article utilisent des données source issues de cellules de feuille de calcul ; le type de source est donc `SHEET` et les opérations d’actualisation se comportent comme indiqué.
{{% /alert %}}

## Démarrage rapide
Si vous avez seulement besoin du code le plus court possible pour actualiser tous les Tableaux Croisés Dynamiques du classeur, un seul appel suffit :

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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

La suite de cet article explique dans quels cas choisir plutôt une API à portée plus limitée.

## Imports requis
Tous les exemples JavaScript de cet article commencent par l’import de module suivant, car les types de pivot sont exposés via le namespace `Aspose.Cells.Pivot` :
- `const Aspose = require('aspose.cells');`

## Actualiser tous les Tableaux Croisés Dynamiques du classeur
Lorsque vous devez vous assurer que chaque cache de pivot et chaque Tableau Croisé Dynamique du classeur reflète les données source les plus récentes, l’API la plus simple et la plus complète est `workbook.refreshAll()`. Un seul appel parcourt l’intégralité du classeur — actualisant chaque `PivotCache` à partir de sa source, puis en recalculant chaque `PivotTable` dépendant. Il s’agit de l’approche recommandée pour les actualisations générales de tout le document lorsque la performance n’est pas un enjeu.
L’exemple suivant crée un classeur avec une plage source contenant des fruits, des années et des montants, crée un Tableau Croisé Dynamique, modifie certaines valeurs source, puis utilise `refreshAll()` pour tout actualiser au moyen d’un seul appel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Créer un nouveau classeur
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Écrire la ligne d'en-tête dans les cellules A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Écrire les lignes de données dans les cellules A2:C9 (8 lignes de données de fruits pour 2020 et 2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Ajouter un tableau croisé dynamique : plage source "A1:C9", cellule de destination "E3"
            const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
            // Attribuer les champs du tableau croisé dynamique : Fruit aux lignes, Year aux colonnes, Amount aux données
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Modifier plusieurs valeurs de Amount dans les données source pour simuler des changements
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Actualiser tous les tableaux croisés dynamiques et caches de tableau croisé dynamique du classeur
            workbook.refreshAll();
            // Enregistrer le classeur
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Actualiser tous les Tableaux Croisés Dynamiques sur une seule feuille de calcul
Parfois, vous n’avez besoin d’actualiser que les Tableaux Croisés Dynamiques qui figurent sur une feuille de calcul précise — par exemple, lorsqu’il est connu que ceux d’autres feuilles ne sont pas liés à votre besoin. Pour ce cas, Aspose.Cells fournit `worksheet.refreshPivotTables()`, dont la portée est limitée à une seule instance de `Worksheet`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## Actualiser un seul Tableau Croisé Dynamique
Lorsque vous souhaitez contrôler précisément un seul Tableau Croisé Dynamique, l’API basée sur le cache vous offre deux options. Le choix dépend de ce qui a réellement changé : les données source sous-jacentes ou uniquement les paramètres d’affichage et de disposition du Tableau Croisé Dynamique lui-même.

### Données source modifiées — Utilisez `pivotCache.refresh()`
Si les données source sous-jacentes ont changé, le point d’entrée approprié est `pivotTable.getPivotCache().refresh()`. Cet appel recharge les données source dans le cache, puis recalcule chaque `PivotTable` qui dépend de ce cache.

### Modification de l’affichage ou de la disposition uniquement — Utilisez `pivotTable.calculateData()`
Si les données source n’ont *pas* changé et que seuls les paramètres d’affichage ou de disposition du Tableau Croisé Dynamique lui-même ont été modifiés (par exemple, si un champ a été déplacé vers une autre zone ou si un paramètre d’actualisation à l’ouverture a été activé ou désactivé), il est inutile de revenir à la source. Le cache contient déjà les bonnes données ; seul le `PivotTable` rendu doit être recalculé. Dans ce cas, `pivotTable.calculateData()` est le bon choix.
L’exemple suivant modifie une propriété qui ne concerne pas la source du Tableau Croisé Dynamique, puis appelle `calculateData()` pour le régénérer à partir du cache existant.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Écrire la ligne d'en-tête des champs Fruit / Year / Amount
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // Écrire 8 lignes de données (lignes 2 à 9, correspondant à la plage source A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Ajouter un tableau croisé dynamique à la cellule de destination E3, avec A1:C9 comme source
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                // Affecter les champs : Fruit aux lignes, Year aux colonnes, Amount aux données
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Modifier une propriété d'affichage/de disposition — il s'agit uniquement d'une modification présentationnelle,
                // elle ne nécessite donc PAS de relire les données source via PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() réaffiche la présentation (données + style) de CE tableau croisé dynamique à partir des
                // données déjà conservées dans le PivotCache. Comme les données source n'ont pas changé,
                // aucun aller-retour vers la source n'est effectué — seules les valeurs en cache sont recalculées
                // dans les cellules de la feuille de calcul.
                pivotTable.calculateData();
                // Enregistrer le classeur sur le disque
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Un classeur contient souvent de nombreux Tableaux Croisés Dynamiques qui reposent tous sur un même cache partagé. Pour les énumérer — par exemple avant d’effectuer une actualisation par lot ou de diagnostiquer l’impact d’un cache partagé — utilisez `pivotCache.getPivotTables()`. Cette méthode retourne la collection de tous les `PivotTable` qui dépendent du cache indiqué.

## Migration depuis la méthode obsolète `pivotTable.refreshData()`
Avant Aspose.Cells for JavaScript via C++ v26.7, la méthode standard pour actualiser un Tableau Croisé Dynamique consistait à appeler `pivotTable.refreshData()` sur chaque Tableau Croisé Dynamique individuellement. À partir de v26.7, cette méthode est marquée **obsolète** et doit être remplacée par les API qui tiennent compte du cache décrites ci-dessus.
L’approche par table avec `refreshData()` pose deux problèmes dans les classeurs réels :
- Elle récupère les données depuis la source *à chaque appel*, même si la source n’a pas changé.
Les remplacements recommandés sont :
L’exemple suivant illustre le nouveau modèle efficace pour les classeurs contenant plusieurs Tableaux Croisés Dynamiques qui partagent un même cache.

## Quelle API d’actualisation devez-vous utiliser ?
Le tableau ci-dessous récapitule les API d’actualisation disponibles et le moment de choisir chacune d’elles.
| Objectif | API recommandée | Remarques |
|------|-----------------|-------|
| Actualiser tout le classeur | `workbook.refreshAll()` | Un seul appel ; couvre tous les caches et tous les tableaux. |
| Actualiser uniquement les Tableaux Croisés Dynamiques d’une feuille | `worksheet.refreshPivotTables()` | Portée limitée à une feuille de calcul. |
| Les données source d’un cache ont changé | `pivotTable.getPivotCache().refresh()` | Actualise TOUS les Tableaux Croisés Dynamiques qui utilisent ce cache partagé. |
| Seuls les paramètres d’affichage ou de disposition ont changé | `pivotTable.calculateData()` | Évite un aller-retour inutile vers la source. |
| Lister tous les Tableaux Croisés Dynamiques d’un cache partagé | `pivotCache.getPivotTables()` | À utiliser pour les énumérer avant une actualisation groupée. |
En pratique, préférez les API basées sur le cache à la méthode obsolète `refreshData()` par table. Elles tiennent compte des caches partagés, évitent les récupérations de source redondantes et vous permettent de choisir la portée la plus étroite qui répond à votre besoin d’actualisation.

## Pièges courants
- **Oublier d’actualiser avant d’enregistrer.** Un Tableau Croisé Dynamique n’écrit ses valeurs affichées dans la feuille de calcul que lorsque sa chaîne de données est actualisée. Si vous modifiez des cellules source, appelez `pivotCache.refresh()` (ou `workbook.refreshAll()`) avant `workbook.save()`, sinon le fichier enregistré contient toujours les anciennes valeurs agrégées.
- **Appeler la méthode obsolète `refreshData()` pour chaque table.** Dans v26.7, `pivotTable.refreshData()` est marquée comme obsolète et récupère à nouveau la source à chaque appel. Avec plusieurs Tableaux Croisés Dynamiques partageant un cache, cela signifie N récupérations redondantes de la source. Selon le cas, remplacez-la par un seul `pivotCache.refresh()` lorsque les données source ont changé, ou par `pivotTable.calculateData()` pour chaque table lorsque seule la disposition a changé.
- **Actualiser lorsque seule la disposition a changé.** Si vous avez modifié uniquement l’affichage d’un Tableau Croisé Dynamique (ordre des colonnes, `getConsolidationFunction()`, etc.) sans toucher aux données source, `pivotCache.refresh()` est inutile et lent. Appelez `pivotTable.calculateData()` pour régénérer l’affichage à partir du cache existant.
- **Source externe non prise en charge par `pivotCache.refresh()`.** Si la source du Tableau Croisé Dynamique provient d’une connexion externe (base de données, cube OLAP, etc.), `pivotCache.refresh()` ne peut pas l’actualiser dans la version v26.7 — il ne prend actuellement en charge que les types de source `SHEET` et `CONSOLIDATION`. Pour les sources externes, rouvrez le classeur ou reconstruisez le cache à partir de la source.

{{< app/cells/assistant language="javascript-cpp" >}}