---
title: Foga samman eller avfoga cellområden med C++
linktitle: Slå samman eller dela upp cellintervall
type: docs
weight: 190
url: /sv/cpp/merge-or-unmerge-range-of-cells/
description: Foga samman och avfoga celler i ett område i Excel med C++ kod.
keywords: c++ foga samman och avfoga celler i ett område, c++ foga samman och avfoga celler i ett område, foga samman och avfoga celler i ett område med c++, foga samman och avfoga celler i ett område med c++, foga samman och avfoga celler i Excel med c++, f++ foga samman och avfoga celler i Excel, c++ foga samman celler i Excel, c++ avfoga celler i Excel, foga samman celler i område med c++
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att slå samman eller dela upp ett cellintervall. Aspose.Cells tillhandahåller [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) och [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) metoder för detta ändamål. Denna artikel förklarar hur man slår samman ett cellintervall till en enda cell.

{{% /alert %}}

## **Exempel**

Följande exempel skapar först ett område - A1:D4 - och fusionerar sedan cellerna i området till en enda cell med hjälp av [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)-metoden. På liknande sätt kan du dela upp celler genom att skapa ett område och använda [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)-metoden.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
