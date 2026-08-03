---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells pour .NET
linktitle: Appliquer des styles aux tableaux croisés dynamiques
description: Apprenez à appliquer des styles intégrés et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for Node.js via Java, couvrant les autoformats XLS hérités, les styles nommés modernes Excel 2007+, les styles personnalisés de tableau croisé dynamique et le raccourci FormatAll.
keywords: Aspose.Cells Node.js via Java style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'application des auto-formats hérités pour les tableaux croisés dynamiques (destinés aux fichiers `.xls`) ainsi que des styles nommés modernes ou personnalisés pour les tableaux croisés dynamiques (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.

{{% /alert %}}

## **Introduction**

Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré au format `.xlsx` ; dans ce cas, c'est l'API de style moderne qui s'applique, et non l'API héritée.

Pour la sortie `.xls` héritée, utilisez la propriété `PivotTable.autoFormatType` conjointement avec l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Cette API correspond au sélecteur d'autoformat que l'Excel classique proposait pour les tableaux croisés dynamiques.

Pour la sortie moderne `.xlsx`, `.xlsm` et `.xlsb`, deux variantes d'API de style sont disponibles :

- `PivotTable.pivotTableStyleType` sélectionne l'un des styles nommés intégrés (thèmes clairs et foncés, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `PivotTable.pivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même via `Worksheets.getTableStyles().addPivotTableStyle(...)`. Les styles personnalisés sont nécessaires dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que les préréglages offrent.

De plus, `PivotTable.formatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, remplaçant tout ce qui a été défini via l'une ou l'autre des API de nom de style ci-dessus. Cela est utile lorsqu'une apparence uniforme est requise indépendamment du thème sous-jacent.

## **Appliquer un autoformat prédéfini XLS hérité**

`PivotTable.autoFormatType` accepte une valeur de l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic`, et `Table1` à `Table10`.

{{% alert color="primary" %}}

`autoFormatType` n'est pris en compte que lorsque le classeur est enregistré au format `.xls`. Lorsque le même classeur est enregistré au format `.xlsx`, `.xlsm` ou `.xlsb`, Excel ignore cette propriété et se rabat sur les paramètres `pivotTableStyleType` et `pivotTableStyleName`.

{{% /alert %}}

L'exemple suivant charge un nouveau classeur, remplit les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.Report5`, et enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}

**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour des **tableaux croisés dynamiques à une dimension** avec uniquement des champs de ligne et des valeurs — ils n'ont pas de style intégré pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du Scénario 2 ci-dessous, qui sont conçus pour la disposition bidimensionnelle qu'utilise Excel moderne.

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// Obtenir la première feuille de calcul
let sheet = workbook.getWorksheets().get(0);

// Remplir les données sources avec une ligne d'en-tête (Fruit, Année, Montant)
// et 9 lignes de données couvrant raisin, myrtille, kiwi, cerise sur 2020 et 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");

sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);

sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);

sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);

sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);

sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);

sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);

sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);

sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);

sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);

// Ajouter un tableau croisé dynamique à la cellule de destination E3, nommé "Pivot1", en utilisant la plage source A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Assigner les champs : Fruit -> Lignes, Année -> Colonnes, Montant -> Données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Appliquer le format automatique prédéfini XLS hérité "Report5"
// Remarque : Cette propriété n'est significative que lors de l'enregistrement au format .xls.
// Lors de l'enregistrement au format .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
// et utilise ce que spécifie PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// Enregistrer le classeur au format hérité .xls
workbook.save("output.xls");
```

## **Appliquer un style prédéfini nommé moderne de tableau croisé dynamique**

`PivotTable.pivotTableStyleType` accepte une valeur de l'énumération `Aspose.Cells.PivotTableStyleType`. L'énumération couvre les thèmes clairs `PivotTableStyleLight1` à `PivotTableStyleLight28` et les thèmes foncés `PivotTableStyleDark1` à `PivotTableStyleDark28`. Les styles ajoutés dans Excel 2017 (la deuxième vague de thèmes clairs et foncés) sont accessibles via la même énumération.

C'est l'API recommandée pour tout format de fichier moderne. Contrairement à l'autoformat hérité, le style sélectionné ici est rendu fidèlement par Excel et survit aux allers-retours avec d'autres outils Office.

L'exemple suivant utilise les mêmes données Fruit/Année/Montant, crée un tableau croisé dynamique identique, applique `PivotTableStyleDark1`, et enregistre le classeur au format `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Ligne d'en-tête : Fruit / Année / Montant
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 lignes de données de Fruit / Année / Montant
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// Ajouter un tableau croisé dynamique à E3 nommé "Pivot1", sourced from A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assigner les champs du tableau croisé dynamique : Fruit -> Zone de ligne, Année -> Zone de colonne, Montant -> Zone de données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Appliquer un style de tableau croisé dynamique prédéfini nommé moderne Excel 2007+.
// PivotTableStyleType est l'API correcte pour les fichiers .xlsx / .xlsm / .xlsb ; AutoFormatType
// est ignoré par Excel pour ces formats. PivotTableStyleDark1 appartient à la famille du thème sombre
// famille (PivotTableStyleDark1..PivotTableStyleDark28), et la même énumération expose également les
// nouveaux thèmes Excel 2017 clair/sombre (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Enregistrer en tant que .xlsx moderne — c'est le format pour lequel PivotTableStyleType est significatif.
workbook.save("output.xlsx");
```

## **Définir et appliquer un style personnalisé de tableau croisé dynamique**

Les préréglages intégrés ne peuvent pas être modifiés. Dès que vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style personnalisé de tableau croisé dynamique. Le flux de travail comporte trois étapes :

1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) via `TableStyle.tableStyleElements.add(TableStyleElementType)`, puis affectez un `Style` à chaque élément via `TableStyleElement.setElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `PivotTable.pivotTableStyleName` sur le nom du style. N'utilisez pas `pivotTableStyleType` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}

`pivotTableStyleName` et `pivotTableStyleType` ne sont pas interchangeables. Utilisez `pivotTableStyleType` pour les préréglages intégrés, et `pivotTableStyleName` pour les styles personnalisés que vous avez définis via `addPivotTableStyle`. Définir les deux est sans danger, mais seul celui qui correspond à la source prévue est rendu.

{{% /alert %}}

Les valeurs `TableStyleElementType` disponibles incluent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.

L'exemple suivant définit un style personnalisé de tableau croisé dynamique avec une fine bordure noire sur `WholeTable` et une police rouge en gras sur `GrandTotalRow`, puis l'applique via `pivotTableStyleName` et enregistre au format `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Remplir les données sources : ligne d'en-tête + 9 lignes de données (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

// Ajouter un tableau croisé dynamique sourced de A1:C10, ancré à E3, nommé "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Étape 1 : enregistrer un nouveau style de tableau croisé dynamique personnalisé et capturer son index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge en gras
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est pour les préréglages intégrés)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Appliquer un seul style à chaque cellule du tableau croisé dynamique avec FormatAll**

`PivotTable.formatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui a été précédemment défini via `pivotTableStyleType` ou `pivotTableStyleName` est remplacé.

{{% alert color="primary" %}}

`formatAll` remplace à la fois `pivotTableStyleType` et `pivotTableStyleName`. Utilisez-le uniquement lorsqu'une apparence uniforme, indépendante du thème, est requise sur l'ensemble du tableau croisé dynamique.

{{% /alert %}}

L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras, et de fines bordures noires sur tous les côtés, puis l'applique avec `formatAll` et enregistre au format `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Remplir les données sources : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);

// Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3, nom "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assigner les champs du tableau croisé dynamique : Fruit -> zone de ligne, Year -> zone de colonne, Amount -> zone de données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Construire un Style qui sera forcé sur chaque cellule du tableau croisé dynamique
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);

// Appliquer FormatAll : force ce style unique sur chaque cellule du tableau croisé dynamique,
// écrasant tout PivotTableStyleType / PivotTableStyleName précédemment défini
pivotTable.formatAll(style);

// Enregistrer le classeur au format moderne .xlsx
workbook.save("output.xlsx");
```

## **Quelle API de style dois-je utiliser ?**

Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.

| Format de fichier cible | API à utiliser | Remarques |
|---|---|---|
| `.xls` (hérité) | `PivotTable.autoFormatType` | Valeurs de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoré lors de l'enregistrement aux formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.pivotTableStyleType` | Valeurs de `Aspose.Cells.PivotTableStyleType` (thèmes clairs/foncés, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurer via `TableStyleElement.setElementStyle(...)`. |
| Tout format (remplacement uniforme) | `PivotTable.formatAll(Style)` | Raccourci qui remplace tout autre paramètre de style sur l'ensemble du tableau croisé dynamique. |

En cas de doute, enregistrez au format `.xlsx` et utilisez `pivotTableStyleType` pour les thèmes intégrés, ou `pivotTableStyleName` pour les thèmes personnalisés.

{{< app/cells/assistant language="nodejs-java" >}}