---
title: Применение расширенного условного форматирования с помощью C++
linktitle: Применение расширенного условного форматирования
description: Как использовать библиотеку Aspose.Cells в C++ для применения расширенного условного форматирования. Настраивая эти критерии, вы получаете больший контроль над внешним видом ячеек.
keywords: Aspose.Cells, Расширенное условное форматирование, C++, Условное, Форматирование
type: docs
weight: 70
url: /ru/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 и более поздние версии (2010/2013/2016) предоставляют некоторые расширенные функции для условного форматирования. Например, он позволяет применять заливку ячеек, границы, цветные значки, стрелки, флажки и форматирование шрифтов и т.д., что стало довольно сложным.

{{% /alert %}}

## **Применить расширенное условное форматирование к файлам Microsoft Excel**
Условное форматирование может:

- Добавлять заштрихованные полосы данных для графического улучшения базовых чисел, вставляя простую столбчатую диаграмму в ячейки.
- Автоматически заливать ячейки цветовыми шкалами на основе их отношения к значениям в других ячейках в диапазоне. По умолчанию наименьшее значение закрашивается красным, постепенно переходя к наибольшему значению зеленым.
- Используйте наборы значков аналогично цветовым шкалам, но вместо заливки ячеек добавляйте маленькие значки, такие как стрелки и светофоры, в ячейки.

Aspose.Cells полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более поздние версии в формате XLSX в реальном времени. В этом примере демонстрируется упражнение для продвинутых типов условного форматирования, включая IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom и другие правила с различными наборами свойств.

### **Вычисление цвета, выбранного Microsoft Excel для условного форматирования ColorScale**
Aspose.Cells позволяет вычислить выбранный Microsoft Excel цвет при использовании условного форматирования ColorScale в файле шаблона. Приведенный ниже образец кода поможет вам научиться вычислять выбранный Microsoft Excel цвет.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
