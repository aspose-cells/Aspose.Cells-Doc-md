---
title: Extraire les données de thème à partir d un fichier Excel avec C++
linktitle: Extraire les données de thème du fichier Excel
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableur. Elle supporte l extraction des données de thème à partir de fichiers Excel, permettant aux utilisateurs d obtenir les informations de style et de mise en forme des documents. Cet article introduira comment extraire les données de thème à partir de fichiers Excel en utilisant la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, Fichier Excel, Données de thème, Style, Format
type: docs
weight: 120
url: /fr/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells permet aux utilisateurs d'extraire des données liées au thème d'un fichier Excel. Par exemple, vous pouvez extraire le nom du thème appliqué au classeur et la couleur du thème appliquée à une cellule ou aux bordures de la cellule, etc.

Vous pouvez appliquer un thème à votre classeur en utilisant Microsoft Excel via la commande Mise en page > Thèmes.

{{% /alert %}}

## Code C++ pour extraire les données de thème d'un fichier Excel

Le code d'exemple suivant convertit le nom du thème appliqué au classeur source, puis extrait la couleur du thème appliquée à la cellule A1 et la couleur du thème appliquée à la bordure inférieure de la cellule.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
