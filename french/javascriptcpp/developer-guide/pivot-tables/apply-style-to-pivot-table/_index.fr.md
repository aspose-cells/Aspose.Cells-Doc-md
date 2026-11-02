---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++
description: Découvrez comment appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++, notamment les formats automatiques XLS hérités, les styles nommés modernes d’Excel 2007+, les styles personnalisés de tableau croisé dynamique et le raccourci FormatAll.
keywords: Aspose.Cells for JavaScript via C++ style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permet d’appliquer à la fois les formats automatiques hérités des tableaux croisés dynamiques (destinés aux fichiers `.xls`) et les styles modernes, nommés ou personnalisés, de tableau croisé dynamique (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L’API que vous devez appeler dépend du format dans lequel le classeur est enregistré, et non du format dans lequel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre ces API est déterminé par le format dans lequel vous enregistrez le classeur, et non par celui à partir duquel vous le lisez. Un classeur chargé depuis un fichier `.xls` peut être réenregistré au format `.xlsx` ; dans ce cas, l’API de style moderne s’applique plutôt que l’API héritée.
- `pivotTable.pivotTableStyleType` sélectionne l’un des styles nommés intégrés (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `pivotTable.pivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même via `workbook.worksheets.tableStyles.addPivotTableStyle(...)`. Les styles personnalisés sont requis lorsque vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce qu’offrent les préréglages.
En outre, `pivotTable.formatAll(style)` est un raccourci qui applique un seul objet `style` à chaque cellule du tableau croisé dynamique, en remplaçant la mise en forme définie par l’une ou l’autre des API ci-dessus. Cette méthode est utile lorsque vous souhaitez une apparence uniforme, indépendamment du thème sous-jacent.

## **Appliquer un format automatique prédéfini pour les fichiers XLS hérités**
`pivotTable.autoFormatType` accepte une valeur de l’énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic`, ainsi que `Table1` à `Table10`.
L’exemple suivant charge un nouveau classeur, remplit le jeu de données d’exemple Fruit/Year/Amount, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.Report5` et enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}
**Pourquoi aucun champ de colonne ?** Les formats automatiques `Report1` à `Report10` et `Table1` à `Table10` ont été conçus dans Excel classique pour des **tableaux croisés dynamiques à une seule dimension** comportant uniquement des champs de ligne et des valeurs — ils ne proposent aucune mise en forme intégrée pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes de `PivotTableStyleType` présentés dans le [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), conçus pour la disposition bidimensionnelle utilisée par Excel moderne.
{{% /alert %}}

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
            // Scénario 1 : Appliquer un formatage automatique prédéfini XLS hérité
            // API utilisée : PivotTable.AutoFormatType
            // Format de fichier cible : .xls (hérité)
            // Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Créer un nouveau classeur
            const workbook = new Workbook();
            // Obtenir la première feuille de calcul
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Remplir les données source avec une ligne d’en-tête (Fruit, Year, Amount)
            // et 9 lignes de données couvrant le raisin, la myrtille, le kiwi et la cerise en 2020 et 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Ajouter un tableau croisé dynamique à la cellule de destination E3, en utilisant la plage source A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Affecter les champs : Fruit -> Lignes, Amount -> Données
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Appliquer le formatage automatique prédéfini « Report5 » pour XLS hérité
            // Remarque : cette propriété n’est prise en compte que lors de l’enregistrement au format .xls.
            // Lorsqu’il est enregistré au format .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
            // et utilise les valeurs spécifiées par PivotTableStyleType / PivotTableStyleName.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Enregistrer le classeur au format .xls hérité
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Appliquer un style moderne, nommé et prédéfini de tableau croisé dynamique**
`pivotTable.pivotTableStyleType` sélectionne l’un des styles nommés intégrés qu’Excel 2007 a introduits pour les tableaux croisés dynamiques. L’énumération `PivotTableStyleType` expose trois familles de thèmes : la famille des thèmes clairs (de `PivotTableStyleLight1` à `PivotTableStyleLight28`), la famille des thèmes moyens (de `PivotTableStyleMedium1` à `PivotTableStyleMedium28`) et la famille des thèmes sombres (de `PivotTableStyleDark1` à `PivotTableStyleDark28`). Elle définit également `None` et `Custom`. Les membres portant les numéros les plus élevés de chaque famille sont les styles ajoutés dans Excel 2017.
Ces préréglages sont en lecture seule. Lorsque vous souhaitez modifier les couleurs, les bordures ou les polices au-delà des options fournies par un préréglage, vous devez définir un style personnalisé de tableau croisé dynamique, comme le montre le [Scénario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Pourquoi utiliser les préréglages modernes plutôt que les formats automatiques de série de rapports ?** Les valeurs `Report1` à `Report10` et `Table1` à `Table10` de `PivotTableAutoFormatType` précèdent l’introduction des champs de colonne dans les tableaux croisés dynamiques ; elles ne comportent donc aucune mise en forme pour les en-têtes de champs de colonne, et Excel affiche ces en-têtes sans mise en forme. Les préréglages `PivotTableStyleType` ont été conçus pour la disposition bidimensionnelle utilisée par Excel moderne et appliquent la même mise en forme aux en-têtes de champs de ligne et de colonne.
{{% /alert %}}

Ce scénario réutilise le jeu de données Fruit/Year/Amount du Scénario 1, ajoute `Year` à la zone des colonnes à côté du champ de ligne `Fruit` via `PivotFieldType.Column`, applique le préréglage `PivotTableStyleDark1` du thème sombre avec `pivotTable.pivotTableStyleType` et enregistre le résultat au format `.xlsx` — le format auquel `PivotTableStyleType` s’applique.

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
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scénario 2 : Appliquer un style prédéfini moderne nommé d’Excel 2007+ à l’aide de PivotTableStyleType.
            // Format de fichier cible : .xlsx. L’énumération PivotTableStyleType se trouve dans l’espace de noms Aspose.Cells
            // (et non dans Aspose.Cells.Pivot) -- c’est pourquoi nous n’avons besoin d’aucune instruction using supplémentaire.
            // Référence GitHub : https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Ligne d’en-tête : Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 lignes de données de Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Ajouter un tableau croisé dynamique à E3, utilisant A1:C10 comme source
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Affecter les champs du tableau croisé dynamique : Fruit -> zone des lignes, Year -> zone des colonnes, Amount -> zone des données
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Appliquer un style moderne prédéfini et nommé de tableau croisé dynamique pour Excel 2007+.
            // PivotTableStyleType est l’API correcte pour les fichiers .xlsx / .xlsm / .xlsb ; AutoFormatType
            // est ignoré par Excel pour ces formats. PivotTableStyleDark1 appartient à la famille des thèmes
            // sombres (PivotTableStyleDark1..PivotTableStyleDark28), et la même énumération expose également
            // les thèmes clair/sombre plus récents d’Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Enregistrer au format .xlsx moderne -- c’est le format pour lequel PivotTableStyleType est pertinent.
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

## **Définir et appliquer un style personnalisé de tableau croisé dynamique**
Les préréglages intégrés ne peuvent pas être modifiés. Lorsque vous souhaitez remplacer les couleurs, les bordures ou les polices des préréglages, vous devez définir un style personnalisé de tableau croisé dynamique. Le flux de travail comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `tableStyles` du classeur à l’aide de `workbook.worksheets.tableStyles.addPivotTableStyle(name)`. Cette méthode renvoie l’index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) à l’aide de `tableStyle.tableStyleElements.add(tableStyleElementType)`, puis attribuez un `style` à chaque élément à l’aide de `tableStyleElement.setElementStyle(style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `pivotTable.pivotTableStyleName` avec le nom du style. N’utilisez pas `pivotTable.pivotTableStyleType` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}
Les propriétés `pivotTable.pivotTableStyleName` et `pivotTable.pivotTableStyleType` ne sont pas interchangeables. Utilisez `pivotTable.pivotTableStyleType` pour les préréglages intégrés et `pivotTable.pivotTableStyleName` pour les styles personnalisés que vous avez définis via `addPivotTableStyle`. Le fait de définir les deux propriétés n’entraîne aucune conséquence ; toutefois, seule celle correspondant au style souhaité est prise en compte lors du rendu.
Les valeurs disponibles de `TableStyleElementType` comprennent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.
L’exemple suivant définit un style personnalisé de tableau croisé dynamique avec une bordure noire fine pour `WholeTable` et une police rouge en gras pour `GrandTotalRow`, l’applique au tableau croisé dynamique via `pivotTable.pivotTableStyleName`, puis enregistre le classeur au format `.xlsx`.
{{% /alert %}}

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
        const { Workbook } = AsposeCells;
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
            // Remplir les données sources : ligne d'en-tête + 9 lignes de données (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
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
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Ajouter un tableau croisé dynamique utilisant A1:C10 comme source et ancré à E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Étape 1 : enregistrer un nouveau style personnalisé de tableau croisé dynamique et récupérer son index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge grasse
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est destiné aux préréglages intégrés)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Appliquer un style à chaque cellule du tableau croisé dynamique avec formatAll**
`pivotTable.formatAll(style)` est un raccourci qui applique un seul objet `style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de ligne et de colonne ainsi que les totaux. La mise en forme définie précédemment par l’une ou l’autre de ces propriétés est remplacée.

{{% alert color="primary" %}}
`formatAll` remplace à la fois `pivotTable.pivotTableStyleType` et `pivotTable.pivotTableStyleName`. Utilisez cette méthode uniquement lorsqu’une apparence uniforme et indépendante du thème est nécessaire sur l’ensemble du tableau croisé dynamique.
L’exemple suivant crée un `style` avec un remplissage jaune uni, une police bleu foncé en gras et des bordures noires fines de tous les côtés, l’applique avec `formatAll`, puis enregistre le classeur au format `.xlsx`.
{{% /alert %}}

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
            // Scénario 4 : appliquer un seul Style à chaque cellule du tableau croisé dynamique avec FormatAll
            // API utilisée : PivotTable.FormatAll(Style)
            // Format cible : .xlsx
            // Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de mise en forme de tableaux croisés dynamiques
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Remplir les données source : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2 à 10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Affecter les champs du tableau croisé dynamique : Fruit -> zone des lignes, Year -> zone des colonnes, Amount -> zone des données
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Créer un Style qui sera appliqué à toutes les cellules du tableau croisé dynamique
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Appliquer FormatAll : impose ce style unique sur toutes les cellules du tableau croisé dynamique,
            // en remplaçant tout PivotTableStyleType / PivotTableStyleName défini précédemment
            pivotTable.formatAll(style);
            // Enregistrer le classeur au format .xlsx moderne
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

## **Quelle API de style dois-je utiliser ?**
Le choix de l’API de style dépend du format de fichier dans lequel vous enregistrez le classeur. Utilisez le tableau ci-dessous comme référence rapide.
| Format de fichier cible | API à utiliser | Remarques |
|---|---|---|
| `.xls` (hérité) | `pivotTable.autoFormatType` | Valeurs de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par exemple `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorées lors de l’enregistrement dans des formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `pivotTable.pivotTableStyleType` | Valeurs de `Aspose.Cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les styles ajoutés dans Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez via `tableStyleElement.setElementStyle(...)`. |
| Tous les formats (remplacement uniforme) | `pivotTable.formatAll(style)` | Raccourci qui remplace tous les autres réglages de style sur l’ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez le classeur au format `.xlsx` et utilisez `pivotTable.pivotTableStyleType` pour les thèmes intégrés, ou `pivotTable.pivotTableStyleName` pour les styles personnalisés.

{{< app/cells/assistant language="javascript-cpp" >}}