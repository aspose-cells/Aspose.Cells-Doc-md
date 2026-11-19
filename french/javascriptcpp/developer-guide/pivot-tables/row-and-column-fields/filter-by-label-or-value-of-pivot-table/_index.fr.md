---
title: Filtrage des Tableaux Croisés Dynamiques par libellé ou valeur
description: Aspose.Cells for JavaScript via C++ prend en charge des capacités de filtrage complètes pour les Tableaux Croisés Dynamiques. Cet article explique comment filtrer les données d’un Tableau Croisé Dynamique à l’aide de filtres de libellé, de filtres de date, de filtres de valeur, de filtres Top 10 et en masquant ou en affichant des éléments du Tableau Croisé Dynamique.
linktitle: Filtrage par libellé ou valeur
keywords: Aspose.Cells, bibliothèque JavaScript via C++, feuille de calcul, Tableau Croisé Dynamique, filtre, filtre de libellé, filtre de valeur, filtre de date, filtre Top 10, élément de Tableau Croisé Dynamique, masquer un élément de Tableau Croisé Dynamique
type: docs
weight: 10
url: /fr/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit cinq stratégies pratiques pour filtrer les données affichées dans un Tableau Croisé Dynamique. Vous pouvez appliquer des filtres de libellé aux champs de ligne ou de colonne fondés sur du texte, utiliser des filtres de date lorsque le champ contient uniquement des cellules date-heure ou vides, appliquer des filtres de valeur aux nombres agrégés, utiliser des filtres Top 10 pour classer les éléments selon un champ de valeur, ou masquer et afficher manuellement des éléments individuels du Tableau Croisé Dynamique à l’aide de la propriété `isHidden`. Chaque stratégie est accessible via des API dédiées présentes sur les classes `PivotField` et `PivotItem`.
{{% /alert %}}

## **Introduction**
Les Tableaux Croisés Dynamiques sont de puissants outils d’analyse, mais les synthèses brutes contiennent souvent bien plus d’informations que vous n’avez besoin d’en présenter. Le filtrage est le principal mécanisme permettant de réduire un Tableau Croisé Dynamique aux lignes, aux colonnes ou aux valeurs qui importent pour un rapport donné. Aspose.Cells for JavaScript via C++ reproduit les capacités de filtrage disponibles dans Microsoft Excel, en les exposant par programme afin que la génération des rapports puisse être entièrement automatisée.
Les stratégies de filtrage suivantes sont abordées dans cet article :
1. **Filtre de libellé** — filtre les éléments d’un champ de ligne ou de colonne en fonction de leurs libellés textuels.
2. **Filtre de date** — filtre les champs de ligne ou de colonne qui contiennent uniquement des valeurs date-heure (ou vides).
3. **Filtre de valeur** — filtre les éléments en fonction des valeurs agrégées d’un champ de données.
4. **Filtre Top 10** — affiche uniquement les N éléments en tête ou en queue, classés selon un champ de valeur.
5. **Masquage / Affichage des éléments du Tableau Croisé Dynamique** — contrôle manuellement la visibilité de chaque élément individuel dans un champ.
Chaque approche utilise une méthode différente de la classe `PivotField` ou une propriété de la classe `PivotItem`. Après l’application de tout filtre, vous devez appeler `pivotCache.refresh()` sur le Tableau Croisé Dynamique afin que les données en cache et les valeurs calculées reflètent le nouvel état du filtre.

## **Filtre de libellé**
Un filtre de libellé permet de filtrer les éléments d’un champ de ligne ou de colonne en comparant leurs libellés textuels à un motif. Cette fonctionnalité est utile lorsque vous souhaitez afficher uniquement les produits dont les noms commencent par une lettre donnée, contiennent un mot particulier ou satisfont un autre critère fondé sur le libellé.
Aspose.Cells expose le filtrage par libellé via la méthode `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. L’argument `filterType` sélectionne le mode de comparaison (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc.). Les arguments `label1` et `label2` fournissent le texte de comparaison — transmettez `""` pour `label2` lorsque vous n’avez besoin que d’une correspondance à une seule valeur, par exemple pour un filtre « commence par » ou « contient ».
L’exemple suivant charge un classeur contenant un Tableau Croisé Dynamique existant, applique un filtre de libellé de sorte que seuls les éléments dont les libellés commencent par un préfixe spécifié restent visibles, actualise le Tableau Croisé Dynamique et enregistre le résultat.

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
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
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
Les filtres de date permettent de réduire un Tableau Croisé Dynamique à l’aide de critères fondés sur les dates, tels qu’aujourd’hui, la semaine dernière, ce mois-ci, le prochain trimestre ou une plage de dates spécifique. Ce sont des filtres spécialisés qui ne fonctionnent qu’avec des champs stockant des informations date-heure.

{{% alert color="primary" %}}
Le filtre de date ne fonctionne que lorsque la zone de ligne ou de colonne contient uniquement des cellules date-heure ou des valeurs vides. Si le champ sous-jacent contient d’autres types de données, tels que des nombres ou du texte, le filtre de date ne produira pas le résultat attendu. Assurez-vous que le champ est formaté comme une date et que toutes les valeurs sont des instances `DateTime` valides ou des cellules vides avant d’appliquer ce filtre.
Aspose.Cells expose le filtrage par date via la méthode `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. L’énumération `PivotFilterType` contient des valeurs de date dédiées telles que `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` et `Between`. Selon le type de filtre choisi, vous transmettez une ou deux valeurs `DateTime` (pour `Between`, transmettez les dates de début et de fin).
L’exemple suivant charge un classeur avec un Tableau Croisé Dynamique dont la zone de ligne contient un champ de date, applique un filtre de date qui limite les éléments visibles à une plage de dates particulière, actualise le Tableau Croisé Dynamique et enregistre le classeur.
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
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
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
Les filtres de valeur agissent sur les valeurs agrégées qu’un Tableau Croisé Dynamique calcule dans sa zone de données. Au lieu de faire correspondre des libellés textuels, ils comparent des totaux numériques à un seuil. Les cas d’utilisation typiques consistent à afficher uniquement les produits dont la somme des ventes dépasse un montant cible ou uniquement les régions dont le nombre de transactions se situe dans une plage.
Aspose.Cells expose le filtrage par valeur via la méthode `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Le paramètre `valueFieldIndex` spécifie le champ de données à évaluer (utilisez `pivotTable.getDataFields().indexOf(dataField)` ou parcourez la collection pour déterminer sa position). Le paramètre `filterType` utilise des valeurs telles que `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` et `ValueLessThanOrEqual`. Les deux arguments `double` fournissent la ou les valeurs de seuil.
L’exemple suivant charge un classeur avec un Tableau Croisé Dynamique, applique un filtre de valeur qui conserve uniquement les éléments dont les ventes agrégées dépassent un seuil numérique, actualise le Tableau Croisé Dynamique et enregistre le classeur.

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
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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
                pivotTable.pivotCache.refresh();
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

## **Filtre Top 10**
Le filtre Top 10 est une forme spécialisée de filtre de valeur qui ne conserve que les N éléments les plus élevés ou les plus bas en fonction d’un champ de valeur choisi. Il est couramment utilisé pour classer des rapports tels que « 10 premiers produits par chiffre d’affaires » ou « 5 dernières régions par nombre de ventes ».

{{% alert color="primary" %}}
Le filtre Top 10 n’est efficace que lorsque le Tableau Croisé Dynamique comporte un ou plusieurs champs de valeur dans la zone de données. Sans au moins un champ de valeur, il n’existe aucune mesure agrégée pour classer les éléments, et le filtre ne peut pas être appliqué.
Aspose.Cells expose le filtrage Top 10 via la méthode `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Le paramètre `valueFieldIndex` est l’index du champ de données dont les valeurs agrégées classent les éléments, `filterType` sélectionne l’unité de `itemCount` (`Count` conserve un nombre fixe d’éléments, `Percent` conserve un pourcentage des éléments, de sorte que `itemCount` est lui-même le pourcentage), `isTop` indique s’il faut conserver les éléments les plus élevés (`true`) ou les plus bas (`false`), et `itemCount` définit le nombre d’éléments ou le pourcentage à conserver.
L’exemple suivant charge un classeur avec un Tableau Croisé Dynamique contenant un champ de valeur, applique un filtre Top 10 pour conserver uniquement les 10 éléments dont la somme des ventes est la plus élevée, actualise le Tableau Croisé Dynamique et enregistre le classeur.
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
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
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

## **Filtrage par masquage ou affichage des éléments du Tableau Croisé Dynamique**
En plus des API de filtrage structuré, Aspose.Cells vous permet de contrôler directement la visibilité de chaque élément individuel du Tableau Croisé Dynamique. En parcourant la collection `pivotField.getPivotItems()` d’un `PivotField` et en basculant la propriété `isHidden`, vous pouvez masquer sélectivement des éléments spécifiques sans appliquer de filtre fondé sur une formule. L’affectation `pivotItem.isHidden = true` masque l’élément du Tableau Croisé Dynamique ; l’affectation `pivotItem.isHidden = false` l’affiche et le rend à nouveau visible.
Cette approche est utile lorsque la règle de filtrage est irrégulière ou propre à un élément, par exemple pour masquer un petit nombre de catégories nommées qui ne doivent pas apparaître dans un rapport particulier. L’exemple ci-dessous charge un Tableau Croisé Dynamique, masque un élément spécifique par son nom, montre comment l’afficher, actualise le Tableau Croisé Dynamique et enregistre le classeur.

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
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
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
Aspose.Cells for JavaScript via C++ fournit un ensemble complet de capacités de filtrage des Tableaux Croisés Dynamiques qui correspondent à celles disponibles dans Microsoft Excel. Les filtres de libellé, de date et de valeur couvrent les scénarios analytiques les plus courants, tandis que le filtre Top 10 gère les rapports de classement. Lorsque la règle de filtrage est irrégulière, la propriété `pivotItem.isHidden` offre une solution de repli flexible au niveau de l’élément. La combinaison de ces stratégies — par exemple, l’application d’un filtre de libellé suivie du masquage d’éléments spécifiques — vous permet de créer entièrement par code des rapports de Tableau Croisé Dynamique précisément ciblés.

{{< app/cells/assistant language="javascript-cpp" >}}