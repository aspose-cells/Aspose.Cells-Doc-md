---
title: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
linktitle: Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux classés ou les moins bien classés d’un champ de tableau croisé dynamique à l’aide de Aspose.Cells for JavaScript via C++. Cet article présente les propriétés AutoShow d’Excel 97-2003 (notamment isAutoShow), la releture des options et le filtre Top 10 d’Excel 2007-365 via filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, tableau croisé dynamique, top 10, affichage automatique, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /fr/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie tous les éléments d’un champ de ligne peut être difficile à lire lorsque ce champ comporte des dizaines d’éléments. Un rapport Top 10 ne conserve que les éléments les mieux classés ou les moins bien classés, ce qui correspond précisément aux besoins des rapports de classement — « les 5 meilleurs produits par chiffre d’affaires » ou « les 3 régions les moins performantes par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet effet, qui correspondent à deux générations de Microsoft Excel.
- **AutoShow d’Excel 97-2003** — les quatre propriétés de `PivotField` suivantes : `isAutoShow`, `isAscendShow`, `autoShowCount` et `autoShowField`. Il s’agit du paramètre classique « Afficher les N premiers/derniers éléments », directement stocké sur le champ du tableau croisé dynamique. Il fonctionne avec toutes les versions d’Excel, qu’elles soient anciennes ou récentes, car il fait partie du format d’origine du tableau croisé dynamique.
- **Filtre Top 10 d’Excel 2007-365** — la méthode `PivotField.filterTop10()`. Il s’agit du filtre de valeurs Top 10 moderne accessible dans le menu du champ, sous « Filtres de valeurs ». Il est stocké sous forme d’objet `PivotFilter` associé au champ et propose un classement fondé sur le nombre d’éléments ou sur un pourcentage.

## **Afficher les 10 premiers éléments dans Excel 97-2003 (AutoShow)**
Le paramètre AutoShow classique se configure par quatre affectations de propriétés de `PivotField` :
- `isAutoShow` — active ou désactive le paramètre AutoShow du champ.
- `isAscendShow` — `false` conserve les éléments les mieux classés (« Haut »), `true` conserve les moins bien classés (« Bas »).
- `autoShowCount` — indique le nombre d’éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `autoShowField` — l’index (à partir de zéro) du **champ de données** dont les valeurs déterminent le classement des éléments. Transmettez la valeur -1 pour classer les éléments selon le champ lui-même.
Le classement peut être effectué à partir d’un champ de valeurs ou du champ lui-même. Deux variantes sont présentées ci-dessous.

### **Classer selon un champ de valeurs**
Classez les éléments du champ de ligne en fonction d’un champ de valeurs standard, tel que Sum of Sales. L’exemple suivant construit un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les mieux classés selon les ventes. `rankBy` vaut 0, car « Sum of Sales » est le champ de données situé à l’index 0.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Afficher les 2 premiers éléments classés par « Sum of Sales » (index 0 du champ de données)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Classer selon le champ lui-même**
Un champ peut également se classer lui-même — transmettez la valeur -1 à `autoShowField`. Cette variante ne nécessite aucun champ de données supplémentaire ; le champ doit simplement se trouver dans la zone des lignes ou des colonnes. L’exemple suivant affiche les 3 sports les moins bien classés selon le champ lui-même. Lorsque ce paramètre est enregistré, l’attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut de ce format. La valeur -1 est relue par `autoShowField`.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Afficher les 3 derniers éléments classés par le champ lui-même (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Lire les options AutoShow actuelles**
Les propriétés `isAutoShow`, `isAscendShow`, `autoShowCount` et `autoShowField` de `PivotField` exposent les options AutoShow actuellement stockées sur le champ. Utilisez-les pour examiner la façon dont un classeur existant, ou un tableau croisé dynamique que vous venez de configurer, affichera ses éléments, notamment lorsque le classeur a été chargé à partir d’un fichier.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Par conséquent, les valeurs relues sont celles que toutes les versions d’Excel appliquent.

## **Remarque**

{{% alert color="primary" %}}
- Après avoir modifié une propriété AutoShow, appelez à nouveau `pivotTable.calculateData()` : les paramètres ne prennent effet dans la mise en page affichée qu’au prochain recalcul.
- Les paramètres AutoShow fonctionnent avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de filtres ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre Top 10 (filterTop10)**
Les versions récentes d’Excel proposent un filtre de valeurs Top 10 dans le menu du champ (Filtres de valeurs, Top 10...). Aspose.Cells représente ce filtre au moyen de la méthode `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — l’index (à partir de zéro) du champ de données dont les valeurs agrégées servent à classer les éléments.
- `type` — détermine la signification de `itemCount`. `PivotFilterType.Count` conserve un nombre fixe d’éléments (option « Éléments » de la boîte de dialogue). `PivotFilterType.Percent` conserve un pourcentage des éléments ; ainsi, `itemCount` correspond directement au pourcentage : la valeur 30 conserve les 30 % d’éléments les mieux classés. `PivotFilterType.Sum` classe les éléments selon la couverture cumulative des valeurs.
- `isTop` — `true` pour « Haut », `false` pour « Bas ».
- `itemCount` — le N dans « Top N » ; son unité dépend de `type`.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Les propriétés AutoShow et `filterTop10` constituent deux fonctionnalités distinctes. AutoShow écrit sur le champ du tableau croisé dynamique l’ensemble classique d’attributs, comprenant notamment `autoShow`. Cette fonctionnalité est prise en charge par toutes les versions d’Excel, depuis Excel 97. `filterTop10` écrit une entrée moderne de type `PivotFilter`. Le filtre qui en résulte nécessite Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version plus ancienne d’Excel, le tableau croisé dynamique qui utilise le filtre moderne affiche à nouveau tous ses éléments. Pour les documents qui doivent faire l’aller-retour via des outils hérités, préférez les propriétés AutoShow ; pour les classeurs modernes, préférez `filterTop10`, car cette méthode se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles connexes**
- [Regrouper les champs d’un tableau croisé dynamique](/cells/fr/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}