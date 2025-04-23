---
title: Paramètres de remplissage avec C++
linktitle: Paramètres de remplissage
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableur. Elle supporte la configuration des paramètres de remplissage des cellules, permettant aux utilisateurs de personnaliser l arrière plan et le style des cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de remplissage des cellules.
keywords: Aspose.Cells, Cells, Paramètres de remplissage, Arrière plan, Style
type: docs
weight: 50
url: /fr/cpp/cells-fill-settings/
---

## **Couleurs et motifs d'arrière-plan**

Microsoft Excel peut définir les couleurs avant-plan (contour) et arrière-plan (remplissage) des cellules et les motifs d'arrière-plan.

Aspose.Cells prend également en charge ces fonctionnalités de manière flexible. Dans ce sujet, nous apprenons à utiliser ces fonctionnalités en utilisant Aspose.Cells.

### **Définition de couleurs et motifs d'arrière-plan**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) possède les méthodes [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) et [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) qui sont utilisées pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fournit des propriétés pour définir les couleurs avant-plan et arrière-plan des cellules. Aspose.Cells fournit une énumération [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) qui contient un ensemble de types prédéfinis de motifs d'arrière-plan qui sont donnés ci-dessous.

|**Motifs d'arrière-plan**|**Description**|
| :- | :- |
|DiagonalCrosshatch|Représente le motif de quadrillage en diagonale|
|DiagonalStripe|Représente un motif de rayures diagonales|
|Gray6|Représente un motif de gris à 6,25%|
|Gray12|Représente un motif de gris à 12,5%|
|Gray25|Représente un motif de gris à 25%|
|Gray50|Représente un motif de gris à 50%|
|Gray75|Représente un motif de gris à 75%|
|HorizontalStripe|Représente un motif de rayures horizontales|
|None|Représente pas d'arrière-plan|
|ReverseDiagonalStripe|Représente un motif de rayures inversées diagonales|
|Solid|Représente un motif solide|
|ThickDiagonalCrosshatch|Représente un motif de quadrillage diagonal épais|
|ThinDiagonalCrosshatch|Représente un motif de quadrillage diagonal fin|
|ThinDiagonalStripe|Représente un motif de rayures diagonales fines|
|ThinHorizontalCrosshatch|Représente un motif de quadrillage horizontal fin|
|ThinHorizontalStripe|Représente un motif de rayures horizontales fines|
|ThinReverseDiagonalStripe|Représente un motif de rayures inversées diagonales fines|
|ThinVerticalStripe|Représente un motif de rayures verticales fines|
|VerticalStripe|Représente un motif de rayures verticales|

Dans l'exemple ci-dessous, la couleur de premier plan de la cellule A1 est définie, mais A2 est configurée pour avoir à la fois des couleurs de premier plan et d'arrière-plan avec un motif d'arrière-plan de rayures verticales.|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Important à savoir**

{{% alert color="primary" %}}

- Pour définir la couleur d'avant-plan ou d'arrière-plan d'une cellule, utilisez les propriétés [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) ou [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Ces deux propriétés prendront effet seulement si la propriété [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) de l'objet [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) est configurée.
- La propriété [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) définit la couleur d'ombrage de la cellule.
  La propriété [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) spécifie le type de motif de fond utilisé pour la couleur d'avant-plan ou d'arrière-plan. Aspose.Cells fournit une énumération, [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), qui contient un ensemble de types prédéfinis de motifs de fond.
- Si vous sélectionnez la valeur *BackgroundType.None* de l'énumération [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), la couleur d'avant-plan n'est pas appliquée.
  De même, la couleur d'arrière-plan n'est pas appliquée si vous sélectionnez les valeurs *BackgroundType.None* ou *BackgroundType.Solid*.
- Lors de la récupération de la couleur d'ombrage/remplissage d'une cellule, si [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) est *BackgroundType.None*, [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) renverra *Color.Empty*.

{{% /alert %}}

### **Application d'effets de remplissage dégradé**

Pour appliquer vos effets de remplissage dégradé souhaités à la cellule, utilisez la méthode [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) en conséquence.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.

Avec Aspose.Cells, il est possible non seulement d'utiliser les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.

### **Ajout de couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fournit une méthode [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) qui prend les paramètres suivants pour ajouter une couleur personnalisée pour modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchid) à la palette avant de l'appliquer sur une police.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).

{{% /alert %}}
