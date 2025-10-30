---
title: Detektera om Arket är Låst med Lösenord med C++
linktitle: Upptäck om arbetsbladet är lösenordsskyddat
type: docs
weight: 360
url: /sv/cpp/detect-if-worksheet-is-password-protected/
description: Lär dig hur du kan detektera om ett ark är lösenordsskyddat med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Det är möjligt att skydda arbetsböcker och ark separat. Till exempel kan ett kalkylblad innehålla ett eller flera ark som är lösenordsskyddade, men själva kalkylbladet kan eller kanske inte är skyddat. Aspose.Cells API ger möjlighet att upptäcka om ett givet ark är lösenordsskyddat eller inte. Denna artikel visar hur man använder Aspose.Cells for C++ API för att uppnå samma.

{{% /alert %}}

Aspose.Cells for C++ har exponerat [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) egenskapen för att upptäcka om ett ark är lösenordsskyddat eller inte. Den booleska egenskapen [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) returnerar **true** om [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) är lösenordsskyddat och **false** annars.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
