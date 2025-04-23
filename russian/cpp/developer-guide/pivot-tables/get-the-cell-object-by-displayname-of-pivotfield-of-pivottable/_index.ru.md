---
title: Получить объект ячейки по DisplayName поле PivotTable с помощью C++
linktitle: Получить объект ячейки по DisplayName поле PivotTable
type: docs
weight: 70
url: /ru/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Узнайте, как получить объект ячейки по отображаемому имени поля сводной таблицы и применить форматирование с использованием Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/), который можно использовать для доступа к объекту ячейки по отображаемому имени поля сводной таблицы. Этот метод полезен, когда нужно выделить или отформатировать заголовок поля сводной таблицы. Эта статья объясняет, как получить объект ячейки по отображаемому имени поля данных и применить к нему форматирование.

{{% /alert %}}

## **Получить объект ячейки по DisplayName поле PivotTable**

Следующий код обращается к первой сводной таблице на листе и затем извлекает ячейку по отображаемому имени второго поля данных этой таблицы. Затем он изменяет цвет заливки и цвет шрифта на светло-голубой и черный соответственно. Ниже приведены скриншоты, показывающие, как выглядит сводная таблица до и после выполнения кода.

|**СводнаяТаблица - До**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**СводнаяТаблица - После**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
