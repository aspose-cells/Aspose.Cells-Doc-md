---
title: Открытие файлов различных версий Microsoft Excel
type: docs
weight: 20
url: /ru/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Открытие файлов различных версий Microsoft Excel**

Приложение часто должно иметь возможность открывать файлы Microsoft Excel, созданные в разных версиях, например, Microsoft Excel 95,97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в одном из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и т. д. Используйте конструктор или укажите метод класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), чтобы указать формат с помощью перечисления [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/).

Перечисление [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|FileFormatType_CSV|Представляет файл CSV|
|FileFormatType_Excel97To2003|Представляет файл Excel 97 - 2003|
|FileFormatType_Xlsx|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX|
|FileFormatType_Xlsm|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM
|FileFormatType_Xltx|Представляет шаблонный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLTX
|FileFormatType_Xltm|Представляет макросодержащий файл Excel 2007/2010/2013/2016/2019 и Office 365 XLTM
|FileFormatType_Xlsb|Представляет двоичный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB
|FileFormatType_SpreadsheetML|Представляет файл SpreadsheetML
|FileFormatType_Tsv|Представляет файл значений, разделенных табуляцией
|FileFormatType_TabDelimited|Представляет файл текста с табуляцией
|FileFormatType_Ods|Представляет файл ODS
|FileFormatType_Html|Представляет файл HTML
|FileFormatType_MHtml|Представляет файл MHTML

### **Открытие файлов Microsoft Excel 95/5.0**

Для открытия файла Microsoft Excel 95/5.0 используйте [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) для загрузки шаблонного файла. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **Открытие файлов Microsoft Excel 97-2003**

Для открытия файла Microsoft Excel 97 - 2003 используйте [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) для загрузки шаблонного файла.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **Открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия формата Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Вы также можете использовать [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) и установить соответствующие атрибуты/опции класса [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) для загрузки шаблонного файла.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.


{{< app/cells/assistant language="cpp" >}}
