---
title: Les graphiques sparkline dans Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells est une bibliothèque Java permettant de travailler avec des fichiers de feuilles de calcul qui prend en charge la création de graphiques sparkline — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des graphiques sparkline de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, graphiques sparkline, sparkline de type ligne, sparkline de type colonne, sparkline de type gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la création de graphiques sparkline à l'intérieur des cellules de la feuille de calcul. Les graphiques sparkline sont des mini-graphiques qui tiennent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparkline de type ligne, colonne et gain/perte, et chacun peut être personnalisé en termes de couleur, épaisseur de ligne, points haut/bas et marqueurs.

{{% /alert %}}

## **Introduction**

Les graphiques sparkline sont de petits graphiques intégrés à une cellule qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de graphiques sparkline : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reflète cette fonctionnalité à travers les API `SparklineGroup` et `SparklineGroupCollection` situées dans l'espace de noms `Aspose.Cells.Charts`.

Dans Aspose.Cells, chaque graphique sparkline que vous ajoutez est créé via `worksheet.getSparklineGroups().add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs des points haut/bas.

{{% alert color="primary" %}}

Un seul `SparklineGroup` peut contenir un ou plusieurs graphiques sparkline qui partagent le même style. Lorsque vous appelez `add` et transmettez une ligne de données ainsi qu'une seule cellule de destination, vous obtenez un graphique sparkline dans cette cellule. Si votre plage de destination est plus large qu'une cellule, un graphique sparkline distinct est dessiné dans chaque cellule de destination, tous utilisant la même plage de style et de données.

{{% /alert %}}

Cet article passe en revue chacun des trois types de graphiques sparkline pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Graphiques sparkline de type ligne**

Un graphique sparkline de type ligne trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour montrer des tendances au fil du temps. Dans Aspose.Cells, un graphique sparkline de type ligne est créé en passant `SparklineType.LINE` à la méthode `add`.

Le flux de travail est le même que pour tout autre type de sparkline :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où le graphique sparkline sera dessiné.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour un sparkline de type ligne, vous pouvez définir la couleur de la ligne à l'aide de `group.getLine().setColor(...)` (qui attend un `CellsColor` de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne, et activer les marqueurs des points haut/bas.
6. Enregistrez le classeur.

L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute un sparkline de type ligne dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points haut et bas.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Étape 1 : Créer un Workbook et obtenir la première feuille de calcul
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Étape 3 : Construire un CellArea pointant vers la cellule de destination F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // colonne F (indexée à partir de 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // ligne 1 (indexée à partir de 0)
            dest.EndRow = 0;

            // Étape 4 : Ajouter un sparkline en ligne de A1:E1 dans F1
            // SparklineGroups.add renvoie l'index du groupe nouvellement ajouté
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de la ligne du sparkline
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Étape 6 : Activer les marqueurs de point haut et de point bas
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Étape 7 : Enregistrer le classeur
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Graphiques sparkline de type colonne**

Un graphique sparkline de type colonne représente chaque point de données sous forme de barre verticale. Cela le rend bien adapté aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptages. Dans Aspose.Cells, vous créez un sparkline de type colonne en passant `SparklineType.COLUMN` à la méthode `add`.

La procédure est identique à celle de l'exemple de sparkline de type ligne :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la même plage source (A1:E1) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.getType()` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple du sparkline de type ligne.

L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue un sparkline de type colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet de repérer facilement d'un coup d'œil les contributions positives et négatives.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Écrire des valeurs d'exemple dans A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Construire un CellArea pointant vers F1 (indice de colonne 5, indice de ligne 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Ajouter un sparkline de type colonne à la cellule de destination
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Confirmer le type de sparkline en lisant group.Type
System.out.println("Sparkline Type added: " + group.getType());

// Enregistrer le classeur
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **Graphiques sparkline de type gain/perte**

Un graphique sparkline de type gain/perte est une variante spéciale du sparkline de type colonne conçu pour ne montrer que deux résultats : une valeur positive est représentée par une barre « vers le haut » (un gain) et une valeur nulle ou négative est représentée par une barre « vers le bas » (une perte). Les graphiques sparkline de type gain/perte sont couramment utilisés pour visualiser des séquences de victoires et de défaites, des résultats de réussite/échec, ou tout résultat binaire au fil du temps.

Dans Aspose.Cells, un graphique sparkline de type gain/perte est créé en passant `SparklineType.STACKED` à la méthode `add`. (Malgré son nom, `SparklineType.STACKED` est la valeur d'énumération utilisée pour demander le rendu de type gain/perte.)

La procédure est la même que pour les deux autres types :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Étant donné que les graphiques sparkline de type gain/perte traitent chaque valeur comme un gain ou une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

L'exemple ci-dessous utilise les mêmes données d'entrée que les deux sections précédentes. Les valeurs 5, -3, 8, -2, 6 sont interprétées comme gain, perte, gain, perte, gain — et le sparkline dessiné dans F1 reflète exactement ce motif.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Remplir avec des données d'exemple
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Construire un CellArea pointant vers F1 (colonne 5, ligne 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Ajouter un sparkline Win/Loss (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Personnaliser le groupe de sparklines
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Définir la couleur du point haut en vert
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// Définir la couleur du point bas en rouge
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// Définir la couleur du point négatif en orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Définir la couleur de la série par défaut (utilisée pour les barres positives)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // Approximation de SteelBlue
group.setSeriesColor(seriesColor);

// Enregistrer le classeur
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinaison des trois types de graphiques sparkline**

Les trois exemples précédents produisent chacun leur propre classeur afin que les fichiers de sortie soient faciles à inspecter de manière isolée. Dans un scénario réel, cependant, vous souhaiterez souvent comparer plusieurs séries de données côte à côte. La façon la plus propre de procéder est de placer plus d'un groupe de sparkline dans la même feuille de calcul, chaque groupe restituant un style différent.

Vous pouvez ajouter plusieurs objets `SparklineGroup` à la même `SparklineGroupCollection`, et chaque groupe peut cibler une cellule de destination différente ou une plage différente. Par exemple, vous pouvez placer un sparkline de type ligne dans F1, un sparkline de type colonne dans F2 et un sparkline de type gain/perte dans F3 — tous lisant à partir des mêmes données sources de la ligne 1 — afin que le lecteur puisse voir trois traitements visuels différents des mêmes nombres.

L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparkline dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant démontre les trois styles de sparkline à la fois.

```java
import com.aspose.cells.*;

// Étape 1 : Créer un classeur et obtenir la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Étape 2 : Remplir des données d'exemple dans la ligne 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Étape 3 : Ajouter un groupe de sparklines de type Ligne à F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Correctif : Utiliser la méthode d'usine statique
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Personnaliser la couleur de la sparkline de type Ligne via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Correctif : Utiliser la méthode d'usine statique
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personnaliser la couleur de la série de la sparkline de type Colonne
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Étape 5 : Ajouter un groupe de sparklines Win/Loss (Empilé) à F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Correctif : Utiliser la méthode d'usine statique
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personnaliser la couleur de la série de la sparkline win/loss
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Lorsque vous combinez plusieurs groupes de sparkline dans une seule feuille de calcul, chaque groupe est indépendant. Ils peuvent partager la même plage source ou utiliser des plages sources différentes, et ils peuvent être stylisés indépendamment. Cela facilite la création d'un petit « tableau de bord » de visualisations intra-cellulaire directement à l'intérieur d'une feuille de calcul existante.

{{% /alert %}}

## **Personnalisation de l'apparence des graphiques sparkline**

Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.getSparklineGroups()`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :

- **`group.getType()`** — le `SparklineType` (LINE, COLUMN ou STACKED). Il est défini lorsque le groupe est ajouté, mais vous pouvez le relire pour le confirmer.
- **`group.getLine().setColor(...)`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur du trait du sparkline de type ligne.
- **`group.getLine().setWeight(...)`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points haut/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — des indicateurs qui activent ou désactivent les marqueurs sur les points de données premier, dernier et négatif.

Pour changer une couleur, créez toujours une instance de `CellsColor` et affectez-la à la propriété appropriée. N'affectez pas directement un `java.awt.Color` aux propriétés de couleur du sparkline — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `add` elle-même renvoie un objet `SparklineGroup` entièrement typé, vous pouvez donc enchaîner les affectations de propriétés sur la valeur de retour ou la stocker dans une variable locale et la personnaliser avant l'enregistrement.



{{< app/cells/assistant language="java" >}}