---
title: Обновление среза с помощью C++
linktitle: Обновление среза
type: docs
weight: 50
url: /ru/cpp/updating-slicer/
description: Эта статья показывает, как обновить срез, чтобы фильтровать данные связанной сводной таблицы или таблицы с помощью API Aspose.Cells for C++.
keywords: Aspose.Cells C++ обновление среза, C++ как изменить срез, как отфильтровать сводную таблицу срезом в C++, C++ Slicer SelectItems, C++ Slicer ClearFilter, C++ Slicer UnselectItems.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Обновление среза означает фильтрацию данных сводной таблицы или таблицы, к которой подключен срез. Когда вы выбираете или отменяете выбор элементов среза в Microsoft Excel, связанная сводная таблица или таблица пересчитывается соответствующим образом. С Aspose.Cells for C++ вам не нужно перебирать элементы кэша среза и обновлять срез вручную — метод [**Slicer.SelectItems(Vector&lt;U16String&gt;, bool)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/selectitems/) обновляет срез и пересчитывает связанную сводную таблицу или таблицу напрямую из элементов фильтра:
- `Slicer.SelectItems(labels, append)` — выбирает указанные метки и пересчитывает связанную сводную таблицу или таблицу. Если `append` равно `true`, изначально выбранные метки сохраняются, а указанные метки добавляются к выделению; если `append` равно `false`, все исходные выделения сбрасываются и выбранными остаются только указанные метки.
- `Slicer.UnselectItems(labels)` — отменяет выбор части выбранных элементов.
- `Slicer.ClearFilter()` — удаляет фильтр и выбирает все элементы.

{{% alert color="primary" %}}
Начиная с версии Aspose.Cells for C++ 26.10, свойство `SlicerCacheItem.Selected` становится доступным только для чтения, и его сеттер больше не поддерживается. Используйте методы `Slicer.SelectItems`, `Slicer.UnselectItems` и `Slicer.ClearFilter` вместо установки `SlicerCacheItem.Selected` для каждого элемента по отдельности.
{{% /alert %}}

## **Как обновить срез**
Следующий образец кода загружает [образец файла Excel](67338475.xlsx), содержащий существующий срез, подключенный к сводной таблице. Он выбирает только элементы "Blue" и "Pink" среза с помощью `Slicer.SelectItems(labels, false)` — сводная таблица пересчитывается напрямую из элементов фильтра, без ручного вызова `Slicer.Refresh()`. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338476.xlsx). На следующем скриншоте показано влияние образца кода на образец файла Excel. Как видно на скриншоте, сводная таблица отображает только отфильтрованные элементы.
![todo:image_alt_text](updating-slicer_1.png)

## **Образец кода**
Замените текущее выделение (выбранными остаются только указанные метки) и пересчитайте связанную сводную таблицу или таблицу:

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
    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    Vector<U16String> labels{ u"Blue", u"Pink" };
    slicer.SelectItems(labels, false);
    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);
    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Сохраните текущие выбранные метки и дополнительно выберите другие элементы:

```cpp
// Keep the current selection and add "Red" to it.
Vector<U16String> moreLabels{ u"Red" };
slicer.SelectItems(moreLabels, true);
```

Отмените выбор части выбранных элементов:

```cpp
// Remove "Pink" from the current selection.
Vector<U16String> toRemove{ u"Pink" };
slicer.UnselectItems(toRemove);
```

Удалите фильтр (выберите все элементы):

```cpp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="cpp" >}}