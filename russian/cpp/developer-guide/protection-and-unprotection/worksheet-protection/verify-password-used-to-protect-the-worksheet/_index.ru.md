---
title: Проверка пароля для защиты листа с помощью C++
linktitle: Проверить использованный пароль для защиты рабочего листа
type: docs
weight: 370
url: /ru/cpp/verify-password-used-to-protect-the-worksheet/
description: Узнайте, как проверить пароль, использованный для защиты листа, с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells APIs улучшили класс [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/), представив несколько полезных свойств и методов. Один из таких методов - [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/), который позволяет указать пароль в виде экземпляра *string* и проверить, был ли этот пароль использован для защиты [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

Метод [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) возвращает **true**, если указанный пароль совпадает с паролем, используемым для защиты данного листа, и **false** — если не совпадает. Следующий код использует метод [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) вместе с свойством [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) для определения защиты пароля и его проверки.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
