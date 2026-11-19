---
title: Afficher les valeurs comme dans le tableau croisé dynamique
linktitle: Afficher les valeurs comme dans le tableau croisé dynamique
description: Afficher les valeurs des champs de données du tableau croisé dynamique sous forme de pourcentage du total, de différence par rapport à un élément de base, de totaux cumulatifs, de classements et plus encore avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tableau croisé dynamique, afficher les valeurs comme, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /fr/javascript-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique agrège normalement chaque champ de données à l'aide d'une fonction d'agrégation telle que `Sum` ou `Count`. La fonction **Show Values As** d’Excel remplace chaque résultat affiché par un calcul secondaire dérivé de cet agrégat — par exemple, un pourcentage du total général, un total cumulé, une différence par rapport à un élément de base choisi ou un classement — vous permettant d'effectuer une analyse comparative sans formules auxiliaires ni colonnes calculées.  
Les utilisations typiques comprennent l'analyse de **la** part du total, incluant les pourcentages d’une ligne, d’une colonne ou du total général ; le reporting cumulé à l’aide d’un total cumulé dans un champ de période ; l’analyse des écarts par rapport à un élément de référence en utilisant la différence ou la différence en pourcentage par rapport à un élément de base ; et le classement des valeurs du plus petit au plus grand ou du plus grand au plus petit.  
Dans Aspose.Cells for JavaScript via C++, l’énumération `PivotShowValuesAsType` sélectionne le calcul secondaire. La propriété en lecture seule `PivotField.showValuesSetting` renvoie un objet `PivotShowValuesSetting`, dont les propriétés modifiables `showValuesAs`, `baseFieldIndex` et `baseItemIndex` configurent le comportement ; la méthode de commodité `PivotField.showValuesAs(...)` applique les mêmes paramètres en un seul appel. Appliquez ces paramètres à un champ de données ou de valeurs obtenu à partir de `PivotTable.dataFields`.

## **Membres de l'énumération PivotShowValuesAsType**
La fonction de champ de données conserve sa fonction d'agrégation, telle que Sum ou Count, tandis que Show Values As ne transforme que la façon dont la valeur agrégée est affichée.  
En plus d'écrire directement les propriétés `PivotShowValuesSetting` (voir la dernière section), une méthode de commodité **en un appel** applique la même configuration. Elle se présente sous deux formes — l’une adressant le champ de base et l’élément de base par indice, l’autre par nom :

```html
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Paramètre | Signification | Quand c'est requis |
| --- | --- | --- |
| `showValuesAsType` | Le calcul secondaire `PivotShowValuesAsType` à appliquer. | Toujours. |
| `baseField` | Indice basé sur zéro du champ de base parmi les champs de base du tableau croisé dynamique (par exemple, l’indice du champ de ligne auquel appartient l’élément de base), ou — dans la forme nom — le nom du champ de base. | Les huit formats relatifs au champ de base ci‑dessous (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) ; passez `0` (ou `null` dans la forme nom) pour tout autre format. |
| `baseItem` | Indice basé sur zéro de l’élément de base, avec deux sentinelles : -1 sélectionne l’élément précédent et -2 l’élément suivant (la liaison JavaScript via C++ n’exporte pas les constantes nommées — passez les valeurs littérales). La forme nom utilise à la place la légende de l’élément de base, et `null` lorsque le format sélectionné n’a pas besoin d’un élément de base. | Seulement les trois formats d’élément de base (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) évaluent l’élément de base ; les cinq formats relatifs au champ (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, les deux classements) l’ignorent — passez `0` ou `null`. |

| Type de calcul | Comportement | Paramètres de l'élément de base |
| --- | --- | --- |
| `Normal` | Aucun calcul secondaire ; la valeur agrégée est affichée telle quelle (par défaut). | — |
| `DifferenceFrom` | Affiche la valeur comme une différence par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PercentageOf` | Affiche la valeur comme un pourcentage de la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `PercentageDifferenceFrom` | Affiche la valeur comme la différence en pourcentage par rapport à la valeur d’un élément de base dans un champ de base. | `baseField` + `baseItem` (un indice ou une légende, ou la sentinelle précédent/suivant) |
| `RunningTotalIn` | Affiche la valeur comme un total cumulé pour les éléments successifs d’un champ de base. | `baseField` (le champ dont l’ordre des éléments pilote l’accumulation) |
| `PercentageOfRow` | Affiche la valeur comme un pourcentage du total de la ligne. | — |
| `PercentageOfColumn` | Affiche la valeur comme un pourcentage du total de la colonne. | — |
| `PercentageOfTotal` | Affiche la valeur comme un pourcentage du total général. | — |
| `Index` | Affiche la valeur en utilisant la formule d’index Excel ((valeur * total général) / (total de ligne * total de colonne)). | — |
| `PercentageOfParentRowTotal` | Affiche la valeur comme un pourcentage de son total de ligne parent (pour les champs de ligne imbriqués). | — |
| `PercentageOfParentColumnTotal` | Affiche la valeur comme un pourcentage de son total de colonne parent (pour les champs de colonne imbriqués). | — |
| `PercentageOfParentTotal` | Affiche la valeur comme un pourcentage de son total parent. | `baseField` (le champ parent dont le total sert de référence) |
| `PercentageOfRunningTotalIn` | Affiche la valeur comme un pourcentage d’un total cumulé dans un champ de base. | `baseField` (le champ d’accumulation) |
| `RankSmallestToLargest` | Classe la valeur du plus petit (1) au plus grand. | `baseField` (le champ dont les éléments définissent le périmètre de classement) |
| `RankLargestToSmallest` | Classe la valeur du plus grand (1) au plus petit. | `baseField` (le champ dont les éléments définissent le périmètre de classement) |

{{% alert color="primary" %}}
`showValuesAs(...)` écrit les propriétés `PivotShowValuesSetting` (`showValuesAs`, `baseFieldIndex` et `baseItemIndex`) — la méthode et l’objet de propriété sont deux manières de configurer le même état, reflétant les sélecteurs de champ de base et d’élément de base dans la boîte de dialogue Show Values As d’Excel.
{{% /alert %}}

## **Afficher les valeurs en pourcentage du total**
Appelez la méthode `PivotField.showValuesAs` avec `PivotShowValuesAsType.PercentageOfTotal` pour convertir chaque cellule de champ de données, y compris le total général, en sa part du total général. Les nombres affichés sont ainsi des proportions de l’ensemble complet des résultats. Ce format mesure chaque valeur uniquement par rapport au total général, il ne nécessite donc aucun champ de base ni aucun élément de base — les arguments de fin (`0`, `0`) sont des espaces réservés que le format ignore, comme le indique le tableau des paramètres ci‑dessus.

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
                // base arguments (0, 0) are placeholders the format ignores
                const dataField = pivotTable.dataFields.get(0);
                dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
                pivotTable.calculateData();
                // Body now reads (underlying values are fractions, shown with the
                // percentage format): Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
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
Lisez la configuration actuelle via `PivotField.showValuesSetting` : la propriété en lecture seule renvoie l’objet `PivotShowValuesSetting` du champ, dont les propriétés décrivent le calcul Show Values As actif. Pour modifier la configuration, appelez la méthode `PivotField.showValuesAs` — elle écrit tous les paramètres en un seul appel, vous n’avez donc jamais besoin d’assigner les propriétés une par une.  
L’objet `PivotShowValuesSetting` expose l’état que `showValuesAs` écrit :
- `showValuesAs` sélectionne le calcul secondaire `PivotShowValuesAsType`.
- `baseFieldIndex` indique l’indice basé sur zéro du champ de base parmi les champs du tableau croisé dynamique. Il est utilisé par les formats relatifs au champ.
- `baseItemIndex` indique l’élément de base : un indice basé sur zéro d’un élément pivot spécifique, ou l’une des deux valeurs sentinelles — -1 pour l’élément précédent, -2 pour l’élément suivant (la liaison n’exporte pas les constantes nommées). Il est utilisé par les formats d’élément de base.
- `baseFieldName` et `baseItemCaption` sont des vues en lecture seule qui rapportent le nom résolu du champ de base et la légende de l’élément de base ; par exemple, après avoir sélectionné la sentinelle d’élément précédent, `baseItemCaption` renvoie `(previous)`.
Après avoir appelé `showValuesAs`, appelez à nouveau `PivotTable.calculateData()` afin que le corps du tableau croisé dynamique soit recalculé et rendu avec la configuration mise à jour.

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
                    `ShowValuesAs: ${settings.showValuesAs}`,
                    `BaseFieldIndex: ${settings.baseFieldIndex}`,
                    `BaseItemIndex: ${settings.baseItemIndex}`,
                    `BaseFieldName: ${settings.baseFieldName}`,
                    `BaseItemCaption: ${settings.baseItemCaption}`
                ];
                document.getElementById('result').innerHTML = messages
                    .map(message => `<p>${message}</p>`)
                    .join("");
                // Switch to a base-item calculation with the one-call method: difference
                // from the value of the previous item in the row field
                // (-1 is the previous-item sentinel; the binding does not export the constant)
                dataField.showValuesAs(
                    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
                    pivotTable.rowFields.get(0).baseIndex,
                    -1
                );
                pivotTable.calculateData();
                // Note: the percentage number format saved by the previous example still
                // clings to the data field cells; the underlying values are now differences
                // Re-read the applied configuration
                messages.push(`ShowValuesAs now: ${dataField.showValuesSetting.showValuesAs}`);
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
- [Gestion des champs de valeurs dans le tableau croisé dynamique](/cells/fr/javascript-cpp/manage-value-fields/)
- [Actualiser le tableau croisé dynamique](/cells/fr/javascript-cpp/refresh-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}