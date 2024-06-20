---
title: Открыть файлы разных версий Microsoft Excel
type: docs
weight: 20
url: /ru/net/opening-different-microsoft-excel-versions-files/
description: Эта статья объясняет, как открывать файлы разных версий Excel, используя Aspose.Cells for .NET API.
keywords: C# Открыть разные файлы Microsoft Excel, Как открыть зашифрованные файлы Excel.
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Как открыть файлы разных версий Microsoft Excel**

Приложение часто должно иметь возможность открывать файлы Microsoft Excel, созданные в различных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может понадобиться загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, разделенные табуляцией или TSV, CSV, ODS и т. д. Используйте конструктор, или укажите тип атрибута [**FileFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), указав формат с использованием перечисления [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype).

Перечисление [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
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

### **Открыть файлы Microsoft Excel 95/5.0**

Для открытия файла Microsoft Excel 95/5.0 используйте [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) для загрузки шаблонного файла. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Открыть файлы Microsoft Excel 97 - 2003**

Для открытия файла Microsoft Excel 97 - 2003 используйте [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) для загрузки шаблонного файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Открыть файлы Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия формата Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) и установить соответствующие атрибуты/опции класса [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) для загрузки шаблонного файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Открыть зашифрованные файлы Excel**

С помощью Microsoft Excel можно создавать зашифрованные файлы. Чтобы открыть зашифрованный файл, используйте [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) и установите его атрибуты и опции (например, укажите пароль) для загрузки шаблонного файла.
Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.


