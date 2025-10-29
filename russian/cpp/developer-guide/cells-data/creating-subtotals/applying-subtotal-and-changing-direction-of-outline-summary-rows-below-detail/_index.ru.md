---
title: Применение Subtotal и изменение направления строк сводки ниже деталей с помощью C++
linktitle: Применение итоговой строки и изменение направления итоговых строк справа от детальной
type: docs
weight: 100
url: /ru/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Узнайте, как применять subtotal и менять направление строк сводки ниже деталей, используя API Aspose.Cells for C++.
keywords: Применить итог, добавить итог, изменить направление строк аутлайна суммари снизу от детализации, изменить направление столбцов аутлайна суммари справа от детализации, создать итог и изменить направление строк аутлайна суммари снизу от детализации
---

{{% alert color="primary" %}}

 В этой статье описано, как применять Subtotal к данным и менять направление строк сводки ниже деталей.

Вы можете применить Subtotal к данным методом [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/). Он принимает следующие параметры:

- **CellArea** - Диапазон, на котором применяется промежуточный итог
- **GroupBy** - Поле для группировки по нулевому индексу
- **Function** - Функция промежуточного итога
- **TotalList** - Массив смещений нулевого индекса, указывающий на поля, к которым добавляются итоги
- **Заменить** - указывает, следует ли заменять текущие подсуммы
- **Разрывы страниц** - указывает, нужно ли добавлять разрыв страницы между группами
- **Итоги ниже данных** - указывает, нужно ли добавлять итог под данными.

Также, вы можете контролировать направление строк сводки **подробных данных** с помощью свойства `Worksheet.Outline.SummaryRowBelow`, как показано на следующем скриншоте. Настройку можно открыть в Microsoft Excel через **Данные > Группировка > Настройки**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Изображения исходных и выходных файлов

На следующем скриншоте показан исходный файл Excel, используемый в приведенном ниже образцовом коде, содержащий некоторые данные в столбцах A и B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

На следующем скриншоте показан выходной файл Excel, созданный образцовым кодом. Как видно, к диапазону A2:B11 было применено итого, и направление контура - сводные строки ниже деталей.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Код на C++, для применения subtotal и изменения направления строк сводки

Вот пример кода для достижения указанного выше результата.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the Cells collection in the first worksheet
    Cells cells = worksheet.GetCells();

    // Create a cellarea i.e.., A2:B11
    CellArea ca = CellArea::CreateCellArea(u"A2", u"B11");

    // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, { 1 }, true, false, true);

    // Set the direction of outline summary
    worksheet.GetOutline().SetSummaryRowBelow(true);

    // Save the excel file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
