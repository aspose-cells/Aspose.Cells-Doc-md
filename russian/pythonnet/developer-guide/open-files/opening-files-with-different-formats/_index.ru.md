---
title: Открытие файлов с различными форматами
type: docs
weight: 30
url: /ru/python-net/opening-files-with-different-formats/
description: API Aspose.Cells для Python via .NET позволяет открывать/читать различные форматы, такие как XLSX, HTML, CSV, ODS, TSV, SXC, FODS и др.
keywords: открыть файлы xlsx, открыть файлы html, прочитать файлы fods, прочитать файлы ods, прочитать файлы sxc, открыть файлы csv, Табличный разделитель, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Используя Aspose.Cells для Python via .NET, вы можете открывать файлы разных форматов. Aspose.Cells для Python via .NET поддерживает открытие ряда форматов файлов, таких как таблицы Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, CSV, TSV, и др.

Если вам нужно знать все поддерживаемые форматы файлов, обратитесь к следующим страницам:
[Поддерживаемые форматы файлов](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Открытие файлов с различными форматами**

Aspose.Cells для Python via .NET позволяет разработчикам открывать файлы таблиц с разными форматами, такими как SpreadsheetML, CSV, TSV, ODS. Для открытия таких файлов разработчики используют тот же метод, что и для файлов разных версий Excel.

### **Открытие файлов SpreadsheetML**

Файлы SpreadsheetML представляют собой XML-представление электронных таблиц, включая всю информацию о них, такую как форматирование, формулы и т. д. С момента Microsoft Excel XP добавлена опция экспорта в формате XML в Microsoft Excel, которая экспортирует ваши электронные таблицы в файлы SpreadsheetML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Открытие файлов HTML**

Aspose.Cells для Python via .NET позволяет открыть HTML-файл в объекте Workbook. HTML-файл должен быть ориентирован на Microsoft Excel, т.е. MS-Excel должен уметь его открыть.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Открытие файлов CSV**

Файлы с разделенными запятыми (CSV) содержат записи, в которых значения разделены запятыми. Данные хранятся в виде таблицы, где каждый столбец разделен запятой и заключен в кавычки. Если значение поля содержит символ двойной кавычки, он экранируется парой символов двойной кавычки. Вы также можете использовать Microsoft Excel для экспорта данных электронных таблиц в CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Открытие файлов CSV и замена недопустимых символов**

В Excel при открытии CSV-файла с особыми символами символы автоматически заменяются. То же самое делает API Aspose.Cells для Python via .NET, что демонстрируется в приведённом ниже примере кода.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Открытие файлов с разделителями табуляции**

Файл с разделителями табуляции (текстовый) содержит данные электронной таблицы, но без какого-либо форматирования. Данные расположены в строках и столбцах, как в таблицах и электронных таблицах. Фактически, файл с разделителями табуляции является особым видом обычного текстового файла с табуляцией между каждым столбцом.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Открытие файлов со значениями, разделенными табуляцией (TSV)**

Файл со значениями, разделенными табуляцией (TSV), содержит данные электронной таблицы, но без какого-либо форматирования. Это то же самое, что и файл с разделителями табуляции, где данные расположены в строках и столбцах, как в таблицах и электронных таблицах.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Открытие файлов SXC**

StarOffice Calc аналогичен Microsoft Excel и поддерживает формулы, графики, функции и макросы. Таблицы, созданные этим программным обеспечением, сохраняются с расширением SXC. Файл SXC также используется для таблиц OpenOffice.org Calc. Aspose.Cells для Python via .NET может читать файлы SXC, как показано в следующем примере кода.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Открытие файлов FODS**

Файл FODS — это электронная таблица, сохранённая в формате OpenDocument XML без сжатия. Aspose.Cells для Python via .NET умеет читать файлы FODS, что демонстрируется в следующем примере кода.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
