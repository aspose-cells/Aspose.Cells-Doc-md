---
title: Get Range with External Links with C++
linktitle: Get Range with External Links
type: docs
weight: 120
url: /cpp/get-range-with-external-links/
description: Learn how to retrieve ranges with external links in Excel files using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Range with External Links**

Often, Excel files access data from other Excel files using external links. Aspose.Cells provides the option to retrieve these external links by using the [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) method. The [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) method returns an array of type [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). The [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) class provides a [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) property which returns the name of the external file. The [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) class exposes the following members.

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/): The end column of the area
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/): The end row of the area
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/): Get the external file name if this is an external reference
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/): Indicates whether this is an area
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/): Indicates whether this is an external link
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/): Indicates which sheet this reference is in
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/): The start column of the area
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/): The start row of the area

The sample code given below demonstrates the use of the [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) method to get ranges with external links.

## **Sample Code**

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
