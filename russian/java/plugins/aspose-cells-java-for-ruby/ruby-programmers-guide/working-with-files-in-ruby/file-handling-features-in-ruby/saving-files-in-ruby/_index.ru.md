---
title: Сохранение Файлов в Ruby
type: docs
weight: 20
url: /ru/java/saving-files-in-ruby/
---

## **Aspose.Cells - Сохранение Файлов**
### **Сохранение файла в выбранное место**
Если разработчикам нужно сохранить свои файлы, используя **Aspose.Cells Java для Ruby**, в определенное место на хранилище, то они могут просто указать имя файла (с его полным путем хранения) и желаемый формат файла (используя перечисление **FileFormatType**) при вызове метода **save** объекта **Workbook**.

**Код на Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

\# Save in default (Excel2003) format

workbook.save(data_dir + "Book1.xls")

#Save in Excel2003 format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

\# Save in Excel2007 xlsx format

workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

\# Save in SpreadsheetML format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)

{{< /highlight >}}
