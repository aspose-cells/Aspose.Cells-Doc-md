---
title: Реализация системы дат 1904 с помощью C++
linktitle: Реализация 1904 го годового системы
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает реализацию системы дат 1904, позволяя пользователям вычислять и форматировать данные на основе системы дат 1904 года, начиная с 1 января 1904 года. В этой статье рассказывается, как реализовать систему дат 1904 с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, 1904 годовая система, электронная таблица, вычисление, форматирование
type: docs
weight: 7000
url: /ru/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel поддерживает две системы дат: 1900-ую систему дат (система даты по умолчанию, реализованная в Excel для Windows) и 1904-ую систему дат. 1904-ая система дат обычно используется для обеспечения совместимости с файлами Macintosh Excel и является системой по умолчанию при использовании Excel для Macintosh. Вы можете установить 1904-ую систему дат для файлов Excel с помощью Aspose.Cells.

{{% /alert %}}

Для реализации 1904-ой годовой системы в Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Инструменты** выберите **Параметры**, а затем выберите вкладку **Расчет**.
1. Выберите опцию **1904 годовая система**.
1. Нажмите **ОК**.

|**Выбор 1904-ой годовой системы в Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
См. следующий образец кода о том, как это сделать с использованием API Aspose.Cells.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
