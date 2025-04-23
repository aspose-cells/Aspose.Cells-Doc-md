---
title: Rileva se il Foglio di Lavoro è Protetto da Password con C++
linktitle: Scoprire se il foglio di lavoro è protetto da password
type: docs
weight: 360
url: /it/cpp/detect-if-worksheet-is-password-protected/
description: Impara come rilevare se un foglio di lavoro è protetto da password usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

È possibile proteggere separatamente workbook e fogli di lavoro. Ad esempio, un foglio di calcolo può contenere uno o più fogli di lavoro protetti da password, tuttavia, il workbook stesso può essere protetto o meno. Le API di Aspose.Cells forniscono i mezzi per rilevare se un determinato foglio di lavoro è protetto da password o no. Questo articolo illustra l'uso dell'API Aspose.Cells for C++ per ottenere lo stesso.

{{% /alert %}}

Aspose.Cells for C++ ha esposto la proprietà [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) per rilevare se un foglio di lavoro è protetto da password o meno. La proprietà di tipo booleano [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) restituisce **true** se [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) è protetto da password e **false** se non lo è.

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
