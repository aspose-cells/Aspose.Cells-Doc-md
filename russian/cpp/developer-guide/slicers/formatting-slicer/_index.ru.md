---
title: Форматирование сегмента слайсера с помощью C++
linktitle: Форматирование фильтра
type: docs
weight: 20
url: /ru/cpp/formatting-slicer/
description: Форматирование слайсеров в Microsoft Excel с помощью Aspose.Cells на C++.
---

## **Возможные сценарии использования**

Вы можете форматировать слайсер в Microsoft Excel, устанавливая его количество колонок или стиль и т.д. Aspose.Cells также позволяет сделать это с использованием свойств [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) и [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/).

## **Форматирование фильтра**

Пожалуйста, ознакомьтесь с следующим кодом; он загружает [пример файла Excel](67338473.xlsx), содержащий слайсер. Он обращается к слайсеру, устанавливает его количество колонок и тип стиля, а затем сохраняет его как [выходной файл Excel](67338474.xlsx). Скриншот показывает, как выглядит слайсер после выполнения примера кода.

![todo:image_alt_text](formatting-slicer_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
