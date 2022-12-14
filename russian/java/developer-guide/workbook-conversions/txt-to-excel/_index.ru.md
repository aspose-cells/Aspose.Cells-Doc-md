---
title: Преобразование CSV, TSV и TXT в Excel
type: docs
weight: 50
url: /ru/java/convert-csv-tsv-and-txt-to-excel/
---
## **Открытие CSV-файлов**

Файлы со значениями, разделенными запятыми (CSV), содержат записи, значения которых разделены запятыми. В файлах CSV данные хранятся в табличном формате, в котором поля разделены запятой и заключены в двойные кавычки. Если значение поля содержит символ двойной кавычки, оно экранируется парой символов двойной кавычки. Вы также можете использовать Microsoft Excel для экспорта данных электронной таблицы в файл CSV.

Чтобы открыть файлы CSV, используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс и выберите**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** значение, заданное в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

## **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Открытие файлов CSV и замена недопустимых символов**

В Excel при открытии файла CSV со специальными символами символы автоматически заменяются. То же самое делает Aspose.Cells API, что продемонстрировано в приведенном ниже примере кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Открытие файлов CSV с помощью предпочтительного парсера**

Это не всегда необходимо, чтобы использовать настройки парсера по умолчанию для открытия файлов CSV. Иногда импорт CSV-файла не приводит к ожидаемому результату, например формат даты не соответствует ожидаемому или пустые поля обрабатываются по-другому. Для этого**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**доступен для предоставления собственного предпочтительного синтаксического анализатора для анализа различных типов данных в соответствии с требованиями. Следующий пример кода демонстрирует использование предпочтительного синтаксического анализатора.

Образец исходного файла и выходные файлы можно загрузить по следующим ссылкам для тестирования этой функции.

[образецPreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Открытие файлов TSV (с разделителями табуляцией)**

Файлы с разделителями табуляцией содержат данные электронной таблицы, но без какого-либо форматирования. Данные располагаются в строках и столбцах, таких как таблицы и электронные таблицы. Вкратце, файл с разделителями табуляцией — это особый тип простого текстового файла с табуляцией между каждым столбцом в тексте.

Чтобы открыть файлы с разделителями табуляцией, разработчики должны использовать**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс и выберите**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** значение, заданное в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

## **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Предварительные темы**
- [Загрузить или импортировать файл CSV с формулами](/cells/ru/java/load-or-import-csv-file-with-formulas/)
- [Обрезать начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

