---
title: Открытие файлов различных версий Excel Microsoft
type: docs
weight: 20
url: /ru/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells может открывать различные Microsoft файлы версий Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованные файлы Excel.

{{% /alert %}}

## **Открытие файлов разных версий Microsoft Excel**

 Приложение часто должно иметь возможность открывать файлы Excel Microsoft, созданные в разных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и т. д. Используйте конструктор или укажите**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** учебный класс'**[Формат файла] (https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** атрибут типа, который определяет формат с помощью**[FileFormatType] (https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**перечисление.

**[FileFormatType] (https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**перечисление содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
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

Чтобы открыть файл Microsoft Excel 95/5.0, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**и установите соответствующий атрибут для**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class для загружаемого файла шаблона. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Открытие Microsoft Excel 97 - 2003 Файлы**

 Чтобы открыть файл Microsoft Excel 97 - 2003, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** и установите соответствующий атрибут для**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Открытие Microsoft файлов Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

 Чтобы открыть файл формата Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** и установите соответствующий атрибут/параметры**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class для загружаемого файла шаблона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Открытие зашифрованных файлов Excel**

 Можно создавать зашифрованные файлы Excel с помощью Microsoft Excel. Чтобы открыть зашифрованный файл, используйте**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**и установите его атрибуты и параметры (например, укажите пароль) для загружаемого файла шаблона.
Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Зашифрованный Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells также поддерживает открытие файлов Excel 2007, 2010, 2013, 2016, 2019, Office 365, защищенных паролем.


