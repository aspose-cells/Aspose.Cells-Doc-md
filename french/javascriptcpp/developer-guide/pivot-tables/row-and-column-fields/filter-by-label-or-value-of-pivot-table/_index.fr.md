---
title: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
linktitle: Filtrage des tableaux croisés dynamiques par étiquette ou valeur
description: Aspose.Cells for JavaScript via C++ prend en charge un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques. Cet article explique comment filtrer les données d’un tableau croisé dynamique à l’aide de filtres d’étiquette, de date et de valeur, de filtres des 10 premiers, ainsi qu’en masquant ou en réaffichant des éléments du tableau croisé dynamique.
keywords: Aspose.Cells, bibliothèque JavaScript via C++, tableur, tableau croisé dynamique, filtre, filtre d’étiquette, filtre de valeur, filtre de date, filtre des 10 premiers, élément de tableau croisé dynamique, masquer un élément de tableau croisé dynamique
type: docs
weight: 10
url: /fr/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit cinq stratégies pratiques pour filtrer les données affichées dans un tableau croisé dynamique. Vous pouvez appliquer des filtres d’étiquette aux champs de ligne ou de colonne contenant du texte, utiliser des filtres de date lorsque le champ contient uniquement des cellules contenant une date et une heure ou des cellules vides, appliquer des filtres de valeur aux valeurs numériques agrégées, utiliser des filtres des 10 premiers pour classer les éléments selon un champ de valeur, ou masquer et réafficher manuellement des éléments du tableau croisé dynamique à l’aide de la propriété `isHidden`. Chaque stratégie est disponible au moyen d’API dédiées sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les tableaux croisés dynamiques sont de puissants outils d’analyse, mais les synthèses brutes contiennent souvent beaucoup plus d’informations que vous n’avez à présenter. Le filtrage est le principal mécanisme permettant de limiter un tableau croisé dynamique aux lignes, aux colonnes ou aux valeurs pertinentes pour un rapport donné. Aspose.Cells for JavaScript via C++ reproduit les capacités de filtrage disponibles dans Microsoft Excel et les expose de manière programmatique afin d’automatiser entièrement la génération des rapports.
Les stratégies de filtrage suivantes sont présentées dans cet article :
1. **Filtre d’étiquette** — filtre les éléments d’un champ de ligne ou de colonne en fonction de leurs libellés textuels.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui contiennent uniquement des valeurs de date et d’heure ou des valeurs vides.
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d’un champ de données.
4. **Filtre des 10 premiers** — affiche uniquement les N premiers ou les N derniers éléments, classés selon un champ de valeur.
5. **Masquage / réaffichage des éléments du tableau croisé dynamique** — contrôle manuellement la visibilité de chaque élément dans un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après avoir appliqué un filtre, vous devez appeler `pivotCache.refresh()` sur le tableau croisé dynamique afin que les données en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre d’étiquette**
Un filtre d’étiquette permet de filtrer les éléments d’un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cette solution est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre donnée, contiennent un mot particulier ou satisfont à un autre critère fondé sur le libellé.
Aspose.Cells expose le filtrage par étiquette via la méthode `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. L’argument `filterType` sélectionne le mode de comparaison, notamment `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank` ou `CaptionIsBlank`. Les arguments `label1` et `label2` fournissent le texte de comparaison ; transmettez `""` pour `label2` lorsque vous n’avez besoin que d’une seule valeur de comparaison (par exemple, pour une comparaison de type « commence par » ou « contient »).
L’exemple suivant charge un classeur contenant un tableau croisé dynamique existant, applique un filtre d’étiquette afin que seuls les éléments dont les libellés commencent par le préfixe spécifié restent visibles, actualise le tableau croisé dynamique et enregistre le résultat.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Charger le classeur existant contenant un tableau croisé dynamique
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Accéder à la feuille de calcul par index (première feuille de calcul)
                    const worksheet = workbook.worksheets.get(0);
                    // Accéder au tableau croisé dynamique par index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Récupérer le premier PivotField de ligne
                    const rowField = pivotTable.rowFields.get(0);
                    // Appliquer le filtre d’étiquette — afficher uniquement les éléments de ligne dont les étiquettes commencent par le préfixe fourni
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Actualiser et recalculer les données du tableau croisé dynamique afin que le filtre prenne effet
                    pivotTable.refreshData();
                    // Enregistrer le classeur sur le disque
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Filtre de date**
Les filtres de date permettent de limiter un tableau croisé dynamique selon des critères fondés sur des dates, tels qu’aujourd’hui, la semaine dernière, ce mois-ci, le trimestre prochain ou une plage de dates spécifique. Ce sont des filtres spécialisés qui ne fonctionnent qu’avec des champs stockant des informations relatives à la date et à l’heure.

{{% alert color="primary" %}}
Le filtre de date ne fonctionne que si la zone des lignes ou des colonnes contient uniquement des cellules contenant une date et une heure ou des valeurs vides. Si le champ sous-jacent contient d’autres types de données, tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Vérifiez que le champ est formaté comme une date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d’appliquer ce filtre.
Aspose.Cells expose le filtrage par date via la méthode `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. L’énumération `PivotFilterType` contient des valeurs spécifiques aux dates, telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous transmettez une ou deux valeurs `DateTime`. Pour `Between`, transmettez les dates de début et de fin.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique dont la zone des lignes contient un champ de date, applique un filtre de date qui restreint les éléments visibles à une plage de dates particulière, actualise le tableau croisé dynamique et enregistre le classeur.
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
        const { Workbook } = AsposeCells;
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Charger le classeur existant qui contient le tableau croisé dynamique
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Accéder à la feuille de calcul qui contient le tableau croisé dynamique (par index)
                const worksheet = workbook.worksheets.get(0);
                // Accéder au tableau croisé dynamique par index
                const pivotTable = worksheet.pivotTables.get(0);
                // Récupérer le champ PivotField de date de la zone de lignes
                // (Le filtre de date fonctionne uniquement lorsque la zone de lignes ou de colonnes contient uniquement des cellules date-heure ou des valeurs vides)
                const dateField = pivotTable.rowFields.get(0);
                // Définir le critère de date pour le filtre Between
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Appliquer le filtre de date au champ du tableau croisé dynamique
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Actualiser et recalculer le tableau croisé dynamique afin que le filtre prenne effet
                pivotTable.refreshData();
                // Enregistrer le classeur
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Filtre de valeur**
Les filtres de valeur agissent sur les valeurs agrégées calculées par un tableau croisé dynamique dans sa zone de données. Au lieu de comparer des étiquettes de texte, ils comparent des totaux numériques à une valeur seuil. Ils permettent notamment d’afficher uniquement les produits dont la somme des ventes dépasse un montant cible, ou seulement les régions dont le nombre de transactions se situe dans une plage donnée.
Aspose.Cells expose le filtrage par valeur via la méthode `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Le paramètre `valueFieldIndex` spécifie le champ de données qui doit être évalué (utilisez `pivotTable.getDataFields().indexOf(dataField)` ou parcourez la collection pour en trouver la position). Le paramètre `filterType` peut prendre des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Les deux arguments `double` fournissent la ou les valeurs de seuil.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique, applique un filtre de valeur qui conserve uniquement les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le tableau croisé dynamique et enregistre le classeur.

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
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Trouver manuellement l'index du champ de données, car PivotFieldCollection ne possède pas IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.refreshData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Filtre des 10 premiers**
Le filtre des 10 premiers est une forme spécialisée de filtre de valeur qui ne conserve que les N premiers ou les N derniers éléments, selon un champ de valeur choisi. Il est couramment utilisé pour les rapports de classement, tels que « les 10 produits générant le plus de revenus » ou « les 5 régions ayant le nombre de ventes le plus faible ».

{{% alert color="primary" %}}
Le filtre des 10 premiers n’est efficace que lorsque le tableau croisé dynamique comporte un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n’existe aucune mesure agrégée permettant de classer les éléments et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtrage des 10 premiers via la méthode `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Le paramètre `valueFieldIndex` correspond à l’indice du champ de données dont les valeurs agrégées servent à classer les éléments. Le paramètre `filterType` sélectionne l’unité de `itemCount` : `Count` conserve un nombre fixe d’éléments, tandis que `Percent` conserve un pourcentage d’éléments ; dans ce cas, `itemCount` représente lui-même le pourcentage. Le paramètre `isTop` indique s’il faut conserver les éléments les plus élevés (true) ou les plus bas (false), et `itemCount` définit le nombre d’éléments ou le pourcentage d’éléments à conserver.
L’exemple suivant charge un classeur contenant un tableau croisé dynamique qui comprend un champ de valeur, applique un filtre des 10 premiers afin de conserver uniquement les 10 éléments dont la somme des ventes est la plus élevée, actualise le tableau croisé dynamique et enregistre le classeur.
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
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Charger le classeur existant qui contient le tableau croisé dynamique
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Accéder à la feuille de calcul qui contient le tableau croisé dynamique (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Accéder au tableau croisé dynamique par index
                const pivotTable = worksheet.pivotTables.get(0);
                // Vérifier qu'il existe au moins un PivotField de valeur dans la zone de données
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Récupérer le PivotField de ligne cible (le champ sur lequel nous voulons appliquer le Top 10)
                const rowField = pivotTable.rowFields.get(0);
                // Le premier (et unique) champ de données se trouve à l'index 0 ; le Top 10 classe les éléments selon celui-ci.
                const valueFieldIndex = 0;
                // Appliquer le filtre Top 10 au champ de ligne :
                //   - valueFieldIndex = 0 — le champ de données utilisé pour classer les éléments
                //   - filterType  = PivotFilterType.Count (conserver un nombre fixe d'éléments ;
                //     PivotFilterType.Percent interpréterait 10 comme « 10 pour cent les plus élevés »)
                //   - isTop       = true (N premiers ; false signifierait N derniers)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Actualiser les données du tableau croisé dynamique et le recalculer afin que le filtre soit appliqué
                pivotTable.refreshData();
                // Enregistrer le classeur
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Filtrage par masquage ou réaffichage des éléments du tableau croisé dynamique**
En plus des API de filtrage structuré, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément d’un tableau croisé dynamique. En parcourant la collection `pivotField.getPivotItems()` d’un `PivotField` et en basculant la propriété `isHidden`, vous pouvez masquer sélectivement des éléments spécifiques sans appliquer de filtre basé sur une formule. L’affectation `pivotItem.isHidden = true` masque l’élément dans le tableau croisé dynamique ; l’affectation `pivotItem.isHidden = false` le rend à nouveau visible.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou spécifique à un élément, par exemple pour masquer quelques catégories identifiées par leur nom qui ne doivent pas apparaître dans un rapport donné. L’exemple ci-dessous charge un tableau croisé dynamique, masque un élément spécifique par son nom, montre comment le réafficher, actualise le tableau croisé dynamique et enregistre le classeur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Charger un classeur existant contenant un tableau croisé dynamique
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Accéder à la première feuille de calcul qui contient le tableau croisé dynamique
                const sheet = workbook.worksheets.get(0);
                // Accéder au tableau croisé dynamique par index (le premier tableau croisé dynamique de la feuille)
                const pivotTable = sheet.pivotTables.get(0);
                // Récupérer le champ cible (le premier champ d'étiquette de ligne dans lequel nous masquerons ou afficherons des éléments)
                const pivotField = pivotTable.rowFields.get(0);
                // Parcourir la collection PivotItems du champ PivotField sélectionné
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Masquer les éléments du tableau croisé dynamique qui correspondent à un nom ou critère spécifique
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Démontrer l'affichage : afficher de nouveau un élément du tableau croisé dynamique previously hidden
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Actualiser et recalculer le tableau croisé dynamique afin que les modifications prennent effet
                pivotTable.refreshData();
                // Enregistrer le classeur — les éléments masqués restent dans les données sous-jacentes
                // mais sont exclus de la sortie affichée du tableau croisé dynamique
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Résumé**
Aspose.Cells for JavaScript via C++ fournit un ensemble complet de fonctionnalités de filtrage des tableaux croisés dynamiques. Ces fonctionnalités correspondent à celles disponibles dans Microsoft Excel. Les filtres d’étiquette, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre des 10 premiers prend en charge les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `pivotItem.isHidden` offre une solution de repli flexible au niveau de chaque élément. La combinaison de ces stratégies — par exemple, l’application d’un filtre d’étiquette suivie du masquage d’éléments spécifiques — vous permet de créer par code des rapports de tableau croisé dynamique précisément ciblés.

{{< app/cells/assistant language="javascript-cpp" >}}