---
title: Фильтр сводной таблицы с помощью C++
linktitle: Фильтр сводной таблицы
type: docs
weight: 130
url: /ru/cpp/add-or-clear-pivot-filter/
description: Узнайте, как добавить фильтр в сводную таблицу с использованием Aspose.Cells и C++.
keywords: Добавление фильтра в сводную таблицу без офиса 2013, офиса 2016, офиса 2019 и офиса 365.
---

## **Возможные сценарии использования**
При создании сводной таблицы с известными данными и необходимости фильтрации, вам нужно изучить и использовать фильтр. Он поможет эффективно отфильтровать нужные данные. Используя API Aspose.Cells, вы можете добавлять и очищать фильтры по значениям полей в сводных таблицах. 

## **Добавить фильтр в сводную таблицу в Excel**
Добавьте фильтр в сводную таблицу в Excel, выполните следующие шаги:

1. Выберите сводную таблицу, которую вы хотите очистить от фильтра. 
2. Нажмите на стрелку раскрывающегося меню для фильтра, который нужно добавить в сводную таблицу.
3. Выберите "Топ-10" из выпадающего меню.
<br>
<img src="3.png" width=80% />
4. Установите режим отображения и количество фильтров.
<br>
<img src="4.png" width=80% />

## **Добавить фильтр в сводную таблицу**
Пожалуйста, ознакомьтесь с следующим образцовым кодом. Он устанавливает данные и создает сводную таблицу на их основе. Затем добавьте фильтр на поля строк сводной таблицы. Наконец, сохраните книгу в формате [output XLSX](filterout.xlsx). После выполнения примера кода книга Excel с фильтром top10 добавляется в рабочий лист.

### **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Очистить фильтр в сводной таблице в Excel**
Очистить фильтр в сводной таблице Excel, следуйте этим шагам:

1. Выберите сводную таблицу, которую вы хотите очистить от фильтра. 
2. Нажмите на стрелку-раскрывающееся меню для фильтра, который вы хотите очистить в сводной таблице.
3. Выберите "Очистить фильтр" в выпадающем меню.
<br>
<img src="1.png" width=80% />
4. Если вы хотите очистить все фильтры из сводной таблицы, вы также можете щелкнуть кнопку "Очистить фильтры" на вкладке Анализ сводной таблицы на ленте в Excel.
<br>
<img src="2.png" width=80% />

## **Очистить фильтр в сводной таблице**
Очистить фильтр в сводной таблице с использованием Aspose.Cells. Пожалуйста, ознакомьтесь с приведенным образцом кода. 
1. Задайте данные и создайте сводную таблицу на их основе. 
2. Добавьте фильтр на строковое поле сводной таблицы. 
3. Сохраните книгу в формате [output XLSX](out_add.xlsx). После выполнения примера кода, в рабочую книгу будет добавлена сводная таблица с фильтром top10. 
4. Очистите фильтр в конкретном поле сводной таблицы. После выполнения кода для очистки фильтра, фильтр в конкретном поле сводной таблицы будет очищен. Пожалуйста, проверьте [output XLSX](out_delete.xlsx).

### **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
