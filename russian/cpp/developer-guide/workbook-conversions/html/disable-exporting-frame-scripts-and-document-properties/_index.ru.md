---
title: Отключить экспорт скриптов кадров и свойств документа с помощью C++
type: docs
weight: 310
url: /ru/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Отключить экспорт скриптов кадров и свойств документа с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells экспортирует скрипты кадров и свойства документа при преобразовании рабочей книги в HTML. В версии 8.6.0 Aspose.Cells for C++ появилась опция, которая позволяет по желанию отключить экспорт скриптов кадров и свойств документа. Используйте свойство HtmlSaveOptions.ExportFrameScriptsAndProperties для отключения экспорта.

{{% /alert %}}

## **Отключение экспорта сценариев рамки и свойств документа**

Следующий образец кода позволяет отключить экспорт сценариев рамки и свойств документа. После преобразования книги в HTML выходной файл не будет содержать никаких сценариев рамки и свойств документа.

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

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
