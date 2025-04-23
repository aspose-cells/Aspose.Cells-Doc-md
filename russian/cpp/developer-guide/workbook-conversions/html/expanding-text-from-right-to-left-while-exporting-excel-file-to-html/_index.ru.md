---
title: Расширение текста справа налево при экспорте файла Excel в HTML с помощью C++
linktitle: Расширение текста справа налево при экспорте файла Excel в HTML
type: docs
weight: 60
url: /ru/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Узнайте, как расширять текст справа налево при экспорте файлов Excel в HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Теперь Aspose.Cells for C++ поддерживает расширение текста справа налево при экспорте Excel в HTML. Эта функция реализована с версии 8.9.0.0. Если ваш исходный файл Excel содержит любой текст, расширяющийся справа налево, Aspose.Cells экспортирует его правильно в HTML.

{{% /alert %}} 

## **Развертывание текста справа налево при экспорте файла Excel в HTML**

Следующий пример преобразует [пример файла Excel](5115502.xlsx) в HTML. Этот скриншот показывает, как выглядит файл Excel в Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Этот скриншот показывает [выходной HTML, созданный с более старой версией](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Этот скриншот показывает [выходной HTML, созданный с новой версией](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Как видно на скриншотах, новая версия расширяет выравненный справа текст слева корректно, как в Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
