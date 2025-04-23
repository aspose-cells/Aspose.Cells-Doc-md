---
title: Чтение меток осей после вычисления графика с помощью C++
linktitle: Чтение меток оси после вычисления диаграммы
description: Узнайте, как читать метки осей в Aspose.Cells for C++ после расчета графика. Наше руководство покажет, как получить доступ и извлечь метки осей, включая их форматирование и позиционирование.
keywords: Aspose.Cells for C++, график, метки осей, расчет, чтение, доступ, извлечение, форматирование, позиционирование.
type: docs
weight: 90
url: /ru/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Возможные сценарии использования**

Вы можете прочитать подписи осей вашей диаграммы после вычисления их значений с помощью метода [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/). Для этой цели используйте метод [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/), который вернет список подписей осей.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, см. следующий образец кода, который загружает [образец файла Excel](ReadAxisLabels.xlsx) и читает подписи осей категорий диаграммы на первом листе. Затем выводятся значения подписей осей на консоль. См. пример вывода на консоль приведенный ниже в качестве справки.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
