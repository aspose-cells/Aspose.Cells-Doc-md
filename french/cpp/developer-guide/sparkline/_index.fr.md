---
title: Sparklines dans Aspose.Cells for C++
description: Aspose.Cells est une bibliothèque C++ permettant de travailler avec des fichiers de feuille de calcul et prenant en charge la création de sparklines, qui sont des mini-graphiques placés à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul, sparklines, sparkline de type ligne, sparkline de type colonne, sparkline de type gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules de la feuille de calcul. Les sparklines sont des mini-graphiques qui tiennent dans une seule cellule, fournissant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines de type ligne, colonne et gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de ligne, de points hauts/bas et de marqueurs.

## **Introduction**
Les sparklines sont de petits graphiques in-cell qui s'avèrent utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans le namespace `Aspose.Cells.Charts`.
Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.SparklineGroups.Add(...)`, qui retourne un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination et les propriétés visuelles telles que la couleur de la ligne, l'épaisseur de la ligne, les marqueurs et les indicateurs de points hauts/bas.
Cet article passe en revue chacun des trois types de sparklines pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines de type ligne**
Une sparkline de type ligne trace une ligne continue passant par les points de données d'une série, ce qui en fait le choix le plus naturel pour représenter des tendances au fil du temps. Dans Aspose.Cells, une sparkline de type ligne est créée en passant `SparklineType.Line` à la méthode `SparklineGroups.Add`.
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination où la sparkline sera dessinée.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne) et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` retourné. Pour une sparkline de type ligne, vous pouvez définir la couleur de la ligne via `group.Line.Color` (qui attend un `CellsColor` issu de `Aspose.Cells.Drawing`), ajuster l'épaisseur de la ligne et activer les marqueurs des points hauts/bas.
6. Enregistrez le classeur.
L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, et ajoute une sparkline de type ligne dans la cellule F1 qui retrace ces valeurs. Il personnalise également la couleur de la ligne en rouge et active les marqueurs pour les points hauts et bas.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Étape 1 : Créer un classeur et obtenir la première feuille de calcul
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Étape 2 : Écrire les valeurs d'exemple 5, -3, 8, -2, 6 dans les cellules A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Étape 3 : Construire un CellArea pointant vers la cellule de destination F1
    CellArea dest;
    dest.StartColumn = 5;   // colonne F (indexée à partir de 0)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // ligne 1 (indexée à partir de 0)
    dest.EndRow = 0;
    // Étape 4 : Ajouter un sparkline en ligne de A1:E1 dans F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Étape 5 : Créer un CellsColor rouge et l'assigner à la couleur de ligne du sparkline
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Étape 6 : Activer les marqueurs de point haut et de point bas
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Étape 7 : Enregistrer le classeur
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines de type colonne**
Une sparkline de type colonne restitue chaque point de données sous forme de barre verticale. Cela la rend bien adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou des comptes. Dans Aspose.Cells, vous créez une sparkline de type colonne en passant `SparklineType.Column` à la méthode `SparklineGroups.Add`.
La procédure reproduit l'exemple de sparkline de type ligne :
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez une ligne de données sources avec les valeurs à visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` résultant — par exemple, en définissant `group.Type` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple de sparkline de type ligne.
L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et restitue une sparkline de type colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet de repérer en un coup d'œil les contributions positives et négatives.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Étape 1 : Créer un classeur et obtenir la première feuille de calcul
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Étape 2 : Écrire des valeurs d'exemple dans A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // Étape 3 : Construire un CellArea pointant vers F1 (index de colonne 5, index de ligne 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Étape 4 : Ajouter un sparkline de type colonne à la cellule de destination
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // Étape 5 : Confirmer le type de sparkline en lisant group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // Étape 6 : Enregistrer le classeur
    wb.Save(u"output_column.xlsx");
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines de type gain/perte**
Une sparkline de type gain/perte est une variante spéciale de la sparkline de type colonne conçue pour afficher seulement deux résultats : une valeur positive est dessinée sous forme de barre « vers le haut » (un gain) et une valeur nulle ou négative est dessinée sous forme de barre « vers le bas » (une perte). Les sparklines de type gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats de réussite/échec, ou tout autre résultat binaire au fil du temps.
Dans Aspose.Cells, une sparkline de type gain/perte est créée en passant `SparklineType.Stacked` à la méthode `SparklineGroups.Add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu de type gain/perte.)
1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Remplissez la plage source. Étant donné que les sparklines de type gain/perte traitent chaque valeur soit comme un gain soit comme une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` retourné, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Étape 1 : Créer un classeur et obtenir la première feuille de calcul
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Étape 2 : Remplir des données d'exemple dans la ligne 1 : A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Étape 3 : Construire une CellArea pointant vers F1 (colonne 5, ligne 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // ligne 1
    dest.EndRow = 0;
    // Étape 4 : Ajouter un sparkline Gagnant/Perdant (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // Étape 5 : Personnaliser le groupe de sparklines
    // Activer les marqueurs de point haut et de point bas
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Définir la couleur du point haut en vert
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Définir la couleur du point bas en rouge
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Définir la couleur des points négatifs en orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Définir la couleur de série par défaut (utilisée pour les barres positives)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Étape 6 : Enregistrer le classeur
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Classeur enregistré avec succès : output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Combinaison des trois types de sparklines**
L'exemple combiné ci-dessous crée un seul classeur, remplit la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparklines dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant démontre les trois styles de sparklines en une seule fois.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Étape 1 : Créer un classeur et obtenir la première feuille de calcul
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Étape 2 : Remplir des données d'exemple dans la ligne 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Étape 3 : Ajouter un groupe de sparklines de type Ligne en F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // Personnaliser la couleur de la sparkline de type Ligne via CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Étape 4 : Ajouter un groupe de sparklines de type Colonne en F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Personnaliser la couleur de la série de sparklines de type Colonne
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Étape 5 : Ajouter un groupe de sparklines de type Victoire/Défaite (Empilé) en F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Personnaliser la couleur de la série de sparklines de type Victoire/Défaite
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Étape 6 : Enregistrer le classeur
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Personnalisation de l'apparence des sparklines**
Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.SparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :
- **`group.Type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour le confirmer.
- **`group.Line.Color`** — la couleur de la ligne, exprimée sous forme de `CellsColor` créé via `workbook.CreateCellsColor()`. C'est la propriété à utiliser pour la couleur du trait de la sparkline de type ligne.
- **`group.Line.Weight`** — l'épaisseur de la ligne en points. Des valeurs plus élevées produisent des lignes plus épaisses.
- **Marqueurs des points hauts/bas** — des indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre en évidence les extrêmes.
- **Marqueurs des points premier/dernier/négatif** — des indicateurs qui basculent les marqueurs sur les points de données premier, dernier et négatifs.
Pour modifier une couleur, créez toujours une instance de `CellsColor` et attribuez-la à la propriété concernée. N'attribuez pas directement une valeur de couleur brute aux propriétés de couleur des sparklines — elles attendent le type `CellsColor` de `Aspose.Cells.Drawing`. La méthode `SparklineGroups.Add` retourne elle-même un objet `SparklineGroup` pleinement typé, ce qui vous permet d'enchaîner les affectations de propriétés sur la valeur de retour ou de la stocker dans une variable locale et de la personnaliser avant l'enregistrement.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}