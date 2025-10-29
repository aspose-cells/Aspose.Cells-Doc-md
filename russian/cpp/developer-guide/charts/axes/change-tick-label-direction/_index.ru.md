---
title: Изменение направления метки шкалы с помощью C++
linktitle: Изменение направления меток делений
description: Узнайте, как изменить направление меток шкалы в Aspose.Cells for C++. Наше руководство поможет вам понять, как регулировать ориентацию меток на осях, включая горизонтальную, вертикальную и наклонную.
keywords: Aspose.Cells for C++, метки шкалы, направление, ориентация, оси, горизонтально, вертикально, наклонно.
type: docs
weight: 170
url: /ru/cpp/change-tick-label-direction/
---

## **Изменение направления меток делений**

Aspose.Cells позволяет изменять направление меток осей, используя свойство [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/). Свойство [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) принимает значение перечисления [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). Перечисление [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) включает следующие члены:

- Горизонтальное
- Вертикальное
- Повернуть90
- Повернуть270
- Стековое

Следующее изображение сравнивает исходный файл и результат:

### **Изображение исходного файла**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Изображение выходного файла**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Следующий фрагмент кода изменяет направление меток делений с Повернуть90 на Горизонтальное.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Исходные и выходные файлы можно загрузить по следующим ссылкам.

[Исходный файл](105480221.xlsx)

[Выходной файл](105480223.xlsx)
{{< app/cells/assistant language="cpp" >}}
