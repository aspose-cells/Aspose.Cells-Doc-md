---
title: Получить лист Excel графика с помощью C++
linktitle: Получить рабочий лист диаграммы
description: Узнайте, как получать связанный с графиком лист Excel с помощью Aspose.Cells for C++. Наш гид покажет, как получить доступ к листу и выполнять операции над ним для манипуляции базовыми данными графика.
keywords: Aspose.Cells for C++, графики Excel, листы, управление данными, базовые данные, операции.
type: docs
weight: 1000
url: /ru/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Иногда нужно получить доступ к листу через ссылку графика. Aspose.Cells предоставляет метод [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/), который возвращает ссылку на лист, содержащий график.

{{% /alert %}}

Пример показывает, как использовать метод [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/). Сначала он выводит имя листа, затем получает первый график на листе и снова выводит название листа с помощью метода [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Ниже приведен вывод консоли, который получается в результате примера. Как видно, он дважды выводит одно и то же имя листа.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
