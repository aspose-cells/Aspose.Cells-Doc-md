---
title: Обновление слайсера с помощью C++
linktitle: Обновление срезки
type: docs
weight: 50
url: /ru/cpp/updating-slicer/
description: Эта статья показывает, как обновлять связанные сводные таблицы, обновляя слайсер с помощью API Aspose.Cells for C++.
keywords: Обновление слайсера в Aspose.Cells C++, изменение слайсера, настройка слайсера в C++, выбор или отмена выбора элементов слайсера.
---

## **Возможные сценарии использования**

Если вы хотите обновить слайсер в Microsoft Excel, выбрав или отменив выбор его элементов, таблица слайсера или сводная таблица обновятся соответственно. Используйте [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/) для выбора или отмены выбора элементов слайсера в Aspose.Cells, затем вызовите метод [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) для обновления таблицы слайсера или сводной таблицы.

## **Как обновить фильтр**

Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий фильтр. Он отменяет выбор 2-го и 3-го элементов фильтра и обновляет фильтр. Затем сохраняет рабочую книгу в [выходной файл Excel](67338476.xlsx). На следующем скриншоте показан эффект образца кода на образцовый файл Excel. Как вы можете видеть на скриншоте, обновление фильтра с выбранными элементами также обновило сводную таблицу соответственно.

![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
