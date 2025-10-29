---
title: Защита или снятие защиты с совместной книги с помощью C++
linktitle: Защита паролем или снятие защиты общей рабочей книги
type: docs
weight: 10
url: /ru/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Узнайте, как защитить паролем или снять защиту с совместной книги, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете защитить или снять защиту общей рабочей книги в Microsoft Excel, как показано на следующем снимке экрана. Aspose.Cells также поддерживает эту функцию с помощью методов [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) и [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Защита паролем или снятие защиты общей книги**

В следующем образце кода создается рабочая книга, защищенная во время включения совместного использования, и сохраняется как [выходной файл Excel](55541777.xlsx). На снимке экрана показано, что при попытке снять защиту Microsoft Excel просит вас ввести пароль для снятия защиты.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
