---
title: Задание пользовательского шаблона форматирования DBNum с помощью C++
linktitle: Указание пользовательского шаблона форматирования с использованием DBNum
description: Aspose.Cells — это библиотека на C++ для работы с файлами электронных таблиц, которая поддерживает форматирование дат и чисел с помощью пользовательских шаблонов форматирования. В этой статье покажется, как использовать библиотеку Aspose.Cells для задания пользовательского шаблона формы dbnum , чтобы пользователи могли больше контролировать отображение чисел.
keywords: Aspose.Cells, библиотека C++, электронная таблица, пользовательский шаблон форматирования, форматирование, dbnum , контроль отображения
type: docs
weight: 110
url: /ru/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Возможные сценарии использования**

Aspose.Cells поддерживает пользовательский шаблон форматирования *DBNum*. Например, если значение ячейки равно 123 и вы задаете его пользовательское форматирование как [DBNum2][$-804]General, оно будет отображаться как 壹佰贰拾叁. Вы можете задать свое собственное форматирование ячейки с помощью метода [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) и свойства [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/).

## **Образец кода**

Следующий пример кода показывает, как указать пользовательский шаблон *DBNum*. Пожалуйста, проверьте его [вывод PDF](43352081.pdf) для получения дополнительной помощи.

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
