---
title: Экспорт условного форматирования DataBar, ColorScale и IconSet при преобразовании Excel в HTML с помощью C++
linktitle: Экспортировать условное форматирование в HTML
type: docs
weight: 30
url: /ru/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Узнайте, как экспортировать условное форматирование DataBar, ColorScale и IconSet при конвертации файлов Excel в HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Вы можете экспортировать условное форматирование DataBar, ColorScale и IconSet при конвертации файла Excel в HTML. Эта функция частично поддерживается Microsoft Excel, но Aspose.Cells for C++ полностью ее поддерживает.

{{% /alert %}} 

## **Экспортировать условное форматирование DataBar, ColorScale и IconSet при преобразовании Excel в HTML**
Следующий скриншот показывает [пример файла Excel](5115558.xlsx) с условным форматированием DataBar, ColorScale и IconSet. Вы можете скачать [пример файла Excel](5115558.xlsx) по указанной ссылке.

![todo:image_alt_text](conversion_1.png)

Следующий скриншот показывает HTML вывод Aspose.Cells с DataBar, ColorScale и IconSet условным форматированием. Как видно, он полностью совпадает с [примером файла Excel](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Образец кода**
Следующий пример кода преобразует пример файла Excel в HTML, что является обычным [преобразованием Excel в HTML](/cells/ru/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
