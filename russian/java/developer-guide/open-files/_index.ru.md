---
title: Открытие файлов с различными форматами
linktitle: Открытие файлов
type: docs
weight: 10
url: /ru/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Разработчики используют Aspose.Cells для открытия файлов для разных целей. Например, открыть файл для извлечения данных из него или использовать заранее определенный файл таблицы стилей для ускорения процесса разработки. Aspose.Cells позволяет разработчикам открывать различные типы исходных файлов. Эти исходные файлы могут быть отчетами Microsoft Excel, SpreadsheetML, файлами с разделенными запятыми (CSV), файлами с табуляцией (TSV) или файлами со значениями, разделенными табуляцией. В этой статье обсуждается открытие этих различных исходных файлов с помощью Aspose.Cells.

Если вам нужно знать все поддерживаемые форматы файлов, обратитесь к следующим страницам:
[Поддерживаемые форматы файлов](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Простые способы открытия файлов Excel**

### **Открытие через путь**

Для открытия файла Microsoft Excel с использованием пути файла, передайте путь файла в качестве параметра при создании экземпляра класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). В следующем образце кода демонстрируется открытие файла Excel с использованием пути файла.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Открытие через Поток**

Иногда файл Excel, который вы хотите открыть, хранится как поток. В этом случае, аналогично открытию файла с использованием пути файла, передайте поток в качестве параметра при создании экземпляра класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). В следующем образце кода демонстрируется открытие файла Excel с использованием потока.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Открытие файлов различных версий Microsoft Excel**

Пользователь может использовать класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) для указания формата файла Excel с использованием перечисления [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

Перечисление [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов**|**Описание**|
| :- | :- |
|Csv|Представляет файл CSV|
|Excel97To2003|Представляет файл Excel 97 - 2003|
|Xlsx|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX|
|Xlsm|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM|
|Xltx|Представляет файл шаблон Excel 2007/2010/2013/2016/2019 и Office 365 XLTX|
|Xltm|Представляет макрос-возможный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLTM|
|Xlsb|Представляет бинарный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB|
|SpreadsheetML|Представляет файл SpreadsheetML|
|Tsv|Представляет файл со значениями, разделенными знаком табуляции|
|TabDelimited|Представляет файл текста с табуляцией|
|Ods|Представляет файл ODS|
|Html|Представляет файл HTML|
|Mhtml|Представляет файл MHTML|

### **Открытие файлов Microsoft Excel 95/5.0**

Для открытия файлов Microsoft Excel 95, создайте экземпляр [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) с путем или потоком файла-шаблона. Образец файла для проверки кода можно загрузить по следующей ссылке:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Открытие файлов Microsoft Excel 97 или более поздних версий XLS**

Для открытия файлов XLS Microsoft Excel XLS 97 или более поздних версий, создайте экземпляр [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) с путем или потоком файла-шаблона. Или используйте метод [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выберите значение [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL-97-TO-2003) в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Открытие файлов Microsoft Excel 2007 или более поздних версий XLSX**

Для открытия файлов XLSX Microsoft Excel 2007 или более поздних версий, создайте экземпляр [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) с путем или потоком файла-шаблона. Или используйте класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выберите значение [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Открытие файлов с различными форматами**

Aspose.Cells позволяет разработчикам открывать файлы электронных таблиц различных форматов, таких как SpreadsheetML, CSV, файлы с разделителями табуляции. Для открытия таких файлов разработчики могут использовать ту же методологию, что и для открытия файлов различных версий Microsoft Excel.

### **Открытие файлов SpreadsheetML**

Файлы SpreadsheetML представляют собой XML-представления ваших электронных таблиц, включая всю информацию о таблице, такую как форматирование, формулы и т. д. С момента появления Microsoft Excel XP была добавлена опция экспорта в формат XML, позволяющая экспортировать электронные таблицы в файлы SpreadsheetML.

Для открытия файлов SpreadsheetML используйте класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выберите значение [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET-ML) в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Открытие файлов CSV**

Файлы с разделенными запятыми (CSV) содержат записи, значения которых разделены или отделены запятыми. В файлах CSV данные хранятся в табличном формате, поля разделены запятой и заключены в кавычки. Если значение поля содержит символ двойной кавычки, он экранируется двойной парой кавычек. Вы также можете использовать Microsoft Excel для экспорта данных вашей таблицы в файл CSV.

Для открытия CSV-файлов используйте класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выберите значение [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), предопределенное в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Открытие файлов CSV и замена недопустимых символов**

В Excel, при открытии CSV-файла с особыми символами, символы автоматически заменяются. То же самое делает API Aspose.Cells, как показано в приведенном ниже примере кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Открытие файлов CSV с использованием предпочтительного парсера**

Не всегда необходимо использовать настройки анализатора по умолчанию для открытия CSV-файлов. Иногда импорт CSV-файла не создает ожидаемый вывод, например, формат даты не соответствует ожиданиям или пустые поля обрабатываются по-разному. Для этой цели доступен [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers), чтобы предоставить собственный предпочтительный анализатор для разбора различных типов данных в соответствии с требованиями. Приведенный ниже образец кода демонстрирует использование предпочтительного анализатора.  

Исходный файл и выходные файлы для примера можно скачать по следующим ссылкам для тестирования этой функции.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Открытие файлов TSV (с разделителями табуляции)**

Файлы с разделителями табуляции содержат данные электронных таблиц, но без какого-либо форматирования. Данные располагаются в строках и столбцах, подобно таблицам и электронным таблицам. Кратко говоря, файл с разделителями табуляции представляет собой особый тип обычного текстового файла, в котором между каждым столбцом стоит табуляция.

Для открытия файлов с разделением табуляцией разработчики должны использовать класс [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и выбрать значение [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), предопределенное в перечислении [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Открытие зашифрованных файлов Excel**

Мы знаем, что с помощью Microsoft Excel можно создавать зашифрованные файлы Excel. Чтобы открыть такие зашифрованные файлы, разработчики должны вызвать специальный перегруженный метод LoadOptions и выбрать значение DEFAULT, предопределенное в перечислении FileFormatType. Этот метод также будет принимать пароль для зашифрованного файла, как показано ниже в примере.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells также поддерживает открытие защищенных паролем файлов MS Excel 2013.

{{% alert color="primary" %}}

Есть серьезные шансы того, что конструктор Workbook может выдать исключение System.OutOfMemoryException при загрузке больших электронных таблиц. Это исключение указывает на то, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому электронная таблица должна быть загружена с включением настроек памяти.

{{% /alert %}}

### **Открытие файлов SXC**

StarOffice Calc подобен Microsoft Excel и поддерживает формулы, диаграммы, функции и макросы. Таблицы, созданные с использованием этого программного обеспечения, сохраняются с расширением SXC. Файл SXC также используется для файлов электронных таблиц OpenOffice.org Calc. Aspose.Cells может читать файлы SXC, как показано в следующем образце кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Открытие файлов FODS**

Файл FODS - это электронная таблица, сохраненная в формате OpenDocument XML без какого-либо сжатия. Aspose.Cells может читать файлы FODS, как показано в следующем образце кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Продвинутые темы**
- [Фильтрация заданных имен при загрузке рабочей книги](/cells/ru/java/filter-defined-names-while-loading-workbook/)
- [Фильтр объектов при загрузке книги или листа](/cells/ru/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Получение предупреждений при загрузке файла Excel](/cells/ru/java/get-warnings-while-loading-excel-file/)
- [Сохранять разделители для пустых строк при экспорте таблиц в формат CSV](/cells/ru/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Загружать книгу с указанным размером бумаги принтера](/cells/ru/java/load-workbook-with-specified-printer-paper-size/)
- [Открытие файлов с различными форматами](/cells/ru/java/opening-different-microsoft-excel-versions-files/)
- [Оптимизация использования памяти при работе с большими файлами с большими наборами данных](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Чтение таблицы чисел, разработанной Apple Inc. с использованием Aspose.Cells](/cells/ru/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Чтение файла CSV с различными кодировками](/cells/ru/java/reading-csv-file-with-multiple-encodings/)
- [Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени](/cells/ru/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Использование API LightCells](/cells/ru/java/using-lightcells-api/)
{{< app/cells/assistant language="java" >}}
