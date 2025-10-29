---
title: Управление данными Excel файлов с помощью Golang через C++
linktitle: Данные ячеек
type: docs
weight: 110
url: /ru/go-cpp/view-and-edit-excel-data/
description: В этой статье описывается, как просматривать и редактировать данные Excel файлов с библиотекой Aspose.Cells, используя C++.
keywords: Aspose.Cells C++ Управление данными Excel файла, добавление данных в Excel файл, получение данных из Excel файла, как повысить эффективность добавления данных, управление данными ячеек, обновление данных ячеек, получение данных ячеек, вставка данных ячеек
---

{{% alert color="primary" %}}

В статье [Доступ к ячейкам рабочего листа](/cells/ru/cpp/accessing-cells-of-a-worksheet/) мы обсудили основные методы доступа к ячейкам в рабочем листе. В этой статье используется один из этих методов для добавления различных типов данных в ячейки.

{{% /alert %}}

## **Как добавить данные в ячейки**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells позволяет разработчикам добавлять данные в ячейки на рабочих листах, вызывая метод [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) класса [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). Aspose.Cells предоставляет перегруженные версии метода [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/), которые позволяют добавлять различные типы данных в ячейки. Используя эти перегруженные версии метода [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/), можно добавить логические, строковые, числовые и даты/время и т. д. значения в ячейку.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData.go" >}}
## **Как улучшить эффективность**

Если вы используете метод [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue_bool/) для вставки большого количества данных на листе, вам следует добавлять значения в ячейки сначала по строкам, а затем по столбцам. Такой подход значительно улучшает эффективность ваших приложений.

## **Как извлечь данные из ячеек**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к рабочим листам в файле. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Класс [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) предоставляет несколько свойств, позволяющих разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают:

- [**StringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/): возвращает строковое значение ячейки.
- [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/): возвращает числовое значение ячейки.
- [**BoolValue**](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/): возвращает логическое значение ячейки.
- [**DateTimeValue**](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/): возвращает дату/время значения ячейки.
- [**FloatValue**](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/): возвращает дробное значение ячейки.
- [**IntValue**](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/): возвращает целочисленное значение ячейки.

Когда поле не заполнено, ячейки со значением [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/) или [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) возбуждают исключение.

Тип данных, содержащихся в ячейке, также можно проверить, используя свойство класса [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). Фактически, свойство класса [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) основано на перечислении [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/), чьи предопределенные значения перечислены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|IsBool|Указывает, что значение ячейки является логическим.|
|IsDateTime|Указывает, что значение ячейки является дата/время.|
|IsNull|Представляет пустую ячейку.|
|IsNumeric|Указывает, что значение ячейки является числовым.|
|IsString|Указывает, что значение ячейки является строкой.|
|IsUnknown|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать вышеперечисленные предопределенные типы значений ячейки для сравнения с типом данных, присутствующим в каждой ячейке.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData-1.go" >}}
{{% alert color="primary" %}}

При работе с рабочими листами пользователи могут добавлять разные типы данных в ячейки. Эти типы данных могут включать логические, целочисленные, числа с плавающей запятой, текст или значения даты/времени. С помощью Aspose.Cells вы можете получить соответствующие значения из ячеек в соответствии с их типами данных.

{{% /alert %}}

## **Продвинутые темы**
- [Доступ к ячейкам листа](/cells/ru/cpp/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/cpp/convert-text-numeric-data-to-number/)
- [Создание итогов](/cells/ru/cpp/creating-subtotals/)
- [Фильтрация данных](/cells/ru/cpp/data-filtering/)
- [Сортировка данных](/cells/ru/cpp/sort-data-of-excel/)
- [Валидация данных](/cells/ru/cpp/data-validation/)
- [Поиск или поиск данных](/cells/ru/cpp/find-or-search-data/)
- [Получение строкового значения ячейки с или без форматирования](/cells/ru/cpp/get-cell-string-value-with-and-without-formatting/)
- [Добавление HTML-форматированного текста в ячейку](/cells/ru/cpp/adding-html-rich-text-inside-the-cell/)
- [Вставка гиперссылок в Excel или OpenOffice](/cells/ru/cpp/insert-hyperlinks-to-excel/)
- [Как и где использовать перечислители](/cells/ru/cpp/how-and-where-to-use-enumerators/)
- [Измерение ширины и высоты значения ячейки в пикселях](/cells/ru/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Чтение значений ячеек в нескольких потоках одновременно](/cells/ru/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/cpp/names-and-indices/)
- [Сначала заполняется строка, а затем столбец.](/cells/ru/cpp/populate-data-first-by-row-then-by-column/)
- [Сохранить префикс одинарной кавычки значения ячейки или диапазона](/cells/ru/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей Rich Text ячейки](/cells/ru/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
