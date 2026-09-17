---
title: Graphiques sparkline dans Aspose.Cells for Python via .NET
linktitle: Graphiques sparkline dans Aspose.Cells for Python via .NET
description: Aspose.Cells est une bibliothèque Python permettant de travailler avec des fichiers de feuilles de calcul qui prend en charge la création de graphiques sparkline — des miniatures de graphiques placées dans les cellules des feuilles de calcul. Cet article explique comment ajouter et personnaliser des graphiques sparkline de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Python, feuille de calcul, graphiques sparkline, graphique sparkline en ligne, graphique sparkline en colonne, graphique sparkline gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de graphiques sparkline dans les cellules des feuilles de calcul. Les graphiques sparkline sont des miniatures de graphiques qui s'intègrent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les graphiques sparkline de type ligne, colonne et gain/perte, et chacun peut être personnalisé en termes de couleur, d'épaisseur de ligne, de points hauts/bas et de marqueurs.

## **Introduction**
Les graphiques sparkline sont de petits graphiques intégrés aux cellules qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de graphiques sparkline : **ligne**, **colonne** et **gain/perte**. Aspose.Cells propose cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans l'espace de noms `aspose.cells.charts`.
Dans Aspose.Cells, chaque graphique sparkline que vous ajoutez est créé via `worksheet.sparkline_groups.add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de graphique sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points hauts/bas.
Cet article présente chacun des trois types de graphiques sparkline pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Graphiques sparkline en ligne**
Un graphique sparkline en ligne trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour afficher des tendances au fil du temps. Dans Aspose.Cells, un graphique sparkline en ligne est créé en passant `SparklineType.Line` à la méthode `sparkline_groups.add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où le graphique sparkline sera dessiné.
4. Appelez `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Le troisième argument — `False` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour un graphique sparkline en ligne, vous pouvez définir la couleur de la ligne à l'aide de `group.line.color` (qui attend un `CellsColor` issu de `aspose.cells.drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs des points hauts/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute un graphique sparkline en ligne dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points hauts et bas.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **Graphiques sparkline en colonne**
Un graphique sparkline en colonne représente chaque point de données sous forme de barre verticale. Cela le rend bien adapté aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptes. Dans Aspose.Cells, vous créez un graphique sparkline en colonne en passant `SparklineType.Column` à la méthode `sparkline_groups.add`.
La procédure est identique à celle de l'exemple du graphique sparkline en ligne :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Construisez un `CellArea` décrivant la cellule de destination.
3. Appelez `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
4. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.type` pour confirmer le type, ou en ajustant la couleur des barres.
5. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple du graphique sparkline en ligne.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue un graphique sparkline en colonne dans F1. Les valeurs négatives sont représentées par des barres descendantes et les valeurs positives par des barres ascendantes, ce qui permet de repérer facilement d'un coup d'œil les contributions positives et négatives.

```python
import aspose.cells as ac
# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
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
# Étape 4 : Ajouter un sparkline de type colonne à la cellule de destination
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Étape 5 : Confirmer le type de sparkline en lisant group.Type
print("Sparkline Type added: " + str(group.type))
# Étape 6 : Enregistrer le classeur
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Graphiques sparkline gain/perte**
Un graphique sparkline gain/perte est une variante spéciale du graphique sparkline en colonne conçu pour n'afficher que deux résultats : une valeur positive est représentée par une barre « ascendante » (une victoire) et une valeur nulle ou négative par une barre « descendante » (une perte). Les graphiques sparkline gain/perte sont couramment utilisés pour visualiser des séquences de victoires et de défaites, des résultats de réussite/échec ou tout résultat binaire au fil du temps.
Dans Aspose.Cells, un graphique sparkline gain/perte est créé en passant `SparklineType.Stacked` à la méthode `sparkline_groups.add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les graphiques sparkline gain/perte traitent chaque valeur soit comme une victoire, soit comme une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres ascendantes et les valeurs non positives deviennent des barres descendantes.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **Combinaison des trois types de graphiques sparkline**
L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de graphiques sparkline dans les cellules F1, F2 et F3 — un de chaque type — afin que le fichier résultant illustre simultanément les trois styles de graphiques sparkline.

```python
import aspose.cells as ac
import System.Drawing
# Étape 1 : Créer un classeur et obtenir la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Étape 2 : Remplir les données d'exemple dans la ligne 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Étape 3 : Ajouter un groupe de sparklines en ligne à F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# Personnaliser la couleur de la sparkline en ligne via CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color
# Étape 4 : Ajouter un groupe de sparklines en colonnes à F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# Personnaliser la couleur de la série de sparklines en colonnes
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color
# Étape 5 : Ajouter un groupe de sparklines Gagne/Perd (Empilé) à F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Personnaliser la couleur de la série de sparklines gagne/perd
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx")
```

## **Personnalisation de l'apparence des graphiques sparkline**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.sparkline_groups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour le confirmer.
- **`group.line.color`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.create_cells_color()`. C'est la propriété à utiliser pour la couleur du trait du graphique sparkline en ligne.
- **`group.line.weight`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points hauts/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus hauts et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — des indicateurs qui activent/désactivent les marqueurs sur les points de données premier, dernier et négatif.
Pour modifier une couleur, créez toujours une instance `CellsColor` et attribuez-la à la propriété concernée. Les propriétés de couleur des graphiques sparkline attendent le type `CellsColor` issu de `aspose.cells.drawing` — ne leur attribuez pas directement une valeur de couleur brute. La méthode `sparkline_groups.add` elle-même renvoie un objet `SparklineGroup` complètement typé, ce qui vous permet d'enchaîner les affectations de propriétés sur la valeur renvoyée ou de la stocker dans une variable locale et de la personnaliser avant l'enregistrement.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}