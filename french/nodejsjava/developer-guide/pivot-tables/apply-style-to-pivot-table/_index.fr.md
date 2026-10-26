---
title: Appliquer des styles aux Tableaux Croisés Dynamiques dans Aspose.Cells for Node.js via Java
linktitle: Appliquer des styles aux Tableaux Croisés Dynamiques dans Aspose.Cells for Node.js via Java
description: Apprenez à appliquer des styles intégrés et personnalisés aux Tableaux Croisés Dynamiques dans Aspose.Cells for Node.js via Java, couvrant les autoformats XLS hérités, les styles nommés modernes d'Excel 2007+, les styles personnalisés de tableau croisé dynamique et le raccourci formatAll.
keywords: style de tableau croisé dynamique Aspose.Cells Node.js via Java, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l'application à la fois des autoformats de tableau croisé dynamique hérités (destinés aux fichiers `.xls`) et des styles nommés ou personnalisés modernes de tableau croisé dynamique (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API à appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les Tableaux Croisés Dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré au format `.xlsx` ; dans ce cas, c'est l'API de style moderne qui s'applique, et non l'API héritée.
- `PivotTable.pivotTableStyleType` sélectionne l'un des styles nommés intégrés (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `PivotTable.pivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même via `Worksheets.getTableStyles().addPivotTableStyle(...)`. Les styles personnalisés sont nécessaires chaque fois que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que proposent les préréglages.
De plus, `PivotTable.formatAll(Style)` est un raccourci qui applique un unique objet `Style` à toutes les cellules du tableau croisé dynamique, remplaçant tout ce qui a été défini via l'une ou l'autre des API de nom de style ci-dessus. Ceci est utile lorsqu'une apparence uniforme est requise, quel que soit le thème sous-jacent.

## **Apply a Legacy XLS Preset Autoformat**
`PivotTable.autoFormatType` accepte une valeur de l'énumération `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `Report1` à `Report10`, `Classic`, et `Table1` à `Table10`.
L'exemple suivant charge un nouveau classeur, remplit les données d'exemple Fruit/Année/Montant, ajoute un Tableau Croisé Dynamique, applique `PivotTableAutoFormatType.Report5` et enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}
**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans l'Excel classique pour les **Tableaux Croisés Dynamiques unidimensionnels** comportant uniquement des champs de ligne et des valeurs ; ils ne disposent pas de mise en forme intégrée pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), qui sont conçus pour la disposition bidimensionnelle utilisée par Excel moderne.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Get the first worksheet
let sheet = workbook.getWorksheets().get(0);
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
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
// Add a pivot table at destination cell E3, using source range A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// Save the workbook in legacy .xls format
workbook.save("output.xls");
```

## **Apply a Modern Named Preset Pivot Table Style**
`PivotTable.setPivotTableStyleType(int)` sélectionne l’un des styles intégrés_denommés qu’Excel 2007 a introduits pour les tableaux croisés dynamiques. L’énumération `PivotTableStyleType` expose trois familles de thèmes : la famille claire allant de `PIVOT_TABLE_STYLE_LIGHT1` à `PIVOT_TABLE_STYLE_LIGHT28`, la famille moyenne allant de `PIVOT_TABLE_STYLE_MEDIUM1` à `PIVOT_TABLE_STYLE_MEDIUM28` et la famille sombre allant de `PIVOT_TABLE_STYLE_DARK1` à `PIVOT_TABLE_STYLE_DARK_28`. Elle définit également `None` et `Custom`. Les membres de numéro plus élevé de chaque famille correspondent aux styles ajoutés dans Excel 2017.
Ces préréglages sont en lecture seule. Dès que vous devez modifier les couleurs, les bordures ou les polices au-delà de ce que fournit un préréglage, vous devez plutôt définir un style personnalisé de tableau croisé dynamique, comme indiqué dans [Scénario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Pourquoi les préréglages modernes plutôt que les mises en forme automatiques de la série de rapports ?** Les valeurs `Report1` à `Report10` et `Table1` à `Table10` de `PivotTableAutoFormatType` précèdent les champs de colonne des tableaux croisés dynamiques ; elles ne comportent donc aucune mise en forme pour les en-têtes de champs de colonne, et Excel affiche ces en-têtes sans mise en forme. Les préréglages `PivotTableStyleType` ont été conçus pour la disposition bidimensionnelle utilisée par les versions modernes d’Excel et appliquent la même mise en forme aux en-têtes de champs de ligne et de colonne.
{{% /alert %}}

Ce scénario réutilise le jeu de données Fruit/Year/Amount du Scénario 1, ajoute `Year` à la zone des colonnes à côté du champ de ligne `Fruit` via `PivotFieldType.COLUMN`, applique le préréglage du thème sombre `PIVOT_TABLE_STYLE_DARK1` avec `pivotTable.setPivotTableStyleType`, puis enregistre le résultat au format `.xlsx` — le format pour lequel `PivotTableStyleType` est pertinent.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
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
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Define and Apply a Custom Pivot Table Style**
Les préréglages intégrés ne peuvent pas être modifiés. Chaque fois que vous devez redéfinir les couleurs, les bordures ou les polices, vous devez définir un style de tableau croisé dynamique personnalisé. Le flux de travail comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) via `TableStyle.tableStyleElements.add(TableStyleElementType)`, puis attribuez un `Style` à chaque élément via `TableStyleElement.setElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en définissant `PivotTable.pivotTableStyleName` sur le nom du style. N'utilisez pas `pivotTableStyleType` ici, car cette propriété sélectionne les préréglages intégrés.

{{% alert color="primary" %}}
`pivotTableStyleName` et `pivotTableStyleType` ne sont pas interchangeables. Utilisez `pivotTableStyleType` pour les préréglages intégrés, et `pivotTableStyleName` pour les styles personnalisés que vous avez définis via `addPivotTableStyle`. Définir les deux est inoffensif, mais seul celui qui correspond à la source prévue est rendu.
Les valeurs disponibles de `TableStyleElementType` incluent `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` et `PageFieldValues`.
L'exemple suivant définit un style de tableau croisé dynamique personnalisé avec une fine bordure noire sur `WholeTable` et une police rouge en gras sur `GrandTotalRow`, puis l'applique via `pivotTableStyleName` et enregistre au format `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row + 9 data rows (A1:C10)
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
// Add pivot table sourced from A1:C10, anchored at E3
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Step 1: register a new custom pivot table style and capture its index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Step 2: add a WholeTable element and apply thin black borders on all four sides
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Step 3: add a GrandTotalRow element and apply bold red font
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Apply One Style to Every Pivot Cell with formatAll**
`PivotTable.formatAll(Style)` est un raccourci qui applique un unique objet `Style` à toutes les cellules du Tableau Croisé Dynamique, y compris la zone de données, les en-têtes de ligne et de colonne, ainsi que les totaux. Tout ce qui a été précédemment défini via `pivotTableStyleType` ou `pivotTableStyleName` est remplacé.

{{% alert color="primary" %}}
`formatAll` remplace à la fois `pivotTableStyleType` et `pivotTableStyleName`. Utilisez-le uniquement lorsqu'une apparence uniforme, indépendante du thème, est requise sur l'ensemble du tableau croisé dynamique.
L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras et de fines bordures noires sur tous les côtés, puis l'applique avec `formatAll` et enregistre au format `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
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
// Add pivot table: source range A1:C10, destination cell E3
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// Apply formatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style);
// Save the workbook in the modern .xlsx format
workbook.save("output.xlsx");
```

## **Which Style API Should I Use?**
Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.
| Format de fichier cible | API à utiliser | Notes |
|---|---|---|
| `.xls` (hérité) | `PivotTable.autoFormatType` | Valeurs de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (par ex. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignoré lors de l'enregistrement dans des formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `PivotTable.pivotTableStyleType` | Valeurs de `Aspose.Cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez via `TableStyleElement.setElementStyle(...)`. |
| Tout format (substitution uniforme) | `PivotTable.formatAll(Style)` | Raccourci qui remplace tous les autres paramètres de style sur l'ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez au format `.xlsx` et utilisez `pivotTableStyleType` pour les thèmes intégrés, ou `pivotTableStyleName` pour les thèmes personnalisés.

{{< app/cells/assistant language="nodejs-java" >}}