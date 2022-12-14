---
title: Открытие файлов различных версий Excel Microsoft
type: docs
weight: 20
url: /ru/java/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells может открывать различные Microsoft файлы версий Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованные файлы Excel.

{{% /alert %}}

## **Открытие файлов разных версий Microsoft Excel**

 Приложение часто должно иметь возможность открывать файлы Excel Microsoft, созданные в разных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и т. д. Используйте конструктор или используйте**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** учебный класс'**[setFileFormat] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat)** метод для указания формата с помощью**[FileFormatType] (https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)**перечисление.

**[FileFormatType] (https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
|:- |:- |
|CSV|Представляет файл CSV|
|EXCEL_97_ТО_2003|Представляет файл Excel 97–2003.|
|XLSX|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.|
|XLSM|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM.|
|XLTX|Представляет файл шаблона Excel 2007/2010/2013/2016/2019 и Office 365 XLTX.|
|XLTM|Представляет XLTM-файл Excel 2007/2010/2013/2016/2019 и Office 365 с поддержкой макросов.|
|XLSB|Представляет двоичный XLSB-файл Excel 2007/2010/2013/2016/2019 и Office 365.|
|SPREADSHET_ML|Представляет файл SpreadsheetML|
|ТСВ|Представляет файл значений, разделенных табуляцией.|
|TAB_DELIMITED|Представляет текстовый файл с разделителями табуляции|
|ОРВ|Представляет файл ODS|
|HTML|Представляет файл HTML|
|M_HTML|Представляет файл MHTML|

### **Открытие Microsoft файлов Excel 95/5.0**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**и установите соответствующий атрибут для**Параметры загрузки**class для загружаемого файла шаблона. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Открытие Microsoft Excel 97 - 2003 Файлы**

 Чтобы открыть файл Microsoft Excel 97 - 2003, используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** и установите соответствующий атрибут для**Параметры загрузки**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Открытие Microsoft файлов Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

 Чтобы открыть файл формата Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** и установите соответствующий атрибут/параметры**Параметры загрузки**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Открытие зашифрованных файлов Excel**

 Можно создавать зашифрованные файлы Excel с помощью Microsoft Excel. Чтобы открыть зашифрованный файл, используйте**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** и установите его атрибуты и параметры (например, укажите пароль) для загружаемого файла шаблона.
Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Зашифрованный Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells также поддерживает открытие файлов Excel 2007, 2010, 2013, 2016, 2019, Office 365, защищенных паролем.
