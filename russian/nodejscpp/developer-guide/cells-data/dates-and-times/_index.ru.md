---  
title: Как управлять датами и временем
type: docs  
weight: 600  
url: /ru/nodejs-cpp/how-to-manage-dates-and-times/  
description: Узнайте, как управлять датами и временем с помощью API Aspose.Cells for Node.js via C++.  
keywords: Как управлять датами и временем, Система дат 1900 года, Система дат 1904 года, Установка дат и времени, Получение дат и времени, Управление датами и временем, Хранение дат и времени в Excel, Отображение дат и времен в ячейках.  
---  

## **Как хранить даты и время в Excel**  
Даты и время хранятся в ячейках в виде чисел. Таким образом, значения ячеек, которые содержат даты и времена, имеют числовой тип. Число, которое указывает дату и время, состоит из компонентов даты (целая часть) и времени (дробная часть). Свойство Cell.DoubleValue возвращает это число.  

## **Как отображать даты и время в Aspose.Cells**  
Чтобы отображать число как дату и время, примените нужный формат даты и времени к ячейке через свойства [Style.getNumber()](https://reference.aspose.com/cells/nodejs-cpp/style/#getNumber--) или [Style.Custom]() . Свойство CellValue.DateTimeValue возвращает объект DateTime, который указывает дату и время, представляемые числом, содержащимся в ячейке.  
<br>  
<image src="1.png" width="70%" />  

## **Как переключить две системы дат в Aspose.Cells**  
MS-Excel хранит даты как числа, которые называются серийными значениями. Серийное значение - это целое число, которое представляет собой количество прошедших дней с первого дня в системе дат. Excel поддерживает следующие системы дат для серийных значений:  

1. Система дат 1900 года. Первая дата - 1 января 1900 года, а ее серийное значение - 1. Последняя дата - 31 декабря 9999 года, ее серийное значение - 2 958 465. Эта система дат используется в книге по умолчанию.  
1. Система дат 1904 года. Первая дата — 1 января 1904 года, её серийное значение равно 0. Последняя дата — 31 декабря 9999 года, её серийное значение равно 2 957 003. Для использования этой системы дат в рабочей книге установите свойство [WorkbookSettings.getDate1904()](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getDate1904--) в значение true.  

Этот пример показывает, что серийные значения, хранящиеся на одной дате в разных системах дат, различны.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SwitchTwoDateSystems.js" >}}


Результат вывода:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **Как установить значение DateTime в Aspose.Cells**  
Этот пример устанавливает значение DateTime в ячейке A1 и A2, устанавливает пользовательский формат для ячейки A1 и числовой формат для ячейки A2, а затем выводит типы значений.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SetDateTimeValue.js" >}}


Результат вывода:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **Как получить значение DateTime в Aspose.Cells**  
Этот пример устанавливает значение DateTime в ячейке A1 и A2, устанавливает пользовательский формат для ячейки A1 и числовой формат для ячейки A2, проверяет типы значений двух ячеек, а затем выводит значение DateTime и отформатированную строку.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-GetDateTimeValue.js" >}}


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

{{< app/cells/assistant language="nodejs-cpp" >}}
