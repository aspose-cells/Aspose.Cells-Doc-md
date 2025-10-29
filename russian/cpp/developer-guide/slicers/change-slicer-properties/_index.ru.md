---
title: Изменение свойств сегмента слайсера с помощью C++
linktitle: Изменить свойства фильтра
type: docs
weight: 70
url: /ru/cpp/change-slicer-properties/
description: Изменяйте свойства сегмента слайсера в файлах Excel, используя Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Возможно, возникнут ситуации, когда вам захочется изменить свойства фильтра, такие как его расположение или высота строк. Aspose.Cells предоставляет вам возможность обновления этих свойств.

## **Изменить свойства фильтра**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца и изменяет его свойства, такие как высота строк, ширина, печатаемость, заголовок и т. д. Затем сохраняет книгу как [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
