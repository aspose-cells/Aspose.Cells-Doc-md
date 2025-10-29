---
title: Примените расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным условиям, с помощью C++
linktitle: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 280
url: /ru/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Узнайте, как применять расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным условиям, используя API Aspose.Cells for C++.
keywords: Применить расширенный фильтр, установить расширенный фильтр, добавить расширенный фильтр, создать расширенный фильтр, Как добавить расширенный фильтр к диапазону
---

## **Возможные сценарии использования**

Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить расширенный фильтр через команду *Данные > Расширенный*, как показано на скриншоте.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells также позволяет использовать расширенный фильтр с помощью метода [**GetAdvancedFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getadvancedfilter/). Аналогично Microsoft Excel, он принимает следующие параметры.

**isFilter**

Указывает, фильтровать ли список на месте.

**listRange**

Диапазон списка.

**criteriaRange**

Диапазон критериев.

**copyTo**

Диапазон, куда копируются данные.

**uniqueRecordOnly**

Отображение или копирование только уникальных строк.

## **Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям**

Следующий пример кода применяет расширенный фильтр к [пробному Excel-файлу](48496692.xlsx) и создает [выходной Excel-файл](48496691.xlsx). Скриншот показывает оба файла для сравнения. Внутри скриншота видно, что данные были отфильтрованы внутри выходного файла согласно сложным условиям.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook
    Workbook workbook(sourceDir + u"sampleAdvancedFilter.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Apply advanced filter on range A5:D19 and criteria range is A1:D2
    // Besides, we want to filter in place
    // And, we want all filtered records not just unique records
    ws.Advanced_Filter(true, u"A5:D19", u"A1:D2", u"", false);

    // Save the workbook in xlsx format
    workbook.Save(outputDir + u"outputAdvancedFilter.xlsx", SaveFormat::Xlsx);

    std::cout << "Advanced filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
