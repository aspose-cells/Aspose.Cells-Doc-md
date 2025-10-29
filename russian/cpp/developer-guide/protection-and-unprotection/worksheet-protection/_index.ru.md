---
title: Защитить и снять защиту листа с помощью C++
linktitle: Защитить и снять защиту листа
type: docs
weight: 40
url: /ru/cpp/protect-and-unprotect-worksheets/
description: Защитить и снять защиту листа Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}
Чтобы предотвратить случайное или умышленное изменение, перемещение или удаление данных на листе, вы можете заблокировать ячейки на листе Excel, а затем защитить лист паролем. 
{{% /alert %}}

## **Защитить и снять защиту листа в MS Excel**

**![защита и снятие защиты листа](protect-and-unprotect-worksheet.png)**

1. Нажмите **Обзор > Защитить лист**.
1. Введите пароль в **поле Пароль**.
1. Выберите варианты **разрешить**.
1. Выберите **OK**, введите пароль для подтверждения, затем снова выберите **OK**.

## **Защитить лист, используя Aspose.Cells for C++**
Для реализации защиты структуры рабочей книги Excel достаточно следующих простых строк кода.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Снять защиту листа с помощью Aspose.Cells for C++**
Снятие защиты листа легко осуществить с помощью API Aspose.Cells. Если лист защищен паролем, требуется правильный пароль.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Расширенные настройки защиты с момента появления Excel XP](/cells/ru/cpp/advanced-protection-settings-since-excel-xp/)
- [Определение, защищен ли рабочий лист паролем](/cells/ru/cpp/detect-if-worksheet-is-password-protected/)
- [Защита листов](/cells/ru/cpp/protecting-worksheets/)
- [Снятие защиты с листа](/cells/ru/cpp/unprotect-a-worksheet/)
- [Проверить Пароль, Используемый для Защиты Листа](/cells/ru/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
