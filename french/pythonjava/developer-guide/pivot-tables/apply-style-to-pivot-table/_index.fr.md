---
title: Application de styles aux tableaux croisés dynamiques
linktitle: Application de styles aux tableaux croisés dynamiques
description: Apprenez à appliquer des styles prédéfinis et personnalisés aux tableaux croisés dynamiques dans Aspose.Cells for Python via Java, en couvrant les autoformats XLS hérités, les styles nommés modernes d'Excel 2007+, les styles de tableau croisé dynamique personnalisés, et le raccourci FormatAll.
keywords: Aspose.Cells Python via Java style de tableau croisé dynamique, PivotTableStyleType, AutoFormatType, FormatAll, style personnalisé, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /fr/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'application des anciens autoformats de tableau croisé dynamique (destinés aux fichiers `.xls`) ainsi que des styles nommés ou personnalisés modernes de tableau croisé dynamique (destinés aux fichiers `.xlsx`, `.xlsm` et `.xlsb`). L'API que vous devez appeler dépend du format de fichier dans lequel le classeur est enregistré, et non du format à partir duquel il a été chargé.

{{% /alert %}}

## **Introduction**

Aspose.Cells expose deux API de style parallèles pour les tableaux croisés dynamiques. Le choix entre elles dépend du format de fichier dans lequel vous enregistrez le classeur, et non du format à partir duquel vous le lisez. Un classeur chargé à partir d'un fichier `.xls` peut être réenregistré au format `.xlsx`, et dans ce cas l'API de style moderne s'applique plutôt que l'ancienne.

Pour la sortie `.xls` héritée, utilisez la méthode `pivotTable.setAutoFormatType(int)` conjointement avec l'énumération `com.aspose.cells.pivot.PivotTableAutoFormatType`. Cette API correspond au sélecteur d'autoformat que l'ancien Excel proposait pour les tableaux croisés dynamiques.

Pour les sorties modernes `.xlsx`, `.xlsm` et `.xlsb`, deux variantes de l'API de style sont disponibles :

- `pivotTable.setPivotTableStyleType(int)` sélectionne l'un des styles nommés prédéfinis (thèmes clairs et sombres, y compris les styles ajoutés dans Excel 2017). Ces préréglages sont en lecture seule.
- `pivotTable.setPivotTableStyleName(String)` sélectionne un style personnalisé que vous définissez vous-même via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Les styles personnalisés sont nécessaires dès que vous souhaitez modifier les couleurs, les bordures ou les polices au-delà de ce que les préréglages offrent.

De plus, `pivotTable.formatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, en supplantant tout ce qui a été défini par l'une ou l'autre des API de nom de style ci-dessus. Cela s'avère utile lorsqu'une apparence uniforme est requise quel que soit le thème sous-jacent.

## **Appliquer un autoformat prédéfini XLS hérité**

La méthode `setAutoFormatType` sur un tableau croisé dynamique accepte une valeur de l'énumération `com.aspose.cells.pivot.PivotTableAutoFormatType`. Les valeurs disponibles sont `REPORT_1` à `REPORT_10`, `CLASSIC`, et `TABLE_1` à `TABLE_10`.

{{% alert color="primary" %}}

`setAutoFormatType` n'est pris en compte que lorsque le classeur est enregistré au format `.xls`. Lorsque le même classeur est enregistré au format `.xlsx`, `.xlsm` ou `.xlsb`, Excel ignore ce paramètre et se rabat sur les paramètres `setPivotTableStyleType` et `setPivotTableStyleName`.

{{% /alert %}}

L'exemple suivant charge un nouveau classeur, renseigne les données d'exemple Fruit/Année/Montant, ajoute un tableau croisé dynamique, applique `PivotTableAutoFormatType.REPORT_5`, puis enregistre le résultat au format `.xls`.

{{% alert color="primary" %}}

**Pourquoi pas de champs de colonne ?** Les autoformats de la série Report (`Report1` à `Report10`, `Table1` à `Table10`) ont été conçus dans Excel classique pour des **tableaux croisés dynamiques à une dimension** avec uniquement des champs de ligne et des valeurs — ils n'ont pas de style intégré pour les en-têtes de champs de colonne. Si votre tableau croisé dynamique nécessite des champs de colonne, utilisez plutôt les préréglages modernes `PivotTableStyleType` du Scénario 2 ci-dessous, qui sont conçus pour la disposition bidimensionnelle qu'utilise Excel moderne.

{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Scénario 1 : Appliquer un format automatique prédéfini XLS hérité
# API utilisée : PivotTable.AutoFormatType
# Format de fichier cible : .xls (hérité)
# Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Créer un nouveau classeur
workbook = Workbook()

# Obtenir la première feuille de calcul
sheet = workbook.getWorksheets().get(0)

# Remplir les données sources avec une ligne d'en-tête (Fruit, Année, Montant)
# et 9 lignes de données couvrant raisin, myrtille, kiwi, cerise pour 2020 et 2021
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

# Assigner les champs : Fruit -> Lignes, Year -> Colonnes, Amount -> Données
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Appliquer le format automatique prédéfini XLS hérité "Report5"
# Remarque : Cette propriété n'a de sens que lors de l'enregistrement en tant que .xls.
# Lors de l'enregistrement en .xlsx/.xlsm/.xlsb, Excel ignore AutoFormatType
# et utilise ce que PivotTableStyleType / PivotTableStyleName spécifie.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Enregistrer le classeur au format .xls hérité
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Appliquer un style de tableau croisé dynamique prédéfini nommé moderne**

La méthode `setPivotTableStyleType` sur un tableau croisé dynamique accepte une valeur de l'énumération `com.aspose.cells.PivotTableStyleType`. L'énumération couvre les thèmes clairs `PIVOT_TABLE_STYLE_LIGHT_1` à `PIVOT_TABLE_STYLE_LIGHT_28` et les thèmes sombres `PIVOT_TABLE_STYLE_DARK_1` à `PIVOT_TABLE_STYLE_DARK_28`. Les styles ajoutés dans Excel 2017 (la deuxième vague de thèmes clairs et sombres) sont accessibles via la même énumération.

C'est l'API recommandée pour tout format de fichier moderne. Contrairement à l'ancien autoformat, le style sélectionné ici est rendu fidèlement par Excel et survit aux aller-retours avec d'autres outils Office.

L'exemple suivant utilise les mêmes données Fruit/Année/Montant, crée un tableau croisé dynamique identique, applique `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1`, puis enregistre le classeur au format `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Scénario 2 : Appliquer un style prédéfini nommé moderne d'Excel 2007+ à l'aide de PivotTableStyleType.
# Format de fichier cible : .xlsx. L'énumération PivotTableStyleType se trouve dans l'espace de noms Aspose.Cells
# (pas dans Aspose.Cells.Pivot) — c'est pourquoi nous n'avons pas besoin d'importation supplémentaire pour cela.
# Référence GitHub : https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Ligne d'en-tête : Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 lignes de données Fruit / Year / Amount
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

# Ajouter un tableau croisé dynamique en E3 nommé "Pivot1", sourcé à partir de A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assigner les champs du tableau croisé dynamique : Fruit -> zone Lignes, Year -> zone Colonnes, Amount -> zone Données
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Appliquer un style de tableau croisé dynamique prédéfini nommé moderne d'Excel 2007+.
# PivotTableStyleType est l'API correcte pour les fichiers .xlsx / .xlsm / .xlsb ; AutoFormatType
# est ignoré par Excel pour ces formats. PivotTableStyleDark1 appartient à la famille des thèmes sombres
# (PivotTableStyleDark1..PivotTableStyleDark28), et la même énumération expose également les
# nouveaux thèmes clairs/sombres d'Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Enregistrer en tant que .xlsx moderne — c'est le format pour lequel PivotTableStyleType est pertinent.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Définir et appliquer un style de tableau croisé dynamique personnalisé**

Les préréglages intégrés ne peuvent pas être modifiés. Dès que vous devez remplacer les couleurs, les bordures ou les polices, vous devez définir un style de tableau croisé dynamique personnalisé. Le flux de travail comporte trois étapes :

1. Ajoutez un style personnalisé à la collection `TableStyles` du classeur via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Cela renvoie l'index du style nouvellement créé.
2. Configurez le style en ajoutant des éléments (tels que `WHOLE_TABLE` ou `GRAND_TOTAL_ROW`) via `tableStyle.getTableStyleElements().add(TableStyleElementType)`, puis attribuez un `Style` à chaque élément via `tableStyleElement.setElementStyle(Style)`.
3. Appliquez le style personnalisé au tableau croisé dynamique en appelant `pivotTable.setPivotTableStyleName(String)` avec le nom du style. N'utilisez pas `setPivotTableStyleType` ici, car cette méthode sélectionne les préréglages intégrés.

{{% alert color="primary" %}}

`setPivotTableStyleName` et `setPivotTableStyleType` ne sont pas interchangeables. Utilisez `setPivotTableStyleType` pour les préréglages intégrés, et `setPivotTableStyleName` pour les styles personnalisés que vous avez définis via `addPivotTableStyle`. Définir les deux est sans conséquence, mais seul celui qui correspond à la source prévue est rendu.

{{% /alert %}}

Les valeurs disponibles de `TableStyleElementType` incluent `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` et `PAGE_FIELD_VALUES`.

L'exemple suivant définit un style de tableau croisé dynamique personnalisé avec une fine bordure noire sur `WHOLE_TABLE` et une police rouge en gras sur `GRAND_TOTAL_ROW`, puis l'applique via `setPivotTableStyleName` et enregistre au format `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

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

# Étape 2 : ajouter un élément WholeTable et appliquer des bordures noires fines sur les quatre côtés
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Étape 3 : ajouter un élément GrandTotalRow et appliquer une police rouge en gras
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Étape 4 : appliquer le style personnalisé par nom (PAS par PivotTableStyleType, qui est destiné aux préréglages intégrés)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Appliquer un seul style à chaque cellule du tableau croisé dynamique avec FormatAll**

`pivotTable.formatAll(Style)` est un raccourci qui applique un seul objet `Style` à chaque cellule du tableau croisé dynamique, y compris la zone de données, les en-têtes de lignes et de colonnes, ainsi que les totaux. Tout ce qui avait été défini auparavant via `setPivotTableStyleType` ou `setPivotTableStyleName` est supplanté.

{{% alert color="primary" %}}

`formatAll` supplante à la fois `setPivotTableStyleType` et `setPivotTableStyleName`. Ne l'utilisez que lorsqu'une apparence uniforme et indépendante du thème est requise pour l'ensemble du tableau croisé dynamique.

{{% /alert %}}

L'exemple suivant crée un `Style` avec un remplissage uni jaune, une police bleu foncé en gras et de fines bordures noires sur tous les côtés, puis l'applique avec `formatAll` et enregistre au format `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Scénario 4 : Appliquer un seul Style à chaque cellule du tableau croisé dynamique en utilisant FormatAll
# API utilisée : PivotTable.FormatAll(Style)
# Format cible : .xlsx
# Référence GitHub : voir le dépôt Aspose.Cells-for-.NET — exemples de style de tableau croisé dynamique

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Remplir les données sources : ligne d'en-tête (ligne 1) + 9 lignes de données (lignes 2-10)
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

# Assigner les champs du tableau croisé dynamique : Fruit -> Zone Ligne, Year -> Zone Colonne, Amount -> Zone Données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Construire un Style qui sera appliqué de force sur chaque cellule du tableau croisé dynamique
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# Appliquer FormatAll : force ce style unique sur chaque cellule du tableau croisé dynamique,
# remplaçant tout PivotTableStyleType / PivotTableStyleName précédemment défini
pivotTable.formatAll(style)

# Enregistrer le classeur au format moderne .xlsx
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Quelle API de style dois-je utiliser ?**

Le choix de l'API de style dépend du format de fichier dans lequel vous enregistrez. Utilisez le tableau ci-dessous comme référence rapide.

| Format de fichier cible | API à utiliser | Remarques |
|---|---|---|
| `.xls` (hérité) | `pivotTable.setAutoFormatType(int)` | Valeurs issues de `com.aspose.cells.pivot.PivotTableAutoFormatType` (par ex. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoré lors de l'enregistrement aux formats modernes. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style intégré) | `pivotTable.setPivotTableStyleType(int)` | Valeurs issues de `com.aspose.cells.PivotTableStyleType` (thèmes clairs/sombres, y compris les ajouts d'Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderne, style personnalisé) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | À utiliser lorsque les préréglages intégrés ne suffisent pas. Configurez via `tableStyleElement.setElementStyle(Style)`. |
| Tout format (substitution uniforme) | `pivotTable.formatAll(Style)` | Raccourci qui supplante tout autre paramètre de style dans l'ensemble du tableau croisé dynamique. |

En cas de doute, enregistrez au format `.xlsx` et utilisez `setPivotTableStyleType` pour les thèmes intégrés, ou `setPivotTableStyleName` pour les thèmes personnalisés.

{{< app/cells/assistant language="python" >}}