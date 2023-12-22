---
title: Управление данными файлов Excel
linktitle: Cells Данные
type: docs
weight: 110
url: /ru/net/view-and-edit-excel-data/
description: В этой статье описывается, как просматривать и редактировать данные файлов Excel с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

 В[Доступ к Cells рабочего листа](/cells/ru/net/accessing-cells-of-a-worksheet/)мы обсудили основные подходы к доступу к ячейкам на листе. В этой статье используется один из таких подходов для добавления в ячейки различных типов данных.

{{% /alert %}}

##  **Как добавить данные в номер Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

 Aspose.Cells позволяет разработчикам добавлять данные в ячейки на листах, вызывая[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт'[**Путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) метод. Aspose.Cells предоставляет перегруженные версии[**Путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) метод, который позволяет разработчикам добавлять в ячейки различные типы данных. Используя эти перегруженные версии[**Путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)В ячейку можно добавить логические, строковые, двойные, целочисленные значения, значения даты/времени и т. д.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **Как повысить эффективность**

 Если вы используете[**Путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Чтобы поместить большой объем данных на лист, вам следует добавлять значения в ячейки сначала по строкам, а затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.

##  **Как получить данные с номера Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к листам в файле. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Класс предоставляет несколько свойств, которые позволяют разработчикам извлекать значения из ячеек в соответствии с их типами данных. Эти свойства включают в себя:

- [**Строковое значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): возвращает строковое значение ячейки.
- [**Двойное значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): возвращает двойное значение ячейки.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): возвращает логическое значение ячейки.
- [**ДатаВремяЗначение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): возвращает значение даты/времени ячейки.
- [**Плавающее значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): возвращает плавающее значение ячейки.
- [**Интвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): возвращает целочисленное значение ячейки.

 Если поле не заполнено, ячейки с[**Двойное значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) или[**Плавающее значение**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)выдает исключение.

 Тип данных, содержащихся в ячейке, также можно проверить с помощью[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт'[**Тип**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) свойство. Фактически,[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт'[**Тип**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) собственность основана на[**Тип ячейкиValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)перечисление, предварительно определенные значения которого перечислены ниже:

|**Cell Типы значений**|**Описание**|
| :- | :- |
|IsBool|Указывает, что значение ячейки является логическим.|
|Исдатевремя|Указывает, что значением ячейки является дата/время.|
|Нулевой|Представляет пустую ячейку.|
|IsNumeric|Указывает, что значение ячейки является числовым.|
|IsString|Указывает, что значение ячейки является строкой.|
|Неизвестно|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать предварительно определенные типы значений ячеек, указанные выше, для сравнения с типом данных, присутствующих в каждой ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Работая над листами, пользователи могут добавлять в ячейки различные типы данных. Эти типы данных могут включать логические значения, целые числа, значения с плавающей запятой, текст или значения даты/времени. С помощью Aspose.Cells вы можете получить соответствующие значения из ячеек в соответствии с их типами данных.

{{% /alert %}}

##  **Предварительные темы**
- [Доступ к Cells рабочего листа](/cells/ru/net/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/net/convert-text-numeric-data-to-number/)
- [Создание промежуточных итогов](/cells/ru/net/creating-subtotals/)
- [Фильтрация данных](/cells/ru/net/data-filtering/)
- [Сортировка данных](/cells/ru/net/sort-data-of-excel/)
- [Валидация данных](/cells/ru/net/data-validation/)
- [Экспорт данных из листа](/cells/ru/net/export-data-from-worksheet/)
- [Найти или найти данные](/cells/ru/net/find-or-search-data/)
- [Получить строковое значение Cell с форматированием и без него](/cells/ru/net/get-cell-string-value-with-and-without-formatting/)
- [Добавление HTML форматированного текста внутри Cell](/cells/ru/net/adding-html-rich-text-inside-the-cell/)
- [Вставка гиперссылок в Excel или OpenOffice](/cells/ru/net/insert-hyperlinks-to-excel/)
- [Импортировать данные в рабочий лист](/cells/ru/net/import-data-into-worksheet/)
- [Как и где использовать перечислители](/cells/ru/net/how-and-where-to-use-enumerators/)
- [Измерьте ширину и высоту значения Cell в пикселях.](/cells/ru/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Чтение значений Cell в нескольких потоках одновременно](/cells/ru/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/net/names-and-indices/)
- [Заполнение данных сначала по строке, затем по столбцу](/cells/ru/net/populate-data-first-by-row-then-by-column/)
- [Сохранять префикс одиночной кавычки для значения или диапазона Cell.](/cells/ru/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей форматированного текста Cell](/cells/ru/net/access-and-update-the-portions-of-rich-text-of-cell/)



