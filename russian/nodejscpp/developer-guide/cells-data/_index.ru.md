---
title: Управление данными файлов Excel
linktitle: Данные ячеек
type: docs
weight: 110
url: /ru/nodejs-cpp/view-and-edit-excel-data/
description: В этой статье описано, как просматривать и редактировать данные файлов Excel с помощью библиотеки Aspose.Cells для Node.js через C++.
keywords: Aspose.Cells Node.js через C++, управление данными Excel файла, добавление данных в Excel, получение данных из Excel, как повысить эффективность добавления данных, управление ячейками, обновление данных, получение данных ячеек, вставка данных в ячейки
---

{{% alert color="primary" %}}

В статье [Доступ к ячейкам листа](/cells/ru/nodejs-cpp/accessing-cells-of-a-worksheet/) обсуждаются основные подходы к доступу к ячейкам листа. В этой статье используется один из этих методов для добавления различных типов данных в ячейки.

{{% /alert %}}

## **Как добавить данные в ячейки**

Aspose.Cells for Node.js via C++ предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получать доступ к каждому листу Excel файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) представляет объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells позволяет разработчикам добавлять данные в ячейки листов, вызывая метод класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-). Предоставляются перегруженные версии метода [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-), которые позволяют добавлять различные виды данных в ячейки. Используя эти перегруженные версии метода [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-), можно добавлять в ячейку значения типа Boolean, строка, двойное, целое или дата/время.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Как улучшить эффективность**

Если вы используете метод [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) для вставки большого объема данных в лист, рекомендуется добавлять значения сначала по строкам, затем по столбцам. Такой подход значительно повышает эффективность ваших приложений.

## **Как извлечь данные из ячеек**

Aspose.Cells for Node.js via C++ предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получать доступ к листам файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент в [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) — объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Класс [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) содержит несколько свойств, позволяющих получать значения из ячеек в зависимости от их типа данных. Эти свойства включают:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): возвращает строковое значение ячейки.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): возвращает двойное значение ячейки.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): возвращает логическое значение ячейки.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): возвращает значение даты/времени ячейки.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): возвращает значение с плавающей точкой ячейки.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): возвращает целочисленное значение ячейки.

Если поле не заполнено, ячейки с [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) или [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) вызывают исключение.

Тип данных, содержащийся в ячейке, также можно проверить, используя метод [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). На самом деле, метод [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) основан на перечислении [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype), предопределённые значения которого приведены ниже:

|**Типы Значений Ячеек**|**Описание**|
| :- | :- |
|IsBool|Указывает, что значение ячейки является логическим.|
|IsDateTime|Указывает, что значение ячейки является дата/время.|
|IsNull|Представляет пустую ячейку.|
|IsNumeric|Указывает, что значение ячейки является числовым.|
|IsString|Указывает, что значение ячейки является строкой.|
|IsUnknown|Указывает, что значение ячейки неизвестно.|

Вы также можете использовать вышеперечисленные предопределенные типы значений ячейки для сравнения с типом данных, присутствующим в каждой ячейке.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Работая с листами, пользователи могут добавлять в ячейки различные типы данных. Эти типы могут включать логические значения, целые числа, числа с плавающей точкой, текст или значения даты/времени. С Aspose.Cells вы можете получать соответствующие значения из ячеек в зависимости от их типа данных.

{{% /alert %}}

## **Продвинутые темы**
- [Доступ к ячейкам листа](/cells/ru/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Преобразование текстовых числовых данных в число](/cells/ru/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Создание итогов](/cells/ru/nodejs-cpp/creating-subtotals/)
- [Фильтрация данных](/cells/ru/nodejs-cpp/data-filtering/)
- [Сортировка данных](/cells/ru/nodejs-cpp/sort-data-of-excel/)
- [Валидация данных](/cells/ru/nodejs-cpp/data-validation/)
- [Поиск или поиск данных](/cells/ru/nodejs-cpp/find-or-search-data/)
- [Получение строкового значения ячейки с или без форматирования](/cells/ru/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Добавление HTML-форматированного текста в ячейку](/cells/ru/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Вставка гиперссылок в Excel или OpenOffice](/cells/ru/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Как и где использовать перечислители](/cells/ru/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Измерение ширины и высоты значения ячейки в пикселях](/cells/ru/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Чтение значений ячеек в нескольких потоках одновременно](/cells/ru/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Преобразование между именем ячейки и индексом строки/столбца](/cells/ru/nodejs-cpp/names-and-indices/)
- [Сначала заполняется строка, а затем столбец.](/cells/ru/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Сохранить префикс одинарной кавычки значения ячейки или диапазона](/cells/ru/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Доступ и обновление частей Rich Text ячейки](/cells/ru/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
