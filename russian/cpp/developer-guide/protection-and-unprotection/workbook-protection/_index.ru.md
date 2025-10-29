---
title: Защитить и снять защиту структуры книги с помощью C++
linktitle: Защита и снятие защиты структуры рабочей книги
type: docs
weight: 40
url: /ru/cpp/protect-and-unprotect-workbook-structure/
description: Защитить и снять защиту структуры книги Excel, используя C++ с Aspose.Cells.
---

{{% alert color="primary" %}}
Чтобы предотвратить просмотр скрытых листов, добавление, перемещение, удаление или скрытие листов другими пользователями и переименование листов, вы можете защитить структуру своей рабочей книги Excel паролем.
{{% /alert %}}

## **Защитить и снять защиту структуры книги в MS Excel**

**![защита и снятие защиты структуры рабочей книги](protect-and-unprotect-workbook-structure.png)**

1. Нажмите **Обзор > Защитить книгу**.
1. Введите пароль в **поле Пароль**.
1. Выберите **OK**, введите пароль для подтверждения, затем снова выберите **OK**.

## **Защитить структуру книги с помощью Aspose.Cells for C++**
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

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Снять защиту структуры книги с помощью Aspose.Cells for C++**
Снятие защиты структуры рабочей книги легко с помощью API Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
Примечание: требуется правильный пароль.
{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
