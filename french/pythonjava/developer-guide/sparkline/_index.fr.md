---
title: Sparklines dans Aspose.Cells for Python via Java
linktitle: Sparklines dans Aspose.Cells for Python via Java
description: Aspose.Cells est une bibliothèque Python via Java pour travailler avec des fichiers de tableur qui prend en charge la création de sparklines, des graphiques miniatures placés dans les cellules des feuilles de calcul. Cet article explique comment ajouter et personnaliser des sparklines en ligne, en colonne et de type gain/perte en utilisant Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Python via Java, tableur, sparklines, sparkline en ligne, sparkline en colonne, sparkline gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules des feuilles de calcul. Les sparklines sont des graphiques miniatures qui s'intègrent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines en ligne, en colonne et de type gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points hauts/bas et de marqueurs.

## **Introduction**
Les sparklines sont de petits graphiques intégrés aux cellules qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans l'espace de noms `Aspose.Cells.Charts`.
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.getSparklineGroups().add(...)`, qui retourne un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et des propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points hauts/bas.
Cet article passe en revue chacun des trois types de sparklines pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines en ligne**
Une sparkline en ligne trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour afficher des tendances au fil du temps. Dans Aspose.Cells, une sparkline en ligne est créée en passant `SparklineType.LINE` à la méthode `add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données source (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` retourné. Pour une sparkline en ligne, vous pouvez définir la couleur de la ligne en utilisant `group.getLine().getColor()` (qui attend un `CellsColor` de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs de points hauts/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline en ligne dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points hauts et bas.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **Sparklines en colonne**
Une sparkline en colonne restitue chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptes. Dans Aspose.Cells, vous créez une sparkline en colonne en passant `SparklineType.COLUMN` à la méthode `add`.
La procédure reprend l'exemple de la sparkline en ligne :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Construisez un `CellArea` décrivant la cellule de destination.
3. Appelez `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
4. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.getType()` pour confirmer le type, ou en ajustant la couleur des barres.
5. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple de sparkline en ligne.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline en colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres vers le bas et les valeurs positives sous forme de barres vers le haut, ce qui permet de repérer facilement d'un coup d'œil les contributions positives et négatives.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Étape 2 : Écrire des valeurs d'exemple dans A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# Étape 3 : Construire un CellArea pointant vers F1 (indice de colonne 5, indice de ligne 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# Étape 4 : Ajouter un sparkline de type Column à la cellule de destination
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# Étape 5 : Confirmer le type de sparkline en lisant group.Type
print("Sparkline Type added: " + str(group.getType()))
# Étape 6 : Enregistrer le classeur
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **Sparklines Gain/Perte**
Une sparkline gain/perte est une variante spéciale de la sparkline en colonne conçue pour ne montrer que deux résultats : une valeur positive est dessinée sous forme de barre « vers le haut » (un gain) et une valeur nulle ou négative est dessinée sous forme de barre « vers le bas » (une perte). Les sparklines gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussi/échoué ou tout résultat binaire au fil du temps.
Dans Aspose.Cells, une sparkline gain/perte est créée en passant `SparklineType.STACKED` à la méthode `add`. (Malgré son nom, `SparklineType.STACKED` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les sparklines gain/perte traitent chaque valeur soit comme un gain soit comme une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` retourné, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **Combinaison des trois types de sparklines**
L'exemple combiné ci-dessous crée un classeur unique, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — afin que le fichier résultant illustre les trois styles de sparklines en une seule fois.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **Personnalisation de l'apparence des sparklines**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.getSparklineGroups()`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.getType()`** — le `SparklineType` (LINE, COLUMN ou STACKED). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour le confirmer.
- **`group.getLine().getColor()`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur de trait des sparklines en ligne.
- **`group.getLine().getWeight()`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs de points hauts/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs de points premier/dernier/négatif** — des indicateurs qui activent ou désactivent les marqueurs sur les premier, dernier et négatif points de données.
Pour modifier une couleur, créez toujours une instance de `CellsColor` et assignez-la à la propriété appropriée. N'assignez pas un `java.awt.Color` directement aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `add` elle-même retourne un objet `SparklineGroup` entièrement typé, vous pouvez donc enchaîner les affectations de propriétés sur la valeur de retour ou la stocker dans une variable locale et la personnaliser avant l'enregistrement.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}