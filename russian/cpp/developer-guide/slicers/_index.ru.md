---
title: Вставка среза с помощью C++
linktitle: Фильтры
type: docs
weight: 170
url: /ru/cpp/create-slicer/
description: Управление срезами Excel файлов с помощью Aspose.Cells в C++
---

## **Возможные сценарии использования**

Срез используется для быстрого фильтрации данных. Он может использоваться для фильтрации данных как в таблице, так и в сводной таблице. Microsoft Excel позволяет создавать срез, выделяя таблицу или сводную таблицу и щелкая *Insert > Slicer*. Aspose.Cells также позволяет создавать срез с помощью метода [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/)

## **Создать нарезчик для сводной таблицы**

Пожалуйста, ознакомьтесь со следующим образцовым кодом. Он загружает [образец Excel-файла](67338470.xlsx), который содержит сводную таблицу. Затем создается срезка на основе первого базового сводного поля. Наконец, рабочая книга сохраняется в формате [XLSX](67338471.xlsx) и [XLSB](67338472.xlsb). Ниже показана срезка, созданная Aspose.Cells в выходном файле Excel.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Создать нарезчик для таблицы Excel**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца. Наконец, он сохраняет книгу в формате [output XLSX](outputCreateSlicerToExcelTable.xlsx).

### **Образец кода**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Дополнительные темы**
- [Изменить свойства фильтра](/cells/ru/cpp/change-slicer-properties/)
- [Нарисуйте фильтр при рендеринге Excel в PDF](/cells/ru/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [Форматирование фильтра](/cells/ru/cpp/formatting-slicer/)
- [Удаление срезки](/cells/ru/cpp/removing-slicer/)
- [Рендеринг срезки](/cells/ru/cpp/rendering-slicer/)
- [Обновление среза](/cells/ru/cpp/updating-slicer/)
