---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Affichez les valeurs des champs de données d’un tableau croisé dynamique en pourcentage du total, en différence par rapport à un élément de base, en totaux cumulatifs, en classements, et plus avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tableau croisé dynamique, afficher les valeurs comme, format d'affichage des données, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /fr/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données avec une fonction d'agrégation telle que `Sum` ou `Count`. La fonctionnalité **Afficher les valeurs comme** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement — vous permettant d’effectuer une analyse comparative sans formules d’aide ou colonnes calculées.  
Les utilisations typiques comprennent l’analyse de **la** part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; la génération de rapports cumulatifs à l’aide d’un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage à partir d’un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for JavaScript via C++, `PivotFieldDataDisplayFormat` sélectionne le calcul secondaire. La propriété en lecture seule `PivotField.showValuesSetting` renvoie un objet `PivotShowValuesSetting`, dont les propriétés modifiables `calculationType`, `baseFieldIndex`, `baseItemPositionType` et `baseItemIndex` configurent le comportement ; la méthode pratique `PivotField.showValuesAs(...)` applique les mêmes quatre paramètres en un appel. Appliquez ces paramètres à un champ de données ou de valeur obtenu à partir de `PivotTable.dataFields`.

## **Membres de l’énumération PivotFieldDataDisplayFormat**
Le champ de données conserve sa fonction d’agrégation, comme Sum ou Count, tandis que **Afficher les valeurs comme** ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d’écrire directement les propriétés `PivotShowValuesSetting` (voir la dernière section), une méthode pratique en un appel applique la même configuration :

```html
dataField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
```

| Paramètre | Signification | Quand il est requis |
| --- | --- | --- |
| `displayFormat` | Le calcul secondaire `PivotFieldDataDisplayFormat` à appliquer. | Toujours. |
| `baseField` | Index de base zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’index du champ de ligne auquel appartient l’élément de base). | Uniquement pour les six formats relatifs à une base ci-dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`) ; ignoré par tout autre format. |
| `baseItemPositionType` | Comment l’élément de base est choisi par rapport à l’élément actuel : `PivotItemPositionType.Previous`, `.Next` ou `.Custom`. | Uniquement pour les trois formats à élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) ; ignoré par tout autre format. |
| `baseItem` | Index de base zéro de l’élément de base. | Uniquement lorsque `baseItemPositionType` est `Custom` (l’index de l’élément sélectionne l’élément de base exact) ; ignoré pour `Previous` / `Next` et pour tout format ne reposant pas sur un élément de base — passer `0`. |

| Type de calcul | Comportement | Paramètres de l’élément de base |
| --- | --- | --- |
| `Normal` | Pas de calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DifferenceFrom` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageOf` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `PercentageDifferenceFrom` | Affiche la valeur comme le pourcentage de différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` uniquement avec `Custom`) |
| `RunningTotalIn` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments pilote l’accumulation) |
| `PercentageOfRow` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur comme un pourcentage du total général. | — |
| `Index` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total de ligne * total de colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur comme un pourcentage du total de la ligne parente (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur comme un pourcentage du total de la colonne parente (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur comme un pourcentage du total parent. | `baseField` (le champ parent servant de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RankSmallestToLargest` | Classe la valeur du plus petit (1) au plus grand. | — |
| `RankLargestToSmallest` | Classe la valeur du plus grand (1) au plus petit. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit les propriétés `PivotShowValuesSetting` (`calculationType`, `baseFieldIndex`, `baseItemPositionType`, `baseItemIndex`) — la méthode et l’objet de propriété sont deux façons de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue **Afficher les valeurs comme** d’Excel.
{{% /alert %}}

## **Afficher les valeurs comme pourcentage du total**
Appelez la méthode `PivotField.showValuesAs` avec `PivotFieldDataDisplayFormat.PercentageOfTotal` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont donc lus comme des proportions de l’ensemble complet des résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni aucun élément de base — les arguments finaux (`0`, `PivotItemPositionType.Previous`, `0`) sont des paramètres factices que le format ignore, comme l’indique le tableau des paramètres ci‑dessus.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Load or create a workbook with source data
                const workbook = new Workbook();
                const dataSheet = workbook.worksheets.get(0);
                const cells = dataSheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Amount";
                const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
                const amounts = [10, 20, 30, 40, 50, 60];
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = amounts[i];
                }
                // Add a pivot table on a new worksheet
                const pivotSheetIndex = workbook.worksheets.add();
                const pivotSheet = workbook.worksheets.get(pivotSheetIndex);
                const pivotTable = pivotSheet.pivotTables.add("=Sheet1!A1:B7", 2, 2);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                // Show the Amount data field as a percentage of the grand total with the
                // one-call method; PercentageOfTotal takes no base item, so the trailing
                // base arguments (0, Previous, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
                    0,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsPercentageOfTotal.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Obtenir et configurer PivotField.showValuesSetting**
Lire la configuration actuelle via `PivotField.showValuesSetting` : la propriété en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les quatre propriétés décrivent le calcul actif d'Afficher les valeurs comme. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs` — elle écrit les quatre paramètres en un seul appel, vous n’avez donc jamais besoin d’affecter chaque propriété séparément.  
L’objet `PivotShowValuesSetting` expose les quatre propriétés écrites par `showValuesAs` :
- `calculationType` sélectionne le calcul secondaire `PivotFieldDataDisplayFormat`.
- `baseFieldIndex` spécifie l’index de base zéro du champ de base au sein des champs du tableau croisé dynamique. Il est utilisé par les formats relatifs à une base.
- `baseItemPositionType` détermine comment l’élément de base est positionné par rapport à l’élément actuel et accepte `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` ou `PivotItemPositionType.Custom`.
- `baseItemIndex` spécifie l’index de base zéro de l’élément de base et est utilisé lorsque `baseItemPositionType` est `Custom`.
Après avoir appelé `showValuesAs`, appelez à nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu à nouveau avec la configuration mise à jour.

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
        const ready = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await ready;
                const file = document.getElementById('fileInput').files[0];
                if (!file) {
                    throw new Error("Please select ShowValuesAsPercentageOfTotal.xlsx.");
                }
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(1);
                const pivotTable = worksheet.pivotTables.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Read the current show-values settings
                const settings = dataField.showValuesSetting;
                const messages = [
                    `CalculationType: ${settings.calculationType}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemPositionType: ${settings.baseItemPositionType}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                dataField.showValuesAs(
                    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    AsposeCells.PivotItemPositionType.Previous,
                    0
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`CalculationType now: ${dataField.showValuesSetting.calculationType}`);
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "ShowValuesAsDifferenceFrom.xlsx";
                downloadLink.style.display = "block";
            } catch (error) {
                document.getElementById('result').innerHTML =
                    `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Articles associés**
- [Gestion des champs de valeur dans le tableau croisé dynamique](/cells/fr/javascript-cpp/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/javascript-cpp/refresh-pivot-table/)
- [Application du style au tableau croisé dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}