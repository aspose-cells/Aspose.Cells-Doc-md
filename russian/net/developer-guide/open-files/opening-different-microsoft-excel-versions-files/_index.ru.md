---
title: Открытие различных файлов версий Excel Microsoft
type: docs
weight: 20
url: /ru/net/opening-different-microsoft-excel-versions-files/
description: В этой статье объясняется, как открывать файлы различных версий Excel с помощью Aspose.Cells for .NET API.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells может открыть ряд различных файлов версий Excel Microsoft, таких как Microsoft Excel 95/97 – 2003, SpreadsheetML, Открытие Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или Зашифрованные файлы Excel.

{{% /alert %}}

##  **Как открыть файлы разных версий Excel Microsoft**

 Приложению часто приходится иметь возможность открывать файлы Excel Microsoft, созданные в разных версиях, например Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Возможно, вам потребуется загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и так далее. Используйте конструктор или укажите**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)**сорт'**[Формат файла](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** атрибут типа, который определяет формат с помощью**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**перечисление.

**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV-файл|Представляет файл CSV.|
|Excel97To2003|Представляет файл Excel 97–2003.|
|XLSX|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.|
|XLSM|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM.|
|XLTX|Представляет файл шаблона Excel 2007/2010/2013/2016/2019 и Office 365 XLTX.|
|XLTM|Представляет файл XLTM Excel 2007/2010/2013/2016/2019 и Office 365 с поддержкой макросов.|
|XLSB|Представляет двоичный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB.|
|SpreadsheetML|Представляет файл SpreadsheetML.|
|Цв|Представляет файл значений, разделенных табуляцией.|
|TabDelimited|Представляет текстовый файл с разделителями табуляции.|
|Коэффициенты|Представляет файл ODS.|
|HTML|Представляет файл HTML.|
|Мhtml|Представляет файл MHTML.|

###  **Открыть файлы Excel 95/5.0 Microsoft**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**и установите связанный атрибут для**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**класс для загружаемого файла шаблона. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Открыть Microsoft файлы Excel 97 - 2003**

 Чтобы открыть файл Microsoft Excel 97 – 2003, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** и установите связанный атрибут для**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**класс для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Откройте Microsoft файлы Excel 2007/2010/2013/2016/2019 и Office 365 XLSX.**

Чтобы открыть формат Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** и установите соответствующий атрибут/параметры**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**класс для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Открыть зашифрованные файлы Excel**

 Можно создавать зашифрованные файлы Excel, используя Microsoft Excel. Чтобы открыть зашифрованный файл, используйте команду**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**и установите его атрибуты и параметры (например, укажите пароль) для загружаемого файла шаблона.
Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[Зашифрованный Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells также поддерживает открытие файлов Excel 2007, 2010, 2013, 2016, 2019, Office 365, защищенных паролем.


