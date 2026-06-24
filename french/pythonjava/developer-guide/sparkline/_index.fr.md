---
title: Sparklines dans Aspose.Cells for Python via Java
linktitle: Sparklines
description: Aspose.Cells est une bibliothèque Python via Java pour travailler avec des fichiers de feuilles de calcul qui prend en charge la création de sparklines — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type ligne, colonne et victoire/défaite à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Python via Java, feuille de calcul, sparklines, sparkline de type ligne, sparkline de type colonne, sparkline de type victoire/défaite, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules d'une feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule et offrent une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines de type ligne, colonne et victoire/défaite, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points hauts/bas et de marqueurs.

{{% /alert %}}

## **Introduction**

Les sparklines sont de petits graphiques intégrés dans une cellule qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données, sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **victoire/défaite**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` disponibles dans le namespace `Aspose.Cells.Charts`.

Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.getSparklineGroups().add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination, ainsi que les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points hauts/bas.

{{% alert color="primary" %}}

Un seul `SparklineGroup` peut contenir une ou plusieurs sparklines qui partagent le même style. Lorsque vous appelez `add` et passez une ligne de données ainsi qu'une seule cellule de destination, vous obtenez une sparkline dans cette cellule. Si votre plage de destination est plus large qu'une cellule, une sparkline distincte est dessinée dans chaque cellule de destination, toutes utilisant la même plage de données et le même style.

{{% /alert %}}

Cet article présente chacun des trois types de sparklines pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Victoire/Défaite** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines de type Ligne**

Une sparkline de type ligne trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour afficher des tendances dans le temps. Dans Aspose.Cells, une sparkline de type ligne est créée en passant `SparklineType.LINE` à la méthode `add`.

Le flux de travail est le même que pour tout autre type de sparkline :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour une sparkline de type ligne, vous pouvez définir la couleur de la ligne via `group.getLine().getColor()` (qui attend un `CellsColor` de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs des points hauts et bas.
6. Enregistrez le classeur.

L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline de type ligne dans la cellule F1 qui retrace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points hauts et bas.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Étape 3 : Construire un CellArea pointant vers la cellule de destination F1
dest = CellArea()
dest.setStartColumn(5)  # colonne F (indexée à 0)
dest.setEndColumn(5)
dest.setStartRow(0)     # ligne 1 (indexée à 0)
dest.setEndRow(0)

# Étape 4 : Ajouter un graphique sparkline de type Ligne de A1:E1 vers F1
# SparklineGroups.add renvoie l'index du groupe nouvellement ajouté
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de la ligne du sparkline
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Étape 6 : Activer les marqueurs de point haut et point bas
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Étape 7 : Enregistrer le classeur
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Sparklines de type Colonne**

Une sparkline de type colonne représente chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les décomptes. Dans Aspose.Cells, vous créez une sparkline de type colonne en passant `SparklineType.COLUMN` à la méthode `add`.

La procédure reproduit celle de l'exemple de la sparkline de type ligne :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la même plage source (A1:E1) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.getType()` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie séparé afin qu'il n'écrase pas l'exemple de la sparkline de type ligne.

L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline de type colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas, et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet de repérer d'un coup d'œil les contributions positives et négatives.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Étape 1 : Créer un Workbook et obtenir la première feuille de calcul
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

# Étape 6 : Enregistrer le workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **Sparklines de type Victoire/Défaite**

Une sparkline de type victoire/défaite est une variante particulière de la sparkline de type colonne, conçue pour n'afficher que deux résultats : une valeur positive est dessinée sous forme de barre « vers le haut » (une victoire) et une valeur nulle ou négative est dessinée sous forme de barre « vers le bas » (une défaite). Les sparklines de type victoire/défaite sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats succès/échec, ou tout résultat binaire dans le temps.

Dans Aspose.Cells, une sparkline de type victoire/défaite est créée en passant `SparklineType.STACKED` à la méthode `add`. (Malgré son nom, `SparklineType.STACKED` est la valeur d'énumération utilisée pour demander le rendu victoire/défaite.)

La procédure est identique à celle des deux autres types :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les sparklines de type victoire/défaite traitent chaque valeur comme une victoire ou une défaite, l'amplitude de la valeur n'a aucune importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut, et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant les couleurs d'accentuation des barres de victoire et de défaite.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

L'exemple ci-dessous utilise les mêmes données d'entrée que les deux sections précédentes. Les valeurs 5, -3, 8, -2, 6 sont interprétées comme victoire, défaite, victoire, défaite, victoire — et la sparkline dessinée dans F1 reflète exactement ce schéma.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Étape 1 : Créer un Workbook et obtenir la première feuille de calcul
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Étape 2 : Remplir des données d'exemple dans la ligne 1 : A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Étape 3 : Construire un CellArea pointant vers F1 (colonne 5, ligne 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # ligne 1
dest.setEndRow(0)

# Étape 4 : Ajouter un sparkline Win/Loss (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Étape 5 : Personnaliser le groupe de sparklines
# Activer les marqueurs des points hauts et bas
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Définir la couleur du point haut en vert
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Définir la couleur du point bas en rouge
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Définir la couleur des points négatifs en orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Définir la couleur par défaut de la série (utilisée pour les barres positives)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Étape 6 : Enregistrer le workbook
workbook.save("output_winloss.xlsx")

print("Workbook enregistré avec succès : output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Combinaison des trois types de sparklines**

Les trois exemples précédents produisent chacun leur propre classeur, afin que les fichiers de sortie soient faciles à inspecter de manière isolée. Dans un scénario réel, cependant, vous souhaiterez souvent comparer plusieurs séries de données côte à côte. La façon la plus propre de procéder consiste à placer plus d'un groupe de sparklines dans la même feuille de calcul, chaque groupe restituant un style différent.

Vous pouvez ajouter plusieurs objets `SparklineGroup` à la même `SparklineGroupCollection`, et chaque groupe peut cibler une cellule de destination différente ou une plage différente. Par exemple, vous pouvez placer une sparkline de type ligne dans F1, une sparkline de type colonne dans F2, et une sparkline de type victoire/défaite dans F3 — toutes lisant les mêmes données sources de la ligne 1 — afin que le lecteur puisse voir trois traitements visuels différents des mêmes nombres.

L'exemple combiné ci-dessous crée un classeur unique, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant démontre les trois styles de sparklines à la fois.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Étape 2 : Remplir des données d'exemple dans la ligne 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Étape 3 : Ajouter un groupe de sparklines de type ligne à F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# Personnaliser la couleur de la sparkline de type ligne via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# Étape 4 : Ajouter un groupe de sparklines de type colonne à F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Personnaliser la couleur de la série de la sparkline de type colonne
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Étape 5 : Ajouter un groupe de sparklines Win/Loss (empilées) à F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Personnaliser la couleur de la série de la sparkline win/loss
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # OrangeFoncé
stackedGroup.setSeriesColor(stackedColor)

# Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Lorsque vous combinez plusieurs groupes de sparklines dans une seule feuille de calcul, chaque groupe est indépendant. Ils peuvent partager la même plage source ou utiliser des plages sources différentes, et ils peuvent être stylisés indépendamment. Cela facilite la création d'un petit « tableau de bord » de visualisations intégrées directement dans une feuille de calcul existante.

{{% /alert %}}

## **Personnalisation de l'apparence des sparklines**

Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.getSparklineGroups()`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :

- **`group.getType()`** — le `SparklineType` (LINE, COLUMN ou STACKED). Il est défini lorsque le groupe est ajouté, mais vous pouvez le relire pour le confirmer.
- **`group.getLine().getColor()`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur du trait d'une sparkline de type ligne.
- **`group.getLine().getWeight()`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points hauts/bas** — indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre l'accent sur les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — indicateurs qui activent ou désactivent les marqueurs sur les points de données premier, dernier et négatif.

Pour modifier une couleur, créez toujours une instance de `CellsColor` et attribuez-la à la propriété correspondante. N'attribuez pas directement un `java.awt.Color` aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `add` elle-même renvoie un objet `SparklineGroup` entièrement typé, ce qui vous permet d'enchaîner les affectations de propriétés sur la valeur de retour, ou de la stocker dans une variable locale et de la personnaliser avant l'enregistrement.



{{< app/cells/assistant language="python" >}}