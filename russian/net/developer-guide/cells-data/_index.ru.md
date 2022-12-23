---
title: Управление данными файлов Excel.
linktitle: Cells Данные
type: docs
weight: 110
url: /ru/net/view-and-edit-excel-data/
description: В этой статье описывается, как просматривать и редактировать данные файлов Excel с библиотекой Aspose.Cells.
---
{{% alert color="primary" %}}

 В[Доступ к Cells рабочего листа](/cells/ru/net/accessing-cells-of-a-worksheet/), мы обсудили основные подходы к доступу к ячейкам на листе. В этой статье используется один из этих подходов для добавления различных типов данных в ячейки.

{{% /alert %}}

## **Добавление данных в Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

Aspose.Cells позволяет разработчикам добавлять данные в ячейки на листах, вызывая[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс'[**путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) метод. Aspose.Cells предоставляет перегруженные версии[**путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) метод, который позволяет разработчикам добавлять в ячейки различные типы данных. Используя эти перегруженные версии[**путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)метод, в ячейку можно добавить логические, строковые, двойные, целочисленные значения, дату/время и т. д.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Повышение эффективности**

 Если вы используете[**путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Чтобы поместить большой объем данных на рабочий лист, вы должны добавить значения в ячейки, сначала по строкам, а затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.

## **Получение данных с Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая позволяет получить доступ к рабочим листам в файле. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Класс предоставляет несколько свойств, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают в себя:

- [**Строковое значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): возвращает строковое значение ячейки.
- [**Двойное значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): возвращает двойное значение ячейки.
- [**логическое значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): возвращает логическое значение ячейки.
- [**ДатаВремяЗначение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): возвращает значение даты/времени ячейки.
- [**Плавающее значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): возвращает значение с плавающей запятой ячейки.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)возвращает целочисленное значение ячейки.

 Когда поле не заполнено, ячейки с[**Двойное значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) или же[**Плавающее значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)выдает исключение.

 Тип данных, содержащихся в ячейке, также можно проверить с помощью[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс'[**Тип**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) имущество. Фактически,[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) учебный класс'[**Тип**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) имущество основано на[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)перечисление, предопределенные значения которого перечислены ниже:

|**Cell Типы значений**|**Описание**|
|:- |:- |
|IsBool|Указывает, что значение ячейки является логическим.|
|Исдатетиме|Указывает, что значением ячейки является дата/время.|
|Нулевой|Представляет собой пустую ячейку.|
|числовой|Указывает, что значение ячейки является числовым.|
|Исстринг|Указывает, что значение ячейки является строкой.|
|Неизвестно|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать указанные выше предопределенные типы значений ячеек для сравнения с типом данных, присутствующих в каждой ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

При работе с рабочими листами пользователи могут добавлять в ячейки различные типы данных. Эти типы данных могут включать логические значения, целые числа, значения с плавающей запятой, текст или значения даты/времени. С помощью Aspose.Cells вы можете получить соответствующие значения из ячеек в соответствии с их типами данных.

{{% /alert %}}

## **Предварительные темы**
- [Доступ к Cells рабочего листа](/cells/ru/net/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/net/convert-text-numeric-data-to-number/)
- [Создание промежуточных итогов](/cells/ru/net/creating-subtotals/)
- [Фильтрация данных](/cells/ru/net/data-filtering/)
- [Сортировка данных](/cells/ru/net/sort-data-of-excel/)
- [Валидация данных](/cells/ru/net/data-validation/)
- [Экспорт данных из рабочего листа](/cells/ru/net/export-data-from-worksheet/)
- [Поиск или поиск данных](/cells/ru/net/find-or-search-data/)
- [Получить строковое значение Cell с форматированием и без него](/cells/ru/net/get-cell-string-value-with-and-without-formatting/)
- [Добавление HTML Rich Text внутри Cell](/cells/ru/net/adding-html-rich-text-inside-the-cell/)
- [Вставьте гиперссылки в Excel или OpenOffice](/cells/ru/net/insert-hyperlinks-to-excel/)
- [Импорт данных в рабочий лист](/cells/ru/net/import-data-into-worksheet/)
- [Как и где использовать перечислители](/cells/ru/net/how-and-where-to-use-enumerators/)
- [Измерьте ширину и высоту значения Cell в пикселях.](/cells/ru/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Одновременное чтение значений Cell в нескольких потоках](/cells/ru/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/net/names-and-indices/)
- [Заполнить данные сначала по строке, а затем по столбцу](/cells/ru/net/populate-data-first-by-row-then-by-column/)
- [Сохранить префикс одиночной кавычки для значения или диапазона Cell](/cells/ru/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей форматированного текста Cell](/cells/ru/net/access-and-update-the-portions-of-rich-text-of-cell/)



