---
title: Управление данными файлов Excel
linktitle: Данные ячеек
type: docs
weight: 110
url: /ru/python-net/view-and-edit-excel-data/
description: В этой статье описано, как просматривать и редактировать данные файлов Excel с помощью библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Excel для Python, Aspose.Cells для Python Управление данными файлов Excel, добавление данных в файл Excel с помощью Python, извлечение данных из файла Excel с помощью Python, Как улучшить эффективность добавления данных в Python, управление данными ячеек Python, обновление данных ячеек Python, получение данных ячеек Python, вставка данных ячеек Python.
---

{{% alert color="primary" %}}

В статье [Доступ к ячейкам листа](/cells/ru/python-net/accessing-cells-of-a-worksheet/) мы обсудили основные подходы к доступу к ячейкам на листе. В этой статье используется один из этих подходов для добавления различных типов данных в ячейки.

{{% /alert %}}

## **Как добавить данные в ячейки**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), позволяющую получить доступ к каждому листу Excel-файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Каждый элемент в коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells для Python via .NET позволяет разработчикам добавлять данные в ячейки на листах, вызывая метод [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) класса [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool). Aspose.Cells для Python via .NET предоставляет перегруженные версии метода [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int), которые позволяют разработчикам добавлять различные виды данных в ячейки. С использованием этих перегруженных версий метода [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) возможно добавить булевое, строковое, вещественное, целочисленное или дату/время и т. д. значения в ячейку.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Как улучшить эффективность**

Если вы используете метод [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) для вставки большого количества данных на листе, вам следует добавлять значения в ячейки сначала по строкам, а затем по столбцам. Такой подход значительно улучшает эффективность ваших приложений.

## **Как извлечь данные из ячеек**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), позволяющую получить доступ к листам в файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Каждый элемент в коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Класс [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) предоставляет несколько свойств, позволяющих разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): возвращает строковое значение ячейки.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): возвращает числовое значение ячейки.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): возвращает логическое значение ячейки.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): возвращает дату/время значения ячейки.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): возвращает дробное значение ячейки.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): возвращает целочисленное значение ячейки.

Когда поле не заполнено, ячейки со значением [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) или [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) возбуждают исключение.

Тип данных, содержащихся в ячейке, также можно проверить, используя свойство класса [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Фактически, свойство класса [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) основано на перечислении [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype), чьи предопределенные значения перечислены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|IS_BOOL|Указывает, что значение ячейки логическое.|
|IS_DATE_TIME|Указывает, что значение ячейки является датой/временем.|
|IS_NULL|Представляет пустую ячейку.|
|IS_NUMERIC|Указывает, что значение ячейки является числовым.|
|IS_STRING|Указывает, что значение ячейки является строкой.|
|IS_ERROR|Указывает, что значение ячейки является значением ошибки.|
|IS_UNKNOWN|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать вышеперечисленные предопределенные типы значений ячейки для сравнения с типом данных, присутствующим в каждой ячейке.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

При работе с рабочими листами пользователи могут добавлять различные типы данных в ячейки. Эти типы данных могут включать логические, целые, с плавающей точкой, текстовые или даты/время значения. С Aspose.Cells для Python via .NET, вы можете получить соответствующие значения из ячеек в соответствии с их типами данных.

{{% /alert %}}

## **Продвинутые темы**
- [Доступ к ячейкам листа](/cells/ru/python-net/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/python-net/convert-text-numeric-data-to-number/)
- [Создание итогов](/cells/ru/python-net/creating-subtotals/)
- [Фильтрация данных](/cells/ru/python-net/data-filtering/)
- [Сортировка данных](/cells/ru/python-net/sort-data-of-excel/)
- [Валидация данных](/cells/ru/python-net/data-validation/)
- [Получение строкового значения ячейки с или без форматирования](/cells/ru/python-net/get-cell-string-value-with-format-strategy/)
- [Добавление HTML-форматированного текста в ячейку](/cells/ru/python-net/adding-html-rich-text-inside-the-cell/)
- [Поиск или поиск данных](/cells/ru/python-net/find-or-search-data/)
- [Вставка гиперссылок в Excel или OpenOffice](/cells/ru/python-net/insert-hyperlinks-to-excel/)
- [Измерение ширины и высоты значения ячейки в пикселях](/cells/ru/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/python-net/names-and-indices/)
- [Сначала заполняется строка, а затем столбец.](/cells/ru/python-net/populate-data-first-by-row-then-by-column/)
- [Сохранить префикс одинарной кавычки значения ячейки или диапазона](/cells/ru/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей Rich Text ячейки](/cells/ru/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
