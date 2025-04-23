---
title: Заполняйте данные сначала по строкам, затем по столбцам с помощью C++
linktitle: Сначала заполните данные по строкам, а затем по столбцам
type: docs
weight: 1000
url: /ru/cpp/populate-data-first-by-row-then-by-column/
description: Узнайте, как заполнять данные сначала по строкам, затем по столбцам через API Aspose.Cells for C++.
keywords: Заполнение данных сначала по строкам, а затем по столбцам; Вставка данных сначала по строкам, а затем по столбцам; Добавление данных сначала по строкам, а затем по столбцам; Высокопроизводительное добавление данных, Высокопроизводительное добавление данных
---

{{% alert color="primary" %}} 

Заполнение электронной таблицы данными сначала по строкам, а затем по столбцам улучшает общую производительность.

{{% /alert %}} 

Размещение данных в последовательности A1, B1, A2, B2 быстрее, чем A1, A2, B1, B2. Если в листе большое количество ячеек и вы следуете второй последовательности, то есть заполняете данные строка за строкой, этот совет может значительно ускорить программу.

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
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
