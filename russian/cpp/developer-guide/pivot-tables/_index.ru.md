---
title: Создание сводной таблицы
linktitle: Создание сводной таблицы
description: Создание и форматирование сводных таблиц с помощью Aspose.Cells for C++.
keywords: Создание сводной таблицы, вставка сводной таблицы, форматирование сводной таблицы.
type: docs
weight: 160
url: /ru/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный отчет с итоговыми данными: она преобразует большой объем необработанных данных, расположенных построчно, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут агрегироваться в качестве значений; сводная таблица выполняет группировку и вычисления:
- **Подведение итогов** — общий объем продаж для каждого продукта, региона или квартала вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в перекрестный отчет, в котором тенденции видны с первого взгляда.
- **Детализация** — дважды щелкните по любому итоговому значению, чтобы просмотреть исходные строки, на основе которых оно рассчитано.
- **Обновление** — при изменении исходных данных одно обновление пересчитывает весь отчет.
Типичные сценарии применения — панели мониторинга продаж, анализ структуры расходов и анализ запасов — подходят для любого вопроса вида «как эти числа распределяются по категориям и временным периодам?». В Aspose.Cells for C++ сводная таблица создается с помощью метода [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) рабочего листа. После создания сводной таблицы с ней можно работать с помощью класса [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/).

## **Создание сводной таблицы**
В приведенном ниже примере кода показано, как создать сводную таблицу и работать с ней. Ознакомьтесь с [выходным файлом Excel](23167010.xlsx), созданным с помощью этого кода, и со снимком экрана, на котором этот файл показан в Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **Пример кода**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Создать новую книгу и получить первый лист
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Записать исходные данные: продажи по виду спорта и кварталу
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // Добавить сводную таблицу в ячейку назначения E3 на основе A1:C8
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Назначить поля сводной таблицы: вид спорта — строки, квартал — столбцы, продажи — данные
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Сохранить книгу
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}