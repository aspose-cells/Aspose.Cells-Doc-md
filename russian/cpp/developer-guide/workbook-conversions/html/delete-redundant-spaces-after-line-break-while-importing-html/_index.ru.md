---
title: Удаляйте лишние пробелы после разрыва строки при импорте HTML с помощью C++
linktitle: Удаление избыточных пробелов после переноса строки при импорте HTML
type: docs
weight: 20
url: /ru/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Узнайте, как удалять лишние пробелы после разрывов строк при импорте HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Пожалуйста, используйте свойство [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) и установите его в **true**, чтобы удалить все лишние пробелы после тега разрыва строки. По умолчанию это свойство равно **false**, и лишние пробелы сохраняются в выходных файлах Excel.

{{% /alert %}}

## Эффект установки свойства HTMLLoadOptions.DeleteRedundantSpaces в значение false и true

На следующем скриншоте показан эффект установки этого свойства в **false** и **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Удаление избыточных пробелов после переноса строки при импорте HTML

### Пример программирования

Следующий пример кода демонстрирует использование свойства [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/). Пожалуйста, установите его **true** или **false**, чтобы получить вывод, как показано на скриншоте выше.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
