---
title: Удаление Связи с Пивотом с помощью C++
linktitle: Удалить связь сводной таблицы
type: docs
weight: 30
url: /ru/cpp/remove-pivot-connection/
description: Узнайте, как удалить соединение с пивотом с помощью библиотеки Aspose.Cells на C++.
keywords: Удалите связь сводной таблицы без офиса 2013, офис 2016, офис 2019 и офиса 365.
---

## **Возможные сценарии использования**

Если вы хотите отсоединить срезку и сводную таблицу в Excel, вам нужно щелкнуть правой кнопкой мыши по срезке и выбрать пункт "Связи отчетов...". В списке опций вы можете оперировать флажком. Точно так же, если вы хотите отсоединить срезку и сводную таблицу программно с помощью API Aspose.Cells, пожалуйста, используйте метод [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/). Он отсоединит срезку и сводную таблицу.

## **Отсоединить срезку и сводную таблицу**

Следующий образец кода загружает [образец файла Excel](remove-pivot-connection.xlsx), содержащий существующую срезку. Он получает доступ к срезке, а затем отсоединяет срезку и сводную таблицу. Наконец, он сохраняет книгу как [выходной файл Excel](remove-pivot-connection-out.xlsx). 

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
