---
title: Sparklines dans Aspose.Cells for Java
linktitle: Sparklines dans Aspose.Cells for Java
description: Aspose.Cells est une bibliothèque Java permettant de travailler avec des fichiers de feuille de calcul et prenant en charge la création de sparklines — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines linéaires, en colonnes et win/loss à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, sparklines, sparkline linéaire, sparkline en colonnes, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules de la feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines linéaires, en colonnes et win/loss, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points haut/bas et de marqueurs.

## **Introduction**
Les sparklines sont de petits graphiques in-cell qui sont utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **linéaire**, **en colonnes** et **win/loss**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans l'espace de noms `Aspose.Cells.Charts`.
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.getSparklineGroups().add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs des points haut/bas.
Cet article passe en revue les trois types de sparklines pris en charge par Aspose.Cells — **Linéaire**, **En colonnes** et **Win/Loss** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines linéaires**
Une sparkline linéaire trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour montrer des tendances au fil du temps. Dans Aspose.Cells, une sparkline linéaire est créée en passant `SparklineType.LINE` à la méthode `add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour une sparkline linéaire, vous pouvez définir la couleur de la ligne à l'aide de `group.getLine().setColor(...)` (qui attend un `CellsColor` de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer les marqueurs des points haut/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline linéaire dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points haut et bas.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Étape 1 : Créer un classeur et obtenir la première feuille de calcul
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
            // Étape 4 : Ajouter un sparkline linéaire de A1:E1 vers F1
            // SparklineGroups.add renvoie l'index du groupe nouvellement ajouté
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Étape 5 : Créer un CellsColor rouge et l'affecter à la couleur de ligne du sparkline
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

## **Sparklines en colonnes**
Une sparkline en colonnes restitue chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptages. Dans Aspose.Cells, vous créez une sparkline en colonnes en passant `SparklineType.COLUMN` à la méthode `add`.
La procédure est identique à celle de l'exemple de sparkline linéaire :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.getType()` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple de sparkline linéaire.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline en colonnes dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet de distinguer facilement les contributions positives et négatives en un coup d'œil.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Écrire des valeurs d'exemple dans A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Construire un CellArea pointant vers F1 (index de colonne 5, index de ligne 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Ajouter un sparkline de type Colonne à la cellule de destination
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirmer le type de sparkline en lisant group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Enregistrer le classeur
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Sparklines Win/Loss**
Une sparkline win/loss est une variante spéciale de la sparkline en colonnes conçue pour ne montrer que deux résultats : une valeur positive est dessinée comme une barre « vers le haut » (une victoire) et une valeur nulle ou négative est dessinée comme une barre « vers le bas » (une défaite). Les sparklines win/loss sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussite/échec, ou tout résultat binaire au fil du temps.
Dans Aspose.Cells, une sparkline win/loss est créée en passant `SparklineType.STACKED` à la méthode `add`. (Malgré son nom, `SparklineType.STACKED` est la valeur d'énumération utilisée pour demander le rendu win/loss.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Comme les sparklines win/loss traitent chaque valeur comme une victoire ou une défaite, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de victoire et de défaite.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Remplir des données d'exemple
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
// Définir la couleur des points négatifs en orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);
// Définir la couleur de série par défaut (utilisée pour les barres positives)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // Approximation de SteelBlue
group.setSeriesColor(seriesColor);
// Enregistrer le classeur
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinaison des trois types de sparklines**
L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — afin que le fichier résultant démontre les trois styles de sparklines en même temps.

```java
import com.aspose.cells.*;
// Étape 1 : Créer un classeur et obtenir la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Étape 2 : Remplir les données d'exemple dans la ligne 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Étape 3 : Ajouter un groupe de sparklines de type Ligne à F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Correctif : Utiliser la méthode fabrique statique
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personnaliser la couleur de la sparkline de type Ligne via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Correctif : Utiliser la méthode fabrique statique
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personnaliser la couleur de la série de sparklines de type Colonne
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Étape 5 : Ajouter un groupe de sparklines de type Gain/Perte (Empilé) à F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Correctif : Utiliser la méthode fabrique statique
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personnaliser la couleur de la série de sparklines de type Gain/Perte
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Étape 6 : Enregistrer le classeur
workbook.save("output_all.xlsx");
```

## **Personnalisation de l'apparence des sparklines**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.getSparklineGroups()`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.getType()`** — le `SparklineType` (LINE, COLUMN ou STACKED). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour confirmer.
- **`group.getLine().setColor(...)`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.createCellsColor()`. C'est la propriété à utiliser pour la couleur du trait de la sparkline linéaire.
- **`group.getLine().setWeight(...)`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points haut/bas** — indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — indicateurs qui activent ou désactivent les marqueurs sur les points de données premier, dernier et négatif.
Pour modifier une couleur, créez toujours une instance `CellsColor` et affectez-la à la propriété correspondante. N'affectez pas un `java.awt.Color` directement aux propriétés de couleur de la sparkline — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `add` elle-même renvoie un objet `SparklineGroup` entièrement typé ; vous pouvez donc enchaîner les affectations de propriétés sur la valeur de retour, ou le stocker dans une variable locale et le personnaliser avant d'enregistrer.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}