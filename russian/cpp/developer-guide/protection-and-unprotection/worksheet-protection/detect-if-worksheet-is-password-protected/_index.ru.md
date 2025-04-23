---
title: Обнаружение защищенного паролем листа с помощью C++
linktitle: Определить, защищен ли рабочий лист паролем
type: docs
weight: 360
url: /ru/cpp/detect-if-worksheet-is-password-protected/
description: Узнайте, как обнаружить, защищен ли лист паролем, с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Можно защищать отдельно рабочие книги и листы. Например, рабочая книга может содержать один или несколько листов с паролем, однако сама рабочая книга может быть защищена или нет. API Aspose.Cells предоставляет средства для определения, защищен ли конкретный лист паролем. Эта статья демонстрирует использование API Aspose.Cells for C++ для достижения этого.

{{% /alert %}}

Aspose.Cells for C++ предоставляет свойство [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) для обнаружения защищен ли лист паролем или нет. Булевое свойство [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) возвращает **true**, если [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) защищен паролем, и **false** — если нет.

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
