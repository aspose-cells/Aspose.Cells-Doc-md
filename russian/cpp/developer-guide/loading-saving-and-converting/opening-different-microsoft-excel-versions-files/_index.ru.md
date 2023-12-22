---
title: Открытие различных файлов версий Excel Microsoft
type: docs
weight: 20
url: /ru/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells может открыть ряд различных файлов версий Excel Microsoft, таких как Microsoft Excel 95/97 – 2003, SpreadsheetML, Открытие Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или Зашифрованные файлы Excel.

{{% /alert %}}

##  **Открытие файлов разных версий Excel Microsoft**

 Приложению часто приходится иметь возможность открывать файлы Excel Microsoft, созданные в разных версиях, например Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Возможно, вам потребуется загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и так далее. Используйте конструктор или укажите**[Рабочая книга](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**сорт'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** метод для указания формата с использованием**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**перечисление.
	
**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|ФилеФорматТип_CSV|Представляет файл CSV.|
|ФилеФорматТип_Excel97To2003|Представляет файл Excel 97–2003.|
|FileFormatType_Xlsx|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.|
|FileFormatType_Xlsm|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM.|
|FileFormatType_Xltx|Представляет файл шаблона Excel 2007/2010/2013/2016/2019 и Office 365 XLTX.|
|FileFormatType_Xltm|Представляет файл XLTM Excel 2007/2010/2013/2016/2019 и Office 365 с поддержкой макросов.|
|FileFormatType_Xlsb|Представляет двоичный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB.|
|FileFormatType_SpreadsheetML|Представляет файл SpreadsheetML.|
|ФилеФорматТип_Цв|Представляет файл значений, разделенных табуляцией.|
|FileFormatType_TabDelimited|Представляет текстовый файл с разделителями табуляции.|
|ФилеФорматТип_Одс|Представляет файл ODS.|
|FileFormatType_Html|Представляет файл HTML.|
|FileFormatType_MHtml|Представляет файл MHTML.|

###  **Открытие файлов Excel 95/5.0 Microsoft**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**и установите связанный атрибут для**Параметры загрузки**класс для загружаемого файла шаблона. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Открытие Microsoft файлов Excel 97 - 2003**

 Чтобы открыть файл Microsoft Excel 97 – 2003, используйте**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** и установите связанный атрибут для**Параметры загрузки**класс для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Открытие Microsoft файлов Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Чтобы открыть формат Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** и установите соответствующий атрибут/параметры**Параметры загрузки**класс для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells также поддерживает открытие файлов Excel 2007, 2010, 2013, 2016, 2019, Office 365, защищенных паролем.


