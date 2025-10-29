---
title: Как управлять датами и временем с помощью C++
linktitle: Как управлять датами и временем
type: docs
weight: 600
url: /ru/cpp/how-to-manage-dates-and-times/
description: Узнайте, как управлять датами и временем с помощью API Aspose.Cells for C++.
keywords: Как управлять датами и временем, Система дат 1900 года, Система дат 1904 года, Установка дат и времени, Получение дат и времени, Управление датами и временем, Хранение дат и времени в Excel, Отображение дат и времен в ячейках.
---

## **Как хранить даты и время в Excel**
Даты и времена хранятся в ячейках как числа. Следовательно, значения ячеек, содержащих даты и время, являются числовыми. Число, указывающее дату и время, состоит из компонентов дата (целая часть) и время (дробная часть). Метод `Cell::GetDoubleValue()` возвращает это число.

## **Как отображать даты и время в Aspose.Cells**
Чтобы отображать число как дату и время, примените необходимый формат даты и времени к ячейке через методы `Style::SetNumber()` или `Style::SetCustom()`. Метод `Cell::GetDateTimeValue()` возвращает объект `DateTime`, который указывает дату и время, представленные числом, содержащимся в ячейке.
<br>
<image src="1.png" width="70%" />

## **Как переключить две системы дат в Aspose.Cells**
MS-Excel хранит даты как числа, которые называются серийными значениями. Серийное значение - это целое число, которое представляет собой количество прошедших дней с первого дня в системе дат. Excel поддерживает следующие системы дат для серийных значений:

1. Система дат 1900 года. Первая дата - 1 января 1900 года, а ее серийное значение - 1. Последняя дата - 31 декабря 9999 года, ее серийное значение - 2 958 465. Эта система дат используется в книге по умолчанию.
1. Система дат 1904. Первая дата — 1 января 1904 года, её сериализованное значение равно 0. Последняя дата — 31 декабря 9999 года, её сериализованное значение равно 2 957 003. Чтобы использовать эту систему дат в рабочей книге, установите свойство `Workbook::GetSettings()->SetDate1904(true)`.

Этот пример показывает, что серийные значения, хранящиеся на одной дате в разных системах дат, различны.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Результат вывода:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Как установить значение DateTime в Aspose.Cells**
Этот пример устанавливает значение `DateTime` в ячейки A1 и A2, задаёт пользовательский формат для A1 и числовой формат для A2, а затем выводит типы значений.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Результат вывода:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Как получить значение DateTime в Aspose.Cells**
Этот пример устанавливает значение `DateTime` в ячейки A1 и A2, задаёт пользовательский формат для A1 и числовой формат для A2, проверяет типы значений двух ячеек и выводит значение `DateTime` и отформатированную строку.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Результат вывода:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="cpp" >}}
