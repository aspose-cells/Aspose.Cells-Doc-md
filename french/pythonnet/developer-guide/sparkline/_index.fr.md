---
title: Graphiques sparkline dans Aspose.Cells pour Aspose.Cells for Python via .NET
linktitle: Sparklines
description: Aspose.Cells est une bibliothèque Python permettant de travailler avec des fichiers de feuilles de calcul qui prend en charge la création de graphiques sparkline — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des graphiques sparkline de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Python, feuille de calcul, graphiques sparkline, graphique sparkline de type ligne, graphique sparkline de type colonne, graphique sparkline de type gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la création de graphiques sparkline à l'intérieur des cellules de la feuille de calcul. Les graphiques sparkline sont des mini-graphiques qui tiennent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les graphiques sparkline de type ligne, colonne et gain/perte, et chacun peut être personnalisé en termes de couleur, d'épaisseur de ligne, de points haut/bas et de marqueurs.

{{% /alert %}}

## **Introduction**

Les graphiques sparkline sont de petits graphiques intégrés à une cellule qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de graphiques sparkline : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans le namespace `aspose.cells.charts`.

Dans Aspose.Cells, chaque graphique sparkline que vous ajoutez est créé via `worksheet.sparkline_groups.add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de graphique sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points haut/bas.

{{% alert color="primary" %}}

Un seul `SparklineGroup` peut contenir un ou plusieurs graphiques sparkline qui partagent le même style. Lorsque vous appelez `add` et passez une ligne de données plus une seule cellule de destination, vous obtenez un graphique sparkline à l'intérieur de cette cellule. Si votre plage de destination est plus large qu'une cellule, un graphique sparkline distinct est dessiné dans chaque cellule de destination, tous utilisant la même plage de données et le même style.

{{% /alert %}}

Cet article passe en revue chacun des trois types de graphiques sparkline pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Graphiques sparkline de type ligne**

Un graphique sparkline de type ligne trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour afficher les tendances au fil du temps. Dans Aspose.Cells, un graphique sparkline de type ligne est créé en passant `SparklineType.Line` à la méthode `sparkline_groups.add`.

Le flux de travail est le même que pour tout autre type de graphique sparkline :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où le graphique sparkline sera dessiné.
4. Appelez `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Le troisième argument — `False` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour un graphique sparkline de type ligne, vous pouvez définir la couleur de la ligne à l'aide de `group.line.color` (qui attend un `CellsColor` provenant de `aspose.cells.drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs des points haut/bas.
6. Enregistrez le classeur.

L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute un graphique sparkline de type ligne dans la cellule F1 qui retrace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points haut et bas.

```python
import aspose.cells as ac
import System.Drawing

# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Étape 3 : Construire un CellArea pointant vers la cellule de destination F1
dest = ac.CellArea()
dest.start_column = 5   # colonne F (indexée à partir de 0)
dest.end_column = 5
dest.start_row = 0      # ligne 1 (indexée à partir de 0)
dest.end_row = 0

# Étape 4 : Ajouter un sparkline en ligne de A1:E1 vers F1
# SparklineGroups.Add renvoie l'index du groupe nouvellement ajouté
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de la ligne du sparkline
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Étape 6 : Activer les marqueurs de point haut et de point bas
group.show_high_point = True
group.show_low_point = True

# Étape 7 : Enregistrer le classeur
workbook.save("output_line.xlsx")
```

## **Graphiques sparkline de type colonne**

Un graphique sparkline de type colonne restitue chaque point de données sous forme de barre verticale. Cela le rend particulièrement adapté aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptes. Dans Aspose.Cells, vous créez un graphique sparkline de type colonne en passant `SparklineType.Column` à la méthode `sparkline_groups.add`.

La procédure reproduit l'exemple du graphique sparkline de type ligne :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la même plage source (A1:E1) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.type` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple du graphique sparkline de type ligne.

L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue un graphique sparkline de type colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet de repérer facilement les contributions positives et négatives d'un coup d'œil.

```python
import aspose.cells as ac

# Étape 1 : Créer un Workbook et obtenir la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Étape 2 : Écrire des valeurs d'exemple dans A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# Étape 3 : Construire un CellArea pointant vers F1 (index de colonne 5, index de ligne 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Étape 4 : Ajouter un sparkline de type Colonne à la cellule de destination
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Étape 5 : Confirmer le type de sparkline en lisant group.Type
print("Sparkline Type added: " + str(group.type))

# Étape 6 : Enregistrer le workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Graphiques sparkline de type gain/perte**

Un graphique sparkline de type gain/perte est une variante spéciale du graphique sparkline de type colonne conçu pour n'afficher que deux résultats : une valeur positive est dessinée sous forme de barre « vers le haut » (un gain) et une valeur nulle ou négative est dessinée sous forme de barre « vers le bas » (une perte). Les graphiques sparkline de type gain/perte sont couramment utilisés pour visualiser des séquences de victoires et de défaites, des résultats de réussite/échec, ou tout résultat binaire au fil du temps.

Dans Aspose.Cells, un graphique sparkline de type gain/perte est créé en passant `SparklineType.Stacked` à la méthode `sparkline_groups.add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)

La procédure est identique aux deux autres types :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les graphiques sparkline de type gain/perte traitent chaque valeur comme un gain ou une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

L'exemple ci-dessous utilise les mêmes données d'entrée que les deux sections précédentes. Les valeurs 5, -3, 8, -2, 6 sont interprétées comme gain, perte, gain, perte, gain — et le graphique sparkline dessiné dans F1 reflète exactement ce motif.

```python
import aspose.cells as ac
import System.Drawing

# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Étape 2 : Remplir des données d'exemple dans la ligne 1 : A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Étape 3 : Construire un CellArea pointant vers F1 (colonne 5, ligne 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # ligne 1
dest.end_row = 0

# Étape 4 : Ajouter un sparkline Gain/Pertes (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Étape 5 : Personnaliser le groupe de sparklines
# Activer les marqueurs de points hauts et points bas
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Définir la couleur du point haut en vert
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Définir la couleur du point bas en rouge
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Définir la couleur du point négatif en orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Définir la couleur de série par défaut (utilisée pour les barres positives)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Étape 6 : Enregistrer le classeur
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **Combinaison des trois types de graphiques sparkline**

Les trois exemples précédents produisent chacun leur propre classeur afin que les fichiers de sortie soient faciles à inspecter de manière isolée. Dans un scénario réel, cependant, vous voudrez souvent comparer plusieurs séries de données côte à côte. La façon la plus propre de procéder consiste à placer plusieurs groupes de graphiques sparkline dans la même feuille de calcul, chaque groupe restituant un style différent.

Vous pouvez ajouter plusieurs objets `SparklineGroup` à la même `SparklineGroupCollection`, et chaque groupe peut cibler une cellule de destination différente ou une plage différente. Par exemple, vous pouvez placer un graphique sparkline de type ligne dans F1, un graphique sparkline de type colonne dans F2, et un graphique sparkline de type gain/perte dans F3 — tous lisant les mêmes données sources de la ligne 1 — afin que le lecteur puisse voir trois traitements visuels différents des mêmes nombres.

L'exemple combiné ci-dessous crée un classeur unique, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de graphiques sparkline dans les cellules F1, F2 et F3 — un de chaque type — afin que le fichier résultant démontre les trois styles de graphiques sparkline en une seule fois.

```python
import aspose.cells as ac
import System.Drawing

# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Étape 2 : Remplir des données d'exemple dans la ligne 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Étape 3 : Ajouter un groupe de sparklines de type Ligne à F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Personnaliser la couleur de la sparkline de type Ligne via CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Personnaliser la couleur de la série de sparklines de type Colonne
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Étape 5 : Ajouter un groupe de sparklines Win/Loss (Empilé) à F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Personnaliser la couleur de la série de sparklines Win/Loss
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

Lorsque vous combinez plusieurs groupes de graphiques sparkline dans une seule feuille de calcul, chaque groupe est indépendant. Ils peuvent partager la même plage source ou utiliser des plages sources différentes, et ils peuvent être stylisés indépendamment. Cela facilite la création d'un petit « tableau de bord » de visualisations intégrées aux cellules directement à l'intérieur d'une feuille de calcul existante.

{{% /alert %}}

## **Personnalisation de l'apparence des graphiques sparkline**

Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.sparkline_groups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :

- **`group.type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lorsque le groupe est ajouté, mais vous pouvez le relire pour le confirmer.
- **`group.line.color`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.create_cells_color()`. C'est la propriété à utiliser pour la couleur du trait du graphique sparkline de type ligne.
- **`group.line.weight`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points haut/bas** — indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — indicateurs qui activent/désactivent les marqueurs sur les points de données premier, dernier et négatif.

Pour changer une couleur, créez toujours une instance de `CellsColor` et attribuez-la à la propriété concernée. Les propriétés de couleur des graphiques sparkline attendent le type `CellsColor` provenant de `aspose.cells.drawing` — n'attribuez pas directement une valeur de couleur brute à ces propriétés. La méthode `sparkline_groups.add` elle-même renvoie un objet `SparklineGroup` entièrement typé, de sorte que vous pouvez enchaîner les affectations de propriétés sur la valeur de retour ou la stocker dans une variable locale et la personnaliser avant d'enregistrer.



{{< app/cells/assistant language="python" >}}