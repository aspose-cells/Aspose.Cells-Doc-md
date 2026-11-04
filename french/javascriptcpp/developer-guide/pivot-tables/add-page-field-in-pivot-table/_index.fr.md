---
title: Ajouter des champs de filtre à un tableau croisé dynamique avec Aspose.Cells for JavaScript via C++
linktitle: Ajouter des champs de filtre à un tableau croisé dynamique avec Aspose.Cells for JavaScript via C++
description: Découvrez comment ajouter et configurer des champs de filtre dans des tableaux croisés dynamiques à l’aide de Aspose.Cells for JavaScript via C++, avec prise en charge du filtrage à sélection unique et multiple.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l’ensemble du cycle de vie des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre à l’aide d’une API de haut niveau ou de la collection `getPageFields()` de bas niveau. Vous pouvez ensuite piloter le filtre en mode à sélection unique, l’effacer pour afficher tous les éléments de filtre ou passer le champ en mode à sélection multiple. Les utilisateurs peuvent ainsi sélectionner plusieurs éléments de filtre simultanément à l’aide de l’interface utilisateur à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**
Un champ de filtre est un champ pivot qui détermine *quel sous-ensemble* des données sources est affiché dans le corps du tableau croisé dynamique. Pour les utilisateurs finaux, il se présente sous la forme d’une liste déroulante en haut du tableau croisé dynamique affiché dans Excel. La sélection d’un des éléments de filtre disponibles reconstruit le corps du tableau croisé dynamique, de sorte que seuls les enregistrements appartenant à l’élément sélectionné sont agrégés. Un champ devient un champ de filtre lorsqu’il est configuré avec `PivotFieldType.Page` plutôt qu’avec `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

## **Ajouter un champ de filtre**

### Ajouter un champ de filtre avec `addFieldToArea`
L’exemple suivant construit un petit jeu de données Fruit / Year / Amount, place un tableau croisé dynamique dans la cellule E3, avec `Fruit` dans la zone des lignes, `Amount` dans la zone des données et `Year` dans la zone des filtres, actualise le tableau croisé dynamique et enregistre le classeur.

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
            worksheet.name = "Data";
            // Configurer la ligne d'en-tête
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Remplir 9 lignes de données d'exemple : Fruit, Year, Amount
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // Ajouter un tableau croisé dynamique ancré dans la cellule E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Ajouter les champs à leurs zones : Fruit comme ligne, Amount comme données, Year comme champ de page
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Actualiser et calculer les données du tableau croisé dynamique
            pivotTable.calculateData();
            // Enregistrer le classeur
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### Ajouter un champ de filtre avec `getPageFields().add`
Lorsque vous travaillez déjà avec une instance de `PivotField`, vous pouvez la transmettre directement à `pivotTable.getPageFields().add(pivotField)`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seul l’ajout final du champ à la zone des filtres est remplacé par l’appel à l’API de bas niveau.

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
            // — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
            //   le Scénario 1a (données Fruit/Year/Amount, pivot en E3, Fruit→Ligne,
            //   Amount→Données). ci-dessous, nous récupérons le PivotField Year de la
            //   collection BaseFields et le transmettons à PageFields.Add — l'alternative
            //   de bas niveau à AddFieldToArea. Le résultat est
            //   fonctionnellement identique au Scénario 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // En-têtes
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Données d'exemple (9 lignes)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Ajouter un tableau croisé dynamique en E3 couvrant A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Fruit -> Ligne, Amount -> Données (Year ira dans la Page ci-dessous)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Approche de bas niveau : récupérer le PivotField Year existant depuis BaseFields
            // et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Actualiser afin que le nouveau champ de page soit reflété dans le classeur enregistré
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Filtrage à sélection unique (Affichage d’un élément de filtre)**
Par défaut, le mode à sélection unique affiche le champ de filtre sous la forme d’une liste déroulante, et la propriété entière `pivotField.currentPageItem` détermine l’élément de filtre qui pilote le corps du tableau croisé dynamique. L’affectation d’un index spécifique sélectionne cet unique élément ; l’affectation de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) efface le filtre afin que tous les éléments de filtre soient agrégés simultanément. Le mode à sélection unique est activé par défaut ; vous n’avez donc pas à l’activer explicitement.

### Afficher tous les éléments
Définir `currentPageItem` sur la valeur sentinelle `0x7FFD` équivaut à effacer le filtre : le corps du tableau croisé dynamique agrège tous les éléments de filtre comme si aucun filtre n’était appliqué.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Créer un nouveau classeur
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Remplir les données Fruit/Year/Amount
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // Créer un tableau croisé dynamique en E3
            const pivotTables = sheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:C7", 2, 4);
            // Configurer les champs du tableau croisé dynamique : Fruit→Ligne, Amount→Données, Year→Page
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Effacer le filtre de page afin que tous les éléments du champ de page soient visibles.
            // 0x7FFD (32765 en décimal) est la valeur sentinelle spéciale signifie « Tous les éléments » —
            // équivalent à sélectionner « (Tous) » dans la liste déroulante du champ de page d’Excel.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
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

### Afficher un élément spécifique
Définir `currentPageItem` sur un index correspondant à un élément ne sélectionne que cet élément de filtre. L’index correspond à la position de l’élément dans la liste triée des éléments du champ de filtre. Par exemple, `1` sélectionne le deuxième élément après le tri.

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
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Créer le classeur
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Ajouter des données d’exemple (Fruit/Année/Montant)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Ajouter un tableau croisé dynamique en E3
                const pivotTables = sheet.pivotTables;
                const pivotTable = pivotTables.add("=A1:C5", 2, 4);
                // Ajouter les champs : Fruit→Ligne, Amount→Données, Year→Page
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Opérations spécifiques au champ de page
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = deuxième élément dans l’ordre trié (par ex. « 2021 »)
                // Actualiser et calculer le tableau croisé dynamique
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Filtrage à sélection multiple**
Le filtrage à sélection multiple transforme la liste déroulante du filtre en liste de cases à cocher et permet à l’utilisateur final de sélectionner plusieurs éléments de filtre simultanément. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. La propriété `pivotField.isMultipleItemSelectionAllowed` doit être définie à `true` avant que l’interface de sélection multiple ne prenne effet. Une fois cette option activée, `pivotItem.isHidden` détermine les éléments qui apparaissent dans la liste de cases à cocher. Vous pouvez ainsi afficher tous les éléments ou n’autoriser que des éléments spécifiques.

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
                //   le scénario 1a (données Fruit/Year/Amount, pivot en E3, Fruit→Ligne,
                //   Amount→Données, Year→Page via AddFieldToArea).
                //   Ci-dessous, nous appliquons un filtrage multi-sélection sur le champ de page.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Données d'exemple : Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTable = pivots.add("=A1:C10", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Activer la multi-sélection sur le champ de page
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Partie A — sélectionner TOUS les éléments (rendre chaque élément visible)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Partie B — sélectionner uniquement des éléments spécifiques selon leur valeur source
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Note :** Lors de l’utilisation du filtrage à sélection multiple via `pivotItem.isHidden`, **au moins un `PivotItem` doit rester visible** (`isHidden === false`). Si tous les éléments sont masqués, Excel échoue à l’ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste d’éléments autorisés pour la sélection multiple contient au moins un élément provenant de vos données sources.

## **Quelle API et quel mode dois-je utiliser ?**
Le tableau ci-dessous présente les situations dans lesquelles utiliser chaque API et chaque mode, afin de vous aider à choisir la combinaison adaptée sans avoir à lire tous les scénarios en détail.
| Scénario / Cas d’utilisation | API recommandée | Propriété utilisée | Remarques |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (cas le plus courant) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | s.o. | API de haut niveau, sur une seule ligne. Utilisez cette API sauf si vous avez besoin d’une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous disposez déjà d’un objet `PivotField` | `pivotTable.getPageFields().add(pivotField)` | s.o. | Utilisez cette méthode lorsque l’objet de champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer afin d’afficher un seul élément de filtre (mode par défaut) | `pivotField.currentPageItem` | définie sur un index spécifique | Par exemple, `1` affiche le deuxième élément de la liste triée. |
| Afficher tous les éléments / effacer le filtre | `pivotField.currentPageItem` | définie sur `0x7FFD` | La valeur sentinelle `0x7FFD` (32765 en décimal) correspond à « tous les éléments ». |
| Activer l’interface de sélection multiple dans Excel | `pivotField.isMultipleItemSelectionAllowed` | définie sur `true` | Obligatoire avant que toute affectation à `isHidden` prenne effet. |
| Masquer / afficher des éléments individuels dans une liste de sélection multiple | `pivotItem.isHidden` | définie pour chaque élément | Au moins un élément doit rester visible (`isHidden === false`). |

{{% alert color="primary" %}}
N’oubliez pas la contrainte de visibilité lors de la configuration du filtrage à sélection multiple. Si tous les `PivotItem` d’un champ de filtre à sélection multiple sont masqués, Excel échoue à l’ouverture du fichier ou affiche un tableau croisé dynamique vide. Établissez votre liste d’éléments autorisés à partir de vos données sources afin qu’au moins un élément reste visible. Les classeurs enregistrés pourront ainsi s’ouvrir de manière fiable sur chaque ordinateur.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}