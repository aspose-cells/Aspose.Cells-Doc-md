---
title: Sparklines dans Aspose.Cells for .NET
linktitle: Sparklines dans Aspose.Cells for .NET
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des fichiers de tableur qui prend en charge la création de sparklines — des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque .NET, tableur, sparklines, sparkline linéaire, sparkline en colonnes, sparkline gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines dans les cellules de la feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines de type ligne, colonne et gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points hauts/bas et de marqueurs.

## **Introduction**
Les sparklines sont de petits graphiques intra-cellulaires utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gain/perte**. Aspose.Cells offre la même fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` disponibles dans le namespace `Aspose.Cells.Charts`.
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.SparklineGroups.Add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points hauts/bas.
Cet article passe en revue chacun des trois types de sparklines pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines de type ligne**
Une sparkline linéaire trace une ligne continue à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour montrer des tendances au fil du temps. Dans Aspose.Cells, une sparkline linéaire est créée en passant `SparklineType.Line` à la méthode `SparklineGroups.Add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez une `CellArea` décrivant la cellule de destination où la sparkline sera tracée.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne) et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour une sparkline linéaire, vous pouvez définir la couleur de la ligne à l'aide de `group.Line.Color` (qui attend un `CellsColor` de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer/désactiver les marqueurs de points hauts/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline linéaire dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points hauts et bas.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Étape 1 : Créer un classeur et obtenir la première feuille de calcul
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Étape 3 : Construire un CellArea pointant vers la cellule de destination F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // colonne F (indexée à 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // ligne 1 (indexée à 0)
            dest.EndRow = 0;
            // Étape 4 : Ajouter un sparkline de type Ligne de A1:E1 vers F1
            // SparklineGroups.Add renvoie l'index du groupe nouvellement ajouté
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de ligne du sparkline
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Étape 6 : Activer les marqueurs de point haut et de point bas
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Étape 7 : Enregistrer le classeur
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Sparklines de type colonne**
Une sparkline en colonnes restitue chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptes. Dans Aspose.Cells, vous créez une sparkline en colonnes en passant `SparklineType.Column` à la méthode `SparklineGroups.Add`.
La procédure reflète celle de l'exemple de la sparkline linéaire :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Construisez une `CellArea` décrivant la cellule de destination.
3. Appelez `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
4. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.Type` pour confirmer le type, ou en ajustant la couleur des barres.
5. Enregistrez le classeur dans un fichier de sortie séparé afin qu'il n'écrase pas l'exemple de la sparkline linéaire.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline en colonnes dans F1. Les valeurs négatives sont dessinées sous forme de barres descendantes et les valeurs positives sous forme de barres montantes, ce qui permet de repérer facilement d'un coup d'œil les contributions positives et négatives.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Étape 1 : Créer un Workbook et obtenir la première feuille de calcul
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Étape 2 : Écrire des valeurs d'exemple dans A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Étape 3 : Construire un CellArea pointant vers F1 (index de colonne 5, index de ligne 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Étape 4 : Ajouter un sparkline de type Column à la cellule de destination
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Étape 5 : Confirmer le type de sparkline en lisant group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Étape 6 : Enregistrer le workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Sparklines de type gain/perte**
Une sparkline gain/perte est une variante spéciale de la sparkline en colonnes conçue pour afficher seulement deux résultats : une valeur positive est dessinée sous forme de barre « vers le haut » (un gain) et une valeur nulle ou négative est dessinée sous forme de barre « vers le bas » (une perte). Les sparklines gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussite/échec, ou tout résultat binaire au fil du temps.
Dans Aspose.Cells, une sparkline gain/perte est créée en passant `SparklineType.Stacked` à la méthode `SparklineGroups.Add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Étant donné que les sparklines gain/perte traitent chaque valeur comme un gain ou une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez une `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexist sur le disque.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Étape 1 : Créer un Workbook et obtenir la première feuille de calcul
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Étape 2 : Remplir les données d'exemple dans la ligne 1 : A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Étape 3 : Construire une CellArea pointant vers F1 (colonne 5, ligne 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // ligne 1
            dest.EndRow = 0;
            // Étape 4 : Ajouter un sparkline Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Étape 5 : Personnaliser le groupe de sparklines
            // Activer les marqueurs des points hauts et bas
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Définir la couleur du point haut en vert
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Définir la couleur du point bas en rouge
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Définir la couleur du point négatif en orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Définir la couleur par défaut de la série (utilisée pour les barres positives)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Étape 6 : Enregistrer le workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combinaison des trois types de sparklines**
L'exemple combiné ci-dessous crée un classeur unique, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant présente les trois styles de sparklines en même temps.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Étape 1 : Créer un classeur et obtenir la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Étape 2 : Remplir des données d'exemple dans la ligne 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Étape 3 : Ajouter un groupe de sparklines de type Ligne à F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Personnaliser la couleur de la sparkline de type Ligne via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Personnaliser la couleur de la série de sparklines de type Colonne
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Étape 5 : Ajouter un groupe de sparklines Win/Loss (Empilé) à F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Personnaliser la couleur de la série de sparklines win/loss
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Étape 6 : Enregistrer le classeur
workbook.Save("output_all.xlsx");
```

## **Personnalisation de l'apparence des sparklines**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.SparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.Type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lorsque le groupe est ajouté, mais vous pouvez le relire pour confirmer.
- **`group.Line.Color`** — la couleur de la ligne, exprimée en tant que `CellsColor` créé via `workbook.CreateCellsColor()`. C'est la propriété à utiliser pour la couleur du trait de la sparkline linéaire.
- **`group.Line.Weight`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs de points hauts/bas** — indicateurs qui activent de petits marqueurs sur les points de données les plus hauts et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs de points premier/dernier/négatif** — indicateurs qui activent/désactivent les marqueurs sur les points de données premier, dernier et négatif.
Pour changer une couleur, créez toujours une instance de `CellsColor` et affectez-la à la propriété correspondante. N'affectez pas directement un `System.Drawing.Color` aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `SparklineGroups.Add` elle-même renvoie un objet `SparklineGroup` complètement typé, vous pouvez donc enchaîner les affectations de propriétés sur la valeur de retour ou la stocker dans une variable locale et la personnaliser avant d'enregistrer.
{{% /alert %}}

## Articles Connexes
- [Convertir une sparkline en image et HTML dans Aspose.Cells for .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)
- [Conversion d'Excel au format OFD](/cells/fr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}