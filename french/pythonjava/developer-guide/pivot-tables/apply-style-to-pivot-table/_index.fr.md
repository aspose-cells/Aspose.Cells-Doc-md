---
title: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via Java
linktitle: Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Python via Java
description: Apprenez à appliquer des styles prédéfinis et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for Python via Java, y compris les autoformats XLS hérités, les styles nommés modernes d'Excel 2007+, les styles personnalisés de tableau croisé dynamique et le raccourci FormatAll.
keywords: Aspose.Cells Python via Java style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge l'application des autoformats hérités des tableaux croisés dynamiques (destinés aux fichiers `.xls`) ainsi que des styles nommés ou personnalisés modernes (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.
{{% /alert %}}

## **Introduction**
Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé depuis un fichier `.xls` peut être réenregistré en `.xlsx`, et dans ce cas, c'est l'API de style moderne qui s'applique plutôt que l'API héritée.
- `pivotTable.setPivotTableStyleType(int)` sélectionne l'un des styles nommés prédéfinis (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `pivotTable.setPivotTableStyleName(String)` sélectionne un style personnalisé que vous définissez vous-même via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Les styles personnalisés sont nécessaires chaque fois que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que les préréglages offrent.
De plus, `pivotTable.formatAll(Style)` est un raccourci qui applique un même objet `Style` à chaque cellule du tableau croisé dynamique, en surchargeant tout ce qui est défini via l'une ou l'autre des API de nom de style ci-dessus. Cela est utile lorsqu'une apparence uniforme est requise quel que soit le thème sous-jacent.

## **Appliquer un autoformat prédéfini XLS hérité**
La méthode `setAutoFormatType` sur un tableau croisé dynamique accepte une valeur de l'énumération `com.aspose.cells.pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `REPORT_1` à `REPORT_10`, `CLASSIC`, et `TABLE_1` à `TABLE_10`.
L'exemple suivant charge un nouveau classeur, renseigne les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.REPORT_5`, puis enregistre le résultat en `.xls`.

{{% alert color="primary" %}}
**Pourquoi pas de champs de colonnes ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour des **tableaux croisés dynamiques unidimensionnels** comportant uniquement des champs de lignes et des valeurs — ils ne disposent pas de mise en forme intégrée pour les en-têtes de champs de colonnes. Si votre tableau croisé dynamique nécessite des champs de colonnes, utilisez plutôt les préréglages modernes `PivotTableStyleType` du [Scénario 2](#apply-a-modern-named-preset-pivot-table-style), qui sont conçus pour la disposition bidimensionnelle utilisée par Excel moderne.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Scénario 1 : Appliquer un autoformat prédéfini XLS hérité
# API utilisée : PivotTable.AutoFormatType
# Format de fichier cible : .xls (hérité)
# Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Créer un nouveau classeur
workbook = Workbook()
# Obtenir la première feuille de calcul
sheet = workbook.getWorksheets().get(0)
# Remplir les données source avec une ligne d'en-tête (Fruit, Year, Amount)
# et 9 lignes de données couvrant grape, blueberry, kiwi, cherry à travers 2020 et 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")
sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)
sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)
sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)
sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)
sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)
sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)
sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)
sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)
sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)
# Ajouter un tableau croisé dynamique à la cellule de destination E3, nommé "Pivot1", en utilisant la plage source A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)
# Assigner les champs : Fruit -> Lignes, Amount -> Données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Appliquer l'autoformat prédéfini XLS hérité "Report5"
# Note : Cette propriété n'a de sens que lors de l'enregistrement en .xls.
# Lorsqu'enregistré en .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
# et utilise ce que PivotTableStyleType / PivotTableStyleName spécifie.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# Enregistrer le classeur au format .xls hérité
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Appliquer un style de tableau croisé dynamique nommé moderne prédéfini**

`pivotTable.setPivotTableStyleType(int)` sélectionne l’un des styles nommés intégrés qu’Excel 2007 a introduits pour les tableaux croisés dynamiques. L’énumération `PivotTableStyleType` expose trois familles de thèmes : la famille claire allant de `PIVOT_TABLE_STYLE_LIGHT1` à `PIVOT_TABLE_STYLE_LIGHT28`, la famille moyenne allant de `PIVOT_TABLE_STYLE_MEDIUM1` à `PIVOT_TABLE_STYLE_MEDIUM28` et la famille sombre allant de `PIVOT_TABLE_STYLE_DARK1` à `PIVOT_TABLE_STYLE_DARK_28`. Elle définit également `None` et `Custom`. Les membres de numéro plus élevé de chaque famille correspondent aux styles ajoutés dans Excel 2017.
Ces préréglages sont en lecture seule. Dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce qu’un préréglage fournit, vous devez plutôt définir un style de tableau croisé dynamique personnalisé, comme indiqué dans [Scénario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Pourquoi les préréglages modernes plutôt que les formats automatiques de série de rapport ?** Les valeurs `Report1` à `Report10` et `Table1` à `Table10` de `PivotTableAutoFormatType` précèdent les champs de colonne des tableaux croisés dynamiques ; elles ne comportent donc aucun style pour les en-têtes de champs de colonne, et Excel affiche ces en-têtes sans style. Les préréglages `PivotTableStyleType` ont été conçus pour la disposition bidimensionnelle utilisée par les versions modernes d’Excel et appliquent le même style aux en-têtes de champs de ligne et de colonne.
{{% /alert %}}

Ce scénario réutilise le jeu de données Fruit/Year/Amount du Scénario 1, ajoute `Year` à la zone des colonnes à côté du champ de ligne `Fruit` au moyen de `PivotFieldType.COLUMN`, applique le préréglage du thème sombre `PIVOT_TABLE_STYLE_DARK1` avec `pivotTable.setPivotTableStyleType`, puis enregistre le résultat sous forme de `.xlsx` — le format pour lequel `PivotTableStyleType` est pertinent.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)
# Add a pivot table at E3 named "Pivot1", sourced from A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```
## **Définir et appliquer un style personnalisé de tableau croisé dynamique**
Les préréglages intégrés ne peuvent pas être modifiés. Chaque fois que vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style personnalisé de tableau croisé dynamique. Le flux de travail comporte trois étapes :
1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WHOLE_TABLE` ou `GRAND_TOTAL_ROW`) via `tableStyle.getTableStyleElements().add(TableStyleElementType)`, puis attribuez un `Style` à chaque élément via `tableStyleElement.setElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en appelant `pivotTable.setPivotTableStyleName(String)` avec le nom du style. N'utilisez pas `setPivotTableStyleType` ici, car cette méthode sélectionne des préréglages intégrés.

{{% alert color="primary" %}}
`setPivotTableStyleName` et `setPivotTableStyleType` ne sont pas interchangeables. Utilisez `setPivotTableStyleType` pour les préréglages intégrés, et `setPivotTableStyleName` pour les styles personnalisés que vous avez définis via `addPivotTableStyle`. Définir les deux est sans incidence, mais seule l'API correspondant à la source prévue est rendue.
Les valeurs disponibles de `TableStyleElementType` incluent `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` et `PAGE_FIELD_VALUES`.
L'exemple suivant définit un style personnalisé de tableau croisé dynamique avec une fine bordure noire sur `WHOLE_TABLE` et une police rouge en gras sur `GRAND_TOTAL_ROW`, puis l'applique via `setPivotTableStyleName` et enregistre en `.xlsx`.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Remplir les données sources : ligne d'en-tête + 9 lignes de données (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)
# Ajouter un tableau croisé dynamique à partir de A1:C10, ancré à E3, nommé "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Étape 1 : enregistrer un nouveau style de tableau croisé dynamique personnalisé et capturer son index
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)
# Étape 2 : ajouter un élément WholeTable et appliquer des bordures fines noires sur les quatre côtés
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge en gras
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est pour les préréglages intégrés)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Appliquer un seul style à chaque cellule du tableau croisé dynamique avec formatAll**
`pivotTable.formatAll(Style)` est un raccourci qui applique un même objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui avait été défini précédemment via `setPivotTableStyleType` ou `setPivotTableStyleName` est écrasé.

{{% alert color="primary" %}}
`formatAll` écrase à la fois `setPivotTableStyleType` et `setPivotTableStyleName`. Utilisez-le uniquement lorsqu'une apparence uniforme et indépendante du thème est requise sur l'ensemble du tableau croisé dynamique.
L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras et de fines bordures noires sur tous les côtés, puis l'applique avec `formatAll` et enregistre en `.xlsx`.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Scénario 4 : Appliquer un seul Style à chaque cellule d'un tableau croisé dynamique en utilisant formatAll
# API utilisée : PivotTable.formatAll(Style)
# Format cible : .xlsx
# Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de mise en forme de tableaux croisés dynamiques
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Remplir les données source : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2 à 10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)
# Ajouter un tableau croisé dynamique : plage source A1:C10, cellule de destination E3, nom "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Affecter les champs du tableau croisé dynamique : Fruit -> zone Ligne, Year -> zone Colonne, Amount -> zone Données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Construire un Style qui sera forcé sur chaque cellule du tableau croisé dynamique
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# Appliquer formatAll : force ce style unique sur chaque cellule du tableau croisé dynamique,
# écrasant tout PivotTableStyleType / PivotTableStyleName précédemment défini
pivotTable.formatAll(style)
# Enregistrer le classeur au format moderne .xlsx
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Quelle API de style dois-je utiliser ?**
Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.
| Format de fichier cible | API à utiliser | Remarques |
|---|---|---|
| `.xls` (hérité) | `pivotTable.setAutoFormatType(int)` | Valeurs de `com.aspose.cells.pivot.PivotTableAutoFormatType` (par exemple `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoré lors de l'enregistrement dans un format moderne. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `pivotTable.setPivotTableStyleType(int)` | Valeurs de `com.aspose.cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurer via `tableStyleElement.setElementStyle(Style)`. |
| N'importe quel format (écrasement uniforme) | `pivotTable.formatAll(Style)` | Raccourci qui écrase tout autre paramètre de style sur l'ensemble du tableau croisé dynamique. |
En cas de doute, enregistrez en `.xlsx` et utilisez `setPivotTableStyleType` pour les thèmes intégrés, ou `setPivotTableStyleName` pour les thèmes personnalisés.


{{< app/cells/assistant language="python" >}}