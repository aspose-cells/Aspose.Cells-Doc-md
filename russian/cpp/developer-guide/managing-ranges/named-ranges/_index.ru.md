---
title: Создание рабочей книги и листа с именованными диапазонами с C++
linktitle: Именованный диапазон
type: docs
weight: 40
url: /ru/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Научитесь создавать рабочие книги и листы с именованными диапазонами с C++ и Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям определить именованные диапазоны с двумя различными областями: книга (также известная как глобальная область) и лист.

- Именованные диапазоны с глобальной областью могут быть доступны с любого листа внутри этой книги, просто используя его имя.
- Именованные диапазоны с областью листа доступны с помощью ссылки на конкретный лист, на котором он был создан.

Aspose.Cells предоставляет ту же функциональность, что и Microsoft Excel для добавления именованных диапазонов с областью книги и листа. При создании именованного диапазона с областью листа следует использовать ссылку на лист в именованном диапазоне, чтобы указать его как именованный диапазон с областью листа.

{{% /alert %}} 

## **Добавление именованного диапазона с областью видимости рабочей книги**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Добавление Именованного Диапазона с Областью Листа**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Создание доступа и копирование именованных диапазонов](/cells/ru/cpp/create-access-and-copy-named-ranges/)
- [Форматирование и изменение именованных диапазонов](/cells/ru/cpp/format-and-modify-named-ranges/)
- [Получить диапазон с внешними ссылками](/cells/ru/cpp/get-range-with-external-links/)
- [Реализация не последовательных диапазонов](/cells/ru/cpp/implementing-non-sequential-ranges/)

