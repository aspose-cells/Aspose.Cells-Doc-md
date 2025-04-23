---
title: Hämta område med externa länkar med C++
linktitle: Hämta intervall med externa länkar
type: docs
weight: 120
url: /sv/cpp/get-range-with-external-links/
description: Lär dig hur du hämtar områden med externa länkar i Excel filer med Aspose.Cells och C++.
---

## **Hämta intervall med externa länkar**

Ofta använder Excel-filer externa länkar för att få åtkomst till data i andra Excel-filer. Aspose.Cells ger möjlighet att hämta dessa externa länkar med hjälp av [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) metoden. [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) metoden returnerar en array av typen [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) klassen tillhandahåller en [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) egenskap som returnerar namnet på den externa filen. [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) klassen exponeras av följande medlemmar.

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/): ändens kolumn för området
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/): ändens rad för området
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/): Hämta det externa filnamnet om detta är en extern referens
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/): Indikerar om detta är ett område
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/): Indikerar om detta är en extern länk
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/): Indikerar vilken bladreferens detta är i
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/): Startkolumn för området
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/): Startrad för området

Kodexemplet nedan visar hur man använder [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) metoden för att hämta områden med externa länkar.

## **Exempelkod**

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
