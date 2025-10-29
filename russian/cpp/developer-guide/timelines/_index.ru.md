---
title: Вставка временной шкалы с помощью C++
linktitle: Линии времени
type: docs
weight: 170
url: /ru/cpp/create-timeline/
description: Узнайте, как создавать временные шкалы с Aspose.Cells с помощью C++.
---

## **Возможные сценарии использования**

Вместо настройки фильтров для отображения дат, вы можете использовать временную шкалу PivotTable — динамический фильтр, который позволяет легко фильтровать по дате/времени и увеличивать нужный период с помощью ползунка. Microsoft Excel позволяет создавать временную шкалу, выбирая сводную таблицу и щелкая по **Вставка > Временная шкала**. Aspose.Cells также позволяет создавать временную шкалу с помощью метода [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/).

## **Создать временную линию для сводной таблицы**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец Excel-файла](input.xlsx) содержащий сводную таблицу. Затем он создает временную линию на основе первого базового поля сводной таблицы. Наконец, он сохраняет книгу в формате [output XLSX](output.xlsx). На следующем скриншоте показана временная линия, созданная Aspose.Cells в выходном файле Excel.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
