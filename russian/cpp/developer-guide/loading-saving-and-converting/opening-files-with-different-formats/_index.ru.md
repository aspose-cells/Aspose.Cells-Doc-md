---
title: Открытие файлов разных форматов
type: docs
weight: 30
url: /ru/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API позволяет открывать/читать различные форматы, такие как XLSX, HTML, CSV, ODS, TSV, SXC, FODS и т. д.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 С помощью Aspose.Cells вы можете открывать файлы разных форматов.**Aspose.Cells** может открывать ряд форматов файлов, таких как Microsoft электронные таблицы Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, файлы со значениями, разделенными запятыми (CSV), файлы со значениями, разделенными табуляцией или табуляцией (TSV) и т. д.

Если вам нужно знать все поддерживаемые форматы файлов, обратитесь к следующим страницам:
[Поддерживаемые форматы файлов](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **Открытие файлов разных форматов**

Aspose.Cells позволяет разработчикам открывать файлы электронных таблиц в различных форматах, таких как SpreadsheetML, значения, разделенные запятыми (CSV), файлы, разделенные табуляцией или значениями, разделенными табуляцией (TSV), ODS. Для открытия таких файлов разработчики могут использовать ту же методологию, которую они используют для открытия файлов разных версий Excel Microsoft.

###  **Открытие файлов SpreadsheetML**

Файлы SpreadsheetML представляют собой XML-представления электронных таблиц, включая всю информацию о них, такую как форматирование, формулы и т. д. Начиная с версии Microsoft Excel XP, в Excel Microsoft добавлена опция экспорта XML, которая экспортирует ваши электронные таблицы в файлы SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **Открытие файлов HTML**

Aspose.Cells позволяет открыть файл HTML в объекте Workbook. Файл HTML должен быть ориентирован на Excel Microsoft, т.е. MS-Excel должен иметь возможность его открыть.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **Открытие файлов CSV**

Файлы со значениями, разделенными запятыми (CSV) содержат записи, в которых значения разделены запятыми. Данные хранятся в виде таблицы, где каждый столбец разделен запятой и заключен в двойную кавычку. Если значение поля содержит символ двойной кавычки, оно экранируется парой символов двойной кавычки. Вы также можете использовать Microsoft Excel для экспорта данных электронной таблицы в CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **Открытие файлов CSV и замена недопустимых символов**

В Excel при открытии файла CSV со специальными символами символы заменяются автоматически. То же самое делает Aspose.Cells API, что показано в примере кода, приведенном ниже.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Пример исходного файла можно загрузить по следующим ссылкам для тестирования этой функции.

[InvalidCharacters.csv](InvalidCharacters.csv)

###  **Открытие текстовых файлов с помощью специального разделителя**

Текстовые файлы используются для хранения данных электронных таблиц без форматирования. Этот файл представляет собой своего рода обычный текстовый файл, который может иметь некоторые настраиваемые разделители.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Пример исходного файла можно загрузить по следующим ссылкам для тестирования этой функции.

[CustomSeparator.txt](CustomSeparator.txt)

###  **Открытие файлов с разделителями табуляцией**

Файл с разделителями табуляцией (текстовый) содержит данные электронной таблицы, но без какого-либо форматирования. Данные расположены в строках и столбцах, как в таблицах и электронных таблицах. По сути, файл с разделителями табуляции представляет собой особый вид обычного текстового файла с табуляцией между каждым столбцом.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **Открытие файлов со значениями, разделенными табуляцией (TSV)**

Файл значений, разделенных табуляцией (TSV), содержит данные электронной таблицы, но без какого-либо форматирования. То же самое и с файлом с разделителями табуляции, где данные расположены в строках и столбцах, как в таблицах и электронных таблицах.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **Открытие файлов SXC**

StarOffice Calc аналогичен Excel Microsoft и поддерживает формулы, диаграммы, функции и макросы. Таблицы, созданные с помощью этого программного обеспечения, сохраняются с расширением SXC. Файл SXC также используется для файлов электронных таблиц OpenOffice.org Calc. Aspose.Cells может читать файлы SXC, как показано в следующем примере кода.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **Открытие файлов FODS**

Файл FODS представляет собой электронную таблицу, сохраненную в формате OpenDocument XML без какого-либо сжатия. Aspose.Cells может читать файлы FODS, как показано в следующем примере кода.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
