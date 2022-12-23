---
title: Открытие файлов различных версий Excel Microsoft
type: docs
weight: 20
url: /ru/python-java/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells может открывать различные Microsoft файлы версий Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие Microsoft Excel 2007/2010/2013/2013/2016/2019 и Office 365 XLSX или зашифрованные файлы Excel.

{{% /alert %}}

## **Открытие файлов разных версий Microsoft Excel**

 Приложение часто должно иметь возможность открывать файлы Excel Microsoft, созданные в разных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может понадобиться загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и так далее. Используйте конструктор или укажите**[Рабочая книга] (https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** учебный класс'**[setFileFormat] (https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat)**метод для указания формата с помощью**[FileFormatType] (https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**перечисление.
	
**[FileFormatType] (https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
|:- |:- |
|CSV|Представляет файл CSV|
|EXCEL_97_ТО_2003|Представляет файл Excel 97–2003.|
|XLSX|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.|
|XLSM|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM.|
|XLTX|Представляет файл шаблона Excel 2007/2010/2013/2016/2019 и Office 365 XLTX.|
|XLTM|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 с поддержкой макросов XLTM.|
|XLSB|Представляет двоичный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB.|
|SPREADSHET_ML|Представляет файл SpreadsheetML|
|TSV|Представляет файл значений, разделенных табуляцией.|
|TAB_DELIMITED|Представляет текстовый файл с разделителями табуляции|
|ODS|Представляет файл ODS|
|HTML|Представляет файл HTML|
|M_HTML|Представляет файл MHTML|

### **Открытие Microsoft файлов Excel 95/5.0**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)**и установите соответствующий атрибут для**Параметры загрузки**class для загружаемого файла шаблона. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Открытие Microsoft Excel 97 - 2003 Файлы**

 Чтобы открыть файл Microsoft Excel 97 - 2003, используйте**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** и установите соответствующий атрибут для**Параметры загрузки**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Открытие Microsoft файлов Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Чтобы открыть формат Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** и установите соответствующий атрибут/параметры**Параметры загрузки**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Открытие зашифрованных файлов Excel**

 Можно создавать зашифрованные файлы Excel с помощью Microsoft Excel. Чтобы открыть зашифрованный файл, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**и установите его атрибуты и параметры (например, укажите пароль) для загружаемого файла шаблона.
Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Зашифрованный Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells также поддерживает открытие файлов Excel 2007, 2010, 2013, 2016, 2019, Office 365, защищенных паролем.


