---
title: Как управлять датами и временем
type: docs
weight: 600
url: /ru/net/how-to-manage-dates-and-times/
description: Узнайте, как управлять датами и временем с помощью Aspose.Cells for .NET API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Как хранить дату и время в Excel**
Даты и время хранятся в ячейках в виде чисел. Таким образом, значения ячеек, содержащих даты и время, имеют числовой тип. Число, определяющее дату и время, состоит из компонентов даты (целая часть) и времени (дробная часть). Свойство Cell.DoubleValue возвращает это число.

##  **Как отображать дату и время в Aspose.Cells**
Чтобы отобразить число в виде даты и времени, примените к ячейке требуемый формат даты и времени с помощью[Стиль.Номер](https://reference.aspose.com/cells/net/aspose.cells/style/number/) или[Стиль.Пользовательский]() свойство. Свойство CellValue.DateTimeValue возвращает объект DateTime, который определяет дату и время, представленные числом, содержащимся в ячейке.
<br>
<image src="1.png" width="70%" />

##  **Как переключить две системы дат в Aspose.Cells**
MS-Excel хранит даты в виде чисел, которые называются серийными значениями. Порядковое значение — это целое число, которое представляет собой количество дней, прошедших с первого дня в системе дат. Excel поддерживает следующие системы дат для серийных значений:

1. Система дат 1900 года. Первая дата — 1 января 1900 года, ее порядковый номер — 1. Последняя дата — 31 декабря 9999 года, ее порядковый номер — 2 958 465. Эта система дат используется в книге по умолчанию.
1.  Система дат 1904 года. Первая дата — 1 января 1904 года, ее серийное значение — 0. Последняя дата — 31 декабря 9999 года, ее серийное значение — 2 957 003. Чтобы использовать эту систему дат в книге, установите[Рабочая книга.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) свойство истинно.


Этот пример показывает, что серийные значения, хранящиеся на одну и ту же дату в разных системах дат, различаются.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Результат вывода:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Как установить значение DateTime в Aspose.Cells**
В этом примере задается значение DateTime в ячейках A1 и A2, задается пользовательский формат A1 и числовой формат A2, а затем выводятся типы значений.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Результат вывода:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Как получить значение DateTime в Aspose.Cells**
В этом примере задается значение DateTime в ячейках A1 и A2, задается пользовательский формат A1 и числовой формат A2, проверяются типы значений двух ячеек, а затем выводятся значение DateTime и форматированная строка.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

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
