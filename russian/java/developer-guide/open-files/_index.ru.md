---
title: Открытие файлов разных форматов
linktitle: Открытые файлы
type: docs
weight: 10
url: /ru/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Разработчики используют Aspose.Cells для открытия файлов для различных целей. Например, откройте файл, чтобы получить из него данные, или используйте предопределенный файл электронной таблицы дизайнера, чтобы ускорить процесс разработки. Aspose.Cells позволяет разработчикам открывать различные типы исходных файлов. Эти исходные файлы могут быть Microsoft отчетами Excel, файлами SpreadsheetML, значениями, разделенными запятыми (CSV), файлами с разделителями табуляции или значениями, разделенными табуляцией (TSV). В этой статье обсуждается открытие этих различных исходных файлов с помощью Aspose.Cells.

Если вам нужно знать все поддерживаемые форматы файлов, обратитесь к следующим страницам:
[Поддерживаемые форматы файлов](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Простые способы открытия файлов Excel**

### **Открытие через Путь**

Чтобы открыть файл Excel Microsoft, используя путь к файлу, передайте путь к файлу в качестве параметра при создании экземпляра**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**учебный класс. В следующем примере кода показано открытие файла Excel с использованием пути к файлу.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Открытие через поток**

Иногда файл Excel, который вы хотите открыть, хранится в виде потока. В этом случае, аналогично открытию файла с использованием пути к файлу, передайте поток в качестве параметра при создании экземпляра**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**учебный класс. В следующем примере кода показано открытие файла Excel с помощью потока.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Открытие файлов разных версий Microsoft Excel**

 Пользователь может использовать**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс, чтобы указать формат файла Excel, используя**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов**|**Описание**|
|:- |:- |
|CSV|Представляет файл CSV|
|Excel97To2003|Представляет файл Excel 97–2003.|
|XLSX|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.|
|XLSM|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM.|
|XLTX|Представляет файл шаблона Excel 2007/2010/2013/2016/2019 и Office 365 XLTX.|
|XLTM|Представляет XLTM-файл Excel 2007/2010/2013/2016/2019 и Office 365 с поддержкой макросов.|
|XLSB|Представляет двоичный XLSB-файл Excel 2007/2010/2013/2016/2019 и Office 365.|
|Электронная таблицаML|Представляет файл SpreadsheetML|
|Цв|Представляет файл значений, разделенных табуляцией.|
|TabDelimited|Представляет текстовый файл с разделителями табуляции|
|шансы|Представляет файл ODS|
|HTML|Представляет файл HTML|
|Mhtml|Представляет файл MHTML|

### **Открытие Microsoft файлов Excel 95/5.0**

 Чтобы открыть Microsoft файлов Excel 95, создайте экземпляр**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instance с путем или потоком файла шаблона. Образец файла для тестирования кода можно скачать по следующей ссылке:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Открытие Microsoft Excel 97 или более поздних версий файлов XLS**

 Чтобы открыть файлы XLS Microsoft Excel XLS 97 или более поздних версий, создайте экземпляр**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** instance с путем или потоком файла шаблона. Или используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** способ и выберите**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** значение в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Открытие Microsoft Excel 2007 или более поздних версий файлов XLSX**

 Чтобы открыть файлы XLSX Microsoft Excel 2007 или более поздних версий, создайте экземпляр**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instance с путем или потоком файла шаблона. Или используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс и выберите**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** значение в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Открытие файлов разных форматов**

Aspose.Cells позволяет разработчикам открывать файлы электронных таблиц в различных форматах, таких как SpreadsheetML, CSV, файлы с разделителями табуляции. Чтобы открыть такие файлы, разработчики могут использовать ту же методологию, что и для открытия файлов различных версий Excel Microsoft.

### **Открытие файлов SpreadsheetML**

Файлы SpreadsheetML представляют собой XML-представления ваших электронных таблиц, включая всю информацию о электронной таблице, такую как форматирование, формулы и т. д. Начиная с Microsoft Excel XP, в Microsoft Excel добавлен параметр экспорта XML, который экспортирует ваши электронные таблицы в файлы SpreadsheetML.

Чтобы открыть файлы SpreadsheetML, используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс и выберите**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** значение в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Открытие CSV-файлов**

Файлы со значениями, разделенными запятыми (CSV), содержат записи, значения которых разделены запятыми. В файлах CSV данные хранятся в табличном формате, в котором поля разделены запятой и заключены в двойные кавычки. Если значение поля содержит символ двойной кавычки, оно экранируется парой символов двойной кавычки. Вы также можете использовать Microsoft Excel для экспорта данных электронной таблицы в файл CSV.

Чтобы открыть файлы CSV, используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс и выберите**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** значение, заданное в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Открытие файлов CSV и замена недопустимых символов**

В Excel при открытии файла CSV со специальными символами символы автоматически заменяются. То же самое делает Aspose.Cells API, что продемонстрировано в приведенном ниже примере кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Открытие файлов CSV с помощью предпочтительного парсера**

Это не всегда необходимо, чтобы использовать настройки парсера по умолчанию для открытия файлов CSV. Иногда импорт CSV-файла не приводит к ожидаемому результату, например формат даты не соответствует ожидаемому или пустые поля обрабатываются по-другому. Для этого**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**доступен для предоставления собственного предпочтительного синтаксического анализатора для анализа различных типов данных в соответствии с требованиями. Следующий пример кода демонстрирует использование предпочтительного синтаксического анализатора.

Образец исходного файла и выходные файлы можно загрузить по следующим ссылкам для тестирования этой функции.

[образецPreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Открытие файлов TSV (с разделителями табуляцией)**

Файлы с разделителями табуляцией содержат данные электронной таблицы, но без какого-либо форматирования. Данные располагаются в строках и столбцах, таких как таблицы и электронные таблицы. Вкратце, файл с разделителями табуляцией — это особый тип простого текстового файла с табуляцией между каждым столбцом в тексте.

Чтобы открыть файлы с разделителями табуляцией, разработчики должны использовать**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** класс и выберите**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** значение, заданное в**[Формат загрузки] (https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**перечисление.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Открытие зашифрованных файлов Excel**

Мы знаем, что можно создавать зашифрованные файлы Excel, используя Microsoft Excel. Чтобы открыть такие зашифрованные файлы, разработчикам следует вызвать специальный перегруженный метод LoadOptions и выбрать значение DEFAULT, предопределенное в перечислении FileFormatType. Этот метод также будет принимать пароль для зашифрованного файла, как показано ниже в примере.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells также поддерживает открытие файлов MS Excel 2013, защищенных паролем.

{{% alert color="primary" %}}

Есть большая вероятность, что конструктор Workbook может вызвать исключение System.OutOfMemoryException при загрузке больших электронных таблиц. Это исключение говорит о том, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому необходимо загрузить электронную таблицу, включив[Настройки памяти](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Открытие SXC файлов**

StarOffice Calc похож на Microsoft Excel и поддерживает формулы, диаграммы, функции и макросы. Электронные таблицы, созданные с помощью этого программного обеспечения, сохраняются с расширением SXC. Файл SXC также используется для файлов электронных таблиц OpenOffice.org Calc. Aspose.Cells может читать файлы SXC, как показано в следующем примере кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Открытие файлов FOD**

Файл FODS представляет собой электронную таблицу, сохраненную в формате OpenDocument XML без какого-либо сжатия. Aspose.Cells может читать файлы FODS, как показано в следующем примере кода.

#### **Пример**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Предварительные темы**
- [Фильтровать определенные имена при загрузке книги](/cells/ru/java/filter-defined-names-while-loading-workbook/)
- [Фильтровать объекты при загрузке книги или листа](/cells/ru/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Получать предупреждения при загрузке файла Excel](/cells/ru/java/get-warnings-while-loading-excel-file/)
- [Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV](/cells/ru/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Загрузить рабочую книгу с указанным размером бумаги для принтера](/cells/ru/java/load-workbook-with-specified-printer-paper-size/)
- [Открытие файлов различных версий Excel Microsoft](/cells/ru/java/opening-different-microsoft-excel-versions-files/)
- [Оптимизация использования памяти при работе с большими файлами с большими наборами данных](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Читать электронную таблицу чисел, разработанную Apple Inc. с использованием Aspose.Cells](/cells/ru/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Чтение файла CSV с несколькими кодировками](/cells/ru/java/reading-csv-file-with-multiple-encodings/)
- [Остановите преобразование или загрузку с помощью InterruptMonitor, если это занимает слишком много времени](/cells/ru/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Использование LightCells API](/cells/ru/java/using-lightcells-api/)
