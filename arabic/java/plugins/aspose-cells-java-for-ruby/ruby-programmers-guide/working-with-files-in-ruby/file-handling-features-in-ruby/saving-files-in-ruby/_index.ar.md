---
title: حفظ الملفات في روبي
type: docs
weight: 20
url: /ar/java/saving-files-in-ruby/
---
## **Aspose.Cells - حفظ الملفات**
### **حفظ الملف في بعض المواقع**
 إذا احتاج المطورون إلى حفظ ملفاتهم باستخدام**Aspose.Cells Java لروبي** إلى بعض مواقع التخزين ، يمكنهم ببساطة تحديد اسم الملف (بمسار التخزين الكامل) وتنسيق الملف المطلوب (باستخدام امتداد**نوع الملف**تعداد) أثناء استدعاء**حفظ**طريقة**دفتر العمل**موضوع.

**كود روبي**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

file_format_type = Rjb::import('com.aspose.cells.FileFormatType')

\# Save in default (Excel2003) format

workbook.save(data_dir + "Book1.xls")

# Save in Excel2003 format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_97_TO_2003)

\# Save in Excel2007 xlsx format

workbook.save(data_dir + "Book1.xls", file_format_type.XLSX)

\# Save in SpreadsheetML format

workbook.save(data_dir + "Book1.xls", file_format_type.EXCEL_2003_XML)

{{< /highlight >}}
