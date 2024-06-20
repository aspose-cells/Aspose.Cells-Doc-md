---
title: Открытие файлов различных версий Microsoft Excel
type: docs
weight: 20
url: /ru/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Открытие файлов различных версий Microsoft Excel**

Приложение часто должно иметь возможность открывать файлы Microsoft Excel, созданные в разных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в одном из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и т. д. Используйте конструктор или укажите метод класса [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook), чтобы указать формат с помощью перечисления [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType).

Перечисление [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

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

Для открытия файла Microsoft Excel 95/5.0 используйте [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) и установите соответствующий атрибут для класса **LoadOptions** для загружаемого шаблона файла. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Открытие файлов Microsoft Excel 97-2003**

Для открытия файла Microsoft Excel 97 - 2003 используйте [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) и установите соответствующий атрибут для класса **LoadOptions** для загружаемого шаблона файла.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия файла в формате Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) и установить соответствующий атрибут/опцию класса **LoadOptions** для загружаемого шаблона файла.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Открытие зашифрованных файлов Excel**

С помощью Microsoft Excel можно создавать зашифрованные файлы. Чтобы открыть зашифрованный файл, используйте [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) и установите его атрибуты и опции (например, укажите пароль) для загрузки шаблонного файла.
Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.


