---
title: Форматирование богатого текста пользовательской метки данных точки графика с помощью C++
description: Узнайте, как добавлять богатые текстовые пользовательские метки данных к точкам графика в Aspose.Cells for C++. Наше руководство покажет, как форматировать метки с помощью различных шрифтов, цветов и вариантов выравнивания для улучшения внешнего вида и читаемости графиков.
keywords: Aspose.Cells for C++, построение графиков, богатый текст, пользовательские метки данных, шрифты, цвета, выравнивание, внешний вид, читаемость.
type: docs
weight: 10
url: /ru/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для создания богатых текстовых пользовательских меток для точек графика. Aspose.Cells предоставляет метод [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/), который возвращает объект [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/), используемый для настройки свойств шрифта текста, таких как цвет, жирность и так далее.

{{% /alert %}}

## Многострочная пользовательская подпись данных точки диаграммы

Следующий код получает первую точку диаграммы первой серии, устанавливает ее текст и затем задает шрифт первых 10 символов, задавая их цвет красным и делая их жирными — **true**.

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

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
