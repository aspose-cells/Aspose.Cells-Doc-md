---
title: Добавить вычисляемое поле в сводную таблицу с помощью C++
linktitle: Добавление вычисляемого поля в сводной таблице
type: docs
weight: 130
url: /ru/cpp/add-calculated-field-in-pivot-table/
description: Как добавить вычисляемое поле в сводную таблицу с Aspose.Cells for C++.
keywords: Добавление вычисляемого поля в сводную таблицу.
---

## **Возможные сценарии использования**
Когда вы создаете сводную таблицу на основе известных данных, вы обнаруживаете, что данные в ней не соответствуют вашим требованиям. Вы хотите объединить эти исходные данные. Например, вам нужно сложить, вычесть, умножить и разделить исходные данные перед тем, как вы их захотите. В этом случае вам нужно создать вычисляемое поле и установить соответствующую формулу для вычислений. Затем выполнить некоторые статистические и другие операции с вычисляемым полем. 

## **Добавление вычисляемого поля в сводной таблице в Excel**
Чтобы добавить вычисляемое поле в сводную таблицу в Excel, выполните следующие шаги:

1. Выберите сводную таблицу, к которой вы хотите добавить вычисляемое поле. 
2. Перейдите на вкладку Analyze в контекстном меню сводной таблицы.
3. Нажмите на "Поля, элементы и наборы" и затем выберите "Вычисляемое поле" в выпадающем меню.
4. В поле "Имя" введите имя для вычисляемого поля.
5. В поле "Формула" введите формулу для выполнения расчета, используя соответствующие имена полей сводной таблицы и математические операторы. 
<br>
<img src="1.png" width=80% />
6. Нажмите "ОК", чтобы создать вычисляемое поле.
7. Новое вычисляемое поле появится в списке полей сводной таблицы в разделе 'Значения'.
8. Перетащите вычисляемое поле в раздел 'Значения' сводной таблицы, чтобы отобразить вычисленные значения.
<br>
<img src="2.png" width=80% />

## **Добавить вычисляемое поле в сводную таблицу с помощью C++**
Добавить расчетное поле в файл Excel с использованием Aspose.Cells. Пожалуйста, ознакомьтесь с следующим образцовым кодом. После выполнения примера кода книга Excel с добавленным расчетным полем сводной таблицы сохраняется в формате [output XLSX](out.xlsx).
1. Задайте исходные данные и создайте сводную таблицу. 
2. Создайте расчетное поле согласно существующему PivotField в сводной таблице.
3. Добавьте расчетное поле в область данных. 
4. Наконец, сохраните книгу в формате [output XLSX](out.xlsx). 

## **Образец кода**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get("B1");
    cell.PutValue(u"Count");

    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");

    cell = cells.Get("A3");
    cell.PutValue(u"Mango");

    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);

    cell = cells.Get("B3");
    cell.PutValue(3);

    cell = cells.Get("B4");
    cell.PutValue(6);

    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);

    cell = cells.Get("C3");
    cell.PutValue(20);

    cell = cells.Get("C4");
    cell.PutValue(30);

    cell = cells.Get("C5");
    cell.PutValue(60);

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to PivotTable and dragging it to data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
