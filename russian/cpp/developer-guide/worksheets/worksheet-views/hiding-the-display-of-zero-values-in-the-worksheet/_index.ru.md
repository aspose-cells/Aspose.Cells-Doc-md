---
title: Скрытие отображения нулевых значений в листе с помощью C++
linktitle: Скрытие отображения нулевых значений в таблице
type: docs
weight: 50
url: /ru/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: В этой статье представлены пример кода, показывающий, как программно скрыть нулевые значения в Excel с помощью API или библиотеки C++.
keywords: скрыть нулевые значения листа Excel в C++
---

{{% alert color="primary" %}} 

Иногда вам нужно скрывать нулевые значения в электронной таблице. Это может быть личным предпочтением или стандартом форматирования.

{{% /alert %}} 

Чтобы скрыть нулевые значения в таблице Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Инструменты** выберите **Параметры**, затем выберите вкладку **Вид**.
1. Отмените выбор опции **Нулевые значения**.
1. Нажмите **ОК**.

Пожалуйста, ознакомьтесь с приведенным ниже образцовым кодом, демонстрирующим скрытие нулей с использованием Aspose.Cells.

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

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
