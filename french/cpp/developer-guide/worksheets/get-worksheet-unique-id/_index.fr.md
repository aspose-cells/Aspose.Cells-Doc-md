---
title: Obtenir l ID unique de la feuille de calcul avec C++
linktitle: Obtenir l ID unique de la feuille de calcul
type: docs
weight: 190
url: /fr/cpp/get-worksheet-unique-id/
description: Cet article montre comment obtenir l ID unique d une feuille Excel en utilisant la bibliothèque C++ et l API de manière programmatique.
keywords: ID unique de la feuille Excel C++, ID de la feuille C++
---

## **Obtenir l'ID unique de la feuille de calcul**

Aspose.Cells fournit la capacité d'obtenir l'ID unique d'une feuille de calcul en utilisant la méthode [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/). Le code ci-dessous démontre l'utilisation de la méthode [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) pour afficher l'ID unique d'une feuille de calcul. Le code utilise ce [fichier Excel d'exemple](105480213.xlsx).

### Code source

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
