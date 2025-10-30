---
title: Extern verlinkte Bereiche mit C++ abrufen
linktitle: Bereich mit externen Links abrufen
type: docs
weight: 120
url: /de/cpp/get-range-with-external-links/
description: Erfahren Sie, wie Sie Bereiche mit externen Verknüpfungen in Excel Dateien mit Aspose.Cells und C++ abrufen.
---

## **Bereich mit externen Links abrufen**

Häufig greifen Excel-Dateien auf Daten aus anderen Excel-Dateien über externe Links zu. Aspose.Cells ermöglicht die Abfrage dieser externen Links mit der [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/)-Methode. Die [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/)-Methode gibt ein Array vom Typ [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) zurück. Die [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)-Klasse bietet eine [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/)-Eigenschaft, die den Namen der externen Datei liefert. Die [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)-Klasse stellt die folgenden Mitglieder bereit.

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/): Die Endspalte des Bereichs
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/): Die Endzeile des Bereichs
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/): Holt den Namen der externen Datei, falls dies eine externe Referenz ist
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/): Gibt an, ob dies ein Bereich ist
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/): Gibt an, ob dies eine externe Verknüpfung ist
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/): Gibt an, in welchem Blatt sich diese Referenz befindet
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/): Der Anfangsspalte des Bereichs
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/): Die Startzeile des Bereichs

Der nachstehende Beispielcode zeigt die Verwendung der [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/)-Methode, um Bereiche mit externen Verknüpfungen zu erhalten.

## **Beispielcode**

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
