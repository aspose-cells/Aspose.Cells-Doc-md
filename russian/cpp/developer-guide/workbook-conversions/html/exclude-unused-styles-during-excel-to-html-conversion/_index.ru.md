---
title: Исключить неиспользуемые стили при преобразовании Excel в HTML с помощью C++
linktitle: Исключить неиспользуемые стили
type: docs
weight: 30
url: /ru/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Узнайте, как исключить неиспользуемые стили при преобразовании Excel в HTML с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Файлы Microsoft Excel могут содержать множество неиспользуемых стилей. При экспорте файла Excel в формат HTML экспортируются эти неиспользуемые стили, что может увеличить размер HTML. Вы можете исключить неиспользуемые стили при преобразовании файла Excel в HTML, установив свойство [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) в **true**. На следующем скриншоте показан пример неиспользуемого стиля внутри итогового HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**

Следующий пример создает рабочую книгу и также добавляет неиспользуемый именованный стиль. Поскольку свойство [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) установлено в **true**, этот неиспользуемый стиль не будет экспортирован в [итоговый HTML](61767778.zip). Если установить его в **false**, то этот неиспользуемый стиль появится в итоговом HTML, что видно в разметке HTML, как показано выше.

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create an unused named style
    Style unusedStyle = wb.CreateStyle();
    unusedStyle.SetName(u"UnusedStyle_XXXXXXXXXXXXXX");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some value in cell C7
    ws.GetCells().Get(u"C7").PutValue(u"This is sample text.");

    // Specify html save options, we want to exclude unused styles
    HtmlSaveOptions opts;

    // Comment this line to include unused styles
    opts.SetExcludeUnusedStyles(true);

    // Save the workbook in html format
    wb.Save(u"outputExcludeUnusedStylesInExcelToHTML.html", opts);

    std::cout << "Workbook saved successfully with unused styles excluded!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
