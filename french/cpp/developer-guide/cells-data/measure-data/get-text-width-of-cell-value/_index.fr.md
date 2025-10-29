---
title: Obtenir la largeur du texte de la valeur de la cellule avec C++
linktitle: Obtenez la largeur du texte de la valeur de la cellule
type: docs
weight: 50
url: /fr/cpp/get-text-width-of-cell-value/
description: Apprenez comment obtenir la largeur du texte de la valeur de la cellule via l API Aspose.Cells for C++.
keywords: Obtenez la largeur du texte de la valeur de la cellule, Obtenez la largeur du texte de la valeur de la cellule
---

## **Obtenir la largeur de texte de la valeur de la cellule**

Parfois, les développeurs peuvent avoir besoin de calculer la largeur de la valeur de la cellule pour organiser les données dans une mise en page. Aspose.Cells fournit la méthode [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) qui permet aux développeurs d'obtenir la largeur du texte de la valeur de la cellule. Le code exemple ci-dessous montre comment utiliser [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) pour accéder à la largeur du texte de la valeur de la cellule.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier Source](96928090.xlsx)

## Code d'exemple

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
