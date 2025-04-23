---
title: Добавление соединения сводной таблицы с помощью C++
linktitle: Добавить связь сводной таблицы
type: docs
weight: 30
url: /ru/cpp/add-pivot-connection/
description: Узнайте, как добавлять соединение сводной таблицы с помощью библиотеки Aspose.Cells и C++.
keywords: Добавить связь сводной таблицы без Office 2013, Office 2016, Office 2019 и Office 365.
---

## **Возможные сценарии использования**

Если вы хотите связать срез и сводную таблицу в Excel, вам нужно щелкнуть правой кнопкой мыши на срезе и выбрать пункт "Связи отчета...". В параметрах вы можете оперировать флажком. Точно так же, если вы хотите связать срез и сводную таблицу с использованием программного интерфейса Aspose.Cells API, пожалуйста, используйте метод [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/). Он свяжет срез и сводную таблицу.

## **Ассоциировать фильтр и сводную таблицу**

Следующий образец кода загружает [образец файла Excel](add-pivot-connection.xlsx), содержащий существующий фильтр. Он получает доступ к фильтру, а затем ассоциирует фильтр и сводную таблицу. Наконец, он сохраняет рабочую книгу как [выходной файл Excel](add-pivot-connection-out.xlsx). 

## **Образец кода**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
