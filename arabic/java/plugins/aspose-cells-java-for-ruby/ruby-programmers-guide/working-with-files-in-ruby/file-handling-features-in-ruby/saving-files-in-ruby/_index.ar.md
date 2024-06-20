---
title: حفظ الملفات في روبي
type: docs
weight: 20
url: /ar/java/saving-files-in-ruby/
---

## **Aspose.Cells - حفظ الملفات**
### **حفظ الملف في موقع معين**
إذا كان المطورون بحاجة إلى حفظ ملفاتهم باستخدام Aspose.Cells Java for Ruby في موقع تخزين معين، فيمكنهم ببساطة تحديد اسم الملف (مع مسار تخزينه الكامل) وتنسيق الملف المطلوب (باستخدام تعداد FileFormatType) أثناء استدعاء طريقة الحفظ لكائن Workbook.

**كود Ruby**

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
