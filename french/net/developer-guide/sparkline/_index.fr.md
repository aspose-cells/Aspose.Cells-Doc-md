---
title: Sparklines dans Aspose.Cells for .NET
linktitle: Sparklines dans Aspose.Cells for .NET
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de classeur qui prend en charge la création de sparklines — graphiques miniatures placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser les sparklines en ligne, en colonne et gagnant/perdant à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque .NET, feuille de calcul, sparklines, sparkline ligne, sparkline colonne, sparkline gagnant/perdant, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules de la feuille de calcul. Les sparklines sont des graphiques miniatures qui s’insèrent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines en ligne, en colonne et gagnant/perdant, chacune pouvant être personnalisée en termes de couleur, d’épaisseur de ligne, de points haut et bas et de marqueurs.
{{% /alert %}}

## **Introduction**
Les sparklines sont de petits graphiques intégrés dans les cellules, utiles lorsque vous souhaitez afficher une tendance rapide à côté d’une ligne ou d’une colonne de données sans occuper l’espace d’un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gagnant/perdant**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` du namespace `Aspose.Cells.Charts`.  
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée avec `worksheet.SparklineGroups.Add(...)`, ce qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l’épaisseur, les marqueurs et les indicateurs de points haut et bas.  
Cet article décrit les trois types de sparklines pris en charge par Aspose.Cells — **ligne**, **colonne** et **gagnant/perdant** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Line Sparklines**
Une sparkline en ligne trace une ligne continue à travers les points de données d’une série, ce qui en fait le choix le plus naturel pour afficher des tendances dans le temps. Dans Aspose.Cells, une sparkline en ligne est créée en transmettant `SparklineType.Line` à la méthode `SparklineGroups.Add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.  
2. Remplissez une ligne de données source (par exemple, ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.  
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.  
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).  
5. Personnalisez éventuellement le `SparklineGroup` retourné. Pour une sparkline en ligne, vous pouvez définir la couleur de la ligne avec `group.Line.Color` (qui attend un `CellsColor` provenant de `Aspose.Cells.Drawing`), ajuster l’épaisseur de la ligne et activer les marqueurs de points haut et bas.  
6. Enregistrez le classeur.  
L’exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, puis ajoute une sparkline en ligne dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points haut et bas.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;
            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Column Sparklines**
Une sparkline en colonne rend chaque point de donnée sous la forme d’une barre verticale. Cela la rend adaptée aux données dont l’amplitude a une signification — par exemple, les chiffres de ventes mensuelles ou les décomptes. Dans Aspose.Cells, vous créez une sparkline en colonne en transmettant `SparklineType.Column` à la méthode `SparklineGroups.Add`.
La procédure reproduit l’exemple de la sparkline en ligne :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.  
2. Remplissez une ligne de données source (par exemple, ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.  
3. Construisez un `CellArea` décrivant la cellule de destination.  
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.  
5. Personnalisez éventuellement le `SparklineGroup` obtenu — par exemple, en définissant `group.Type` pour confirmer le type, ou en ajustant la couleur des barres.  
6. Enregistrez le classeur dans un fichier de sortie distinct afin de ne pas écraser l’exemple de la sparkline en ligne.  
L’exemple ci‑dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et rend une sparkline en colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres descendantes et les valeurs positives sous forme de barres ascendantes, ce qui permet de repérer d’un seul coup d’œil les contributions positives et négatives.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Win/Loss Sparklines**
Une sparkline gagnant/perdant est une variante spéciale de la sparkline en colonne conçue pour n’afficher que deux issues : une valeur positive apparaît sous forme de barre « haut » (un gain) et une valeur nulle ou négative sous forme de barre « bas » (une perte). Les sparklines gagnant/perdant sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussite/échec, ou tout résultat binaire dans le temps.  
Dans Aspose.Cells, une sparkline gagnant/perdant est créée en transmettant `SparklineType.Stacked` à la méthode `SparklineGroups.Add`. (Malgré le nom, `SparklineType.Stacked` est la valeur d’énumération utilisée pour demander le rendu gagnant/perdant.)  
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.  
2. Remplissez la plage source. Parce que les sparklines gagnant/perdant traitent chaque valeur comme un gain ou une perte, l’amplitude de la valeur n’a pas d’importance — seul le signe compte.  
3. Construisez un `CellArea` décrivant la cellule de destination.  
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.  
5. Personnalisez éventuellement le `SparklineGroup` retourné, par exemple en définissant des couleurs d’accentuation pour les barres de gain et de perte.  
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;
            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combining All Three Sparkline Types**
L’exemple combiné ci‑dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant illustre les trois styles de sparklines simultanément.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
 // Step 6: Save the workbook
workbook.Save("output_all.xlsx");
```

## **Customizing Sparkline Appearance**
Une fois qu’un `SparklineGroup` a été créé et ajouté à `worksheet.SparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d’enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.Type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lors de l’ajout du groupe, mais vous pouvez le relire pour confirmer.  
- **`group.Line.Color`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.CreateCellsColor()`. C’est la propriété à utiliser pour la couleur du trait de la sparkline en ligne.  
- **`group.Line.Weight`** — l’épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.  
- **Marqueurs de points haut/bas** — indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.  
- **Marqueurs de premier/dernier/point négatif** — indicateurs qui basculent les marqueurs sur les premiers, derniers et points négatifs.  
Pour changer une couleur, créez toujours une instance de `CellsColor` et affectez‑la à la propriété concernée. N’affectez pas directement un `System.Drawing.Color` aux propriétés de couleur de la sparkline — elles attendent le type `CellsColor` provenant de `Aspose.Cells.Drawing`. La méthode `SparklineGroups.Add` renvoie elle‑même un objet `SparklineGroup` complètement typé, vous pouvez donc chaîner les affectations de propriétés sur la valeur de retour ou la stocker dans une variable locale avant de la personnaliser puis d’enregistrer le classeur.

## Related Articles
- [Convertir les Sparklines en image et HTML dans Aspose.Cells for .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans le tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)
- [Conversion d'Excel au format OFD](/cells/fr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}