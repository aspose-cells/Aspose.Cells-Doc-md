---
title: Hämta cellvalidering i ODS filer med C++
linktitle: Få cellvalidering i ODS filer
type: docs
weight: 180
url: /sv/cpp/get-cell-validation-in-ods-files/
description: Lär dig hur du hämtar cellvalidering i ODS filer med Aspose.Cells for C++.
keywords: Få cellvalidering, Hämta cellvalidering 
---

## **Hämta cellvalidering i ODS-filer**

Med Aspose.Cells for C++ kan du hämta den validering som är tillämpad på en cell i ODS-filer. API:et erbjuder metoden [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) i klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Följande kodexempel demonstrerar användningen av [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/)-metoden genom att ladda filen [source ODS](101089354.ods) och läsa valideringen av cell A9.

### **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
