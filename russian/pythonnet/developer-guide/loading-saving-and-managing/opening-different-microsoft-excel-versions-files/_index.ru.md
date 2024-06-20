---
title: Открытие файлов различных версий Microsoft Excel
type: docs
weight: 20
url: /ru/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Открытие файлов различных версий Microsoft Excel**

Приложение часто должно иметь возможность открывать файлы Microsoft Excel, созданные в различных версиях, например Microsoft Excel 95,97, или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Вам может потребоваться загрузить файл в одном из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и т.д. Используйте конструктор или укажите атрибут **file_format** класса **Workbook**, указывающий формат с использованием перечисления **FileFormatType**.

Перечисление **FileFormatType** содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV|Представляет собой файл CSV|
|EXCEL_97_TO_2003|Представляет собой файл Excel 97 - 2003|
|XLSX|Представляет собой файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX|
|XLSM|Представляет собой файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM|
|Xltx|Представляет файл шаблон Excel 2007/2010/2013/2016/2019 и Office 365 XLTX|
|XLTX|Представляет собой макрос-включенный XLTM файл Excel 2007/2010/2013/2016/2019 и Office 365|
|XLSB|Представляет собой двоичный файл XLSB Excel 2007/2010/2013/2016/2019 и Office 365|
|SPREADSHEET_ML|Представляет собой файл SpreadsheetML|
|TSV|Представляет собой файл значений, разделенных табуляцией|
|TAB_DELIMITED|Представляет собой файл текста, разделенного табуляцией|
|ODS|Представляет собой файл ODS|
|HTML|Представляет собой файл HTML|
|M_HTML|Представляет собой файл MHTML|

### **Открытие файлов Microsoft Excel 95/5.0**

Для открытия файла Microsoft Excel 95/5.0 используйте **LoadOptions** и укажите соответствующий атрибут для класса **LoadOptions** для загрузки файла-шаблона. Пример файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Открытие файлов Microsoft Excel 97-2003**

Для открытия файла Microsoft Excel 97 - 2003 используйте **LoadOptions** и укажите соответствующий атрибут для класса **LoadOptions** для загрузки файла-шаблона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия файла в формате Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Также вы можете использовать **LoadOptions** и установить соответствующие атрибуты/опции класса **LoadOptions** для загрузки файла-шаблона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Открытие зашифрованных файлов Excel**

Можно создавать зашифрованные файлы Excel с помощью Microsoft Excel. Для открытия зашифрованного файла используйте **LoadOptions** и установите его атрибуты и опции (например, укажите пароль) для загрузки файла-шаблона.
Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.


