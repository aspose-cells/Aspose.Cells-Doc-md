---
title: Отрисовка пользовательского формата даты g и ge, мм, дд с помощью C++
description: Aspose.Cells — это библиотека на C++ для работы с файлами электронных таблиц, которая поддерживает отображение дат с помощью пользовательских шаблонов формата dates g и ge . В этой статье будет описано, как отображать пользовательские шаблоны формата дат с помощью библиотеки Aspose.Cells, чтобы пользователи могли управлять тем, как отображаются даты, если они этого захотят.
keywords: Aspose.Cells, библиотека C++, электронная таблица, пользовательский формат даты, отображение, шаблон g , шаблон ge , контроль отображения
type: docs
weight: 160
url: /ru/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Теперь Aspose.Cells может выводить пользовательские шаблоны формата дат, такие как g, ge.mm.dd и подобные. Пожалуйста, проверьте прикрепленный [исходный файл Excel](5112361.xlsx) и [конвертированный PDF](5112360.pdf) с помощью Aspose.Cells для вашего справки.

{{% /alert %}}

Приведенный ниже образец кода преобразует [исходный файл Excel](5112361.xlsx), содержащий значения дат с пользовательскими шаблонами формата 'g' и 'ge.mm.dd' в [выходной PDF](5112360.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
