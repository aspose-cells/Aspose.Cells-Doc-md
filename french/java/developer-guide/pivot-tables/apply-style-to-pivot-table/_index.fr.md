---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Java
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Java
description: Découvrez comment appliquer des styles prédéfinis et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for Java, en couvrant les mises en forme automatiques héritées pour XLS, les styles nommés modernes d’Excel 2007+, les styles personnalisés de tableau croisé dynamique et le raccourci formatAll.
keywords: style de tableau croisé dynamique Aspose.Cells for Java, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permet d’appliquer aux tableaux croisés dynamiques à la fois les mises en forme automatiques héritées (destinées aux fichiers `.xls`) et les styles modernes nommés ou personnalisés (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L’API à appeler dépend du format dans lequel le classeur est enregistré, et non de celui depuis lequel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format dans lequel vous enregistrez le classeur, et non du format depuis lequel vous le lisez. Un classeur chargé depuis un fichier `.xls` peut être enregistré à nouveau au format `.xlsx` ; dans ce cas, l’API de style moderne s’applique plutôt que l’API héritée.
- `PivotTable.PivotTableStyleType` sélectionne l’un des styles nommés prédéfinis (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces styles prédéfinis sont en lecture seule.
- `PivotTable.PivotTableStyleName` sélectionne un style personnalisé que vous définissez vous-même via `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)`. Les styles personnalisés sont nécessaires chaque fois que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce qu’offrent les styles prédéfinis.
En outre, `PivotTable.formatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, en remplaçant le style défini par l’une ou l’autre des API de style ci-dessus. Ce raccourci est utile lorsqu’une apparence uniforme est requise, quel que soit le thème sous-jacent.

## **Appliquer une mise en forme automatique XLS héritée prédéfinie**
`PivotTable.AutoFormatType` accepte une valeur de l’énumération `com.aspose.cells.PivotTableAutoFormatType`. Les valeurs disponibles sont `REPORT_1` à `REPORT_10`, `CLASSIC`, ainsi que `TABLE_1` à `TABLE_10`.
L’exemple suivant charge un classeur neuf, renseigne les données d’exemple Fruit/Year/Amount, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.REPORT_5`, puis enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}
**Pourquoi pas de champ de colonne ?** Les mises en forme automatiques de type Rapport ou Table (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçues dans Excel classique pour les **tableaux croisés dynamiques à une seule dimension**, avec uniquement des champs de ligne et des valeurs : elles ne proposent aucune mise en forme intégrée pour les en-têtes des champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), conçus pour la disposition à deux dimensions utilisée par Excel moderne.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Scénario 1 : Appliquer un formatage automatique prédéfini XLS hérité
// API utilisée : PivotTable.AutoFormatType
// Format de fichier cible : .xls (hérité)
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Créer un nouveau classeur
Workbook workbook = new Workbook();
// Obtenir la première feuille de calcul
Worksheet sheet = workbook.getWorksheets().get(0);
// Remplir les données source avec une ligne d'en-tête (Fruit, Year, Amount)
// et 9 lignes de données couvrant le raisin, la myrtille, le kiwi et la cerise en 2020 et 2021
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
// Ajouter un tableau croisé dynamique à la cellule de destination E3, nommé, en utilisant la plage source A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Attribuer les champs : Fruit -> Lignes, Amount -> Données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Appliquer le formatage automatique prédéfini XLS hérité "Report5"
// Remarque : cette propriété n'a de sens que lors de l'enregistrement au format .xls.
// Lors de l'enregistrement aux formats .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
// et utilise les paramètres indiqués par PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Enregistrer le classeur au format .xls hérité
workbook.save("output.xls");
```

## **Appliquer un style moderne prédéfini et nommé aux tableaux croisés dynamiques**
`PivotTable.setPivotTableStyleType(int)` sélectionne l’un des styles nommés intégrés qu’Excel 2007 a introduits pour les tableaux croisés dynamiques. L’énumération `PivotTableStyleType` expose trois familles de thèmes : la famille claire allant de `PIVOT_TABLE_STYLE_LIGHT1` à `PIVOT_TABLE_STYLE_LIGHT28`, la famille moyenne allant de `PIVOT_TABLE_STYLE_MEDIUM1` à `PIVOT_TABLE_STYLE_MEDIUM28`, et la famille sombre allant de `PIVOT_TABLE_STYLE_DARK1` à `PIVOT_TABLE_STYLE_DARK_28`. Elle définit également `None` et `Custom`. Les membres portant les numéros les plus élevés de chaque famille correspondent aux styles ajoutés dans Excel 2017.
Ces préréglages sont en lecture seule. Dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce qu’un préréglage fournit, vous devez définir à la place un style de tableau croisé dynamique personnalisé, comme indiqué dans [Scénario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Pourquoi les préréglages modernes plutôt que les formats automatiques de la série de rapports ?** Les valeurs `Report1` à `Report10` et `Table1` à `Table10` de `PivotTableAutoFormatType` précèdent les champs de colonne des tableaux croisés dynamiques ; par conséquent, elles n’incluent aucune mise en forme pour les en-têtes de champs de colonne, et Excel affiche ces en-têtes sans mise en forme. Les préréglages `PivotTableStyleType` ont été conçus pour la disposition bidimensionnelle utilisée par les versions modernes d’Excel et appliquent la même mise en forme aux en-têtes de champs de ligne et de colonne.
{{% /alert %}}

Ce scénario réutilise le jeu de données Fruit/Year/Amount du Scénario 1, ajoute `Year` à la zone de colonnes à côté du champ de ligne `Fruit` à l’aide de `PivotFieldType.COLUMN`, applique le préréglage de thème sombre `PIVOT_TABLE_STYLE_DARK1` avec `pivotTable.setPivotTableStyleType`, puis enregistre le résultat sous `.xlsx` — le format pour lequel `PivotTableStyleType` est pertinent.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx - this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Définir et appliquer un style personnalisé de tableau croisé dynamique**
Les styles prédéfinis ne peuvent pas être modifiés. Pour remplacer les couleurs, les bordures ou les polices, vous devez définir un style personnalisé de tableau croisé dynamique. Le flux de travail comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Cette méthode renvoie l’index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WholeTable` ou `GrandTotalRow`) via `TableStyle.getTableStyleElements().add(TableStyleElementType)`, puis attribuez un objet `Style` à chaque élément via `TableStyleElement.setElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en affectant le nom du style à `PivotTable.PivotTableStyleName`. N’utilisez pas `PivotTableStyleType` ici, car cette propriété sélectionne les styles prédéfinis.

{{% alert color="primary" %}}
`PivotTableStyleName` et `PivotTableStyleType` ne sont pas interchangeables. Utilisez `PivotTableStyleType` pour les styles prédéfinis et `PivotTableStyleName` pour les styles personnalisés que vous avez définis via `addPivotTableStyle`. Définir les deux n’entraîne aucune conséquence, mais seul le style correspondant à la source prévue est rendu.
Les valeurs disponibles de `TableStyleElementType` comprennent `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` et `PAGE_FIELD_VALUES`.
L’exemple suivant définit un style personnalisé de tableau croisé dynamique avec une bordure noire fine sur `WholeTable` et une police rouge grasse sur `GrandTotalRow`, puis l’applique via `PivotTableStyleName` et enregistre le résultat au format `.xlsx`.
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Remplir les données source : ligne d'en-tête + 9 lignes de données (A1:C10)
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
// Ajouter un tableau croisé dynamique utilisant A1:C10 comme source, ancré à E3 et nommé
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Étape 1 : enregistrer un nouveau style personnalisé de tableau croisé dynamique et récupérer son index
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge grasse
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est destiné aux styles prédéfinis)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Appliquer un style à chaque cellule du tableau croisé dynamique avec formatAll**
`PivotTable.formatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris aux cellules de la zone de données, aux en-têtes de ligne et de colonne ainsi qu’aux totaux. Tout style défini précédemment via `PivotTableStyleType` ou `PivotTableStyleName` est remplacé.

{{% alert color="primary" %}}
`formatAll` remplace à la fois `PivotTableStyleType` et `PivotTableStyleName`. Utilisez-le uniquement lorsqu’une apparence uniforme et indépendante du thème est requise sur l’ensemble du tableau croisé dynamique.
L’exemple suivant crée un `Style` avec un remplissage jaune uni, une police bleu foncé grasse et des bordures noires fines sur tous les côtés, puis l’applique avec `formatAll` et enregistre le classeur au format `.xlsx`.
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Remplir les données source : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
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
// Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3, nom
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Affecter les champs du tableau croisé dynamique : Fruit -> zone de lignes, Year -> zone de colonnes, Amount -> zone de données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Créer un Style qui sera appliqué à toutes les cellules du tableau croisé dynamique
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());
// Appliquer formatAll : impose ce style unique à toutes les cellules du tableau croisé dynamique,
// en remplaçant tout PivotTableStyleType / PivotTableStyleName défini précédemment
pivotTable.formatAll(style);
// Enregistrer le classeur au format .xlsx moderne
workbook.save("output.xlsx");
```

## **Quelle API de style utiliser ?**
Le choix de l’API de style dépend du format de fichier dans lequel vous enregistrez le classeur. Utilisez le tableau ci-dessous comme référence rapide.
| Format de fichier cible | API à utiliser | Remarques |
|---|---|---|
| `.xls` (hérité) | `PivotTable.AutoFormatType` | Valeurs de `com.aspose.cells.PivotTableAutoFormatType` (par ex. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ce réglage est ignoré lors de l’enregistrement dans des formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style prédéfini) | `PivotTable.PivotTableStyleType` | Valeurs de `com.aspose.cells.PivotTableStyleType` (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | À utiliser lorsque les styles prédéfinis ne suffisent pas. Configurez le style via `TableStyleElement.setElementStyle(...)`. |
| Tout format (remplacement uniforme) | `PivotTable.formatAll(Style)` | Raccourci qui remplace tous les autres réglages de style sur l’ensemble du tableau croisé dynamique. |
En cas d’hésitation, enregistrez le classeur au format `.xlsx` et utilisez `PivotTableStyleType` pour les thèmes prédéfinis, ou `PivotTableStyleName` pour les thèmes personnalisés.

{{< app/cells/assistant language="java" >}}