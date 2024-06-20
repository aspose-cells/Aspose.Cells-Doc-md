---
title: Преобразование CSV, TSV и TXT в Excel
type: docs
weight: 50
url: /ru/java/convert-csv-tsv-and-txt-to-excel/
---

## **Открытие файлов CSV**

Файлы с разделенными запятыми (CSV) содержат записи, значения которых разделены или отделены запятыми. В файлах CSV данные хранятся в табличном формате, поля разделены запятой и заключены в кавычки. Если значение поля содержит символ двойной кавычки, он экранируется двойной парой кавычек. Вы также можете использовать Microsoft Excel для экспорта данных вашей таблицы в файл CSV.

Для открытия CSV-файлов используйте класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выберите значение [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), предопределенное в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Открытие файлов CSV и замена недопустимых символов**

В Excel, при открытии CSV-файла с особыми символами, символы автоматически заменяются. То же самое делает API Aspose.Cells, как показано в приведенном ниже примере кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Открытие файлов CSV с использованием предпочтительного парсера**

Не всегда необходимо использовать настройки анализатора по умолчанию для открытия CSV-файлов. Иногда импорт CSV-файла не создает ожидаемый вывод, например, формат даты не соответствует ожиданиям или пустые поля обрабатываются по-разному. Для этой цели доступен [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers), чтобы предоставить собственный предпочтительный анализатор для разбора различных типов данных в соответствии с требованиями. Приведенный ниже образец кода демонстрирует использование предпочтительного анализатора.  

Исходный файл и выходные файлы для примера можно скачать по следующим ссылкам для тестирования этой функции.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Открытие файлов TSV (с разделителями табуляции)**

Файлы с разделителями табуляции содержат данные электронных таблиц, но без какого-либо форматирования. Данные располагаются в строках и столбцах, подобно таблицам и электронным таблицам. Кратко говоря, файл с разделителями табуляции представляет собой особый тип обычного текстового файла, в котором между каждым столбцом стоит табуляция.

Для открытия файлов с разделением табуляцией разработчики должны использовать класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выбрать значение [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), предопределенное в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Продвинутые темы**
- [Загрузить или импортировать файл CSV с формулами](/cells/ru/java/load-or-import-csv-file-with-formulas/)
- [Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

