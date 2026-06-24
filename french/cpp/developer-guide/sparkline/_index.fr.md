---
title: Graphiques sparkline dans Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells est une bibliothèque C++ dédiée à la manipulation de fichiers de tableurs qui prend en charge la création de graphiques sparkline — des miniatures graphiques placées à l'intérieur des cellules de la feuille de calcul. Cet article explique comment ajouter et personnaliser des sparklines de type ligne, colonne et gain/perte à l'aide de la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, bibliothèque C++, tableur, sparklines, sparkline en ligne, sparkline en colonne, sparkline gain/perte, SparklineGroup, SparklineType
type: docs
weight: 195
url: /fr/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la création de sparklines à l'intérieur des cellules de la feuille de calcul. Les sparklines sont des graphiques miniatures qui tiennent dans une seule cellule, offrant une représentation visuelle rapide des tendances des données. Aspose.Cells prend en charge les sparklines de type ligne, colonne et gain/perte, et chacune peut être personnalisée en termes de couleur, d'épaisseur de trait, de points haut/bas et de marqueurs.

{{% /alert %}}

## **Introduction**

Les sparklines sont de petits graphiques intra-cellulaires qui s'avèrent utiles lorsque vous souhaitez afficher une tendance rapide à côté d'une ligne ou d'une colonne de données sans occuper l'espace d'un graphique complet. Excel prend en charge trois types de sparklines : **ligne**, **colonne** et **gain/perte**. Aspose.Cells reproduit cette fonctionnalité via les API `SparklineGroup` et `SparklineGroupCollection` que l'on trouve dans l'espace de noms `Aspose.Cells.Charts`.

Dans Aspose.Cells, chaque sparkline que vous ajoutez est créée via `worksheet.SparklineGroups.Add(...)`, qui renvoie un objet `SparklineGroup`. Vous pouvez ensuite utiliser cet objet pour définir le type de sparkline, la plage de données, la cellule de destination, ainsi que les propriétés visuelles telles que la couleur du trait, l'épaisseur du trait, les marqueurs et les indicateurs de points haut/bas.

{{% alert color="primary" %}}

Un seul `SparklineGroup` peut contenir une ou plusieurs sparklines qui partagent le même style. Lorsque vous appelez `Add` et passez une ligne de données ainsi qu'une seule cellule de destination, vous obtenez une sparkline dans cette cellule. Si votre plage de destination est plus large qu'une cellule, une sparkline distincte est dessinée dans chaque cellule de destination, toutes utilisant la même plage de données et le même style.

{{% /alert %}}

Cet article passe en revue chacun des trois types de sparkline pris en charge par Aspose.Cells — **Ligne**, **Colonne** et **Gain/Perte** — et montre comment les ajouter, personnaliser leurs couleurs et enregistrer le classeur résultant.

## **Sparklines en ligne**

Une sparkline en ligne trace un trait continu à travers les points de données d'une série, ce qui en fait le choix le plus naturel pour représenter des tendances dans le temps. Dans Aspose.Cells, une sparkline en ligne est créée en passant `SparklineType.Line` à la méthode `SparklineGroups.Add`.

Le flux de travail est le même que pour tout autre type de sparkline :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Renseignez une ligne de données sources (par exemple, la ligne 1, colonnes A à E) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination dans laquelle la sparkline sera dessinée.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Le troisième argument — `false` — indique à Aspose.Cells que la plage de données est horizontale (une ligne), et non verticale (une colonne).
5. Personnalisez éventuellement le `SparklineGroup` renvoyé. Pour une sparkline en ligne, vous pouvez définir la couleur du trait à l'aide de `group.Line.Color` (qui attend un `CellsColor` issu de `Aspose.Cells.Drawing`), ajuster l'épaisseur du trait, et activer/désactiver les marqueurs des points haut/bas.
6. Enregistrez le classeur.

L'exemple suivant crée un classeur, écrit les valeurs 5, -3, 8, -2, 6 dans les cellules A1 à E1, puis ajoute une sparkline en ligne dans la cellule F1 qui trace ces valeurs. Il personnalise également la couleur du trait en rouge et active les marqueurs pour les points haut et bas.

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

## **Sparklines en colonne**

Une sparkline en colonne représente chaque point de données sous forme de barre verticale. Cela la rend particulièrement adaptée aux données dont l'amplitude est significative — par exemple, les chiffres de ventes mensuels ou les comptages. Dans Aspose.Cells, vous créez une sparkline en colonne en passant `SparklineType.Column` à la méthode `SparklineGroups.Add`.

La procédure reflète celle de l'exemple de la sparkline en ligne :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Renseignez la même plage source (A1:E1) avec les valeurs que vous souhaitez visualiser.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` obtenu — par exemple, en définissant `group.Type` pour confirmer le type, ou en ajustant la couleur des barres.
6. Enregistrez le classeur dans un fichier de sortie distinct afin qu'il n'écrase pas l'exemple de sparkline en ligne.

L'exemple ci-dessous écrit les valeurs 5, -3, 8, -2, 6 dans A1:E1 et affiche une sparkline en colonne dans F1. Les valeurs négatives sont dessinées sous forme de barres orientées vers le bas, et les valeurs positives sous forme de barres orientées vers le haut, ce qui permet de repérer en un coup d'œil les contributions positives et négatives.

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

    // Étape 3 : Construire un CellArea pointant vers F1 (indice de colonne 5, indice de ligne 0)
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

## **Sparklines Gain/Perte**

Une sparkline gain/perte est une variante particulière de la sparkline en colonne conçue pour ne montrer que deux résultats : une valeur positive est dessinée sous forme de barre vers le haut (un gain) et une valeur nulle ou négative est dessinée sous forme de barre vers le bas (une perte). Les sparklines gain/perte sont couramment utilisées pour visualiser des séquences de victoires et de défaites, des résultats réussite/échec, ou tout résultat binaire au fil du temps.

Dans Aspose.Cells, une sparkline gain/perte est créée en passant `SparklineType.Stacked` à la méthode `SparklineGroups.Add`. (Malgré son nom, `SparklineType.Stacked` est la valeur d'énumération utilisée pour demander le rendu gain/perte.)

La procédure est identique à celle des deux autres types :

1. Créez un nouveau `Workbook` et accédez à la première feuille de calcul.
2. Renseignez la plage source. Étant donné que les sparklines gain/perte traitent chaque valeur soit comme un gain, soit comme une perte, l'amplitude de la valeur n'a pas d'importance — seul son signe compte. Les valeurs positives deviennent des barres vers le haut, et les valeurs non positives deviennent des barres vers le bas.
3. Construisez un `CellArea` décrivant la cellule de destination.
4. Appelez `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Personnalisez éventuellement le `SparklineGroup` renvoyé, par exemple en définissant des couleurs d'accentuation pour les barres de gain et de perte.
6. Enregistrez le classeur sous un nom de fichier distinct afin que les trois exemples puissent coexister sur le disque.

L'exemple ci-dessous utilise les mêmes données d'entrée que les deux sections précédentes. Les valeurs 5, -3, 8, -2, 6 sont interprétées comme gain, perte, gain, perte, gain — et la sparkline dessinée dans F1 reflète exactement cette configuration.

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

    // Étape 4 : Ajouter un sparkline Win/Loss (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Étape 5 : Personnaliser le groupe de sparklines
    // Activer les marqueurs des points hauts et des points bas
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

    // Définir la couleur par défaut de la série (utilisée pour les barres positives)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Étape 6 : Enregistrer le classeur
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Combinaison des trois types de sparkline**

Les trois exemples précédents produisent chacun leur propre classeur, de sorte que les fichiers de sortie sont faciles à inspecter de manière isolée. Dans un scénario réel, vous souhaiterez souvent comparer plusieurs séries de données côte à côte. La manière la plus élégante d'y parvenir consiste à placer plusieurs groupes de sparklines dans la même feuille de calcul, chaque groupe restituant un style différent.

Vous pouvez ajouter plusieurs objets `SparklineGroup` à la même `SparklineGroupCollection`, et chaque groupe peut cibler une cellule de destination différente ou une plage différente. Par exemple, vous pouvez placer une sparkline en ligne dans F1, une sparkline en colonne dans F2, et une sparkline gain/perte dans F3 — toutes lisant à partir de la même source de données dans la ligne 1 — afin que le lecteur puisse voir trois traitements visuels différents des mêmes chiffres.

L'exemple combiné ci-dessous crée un classeur unique, renseigne la ligne 1 avec les valeurs 5, -3, 8, -2, 6, puis ajoute trois groupes de sparkline dans les cellules F1, F2 et F3 — un de chaque type — de sorte que le fichier résultant illustre les trois styles de sparkline en une seule fois.

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

    // Étape 3 : Ajouter un groupe de sparklines de type Ligne à F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Personnaliser la couleur de la sparkline de type ligne via CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Étape 4 : Ajouter un groupe de sparklines de type Colonne à F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Personnaliser la couleur de la série de la sparkline de type colonne
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Étape 5 : Ajouter un groupe de sparklines de type Victoire/Défaite (Empilé) à F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Personnaliser la couleur de la série de la sparkline de type victoire/défaite
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Étape 6 : Enregistrer le classeur
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Lorsque vous combinez plusieurs groupes de sparkline dans une seule feuille de calcul, chaque groupe est indépendant. Ils peuvent partager la même plage source ou utiliser des plages sources différentes, et ils peuvent être stylisés indépendamment. Cela facilite la création d'un petit « tableau de bord » de visualisations intra-cellulaires directement à l'intérieur d'une feuille de calcul existante.

{{% /alert %}}

## **Personnalisation de l'apparence des sparklines**

Une fois qu'un `SparklineGroup` a été créé et ajouté à `worksheet.SparklineGroups`, vous pouvez lire ou modifier plusieurs de ses propriétés visuelles avant d'enregistrer le classeur. Les propriétés les plus couramment personnalisées sont :

- **`group.Type`** — le `SparklineType` (Line, Column ou Stacked). Il est défini lors de l'ajout du groupe, mais vous pouvez le relire pour le confirmer.
- **`group.Line.Color`** — la couleur du trait, exprimée sous forme de `CellsColor` créé via `workbook.CreateCellsColor()`. C'est la propriété à utiliser pour la couleur du trait d'une sparkline en ligne.
- **`group.Line.Weight`** — l'épaisseur du trait en points. Des valeurs plus élevées produisent des traits plus épais.
- **Marqueurs de points haut/bas** — indicateurs qui activent de petits marqueurs sur les points de données les plus élevés et les plus bas, utiles pour mettre l'accent sur les extrêmes.
- **Marqueurs de points premier/dernier/négatif** — indicateurs qui activent/désactivent les marqueurs sur les points de données premier, dernier et négatif.

Pour modifier une couleur, créez toujours une instance de `CellsColor` et affectez-la à la propriété appropriée. N'affectez pas une valeur de couleur brute directement aux propriétés de couleur de la sparkline — elles attendent le type `CellsColor` issu de `Aspose.Cells.Drawing`. La méthode `SparklineGroups.Add` elle-même renvoie un objet `SparklineGroup` entièrement typé, ce qui vous permet d'enchaîner les affectations de propriétés sur la valeur de retour, ou de la stocker dans une variable locale et de la personnaliser avant l'enregistrement.



{{< app/cells/assistant language="cpp" >}}