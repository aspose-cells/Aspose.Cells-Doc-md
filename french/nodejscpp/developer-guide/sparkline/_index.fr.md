---
title: Sparklines dans Aspose.Cells pour Aspose.Cells for Node.js via C++
linktitle: Sparklines
description: Aspose.Cells est une bibliothèque Node.js permettant de travailler avec des fichiers tableurs qui prend en charge la création de sparklines — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Node.js, tableur, sparklines, sparkline en ligne, sparkline en colonne, sparkline gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules de la feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines de type ligne, colonne et gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points haut/bas et de marqueurs.

{{% /alert %}}

## **Introduction**

Les sparklines sont de petits graphiques intégrés aux cellules, utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reflète cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans le namespace `Aspose.Cells.Charts`.

Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.sparklineGroups.add(...)`, qui retourne un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination, ainsi que les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs des points haut/bas.

{{% alert color="primary" %}}

Un seul `SparklineGroup` peut contenir une ou plusieurs sparklines qui partagent le même style. Lorsque vous appelez `add` et passez une ligne de données ainsi qu'une seule cellule de destination, vous obtenez une sparkline à l'intérieur de cette cellule. Si votre plage de destination est plus large qu'une seule cellule, une sparkline distincte est dessinée dans chaque cellule de destination, toutes utilisant la même plage de données et le même style.

{{% /alert %}}

Cet article passe en revue chacun des trois types de sparklines pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines en ligne**

Une sparkline en ligne trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour montrer des tendances au fil du temps. Dans Aspose.Cells, une sparkline en ligne est créée en passant `SparklineType.Line` à la méthode `sparklineGroups.add`.

Le flux de travail est le même que pour tout autre type de sparkline :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données source (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` retourné. Pour une sparkline en ligne, vous pouvez définir la couleur de la ligne à l'aide de `group.line.color` (qui attend un `CellsColor` provenant de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs des points haut/bas.
6. Enregistrez le classeur.

L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline en ligne dans la cellule F1 qui retrace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points haut et bas.

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
dest.setStartColumn(5);   // colonne F (indexée à 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // ligne 1 (indexée à 0)
dest.setEndRow(0);

// Étape 4 : Ajouter un graphique sparkline en ligne de A1:E1 dans F1
// SparklineGroups.Add renvoie l'index du groupe nouvellement ajouté
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de la ligne sparkline
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Étape 6 : Activer les marqueurs des points hauts et bas
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Étape 7 : Enregistrer le classeur
workbook.save("output_line.xlsx");
```

## **Sparklines en colonne**

Une sparkline en colonne restitue chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'ampleur est significative — par exemple, les chiffres de ventes mensuels ou les comptes. Dans Aspose.Cells, vous créez une sparkline en colonne en passant `SparklineType.Column` à la méthode `sparklineGroups.add`.

La procédure reflète l'exemple de la sparkline en ligne :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la même plage source (A1:E1) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.type` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple de sparkline en ligne.

L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline en colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet d'identifier facilement d'un coup d'œil les contributions positives et négatives.

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

## **Sparklines Gain/Perte**

Une sparkline gain/perte est une variante spéciale de la sparkline en colonne conçue pour ne montrer que deux résultats : une valeur positive est dessinée sous forme de barre « vers le haut » (une victoire) et une valeur nulle ou négative est dessinée sous forme de barre « vers le bas » (une perte). Les sparklines gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussite/échec, ou tout résultat binaire au fil du temps.

Dans Aspose.Cells, une sparkline gain/perte est créée en passant `SparklineType.Stacked` à la méthode `sparklineGroups.add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'enum utilisée pour demander le rendu gain/perte.)

La procédure est la même que pour les deux autres types :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les sparklines gain/perte traitent chaque valeur soit comme une victoire soit comme une perte, l'ampleur de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` retourné, par exemple en définissant des couleurs d'accentuation pour les barres de victoire et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

L'exemple ci-dessous utilise les mêmes données d'entrée que les deux sections précédentes. Les valeurs 5, -3, 8, -2, 6 sont interprétées comme victoire, perte, victoire, perte, victoire — et la sparkline dessinée dans F1 reflète exactement ce motif.

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

// Définir la couleur par défaut de la série (utilisée pour les barres positives)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Étape 6 : Enregistrer le classeur
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinaison des trois types de sparklines**

Les trois exemples précédents produisent chacun leur propre classeur afin que les fichiers de sortie soient faciles à inspecter de manière isolée. Dans un scénario réel, cependant, vous voudrez souvent comparer plusieurs séries de données côte à côte. La manière la plus propre de procéder consiste à placer plus d'un groupe de sparklines dans la même feuille de calcul, chaque groupe restituant un style différent.

Vous pouvez ajouter plusieurs objets `SparklineGroup` à la même `SparklineGroupCollection`, et chaque groupe peut cibler une cellule de destination différente ou une plage différente. Par exemple, vous pourriez placer une sparkline en ligne dans F1, une sparkline en colonne dans F2 et une sparkline gain/perte dans F3 — lisant toutes les mêmes données source de la ligne 1 — afin que le lecteur puisse voir trois traitements visuels différents des mêmes chiffres.

L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant démontre les trois styles de sparklines à la fois.

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
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personnaliser la couleur de la série de la sparkline de type Colonne
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Étape 5 : Ajouter un groupe de sparklines de type Gain/Perte (Empilé) à F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personnaliser la couleur de la série de la sparkline Gain/Perte
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Lorsque vous combinez plusieurs groupes de sparklines dans une seule feuille de calcul, chaque groupe est indépendant. Ils peuvent partager la même plage source ou utiliser des plages source différentes, et ils peuvent être stylisés indépendamment. Cela facilite la construction d'un petit « tableau de bord » de visualisations intra-cellulaires directement à l'intérieur d'une feuille de calcul existante.

{{% /alert %}}

## **Personnalisation de l'apparence des sparklines**

Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.sparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :

- **`group.type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour confirmation.
- **`group.line.color`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur du tracé de la sparkline en ligne.
- **`group.line.weight`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points haut/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — des indicateurs qui activent/désactivent les marqueurs sur les points de données premier, dernier et négatif.

Pour changer une couleur, créez toujours une instance de `CellsColor` et affectez-la à la propriété concernée. N'affectez pas directement un `System.Drawing.Color` aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `sparklineGroups.add` elle-même retourne un objet `SparklineGroup` pleinement typé, vous pouvez donc enchaîner les affectations de propriétés sur la valeur de retour ou stocker celui-ci dans une variable locale et le personnaliser avant l'enregistrement.



{{< app/cells/assistant language="javascript" >}}