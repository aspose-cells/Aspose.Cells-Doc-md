---
title: Graphiques sparkline dans Aspose.Cells for Node.js via Java
description: Aspose.Cells est une bibliothèque Node.js via Java permettant de travailler avec des fichiers de tableur et prend en charge la création de graphiques sparkline — des mini-graphiques placés dans les cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type courbe, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, bibliothèque Node.js via Java, tableur, sparklines, sparkline de type courbe, sparkline de type colonne, sparkline de type gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines dans les cellules d'une feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule et offrent une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines de type courbe, colonne et gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de trait, de points haut/bas et de marqueurs.
{{% /alert %}}

## **Introduction**
Les sparklines sont de petits graphiques dans une cellule, utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **courbe**, **colonne** et **gain/perte**. Aspose.Cells offre la même fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` situées dans le namespace `com.aspose.cells.Charts`.
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.SparklineGroups.add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur du trait, l'épaisseur du trait, les marqueurs et les indicateurs de points haut/bas.
Cet article passe en revue les trois types de sparklines pris en charge par Aspose.Cells — **Courbe**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines de type Courbe**
Une sparkline de type courbe trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour représenter des tendances au fil du temps. Dans Aspose.Cells, une sparkline de type courbe est créée en passant `SparklineType.Line` à la méthode `SparklineGroups.add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Vous pouvez éventuellement personnaliser le `SparklineGroup` renvoyé. Pour une sparkline de type courbe, vous pouvez définir la couleur du trait à l'aide de `group.Line.Color` (qui attend une `CellsColor` issue de `com.aspose.cells.Drawing`), ajuster l'épaisseur du trait et activer les marqueurs des points haut/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, puis ajoute une sparkline de type courbe dans la cellule F1 qui retrace ces valeurs. Il personnalise également la couleur du trait en rouge et active les marqueurs pour les points haut et bas.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Étape 3 : Construire une CellArea pointant vers la cellule de destination F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // colonne F (indexée à partir de 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // ligne 1 (indexée à partir de 0)
dest.setEndRow(0);
// Étape 4 : Ajouter une ligne sparkline de A1:E1 dans F1
// SparklineGroups.Add renvoie l'index du groupe nouvellement ajouté
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de ligne du sparkline
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Étape 6 : Activer les marqueurs des points hauts et bas
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Étape 7 : Enregistrer le classeur
workbook.save("output_line.xlsx");
```

## **Sparklines de type Colonne**
Une sparkline de type colonne représente chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou des comptages. Dans Aspose.Cells, vous créez une sparkline de type colonne en passant `SparklineType.Column` à la méthode `SparklineGroups.add`.
La procédure est la même que pour l'exemple de la sparkline de type courbe :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources avec les valeurs à visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.Type` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple de la sparkline de type courbe.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et affiche une sparkline de type colonne dans F1. Les valeurs négatives sont représentées par des barres orientées vers le bas et les valeurs positives par des barres orientées vers le haut, ce qui permet de repérer d'un coup d'œil les contributions positives et négatives.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Étape 2 : Écrire des valeurs d'exemple dans A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Étape 3 : Construire un CellArea pointant vers F1 (index de colonne 5, index de ligne 0)
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

## **Sparklines de type Gain/Perte**
Une sparkline de type gain/perte est une variante spéciale de la sparkline de type colonne conçue pour n'afficher que deux résultats : une valeur positive est représentée par une barre vers le haut (un gain) et une valeur nulle ou négative est représentée par une barre vers le bas (une perte). Les sparklines de type gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussite/échec, ou tout résultat binaire au fil du temps.
Dans Aspose.Cells, une sparkline de type gain/perte est créée en passant `SparklineType.Stacked` à la méthode `SparklineGroups.add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les sparklines de type gain/perte traitent chaque valeur soit comme un gain, soit comme une perte, l'amplitude de la valeur n'a aucune importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Vous pouvez éventuellement personnaliser le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Étape 2 : Remplir des données d'exemple dans la ligne 1 : A1=5, B1=-3, C1=8, D1=-2, E1=6
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
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Étape 5 : Personnaliser le groupe de sparklines
// Activer les marqueurs de point haut et de point bas
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Définir la couleur du point haut en vert
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Définir la couleur du point bas en rouge
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Définir la couleur des points négatifs en orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Définir la couleur par défaut de la série (utilisée pour les barres positives)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Étape 6 : Enregistrer le classeur
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinaison des trois types de sparklines**
L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — afin que le fichier résultant présente les trois styles de sparklines en une seule fois.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Étape 2 : Remplir les données d'exemple dans la ligne 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Étape 3 : Ajouter un groupe de sparklines de type Ligne à F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personnaliser la couleur de la sparkline de type Ligne via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personnaliser la couleur de la série de sparklines de type Colonne
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Étape 5 : Ajouter un groupe de sparklines de type Win/Loss (Empilé) à F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personnaliser la couleur de la série de sparklines de type win/loss
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx");
```

## **Personnalisation de l'apparence des sparklines**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.SparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.Type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour le confirmer.
- **`group.Line.Color`** — la couleur du trait, exprimée sous forme de `CellsColor` créée via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur du trait d'une sparkline de type courbe.
- **`group.Line.Weight`** — l'épaisseur du trait en points. Des valeurs plus élevées produisent des traits plus épais.
- **Marqueurs des points haut/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — des indicateurs qui activent ou désactivent les marqueurs sur le premier, le dernier et les points de données négatifs.
Pour modifier une couleur, créez toujours une instance de `CellsColor` et affectez-la à la propriété correspondante. N'affectez pas directement une `java.awt.Color` aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` issu de `com.aspose.cells.Drawing`. La méthode `SparklineGroups.add` elle-même renvoie un objet `SparklineGroup` complètement typé, ce qui vous permet d'enchaîner les affectations de propriétés sur la valeur de retour ou de la stocker dans une variable locale et de la personnaliser avant l'enregistrement.

{{< app/cells/assistant language="javascript" >}}