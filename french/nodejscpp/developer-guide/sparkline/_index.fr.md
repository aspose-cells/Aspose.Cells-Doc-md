---
title: Sparklines dans Aspose.Cells for Node.js via C++
linktitle: Sparklines dans Aspose.Cells for Node.js via C++
description: Aspose.Cells est une bibliothèque Node.js permettant de travailler avec des fichiers de feuilles de calcul qui prend en charge la création de sparklines — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Node.js, feuille de calcul, sparklines, sparkline linéaire, sparkline en colonnes, sparkline gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules de la feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule, fournissant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines linéaires, en colonnes et gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points hauts/bas et de marqueurs.

## **Introduction**
Les sparklines sont de petits graphiques in-cell qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans le namespace `Aspose.Cells.Charts`.
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.sparklineGroups.add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points hauts/bas.
Cet article passe en revue chacun des trois types de sparklines pris en charge par Aspose.Cells — **Linéaire**, **En colonnes** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines linéaires**
Une sparkline linéaire trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour montrer des tendances au fil du temps. Dans Aspose.Cells, une sparkline linéaire est créée en passant `SparklineType.Line` à la méthode `sparklineGroups.add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne) et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour une sparkline linéaire, vous pouvez définir la couleur de la ligne via `group.line.color` (qui attend un `CellsColor` de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs des points hauts/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline linéaire dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points hauts et bas.

```javascript
const AsposeCells = require("aspose.cells");
// Étape 1 : Créer un classeur et obtenir la première feuille de calcul
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Étape 3 : Construire un CellArea pointant vers la cellule de destination F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // colonne F (indexée à partir de 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // ligne 1 (indexée à partir de 0)
dest.setEndRow(0);
// Étape 4 : Ajouter un sparkline de type Ligne depuis A1:E1 dans F1
// SparklineGroups.Add renvoie l'index du groupe nouvellement ajouté
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de la ligne du sparkline
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Étape 6 : Activer les marqueurs de point haut et de point bas
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Étape 7 : Enregistrer le classeur
workbook.save("output_line.xlsx");
```

## **Sparklines en colonnes**
Une sparkline en colonnes affiche chaque point de données sous forme de barre verticale. Cela la rend bien adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les décomptes. Dans Aspose.Cells, vous créez une sparkline en colonnes en passant `SparklineType.Column` à la méthode `sparklineGroups.add`.
La procédure est calquée sur l'exemple de la sparkline linéaire :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.type` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie séparé afin qu'il n'écrase pas l'exemple de la sparkline linéaire.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline en colonnes dans F1. Les valeurs négatives sont dessinées sous forme de barres descendant vers le bas et les valeurs positives sous forme de barres montant vers le haut, ce qui permet de repérer d'un coup d'œil les contributions positives et négatives.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Étape 2 : Écrire des valeurs d'exemple dans A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Étape 3 : Construire un CellArea pointant vers F1 (indice de colonne 5, indice de ligne 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Étape 4 : Ajouter un sparkline de type Colonne à la cellule de destination
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Étape 5 : Confirmer le type de sparkline en lisant group.Type
console.log("Sparkline Type added: " + group.getType());
// Étape 6 : Enregistrer le classeur
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Sparklines gain/perte**
Une sparkline gain/perte est une variante spéciale de la sparkline en colonnes conçue pour afficher seulement deux résultats : une valeur positive est dessinée comme une barre « vers le haut » (un gain) et une valeur nulle ou négative est dessinée comme une barre « vers le bas » (une perte). Les sparklines gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats de réussite/échec ou tout autre résultat binaire au fil du temps.
Dans Aspose.Cells, une sparkline gain/perte est créée en passant `SparklineType.Stacked` à la méthode `sparklineGroups.add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les sparklines gain/perte traitent chaque valeur soit comme un gain soit comme une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe en a. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Étape 2 : Remplir les données d'exemple dans la ligne 1 : A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Étape 3 : Construire un CellArea pointant vers F1 (colonne 5, ligne 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // ligne 1
dest.setEndRow(0);
// Étape 4 : Ajouter un sparkline Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Étape 5 : Personnaliser le groupe de sparklines
// Activer les marqueurs de point haut et de point bas
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Définir la couleur du point haut en vert
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Définir la couleur du point bas en rouge
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Définir la couleur du point négatif en orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Définir la couleur de série par défaut (utilisée pour les barres positives)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Étape 6 : Enregistrer le classeur
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinaison des trois types de sparklines**
L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant démontre les trois styles de sparklines en une seule fois.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Étape 2 : Remplir des données d'exemple dans la ligne 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Étape 3 : Ajouter un groupe de sparklines de type ligne à F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personnaliser la couleur de la sparkline de type ligne via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Étape 4 : Ajouter un groupe de sparklines de type colonne à F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personnaliser la couleur de la série de sparklines de type colonne
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Étape 5 : Ajouter un groupe de sparklines de type gain/perte (empilé) à F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personnaliser la couleur de la série de sparklines gain/perte
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx");
```

## **Personnalisation de l'apparence des sparklines**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.sparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lorsque le groupe est ajouté, mais vous pouvez le relire pour le confirmer.
- **`group.line.color`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créée via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur de trait de la sparkline linéaire.
- **`group.line.weight`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points hauts/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus hauts et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — des indicateurs qui activent/désactivent les marqueurs sur les points de données premier, dernier et négatif.
Pour changer une couleur, créez toujours une instance de `CellsColor` et affectez-la à la propriété appropriée. N'affectez pas directement un `System.Drawing.Color` aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `sparklineGroups.add` elle-même renvoie un objet `SparklineGroup` entièrement typé, vous pouvez donc enchaîner les affectations de propriétés sur la valeur de retour ou la stocker dans une variable locale et la personnaliser avant l'enregistrement.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}