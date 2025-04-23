---
title: Vérifier le format numérique personnalisé lors de la définition de la propriété Style.Custom avec C++
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuilles de calcul, qui supporte la vérification des formats numériques personnalisés lors du stylage. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats numériques personnalisés afin de garantir que le style est correct.
keywords: Aspose.Cells, bibliothèques C++, feuilles de calcul, stylage, formatage numérique personnalisé, vérification, validation
type: docs
weight: 170
url: /fr/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous assignez un format numérique personnalisé invalide à la propriété [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/), Aspose.Cells ne lancera pas d'exception. Mais si vous souhaitez que Aspose.Cells vérifie si le format numérique personnalisé assigné est valide ou non, veuillez définir la propriété [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) sur **true**.

## **Vérifier le format de nombre personnalisé lors du réglage de la propriété Style.Custom**

Le code d'exemple suivant assigne un format numérique personnalisé invalide à la propriété [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Étant donné que nous avons déjà défini la propriété [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) sur **true**, une exception sera levée, par exemple, format numérique invalide. Veuillez lire les commentaires dans le code pour plus d'aide.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
