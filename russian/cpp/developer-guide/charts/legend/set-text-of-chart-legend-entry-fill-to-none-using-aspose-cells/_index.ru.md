---
title: Установить Текст элемента легенды графика в None с помощью C++
linktitle: Установить Текст элемента легенды графика в None
description: Узнайте, как использовать Aspose.Cells for C++ для установки текста заливки элемента легенды графика в none. Наше руководство продемонстрирует, как изменить цвет заливки элементов легенды в диаграммах Microsoft Excel для лучшей визуализации и настройки.
keywords: Aspose.Cells for C++, Заливка элемента легенды, Microsoft Excel, Визуализация, Настройка.
type: docs
weight: 320
url: /ru/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Если вы хотите установить текст заливки легенды графика на никуда, чтобы он не отображался внутри легенды графика, то установите [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) в **true**.

{{% /alert %}}

В следующем образце кода устанавливается текст заливки второй записи легенды графика на никуда. Скачайте [образец excel-файла](5115219.xlsx), использованный в этом коде, и [выходной excel-файл](5115217.xlsx), который он создает, для вашего ориентира.

На следующем скриншоте показан эффект этого кода на [образце excel-файла](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
