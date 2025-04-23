---
title: Управление данными файлов Excel
linktitle: Данные ячеек
type: docs
weight: 110
url: /ru/net/view-and-edit-excel-data/
description: Эта статья описывает, как просматривать и редактировать данные файлов Excel с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells C# Управление данными файла Excel, добавление данных в файл Excel, получение данных из файла Excel, Как улучшить эффективность добавления данных, управление данными ячеек, обновление данных ячеек, получение данных ячеек, вставка данных ячеек
---

{{% alert color="primary" %}}

При [Доступ к Ячейкам Рабочего Листа](/cells/ru/net/accessing-cells-of-a-worksheet/), мы обсудили основные методы доступа к ячейкам в рабочем листе. В этой статье используется один из этих методов для добавления различных типов данных в ячейки.

{{% /alert %}}

## **Как добавить данные в ячейки**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells позволяет разработчикам добавлять данные в ячейки на рабочих листах, вызывая метод [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Aspose.Cells предоставляет перегруженные версии метода [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index), которые позволяют добавлять различные типы данных в ячейки. Используя эти перегруженные версии метода [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index), можно добавить логические, строковые, числовые и даты/время и т. д. значения в ячейку.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Как улучшить эффективность**

Если вы используете метод [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) для вставки большого количества данных на листе, вам следует добавлять значения в ячейки сначала по строкам, а затем по столбцам. Такой подход значительно улучшает эффективность ваших приложений.

## **Как извлечь данные из ячеек**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к рабочим листам в файле. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Класс [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) предоставляет несколько свойств, позволяющих разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): возвращает строковое значение ячейки.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): возвращает числовое значение ячейки.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): возвращает логическое значение ячейки.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): возвращает дату/время значения ячейки.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): возвращает дробное значение ячейки.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): возвращает целочисленное значение ячейки.

Когда поле не заполнено, ячейки со значением [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) или [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) возбуждают исключение.

Тип данных, содержащихся в ячейке, также можно проверить, используя свойство класса [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Фактически, свойство класса [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) основано на перечислении [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype), чьи предопределенные значения перечислены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|IsBool|Указывает, что значение ячейки является логическим.|
|IsDateTime|Указывает, что значение ячейки является дата/время.|
|IsNull|Представляет пустую ячейку.|
|IsNumeric|Указывает, что значение ячейки является числовым.|
|IsString|Указывает, что значение ячейки является строкой.|
|IsUnknown|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать вышеперечисленные предопределенные типы значений ячейки для сравнения с типом данных, присутствующим в каждой ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

При работе с рабочими листами пользователи могут добавлять разные типы данных в ячейки. Эти типы данных могут включать логические, целочисленные, числа с плавающей запятой, текст или значения даты/времени. С помощью Aspose.Cells вы можете получить соответствующие значения из ячеек в соответствии с их типами данных.

{{% /alert %}}

## **Продвинутые темы**
- [Доступ к ячейкам листа](/cells/ru/net/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/net/convert-text-numeric-data-to-number/)
- [Создание итогов](/cells/ru/net/creating-subtotals/)
- [Фильтрация данных](/cells/ru/net/data-filtering/)
- [Сортировка данных](/cells/ru/net/sort-data-of-excel/)
- [Валидация данных](/cells/ru/net/data-validation/)
- [Экспорт данных из рабочего листа](/cells/ru/net/export-data-from-worksheet/)
- [Поиск или поиск данных](/cells/ru/net/find-or-search-data/)
- [Получение строкового значения ячейки с или без форматирования](/cells/ru/net/get-cell-string-value-with-and-without-formatting/)
- [Добавление HTML-форматированного текста в ячейку](/cells/ru/net/adding-html-rich-text-inside-the-cell/)
- [Вставка гиперссылок в Excel или OpenOffice](/cells/ru/net/insert-hyperlinks-to-excel/)
- [Импорт данных в рабочий лист](/cells/ru/net/import-data-into-worksheet/)
- [Как и где использовать перечислители](/cells/ru/net/how-and-where-to-use-enumerators/)
- [Измерение ширины и высоты значения ячейки в пикселях](/cells/ru/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Чтение значений ячеек в нескольких потоках одновременно](/cells/ru/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/net/names-and-indices/)
- [Сначала заполняется строка, а затем столбец.](/cells/ru/net/populate-data-first-by-row-then-by-column/)
- [Сохранить префикс одинарной кавычки значения ячейки или диапазона](/cells/ru/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей Rich Text ячейки](/cells/ru/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
