---
title: Obtenir une plage avec des liens externes avec C++
linktitle: Obtenir une plage avec des liens externes
type: docs
weight: 120
url: /fr/cpp/get-range-with-external-links/
description: Apprenez comment récupérer des plages avec des liens externes dans des fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Obtenir une plage avec des liens externes**

Souvent, les fichiers Excel accèdent à des données provenant d'autres fichiers Excel via des liens externes. Aspose.Cells offre l'option de récupérer ces liens externes en utilisant la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/). La méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) retourne un tableau de type [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). La classe [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) fournit une propriété [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) qui retourne le nom du fichier externe. La classe [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) expose les membres suivants.

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/) : La colonne finale de la zone
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/) : La ligne finale de la zone
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) : Obtenir le nom du fichier externe si c'est une référence externe
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/) : Indique si c'est une zone
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/) : Indique s'il s'agit d'un lien externe
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/) : Indique dans quelle feuille cette référence se trouve
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/) : La colonne de départ de la zone
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/) : La ligne de départ de la zone

Le code d'exemple ci-dessous montre l'utilisation de la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) pour obtenir des plages avec des liens externes.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"SampleExternalReferences.xlsx");

    WorksheetCollection sheets = workbook.GetWorksheets();
    NameCollection namedRanges = sheets.GetNames();

    for (int i = 0; i < namedRanges.GetCount(); ++i)
    {
        Name namedRange = namedRanges.Get(i);
        Vector<ReferredArea> referredAreas = namedRange.GetReferredAreas(true);

        if (!referredAreas.IsNull())
        {
            for (int j = 0; j < referredAreas.GetLength(); ++j)
            {
                ReferredArea referredArea = referredAreas[j];
                std::cout << "IsExternalLink: " << referredArea.IsExternalLink() << std::endl;
                std::cout << "IsArea: " << referredArea.IsArea() << std::endl;
                std::cout << "SheetName: " << referredArea.GetSheetName().ToUtf8() << std::endl;
                std::cout << "ExternalFileName: " << referredArea.GetExternalFileName().ToUtf8() << std::endl;
                std::cout << "StartColumn: " << referredArea.GetStartColumn() << std::endl;
                std::cout << "StartRow: " << referredArea.GetStartRow() << std::endl;
                std::cout << "EndColumn: " << referredArea.GetEndColumn() << std::endl;
                std::cout << "EndRow: " << referredArea.GetEndRow() << std::endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
