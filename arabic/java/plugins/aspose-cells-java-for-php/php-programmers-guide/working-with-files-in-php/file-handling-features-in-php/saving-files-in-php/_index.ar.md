---
title: حفظ الملفات في PHP
type: docs
weight: 20
url: /ar/java/saving-files-in-php/
---

## **Aspose.Cells - حفظ الملفات**
### **حفظ الملف في موقع معين**
إذا كان المطورون بحاجة إلى حفظ ملفاتهم باستخدام **Aspose.Cells Java for PHP** في موقع تخزين معين، يمكنهم ببساطة تحديد اسم الملف (مع مسار تخزينه الكامل) وتنسيق الملف المطلوب (باستخدام تعداد **FileFormatType**) أثناء استدعاء طريقة **save** لكائن **Workbook**.

**كود PHP**

{{< highlight php >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **حفظ الملفات (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
