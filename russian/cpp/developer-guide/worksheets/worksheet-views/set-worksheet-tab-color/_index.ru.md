---
title: Установить цвет вкладки листа с помощью C++
linktitle: Установка цвета вкладки таблицы
type: docs
weight: 120
url: /ru/cpp/set-worksheet-tab-color/
description: В этой статье представлен пример кода, который программно устанавливает цвет вкладки листа Excel с помощью C++ API или библиотеки.
keywords: установить цвет вкладки Excel с помощью C++, код для установки цвета вкладки Excel с помощью C++
---

{{% alert color="primary" %}}

Aspose.Cells позволяет изменять цвет отдельных вкладок таблицы, чтобы выделить их из остальных. Например, вы можете сделать вкладку Expenses красной, Sales зеленой, Assets синей и т. д.

{{% /alert %}}

## **Установка цвета вкладки таблицы в Microsoft Excel**
1. Щелкните правой кнопкой мыши на вкладке в листе внизу текущей таблицы.
1. Выберите **Цвет вкладки**.
1. Выберите цвет из палитры.
1. Нажмите **ОК**.

## **Установка цвета вкладки таблицы с помощью Aspose.Cells**
Приведенный ниже образцовый код показывает, как установить цвет вкладки с помощью Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
