---
title: Trouver des cellules avec un style spécifique avec C++
linktitle: Trouver des cellules avec un style spécifique
type: docs
weight: 190
url: /fr/cpp/find-cells-with-specific-style/
description: Apprenez comment rechercher ou trouver des cellules avec un style particulier appliqué via l API Aspose.Cells for C++.
keywords: Trouver des cellules avec un style particulier appliqué, Rechercher des cellules avec un style particulier appliqué
---

{{% alert color="primary" %}}

Parfois, vous devez trouver des cellules avec un style particulier appliqué. Vous pouvez utiliser Aspose.Cells pour trouver toutes les cellules avec un style commun. Aspose.Cells fournit la propriété [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) que vous pouvez utiliser pour spécifier le style à rechercher dans les cellules.

{{% /alert %}}

Dans cet exemple, le code trouve toutes les cellules ayant le même style que celle de la cellule A1. Après l'exécution du code, toutes les cellules ayant le même style que A1 contiennent le texte "Trouvé".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
