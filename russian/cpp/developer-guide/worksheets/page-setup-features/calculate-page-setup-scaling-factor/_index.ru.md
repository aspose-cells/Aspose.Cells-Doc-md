---
title: Вычислить коэффициент масштабирования страницы в C++
linktitle: Вычислить масштабирование настройки страницы
type: docs
weight: 300
url: /ru/cpp/calculate-page-setup-scaling-factor/
description: Данная статья содержит пример кода, объясняющий, как использовать C++ API или библиотеку для вычисления коэффициента масштабирования страницы с помощью функции Масштабировать по n страниц по ширине и m по высоте листа Excel программно.
keywords: Масштабировать по n страниц по ширине и m по высоте Excel C++, расчет коэффициента масштабирования страницы на языке C++
---

{{% alert color="primary" %}}

Когда вы устанавливаете масштабирование настройки страницы с помощью опции **Вписать на n страницы по ширине и m по высоте**, Microsoft Excel вычисляет масштабный коэффициент настроек страницы. Вы можете рассчитать то же самое, используя свойство [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/). Это свойство возвращает значение double, которое можно преобразовать в процентное значение. Например, если оно возвращает 0,5, это означает, что коэффициент масштабирования составляет 50%.

{{% /alert %}}

В следующем примере кода показано, как рассчитать масштабный коэффициент настроек страницы, используя свойство [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
