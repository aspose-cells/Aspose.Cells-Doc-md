---
title: Копирование Sparkline по указанию диапазона данных и расположения группы Sparkline с помощью C++
linktitle: Копирование Sparkline по указанию диапазона данных и расположения
type: docs
weight: 300
url: /ru/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Узнайте, как копировать sparklines, указывая диапазон данных и расположение с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel позволяет копировать минидиаграмму, указывая диапазон данных и местоположение группы минидиаграмм. Aspose.Cells поддерживает эту функцию.

{{% /alert %}}

Для копирования минидиаграммы в другие ячейки в Microsoft Excel:

1. Выберите ячейку, содержащую минидиаграмму.
1. Выберите **Edit Data** в разделе **Sparkline** вкладки **Design**.
1. Выберите **Edit Group Location & Data**.
1. Укажите диапазон данных и местоположение.
1. Нажмите **ОК**.

Aspose.Cells предоставляет метод `SparklineCollection.Add(dataRange, row, column)`, чтобы задать диапазон данных и расположение группы слайсинов. Следующий пример загружает исходный файл Excel, как показано на скриншоте выше, затем обращается к первой группе слайсинов и добавляет диапазоны данных и расположения. В конце он сохраняет итоговый файл Excel на диск, как показано на скриншоте выше.

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
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
