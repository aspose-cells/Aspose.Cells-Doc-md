---
title: Указание автора при защите книги паролем с помощью C++
linktitle: Укажите автора при защите от записи книги
type: docs
weight: 40
url: /ru/cpp/specify-author-while-write-protecting-workbook/
description: Узнайте, как указать имя автора при защите книги паролем, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете указать имя автора при защите книги с помощью API Aspose.Cells. Для этой цели используйте свойство [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/).

## **Укажите автора при защите от записи книги**

Следующий пример кода иллюстрирует использование свойства [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/). Код создает пустую книгу, защищает ее паролем, указывает имя автора и сохраняет как [выходной файл Excel](67338582.xlsx). Следующий скриншот показывает эффект использования этого примера на выходном файле.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
