---
title: Получить все индексы скрытых строк после обновления AutoFilter с помощью C++
linktitle: Получить все скрытые индексы строк после обновления автофильтра
type: docs
weight: 320
url: /ru/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Узнайте, как получить все индексы скрытых строк после обновления AutoFilter с помощью API Aspose.Cells for C++.
keywords: Получите все скрытые индексы строк после обновления автофильтра, получите все скрытые индексы строк после обновления автофильтра, получите все скрытые индексы строк после обновления автофильтра
---

## **Возможные сценарии использования**

Когда вы применяете автофильтр к ячейкам листа, то некоторые строки автоматически скрываются. Однако может возникнуть ситуация, когда некоторые строки уже были скрыты вручную пользователем Excel, и они не скрыты автофильтром. Поэтому сложно знать, какие из строк были скрыты автофильтром, а какие - вручную. Aspose.Cells решает эту проблему с помощью метода int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/). Этот метод возвращает индексы строк всех строк, скрытых автофильтром, и не вручную пользователем Excel.

## **Получить все скрытые индексы строк после обновления автофильтра**

Пожалуйста, посмотрите следующий образец кода, который загружает [образец Excel-файла](64716909.xlsx), содержащий некоторые из строк, скрытых вручную пользователем Excel. Код применяет автофильтр и обновляет его с помощью метода int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/), который возвращает индексы скрытых строк автофильтром. Затем он выводит индексы скрытых строк в консоль, а также имена ячеек и их значения.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
