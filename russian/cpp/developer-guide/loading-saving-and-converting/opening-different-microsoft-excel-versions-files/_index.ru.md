---
title: Открытие файлов различных версий Excel Microsoft
type: docs
weight: 20
url: /ru/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells может открывать различные Microsoft файлы версий Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованные файлы Excel.

{{% /alert %}}

## **Открытие файлов разных версий Microsoft Excel**

 Приложение часто должно иметь возможность открывать файлы Excel Microsoft, созданные в разных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и т. д. Используйте конструктор или укажите**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** учебный класс'**[SetFileFormat] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)** метод для указания формата с помощью**[FileFormatType] (https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**перечисление.
	
**[FileFormatType] (https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
|:- |:- |
|FileFormatType_CSV|Представляет файл CSV|
|FileFormatType_Excel97To2003|Представляет файл Excel 97–2003.|
|FileFormatType_Xlsx|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.|
|FileFormatType_Xlsm|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM.|
|FileFormatType_Xltx|Представляет файл шаблона Excel 2007/2010/2013/2016/2019 и Office 365 XLTX.|
|FileFormatType_Xltm|Представляет XLTM-файл Excel 2007/2010/2013/2016/2019 и Office 365 с поддержкой макросов.|
|FileFormatType_Xlsb|Представляет двоичный XLSB-файл Excel 2007/2010/2013/2016/2019 и Office 365.|
|FileFormatType_SpreadsheetML|Представляет файл SpreadsheetML|
|FileFormatType_Tsv|Представляет файл значений, разделенных табуляцией.|
|FileFormatType_TabDelimited|Представляет текстовый файл с разделителями табуляции|
|FileFormatType_Ods|Представляет файл ODS|
|FileFormatType_Html|Представляет файл HTML|
|FileFormatType_MHtml|Представляет файл MHTML|

### **Открытие Microsoft файлов Excel 95/5.0**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**и установите соответствующий атрибут для**ILoadOptions**class для загружаемого файла шаблона. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Открытие Microsoft Excel 97 - 2003 Файлы**

 Чтобы открыть файл Microsoft Excel 97 - 2003, используйте**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** и установите соответствующий атрибут для**ILoadOptions**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Открытие Microsoft файлов Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

 Чтобы открыть файл формата Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** и установите соответствующий атрибут/параметры**ILoadOptions**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells также поддерживает открытие файлов Excel 2007, 2010, 2013, 2016, 2019, Office 365, защищенных паролем.


