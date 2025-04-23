---
title: Afficher les formules au lieu des valeurs dans une feuille de calcul avec C++
linktitle: Afficher les formules au lieu des valeurs
type: docs
weight: 20
url: /fr/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Cet article fournit un code d exemple pour utiliser l API C++ afin d afficher de manière programmée les formules plutôt que les valeurs dans une feuille de calcul ou une feuille Excel.
---

{{% alert color="primary" %}}

Il est possible d'afficher des formules au lieu des valeurs calculées dans Microsoft Excel en utilisant l'option **Afficher les formules** de l'onglet **Formules**. Lorsque les formules sont affichées, Microsoft Excel affiche les formules dans la feuille de calcul. Vous pouvez obtenir le même résultat en utilisant Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit une propriété [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/). Définissez-la sur **true** pour demander à Microsoft Excel d'afficher des formules.

```cpp
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

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
