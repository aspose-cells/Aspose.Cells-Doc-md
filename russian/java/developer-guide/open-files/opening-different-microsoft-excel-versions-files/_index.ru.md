---
title: Открытие файлов различных версий Microsoft Excel
type: docs
weight: 20
url: /ru/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Открытие файлов различных версий Microsoft Excel**

Приложение часто должно иметь возможность открывать файлы Microsoft Excel, созданные в различных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и так далее. Используйте конструктор или используйте метод [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat) класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) для указания формата с использованием перечисления [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType).

Перечисление [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV|Представляет собой файл CSV|
|EXCEL_97_TO_2003|Представляет собой файл Excel 97 - 2003|
|XLSX|Представляет собой файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX|
|XLSM|Представляет собой файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM|
|XLTX|Представляет собой файл шаблона XLTX Excel 2007/2010/2013/2016/2019 и Office 365|
|XLTM|Представляет собой макросохраненный файл XLTM Excel 2007/2010/2013/2016/2019 и Office 365|
|XLSB|Представляет собой двоичный файл XLSB Excel 2007/2010/2013/2016/2019 и Office 365|
|SPREADSHEET_ML|Представляет собой файл SpreadsheetML|
|TSV|Представляет собой файл значений, разделенных табуляцией|
|TAB_DELIMITED|Представляет собой файл текста, разделенного табуляцией|
|ODS|Представляет собой файл ODS|
|HTML|Представляет собой файл HTML|
|M_HTML|Представляет собой файл MHTML|

### **Открытие файлов Microsoft Excel 95/5.0**

Для открытия файла Microsoft Excel 95/5.0 используйте [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) для загрузки шаблонного файла. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Открытие файлов Microsoft Excel 97-2003**

Для открытия файла Microsoft Excel 97 - 2003 используйте [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) для загрузки шаблонного файла.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия формата Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и установить соответствующие атрибуты/опции класса [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) для загрузки шаблонного файла.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Открытие зашифрованных файлов Excel**

С помощью Microsoft Excel можно создавать зашифрованные файлы. Чтобы открыть зашифрованный файл, используйте [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) и установите его атрибуты и опции (например, укажите пароль) для загрузки шаблонного файла. 
Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.
